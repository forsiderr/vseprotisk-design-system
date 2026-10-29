# Upgates SCSS architecture — verified findings

Analyzed live at `vseprotisk.t2.upgates.shop`. Compiled output:
`/_critical.scss.css`, `/_after.scss.css`. Source: Upgates custom-variables SCSS.

## Confirmed contract

1. **Custom-variables SCSS slot** compiles before theme partials and can
   override every `!default` variable. This is THE pixel-perfect lever.
2. `custom.scss` is for real SCSS rules, separate from the variables slot.
3. Theme uses **Bootstrap-4-architected `!default` maps**; semantic maps
   (`$colors-bg`, `$colors-text`, `$colors-fg-complete`, `$colors-fg-text`,
   `$colors-button`, `$colors-text-separate`, `$colors-dropdown-*`,
   `$colors-table-*`) iterate into utility/component classes.
4. Official compiled CSS declares cascade layers
   `base, modules, modules-override, templates, templates-override,
   utilities, utilities-override, override` — sanctioned override slot.
5. **Colors in compiled CSS are literals** (~514 hex/rgba in `_critical`). The
   `--colors-*` custom props are DEFINED but NEVER `var()`-consumed. So a
   runtime `:root{ --x: … }` overlay does NOT reskin colors — SCSS-layer
   variable override is required.

## Why out-of-the-box is "far from pixel-perfect"

| System | Upgates default | Problem vs a designed system |
|---|---|---|
| Colors | single-hue, `lighten/darken-max(...6%)` mechanical ramps | can't match a designed multi-step ramp |
| Spacing | `$spacers` = 1/3-rem steps (`.33334rem …`) | reads "off" against a 4/8px grid |
| Type | `em` scale + `$scale-factor` fluid vw growth | won't match a fixed px Figma scale |
| Radius | `$radius-sizes`: `0/.25rem/.45rem/2rem/50%` | arbitrary-ish |
| Shadow | auto multi-layer `shadow-multiple()` | not designed |

All five are **map overrides**, not CSS-rule fights -> the token pipeline.

## Strategy

- **Stage 1 (SCSS, 80%):** tokens.json -> custom-variables slot. Values in,
  factory out. No overlay CSS.
- **Stage 2 (runtime, residue):** small `@layer override` stylesheet for
  token-ignoring components / JS-hardcoded SVG fills. Versioned.
- **Designer admin** stays the blessed surface for brand seeds you don't take
  over.

## Unknowns / to verify per-instance
- Exact `$brand-primary/secondary/conversion` definitions (in a base/settings
  partial not included in this dump).
- Exact `designer-value()` semantics (bridges admin pickers -> build).
- Whether template design files are locked (decides template-bending levers).
- Whether the variables slot truly recompiles on save (2-min red test).
