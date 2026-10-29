# Všeprotisk Design System — Upgates custom-variables pipeline

Design-token overlay for Upgates' SCSS build. Maps one source of truth
(Figma → `tokens/design-tokens.json`) onto Upgates' `!default` variables so
the theme compiles with **your** values — no per-component CSS fighting.

## Why this works

Upgates provides a **custom-variables SCSS slot** that compiles BEFORE the
theme partials. Nearly every theme variable is `!default`, so anything you set
in that slot wins. This file lives in the slot. It emits token *values* into
Upgates' variable maps (`$spacers`, `$font-sizes`, `$radius-sizes`, `$shadows`,
`$colors-bg`, …); the platform's build factory then reproduces every component
from them as literals.

Verified against `vseprotisk.t2.upgates.shop` theme output (see
`docs/architecture.md`).

## The critical lever (confirm yours)

If the custom-variables slot compiles with the theme, this entire system works.
Sanity test once:

```scss
$colors-bg: ( "pr": #ff0000 ) !default;
```

Save in the slot, load homepage. A `.bg-pr` element turning red = levers on.

## Workflow

```
Figma (design)  →  tokens/design-tokens.json  →  dist/_variables.scss  →  Upgates slot
```

1. Edit `tokens/design-tokens.json` only. Never hand-edit `dist/_variables.scss`.
2. Rebuild: `python3 build/generate.py`
3. Paste `dist/_variables.scss` into the Upgates custom-variables SCSS slot.
4. Save / recompile in Designer. Verify on a staging shop first.

## Layout

```
tokens/design-tokens.json   source of truth (colors, spacing, type, radius, shadow)
build/generate.py           token -> Upgates-variable generator
dist/_variables.scss        GENERATED, paste into Upgates slot
docs/architecture.md        verified Upgates SCSS architecture & limits
```

## Conventions

- Generation uses a 4px grid, fixed px type scale, and explicit color maps —
  the three things Upgates' defaults do worst (see docs/architecture.md).
- Keep Designer admin as the blessed surface for what you don't override.
- Tier-3 residual overrides (token-ignoring components, JS-hardcoded SVG fills)
  stay in a separate `custom.scss` / head-injected stylesheet — never in the
  generated variables file.
