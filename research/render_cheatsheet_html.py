#!/usr/bin/env python3
"""Render intent-cheatsheet.json into a clean standalone HTML file for local viewing."""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "intent-cheatsheet.json"
OUT = ROOT / "upgates-intent-cheatsheet.html"

data = json.loads(SRC.read_text())

PATH_BADGE = {
    "slot":     ("✅", "slot",     "#e6f4ea", "#1e7e34"),
    "admin":    ("⚠️", "admin",    "#fef3e2", "#9a6a00"),
    "override": ("✋", "override", "#fdeaea", "#b00020"),
    "partial":  ("🔶", "partial",  "#e8f0fe", "#1a56db"),
}

rows_html = []
for it in data["intents"]:
    sym, label, bg, fg = PATH_BADGE.get(it["path"], ("❔", it["path"], "#eee", "#333"))
    var = html.escape(it.get("var", "—"))
    notes = html.escape(it.get("notes", ""))
    title = html.escape(it["intent"])
    rows_html.append(
        f"<tr><td class='intent'>{title}</td>"
        f"<td><span class='badge' style='background:{bg};color:{fg}'>{sym} {label}</span></td>"
        f"<td><code>{var}</code></td>"
        f"<td class='notes'>{notes}</td></tr>"
    )

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Upgates design-intent cheat sheet</title>
<style>
  :root {{ --ink:#1f2933; --mut:#6b7280; --line:#e5e7eb; --ac:#364153; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
         color:var(--ink); margin:0; padding:32px; background:#fafbfc; line-height:1.5; }}
  .wrap {{ max-width:1000px; margin:0 auto; }}
  h1 {{ font-size:26px; margin:0 0 4px; }}
  .sub {{ color:var(--mut); margin:0 0 20px; font-size:14px; }}
  .legend {{ background:#fff; border:1px solid var(--line); border-radius:10px; padding:16px 20px; margin-bottom:24px; }}
  .legend b {{ display:block; margin-bottom:8px; font-size:13px; text-transform:uppercase; letter-spacing:.04em; color:var(--mut); }}
  .legend ul {{ margin:0; padding-left:20px; font-size:14px; }}
  .legend li {{ margin:3px 0; }}
  table {{ width:100%; border-collapse:collapse; background:#fff; border-radius:10px; overflow:hidden;
          box-shadow:0 1px 3px rgba(0,0,0,.06); }}
  th {{ background:#f3f4f6; text-align:left; padding:12px 14px; font-size:12px; text-transform:uppercase;
       letter-spacing:.05em; color:var(--mut); border-bottom:1px solid var(--line); }}
  td {{ padding:12px 14px; border-bottom:1px solid var(--line); vertical-align:top; font-size:14px; }}
  tr:last-child td {{ border-bottom:none; }}
  td.intent {{ font-weight:600; }}
  td code {{ background:#f3f4f6; padding:2px 6px; border-radius:5px; font-size:12.5px; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  td.notes {{ color:var(--mut); font-size:13px; }}
  .badge {{ display:inline-block; padding:3px 10px; border-radius:999px; font-size:12.5px; font-weight:600; white-space:nowrap; }}
  @media (max-width:720px) {{ body{{padding:16px}} th{{font-size:11px}} .wrap{{overflow-x:auto}} }}
</style>
</head>
<body>
<div class="wrap">
  <h1>Upgates — design-intent cheat sheet</h1>
  <p class="sub">"Which of the ~686 SCSS variables can I change in the slot vs. the Designer admin vs. hand-override?" — {len(data["intents"])} design intents, mapped.</p>

  <div class="legend"><b>How to read it</b>
    <ul>
      <li><b>slot</b> — change it in the custom-variables SCSS slot. System-wide, no CSS.</li>
      <li><b>admin</b> — change it in the Designer admin UI (color / brand system). NOT the slot.</li>
      <li><b>override</b> — no variable covers it; write an <code>@layer override</code> CSS rule by hand.</li>
      <li><b>partial</b> — split across layers (see notes).</li>
    </ul>
    <p style="margin:10px 0 0;font-size:13px;color:var(--mut)">Rule of thumb: try the slot variable first; only hand-override when no variable exists.</p>
  </div>

  <table>
    <thead><tr><th>You want to change…</th><th>Path</th><th>Variable / where</th><th>Notes</th></tr></thead>
    <tbody>
      {''.join(rows_html)}
    </tbody>
  </table>
  <p class="sub" style="margin-top:18px">Generated from the raw Upgates SCSS variable dump. Re-run the mapper after any theme/Upgates update.</p>
</div>
</body>
</html>
"""
OUT.write_text(doc)
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
