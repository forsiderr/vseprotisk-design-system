# Upgates — design-intent cheat sheet

**How to read the 'path' column:**
- **slot** = change in the custom-variables SCSS slot (system-wide, no CSS).
- **admin** = change in the Designer admin UI (color/brand system) — NOT the slot.
- **override** = no variable covers it — hand-write an `@layer override` rule.

> Tip: when in doubt, 'change it via slot variable first; only hand-override if
> there is genuinely no variable.' This tool is the lookup that tells you which is which.

| You want to change… | Path | Variable / where | Notes |
|---|---|---|---|
| **button background color** | ⚠️ admin | `—` | $colors-button -> Designer color panel. Hover color via $btn-hover-bg-darken (slot, % darken) or hand-override. |
| **button hover state (darken amount)** | ✅ slot | `btn-hover-bg-darken` | $lightness-level %. Set darker/lighter directly. |
| **button padding** | ✅ slot | `btn-padding-y / btn-padding-x / btn-padding-xl-*` |  |
| **button radius** | ✅ slot | `btn-border-radius` | derived from border-radius-base(); often you must override radius-sizes or hand-CSS. |
| **button font weight/size** | ✅ slot | `btn-font-weight / font-sizes` |  |
| **button focus ring (width/opacity)** | ✅ slot | `input-btn-focus-width / input-btn-focus-opacity` |  |
| **button transition/animation** | ✅ slot | `btn-transition / btn-preloader-*` |  |
| **button text color** | ⚠️ admin | `—` | $colors-button-text-separate -> Designer. |
| **link hover (underline)** | ✅ slot | `link-hover-decoration / link-text-hover-decoration` |  |
| **link hover background tint** | ⚠️ admin | `link-hover-bg` | color system -> Designer. |
| **nav dropdown hover bg** | ⚠️ admin | `dropdown-link-hover-bg / nav-link-bg-hover / navbar-bg-hover` | all flow from $link-hover-bg -> Designer. |
| **heading sizes (H1-H6)** | ✅ slot | `hhg-font-size / h1-font-size / h2-font-size ...` | multiply $scale-factor; max sizes via *-max; growth via *-grow. |
| **body/global font size** | ✅ slot | `font-size-base / font-size-base-max` | elastic factor via font-size-elastic-*. |
| **global font family** | ✅ slot | `font-families / brand or admin` | $font-family-base likely admin; see font-family-base. |
| **spacing/whitespace rhythm** | ✅ slot | `spacers` | the whole 0-7 scale. Also gaps/gutters mirror it. |
| **page container max width** | ✅ slot | `container-xs/sm/md/lg/xl/xxl` |  |
| **grid gutters** | ✅ slot | `gutters / grid-gutter-width` | gutters=$spacers by default. |
| **navbar height** | ✅ slot | `navbar-height / navbar-height-sm / navbar-height-lg` |  |
| **product card image height** | ✅ slot | `products-list-img-height / products-list2-img-height` | fixed px; per-layout vars. |
| **card padding & radius** | ✅ slot | `card-padding-x / card-padding-y / card-border-radius` |  |
| **alert / status colors (success, danger, warning, info)** | ⚠️ admin | `colors` | Designer panel (upech/nebezpeci/upozorneni/info). |
| **badge (cart count) look** | ✅ slot | `badge-* (font-size, padding, min-width, radius)` |  |
| **input field height/padding** | ✅ slot | `input-padding-y / input-padding-x / input-height` |  |
| **input field background/color** | ⚠️ admin | `input-bg / input-color` | derive from color system -> Designer. |
| **modal width** | ✅ slot | `modal-dialog-width / modal-dialog-width-lg / -sm` |  |
| **dropdown menu width** | ✅ slot | `dropdown-width / dropdown-width-lg` |  |
| **shadow depth** | ✅ slot | `shadows (0/sm/md/lg/xl/xxl)` |  |
| **border radius scale** | ✅ slot | `radius-sizes (0/1/2/3/4)` | controls .ra-* utilities. |
| **carousel arrows/dots opacity** | ✅ slot | `carousel-nav-opacity / carousel-dot-opacity(-hover)` |  |
| **table cell padding** | ✅ slot | `table-cell-padding-y / -x` |  |
| **tooltip styling** | 🔶 partial | `tooltip-* (padding, radius) / tooltip-bg-color` | shape via slot; bg/text color via Designer. |
| **text selection color / focus color / active colors** | ⚠️ admin | `active / input-btn-focus-color` | brand-derived -> Designer. |
