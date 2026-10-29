#!/usr/bin/env python3
"""
Všeprotisk design-token -> Upgates custom-variables generator.

Reads tokens/design-tokens.json and emits dist/_variables.scss — a file you
paste wholesale into Upgates' "custom variables" SCSS slot. The slot compiles
BEFORE the theme partials, so every !default map here is yours.

Usage:
    python build/generate.py

Never hand-edit dist/_variables.scss. Edit tokens/design-tokens.json and rebuild.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens" / "design-tokens.json"
OUT = ROOT / "dist" / "_variables.scss"

WARN = "// GENERATED FILE — do not hand-edit. Source: tokens/design-tokens.json"


def scss_map(name: str, items: dict) -> str:
    body = ",\n".join(f'\t"{k}":  {str(v)}' for k, v in items.items())
    return f"${name}: (\n{body},\n) !default;"


def build(t: dict) -> str:
    out = [WARN, f"// Generated {__import__('datetime').datetime.now():%Y-%m-%d %H:%M}", ""]

    # Brand seeds (master controls, Designer-safe)
    brand = t["brand"]
    out += [
        "// ===== Brand seeds =================================",
        f"$brand-primary:     {brand['primary']} !default;",
        f"$brand-secondary:   {brand['secondary']} !default;",
        f"$brand-conversion:  {brand['conversion']} !default;",
        "",
    ]

    # Spacing scale
    out += [
        "// ===== Spacing (your grid, not Upgates 1/3-rem) ====",
        f"// Rule: {t['spacing']['grid_rule']}",
        scss_map("spacers", t["spacing"]["scale"]),
        "",
    ]

    # Type scale
    out += [
        "// ===== Type scale (fixed px) =======================",
        f"// Rule: {t['type']['base_scale_rule']}",
        scss_map("font-sizes", t["type"]["sizes"]),
        f"$scale-factor: {t['type']['scale_factor']} !default;",
        "",
    ]

    # Radius
    out += [
        "// ===== Radius ======================================",
        scss_map("radius-sizes", t["radius"]),
        "",
    ]

    # Shadows
    out += [
        "// ===== Shadows =====================================",
        scss_map("shadows", t["shadow"]),
        "",
    ]

    # Semantic color maps — these are the factory inputs
    out += ["// ===== Semantic color maps ======================"]
    colors = t["colors"]
    bg = colors["background"]
    fg_txt = colors["foreground_text"]
    txt = colors["text_separate"]

    # $colors-bg
    out.append(scss_map("colors-bg", bg))

    # $colors-fg-text (text on fg backgrounds)
    out.append("// foreground text on filled surfaces")
    out.append(scss_map("colors-fg-text", fg_txt))

    # $colors-button (filled button backgrounds)
    btn = {**bg}
    out.append("// button backgrounds (inherit bg palette by default)")
    out.append(scss_map("colors-button", btn))

    # $colors-text-separate / plain text roles
    out.append("// standalone / separated text")
    out.append(scss_map("colors-text-separate", txt))

    return "\n".join(out) + "\n"


def main() -> int:
    if not TOKENS.exists():
        print(f"missing tokens file: {TOKENS}", file=sys.stderr)
        return 1
    t = json.loads(TOKENS.read_text())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build(t))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
