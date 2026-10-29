#!/usr/bin/env python3
"""
Upgates variables -> designer reference mapper.

Reads a raw Upgates _variables.scss (the one you dumped) and emits a Markdown
reference answering, for every variable:
  - what visual thing it controls (inline comment + value)
  - whether it is slot-editable (!default and NOT admin/designer-locked)
  - what it resolves to (literal value, or the expression if calculated)
  - which CSS utility/component it feeds (the "// .xxx" comments)

Usage:
    python3 research/map_variables.py [path/to/_variables.scss]

Output:
    research/upgates-variables-reference.md  (Markdown, grouped by section)
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_IN = ROOT / "research" / "_variables.scss"
OUT = ROOT / "research" / "upgates-variables-reference.md"
DETAIL = ROOT / "research" / "variables-index.json"


@dataclass
class Var:
    name: str
    value: str
    section: str
    line_no: int
    default: bool = False
    admin_linked: bool = False        # uses designer-value() or an admin _designer var
    brand_derived: bool = False       # built from $brand-* seeds
    calc: bool = False                # value uses calc() or a function
    comment: str = ""                 # //  inline note about the CSS class it feeds
    map: bool = False
    body: str = ""                    # raw body text (for multi-line maps)
    map_keys: list = field(default_factory=list)


SECTION_HEAD = re.compile(r"^\s*//\s*([A-Z]+.+?)+\s*\*{3,}\s*$")
ADMIN_VAR = re.compile(r"designer-value\(|_designer\b")
BRAND = re.compile(r"\$brand-")
CALC = re.compile(r"calc\(|darken-max\(|lighten\(|saturat|lightness-max|saturation-max|hsl\(|map-get|shadow-|border-|contrast-|color-yiq|spacer")
INLINE_CMT = re.compile(r"//\s*(.+?)\s*$")


def parse(path: Path) -> list[Var]:
    vars_: list[Var] = []
    section = "UNGROUPED"
    in_map = False
    cur: Var | None = None
    pending_comment = ""

    lines = path.read_text(encoding="utf-8").splitlines()
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip()
        stripped = line.strip()

        # Section header: "// NAME ****"
        sec = SECTION_HEAD.match(line)
        if sec and not stripped.startswith("//="):
            # capture the title word(s)
            m = re.match(r"//\s*([A-Za-zčřžšČŘŽŠÚÉÁÍÓÝ /-]+?)\s*[*# ]*$", line)
            if m:
                section = m.group(1).strip().upper()
                continue

        if stripped.startswith("//"):  # trailing footnote not attached yet
            c = INLINE_CMT.search(line)
            if c and not in_map:
                pending_comment = c.group(1)
            continue

        if stripped == "":
            continue

        # map start:  $name: ( ... )  -> capture keys between braces
        m = re.match(r"^\$([a-zA-Z0-9_-]+)\s*:\s*\(?\s*$", line)
        m2 = re.match(r"^\$([a-zA-Z0-9_-]+)\s*:\s*\((.*)\)\s*;?\s*$", line)
        flat = re.match(r"^\$([a-zA-Z0-9_-]+)\s*:\s*([^;{]+)(;?)\s*$", line)

        if m:
            name = m.group(1)
            cur = Var(name, "(map)", section, i, map=True, comment=pending_comment)
            cur.default = "!default" in raw
            cur.admin_linked = bool(ADMIN_VAR.search(raw)) or bool(ADMIN_VAR.search(pending_comment))
            cur.brand_derived = bool(BRAND.search(raw)) or bool(BRAND.search(pending_comment))
            cur.calc = bool(CALC.search(raw))
            vars_.append(cur)
            in_map = True
            pending_comment = ""
            continue

        m2 = re.match(r"^\$([a-zA-Z0-9_-]+)\s*:\s*\((.*)\)\s*;?\s*$", line)
        if m2:
            name = m2.group(1)
            cur = Var(name, m2.group(2)[:120], section, i, map=True, comment=pending_comment)
            cur.body = m2.group(2)
            cur.default = "!default" in raw
            cur.admin_linked = bool(ADMIN_VAR.search(raw))
            cur.brand_derived = bool(BRAND.search(raw))
            cur.calc = bool(CALC.search(raw))
            cur.map_keys = re.findall(r'"([a-z0-9_-]+)"\s*:', m2.group(2))
            vars_.append(cur)
            in_map = False
            pending_comment = ""
            continue

        if flat:
            name = flat.group(1)
            value = flat.group(2).strip()
            cur = Var(name, value, section, i, comment=pending_comment)
            cur.default = "!default" in raw
            cur.admin_linked = bool(ADMIN_VAR.search(raw))
            cur.brand_derived = bool(BRAND.search(raw))
            cur.calc = bool(CALC.search(raw))
            vars_.append(cur)
            pending_comment = ""
            continue

        # inside a map we already opened: collect keys + body
        if in_map and cur:
            cur.body += line + "\n"
            if '"' in line or ":" in line:
                k = re.match(r'\s*"([^"]+)"\s*:', line)
                if k and k.group(1) not in cur.map_keys:
                    cur.map_keys.append(k.group(1))
            if BRAND.search(raw):
                cur.brand_derived = True
            if ADMIN_VAR.search(raw):
                cur.admin_linked = True
        # map close: only a line that BEGINS with ')' closes the map
        # (body lines like calc(...) also contain ')' — don't let those close it)
        if in_map and cur and re.match(r"^\s*\)", line):
            if "!default" in raw:
                cur.default = True
            in_map = False

    return vars_


def propagate(vars_: list[Var]) -> None:
    """Transitive brand/admin propagation.

    If a variable's value references another variable that is brand-derived
    or admin-linked, it is itself effectively brand/admin. This matters for
    the color system: `$colors-bg` -> `$color-bg-primary` -> `$brand-primary`,
    so it must be tagged admin later, not slot, even though no `$brand-`
    literal appears in its own body. Iterate to fixpoint.
    """
    def strip_name(val: str) -> list[str]:
        return re.findall(r"\$([a-zA-Z0-9_-]+)", val)

    # build name -> record
    by_name = {v.name: v for v in vars_}
    changed = True
    while changed:
        changed = False
        for v in vars_:
            if v.brand_derived and v.admin_linked:
                continue
            # scan the literal value AND the map body for referenced vars
            haystack = (v.value or "") + "\n" + (getattr(v, "body", "") or "")
            for ref in strip_name(haystack):
                r = by_name.get(ref)
                if r and (r.brand_derived or r.admin_linked):
                    if not v.brand_derived:
                        v.brand_derived = True
                        changed = True
                    if r.admin_linked and not v.admin_linked:
                        v.admin_linked = True
                        changed = True


def resolve_value(v: Var) -> str:
    """Best-effort human value: literal if possible, else the expression."""
    val = v.value.strip().rstrip(";")
    if v.map:
        keys = ", ".join(v.map_keys[:24]) if v.map_keys else "…"
        return f"map[{keys}]"
    if v.calc or re.search(r"\$[a-zA-Z]", val):
        return f"`{val}` (calculated)"
    return val


def render(vars_: list[Var], src: str) -> str:
    out = [
        "# Upgates variables — designer reference",
        "",
        f"Source: `{src}`  ·  {len(vars_)} variables parsed.",
        "",
        "> **How to read this:** a variable is **slot-editable** when it is `!default`, NOT",
        "> derived from a `$brand-*` seed, and NOT admin-linked (`designer-value()`).",
        "> - ✅ **slot** = set it in the custom-variables slot.",
        "> - ⚠️ **admin** = brand-derived or admin-linked → set it in the Designer UI,",
        ">   not the slot.",
        "",
        "## Cheat sheet — the basics you should rarely override in CSS",
        "",
        "| Variable | Where to set | What it controls | Value |",
        "|---|---|---|---|",
    ]

    # group by section, order by appearance
    seen = []
    for v in vars_:
        if v.section not in seen:
            seen.append(v.section)

    # cheat sheet picks
    cs_rows = []
    for v in vars_:
        if v.name in ("spacers", "container-xxl", "font-sizes", "radius-sizes", "shadows",
                        "colors-bg", "colors-text", "btn-padding-y", "grid-gutter-width",
                        "colors-fg-text", "body-color", "body-bg", "navbar-height",
                        "products-list-img-height"):
            where = "✅ slot" if _editable(v) else ("⚠️ admin" if (v.brand_derived or v.admin_linked) else "🚫?")
            cs_rows.append(f"| `{v.name}` | {where} | {v.comment[:50]} | {resolve_value(v)} |")
    out.extend(cs_rows)

    out += ["", "---", ""]

    for sec in seen:
        items = [v for v in vars_ if v.section == sec]
        out += [f"## {sec}", "", "| Variable | Where | Value | Controls (class) |", "|---|---|---|---|"]
        for v in items:
            where = "✅ slot" if _editable(v) else ("⚠️ admin" if (v.brand_derived or v.admin_linked) else "🚫?")
            cmt = v.comment[:55]
            out.append(f"| `{v.name}` | {where} | {resolve_value(v)} | {cmt} |")
        out.append("")

    return "\n".join(out)


def _editable(v: Var) -> bool:
    """True when a variable can be set in the custom-variables slot."""
    return bool(v.default) and not (v.brand_derived or v.admin_linked)


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_IN
    if not src.exists():
        print(f"missing input: {src}  — put the raw Upgates _variables.scss there and re-run.", file=sys.stderr)
        return 1
    vars_ = parse(src)
    propagate(vars_)
    OUT.write_text(render(vars_, src.name))
    DETAIL.write_text(json.dumps([
        {"name": v.name, "value": v.value, "section": v.section, "line": v.line_no,
         "default": v.default, "admin_linked": v.admin_linked, "brand": v.brand_derived,
         "calc": v.calc, "comment": v.comment, "map": v.map, "keys": v.map_keys}
        for v in vars_
    ], ensure_ascii=False, indent=2))
    print(f"parsed {len(vars_)} variables -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
