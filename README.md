# Všeprotisk design system — Upgates override layer

Pixel-perfect storefront redesign on Upgates, powered by **Penpot** designs and a
**single-owner external override layer**. See `docs/architecture.md` for the full
strategy and `research/` for the theme-analysis tooling.

## What this is

A system where the whole design system is built as an **external SCSS/CSS override
layer** (`@layer override`), decoupled from Upgates' variable/Designer quirks.
One owner, one pipeline: Penpot → override CSS → staging audit → live.

**Useful current artifacts:**
- `research/upgates-intent-cheatsheet.md` / `.html` — the "can I change X via
  slot variable or must I hand-override?" design-intent map (32 intents).
- `research/map_variables.py` — parse a raw `_variables.scss` dump into a
  per-variable reference (slot vs admin). Re-run on new themes.
- `tokens/design-tokens.json` — the `--vsp-*` token source (fill from Penpot).

## The guiding rule

> Try the variable/setting first; only hand-override when no variable exists.
> And because variables are entangled with Designer state we can't own, the
> override layer is the *primary* pointer for anything we want full control over.

## Layout

```
.hermes.md                  project context — auto-loaded in this repo
docs/architecture.md        settled strategy (v2)
research/                   live-theme analysis + cheat sheets
tokens/design-tokens.json   --vsp-* token source (Penpot home)
```
