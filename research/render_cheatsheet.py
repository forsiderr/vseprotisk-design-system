#!/usr/bin/env python3
"""Render intent-cheatsheet.json into a readable Markdown cheat sheet."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "intent-cheatsheet.json"
OUT = ROOT / "upgates-intent-cheatsheet.md"

data = json.loads(SRC.read_text())
out = [
    "# Upgates — design-intent cheat sheet",
    "",
    "**How to read the 'path' column:**",
    "- **slot** = change in the custom-variables SCSS slot (system-wide, no CSS).",
    "- **admin** = change in the Designer admin UI (color/brand system) — NOT the slot.",
    "- **override** = no variable covers it — hand-write an `@layer override` rule.",
    "",
    "> Tip: when in doubt, 'change it via slot variable first; only hand-override if",
    "> there is genuinely no variable.' This tool is the lookup that tells you which is which.",
    "",
    "| You want to change… | Path | Variable / where | Notes |",
    "|---|---|---|---|",
]
for it in data["intents"]:
    var = it.get("var", "—")
    path = it["path"]
    label = {"slot": "✅ slot", "admin": "⚠️ admin", "override": "✋ override", "partial": "🔶 partial"}.get(path, path)
    out.append(f"| **{it['intent']}** | {label} | `{var}` | {it.get('notes','')} |")

OUT.write_text("\n".join(out) + "\n")
print(f"wrote {OUT} ({len(data['intents'])} intents)")
