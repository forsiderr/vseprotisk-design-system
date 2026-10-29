# Všeprotisk — Upgates design-system architecture (settled)

Version: 2.0 — encodes the final, agreed strategy. Supersedes the earlier
"custom-variables slot as primary lever" draft (v1), which is deliberately
removed as deprecated.

## The decision (lock this in)

**Single-owner, FULL override layer — Upgates variables are NOT the primary lever.**

Rationale, user-driven and validated across this engagement:
- Upgates variables/Designer-admin are entangled with **editor state I cannot own**.
  Setting `$spacers` etc. only feeds the theme's *defaults*; the rendered output
  resolves through the Designer admin's active option state (`designer-value()`
  pattern in the theme). Editing the file alone does not reliably control the
  result → splits the dev pipeline. Rejected.
- The **external override layer is the one surface decoupled from that state.**
  It writes directly to the compiled-output cascade (`@layer override`), so
  whatever Designer/variables resolve to, our layer wins by cascade position.
- Consequence: **one owner, one pipeline.** The user designs in Penpot → I build
  the override layer. There is no manual step they must repeat in the Designer.

## Injection path

- External SCSS/CSS pasted into `custom.scss` OR loaded via `<head>`.
- **Everything inside `@layer override { … }`** so it wins deterministically.
- The platform's compiled CSS (`_critical.scss.css` / `_after.scss.css`) both open
  with the cascade-layer declaration — the `override` layer is sanctioned and real.

## Update-survival strategy

Upgates' staging / test version of design gives an **audit window before live**.
Use it deliberately after every platform or theme update:

1. **Manual visual pass** — catches obvious breakage (button lost color, header
   collapsed).
2. **Class-check (lightweight contract)** — every selector the override layer
   references recorded in one list → probe the live/staging shop for each →
   flag any that no longer exist. Catches *subtle* breakage a visual pass misses
   (a spacing var drifting, padding shifting 4px, a closed gap).
3. Fix deliberately, then ship through the same staging → live flow.

The staging window provides the *time*; the class-check provides the *completeness*.

## Penpot → override pipeline (target)

```
Penpot designs
  ├─ design-tokens JSON  (W3C)   → maps into --vsp-* custom properties
  └─ per-screen images / SVG     → reference for building the override layer
        ↓
override layer (external, @layer override)
        ↓
custom.scss or <head>-injected, applied on staging → audit → promote to live
```

## Non-negotiables (operating rules)

1. **Ask before scaffolding/build tools** during strategy — deliver research +
   validated strategy first.
2. **Designer-first** — never edit theme template files; overlay CSS is the
   privileged surface.
3. **No `!important` towers, no full-theme rewrites.**
4. **Verify every rule by inspect** (right-click → Inspect → computed style → write
   → re-check). Re-inspect after every theme update. The survival contract.
5. **Target only theme selectors you have inspected, never guessed.**
6. **All values via `--vsp-*` custom properties**, one labeled section per visual
   concern. Restraint = small maintenance surface.

## What remains unresolved (verify when it matters)

- Whether the Design API can also write the Designer admin *color settings*
  (the pickers) vs. only code files. Decides if color ever joins the automated
  path; currently color would be a one-time manual Designer config **or** handled
  by the override layer's own rules (which we can do — the override layer is
  independent of the admin state).
- Exact `$brand-*` definitions and `designer-value()` semantics (base/settings
  partial not in our dump). Not blocking — the override layer does not depend on
  them.

## Repo layout

```
.hermes.md                  project context — auto-loaded when working in this repo
README.md                   quick orientation
docs/architecture.md        this file
tokens/design-tokens.json   --vsp-* token source (Penpot home, still to be filled)
research/                   live-theme analysis tooling + references
  map_variables.py          parse raw _variables.scss dump
  intent-cheatsheet.json    design-intent map (slot/admin/override/partial)
  upgates-intent-cheatsheet.* rendered cheat sheets
  upgates-variables-reference.md  full per-variable reference
  variables-index.json      mapper structured output
  _variables.scss           the theme variable dump (reference)
```
