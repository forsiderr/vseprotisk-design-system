# Upgates variables — designer reference

Source: `_variables.scss`  ·  686 variables parsed.

> **How to read this:** a variable is **slot-editable** when it is `!default`, NOT
> derived from a `$brand-*` seed, and NOT admin-linked (`designer-value()`).
> - ✅ **slot** = set it in the custom-variables slot.
> - ⚠️ **admin** = brand-derived or admin-linked → set it in the Designer UI,
>   not the slot.

## Cheat sheet — the basics you should rarely override in CSS

| Variable | Where to set | What it controls | Value |
|---|---|---|---|
| `colors-bg` | ⚠️ admin | Base background and text colors .bg-xxx | map[pr, se, co, de, des, dec, gr, re, ye, cy, bl, wh] |
| `colors-text` | ⚠️ admin |  | map[pr, se, co, de, des, dec, gr, re, ye, cy, wh, bl] |
| `colors-fg-text` | ⚠️ admin |  | map[pr, se, co, de, des, dec, wh] |
| `body-bg` | ⚠️ admin | Body body | `map-get($colors-bg, "wh") !default` (calculated) |
| `body-color` | ⚠️ admin |  | `map-get($colors-text-separate, "pr") !default` (calculated) |
| `spacers` | ✅ slot |  | map[0, 1, 2, 3, 4, 5, 6, 7] |
| `radius-sizes` | ✅ slot | .ras-xxx (responsive) | map[0, 1, 2, 3, 4] |
| `shadows` | ✅ slot |  | map[0, sm, md, lg, xl, xxl] |
| `font-sizes` | ✅ slot | em | map[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| `btn-padding-y` | ✅ slot | Buttons .btn | `$input-btn-padding-y !default` (calculated) |
| `navbar-height` | ✅ slot |  | 3.6rem !default |
| `products-list-img-height` | ✅ slot | Products list .p-i | 242px !default |

---

## COLOR SYSTEM

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `lightness-level` | ✅ slot | 6% !default |  |
| `text-saturation-max` | ✅ slot | `25% !default` (calculated) |  |
| `text-lightness-max` | ✅ slot | `25% !default` (calculated) |  |
| `text-lightness-level` | ✅ slot | 15% !default |  |
| `color-white` | ✅ slot | #fff !default | Base colors |
| `color-green` | ⚠️ admin | `$brand-green !default` (calculated) |  |
| `color-red` | ⚠️ admin | `$brand-red !default` (calculated) |  |
| `color-yellow` | ⚠️ admin | `$brand-yellow !default` (calculated) |  |
| `color-cyan` | ⚠️ admin | `$brand-cyan !default` (calculated) |  |
| `color-black` | ✅ slot | #000 !default |  |
| `primary-hue` | ⚠️ admin | `hue($brand-primary) !default` (calculated) | Color helpers |
| `primary-saturation` | ⚠️ admin | `saturation($brand-primary) !default` (calculated) |  |
| `primary-lightness` | ⚠️ admin | `lightness($brand-primary) !default` (calculated) |  |
| `secondary-hue` | ⚠️ admin | `hue($brand-secondary) !default` (calculated) |  |
| `secondary-saturation` | ⚠️ admin | `saturation($brand-secondary) !default` (calculated) |  |
| `secondary-lightness` | ⚠️ admin | `lightness($brand-secondary) !default` (calculated) |  |
| `conversion-hue` | ⚠️ admin | `hue($brand-conversion) !default` (calculated) |  |
| `conversion-saturation` | ⚠️ admin | `saturation($brand-conversion) !default` (calculated) |  |
| `conversion-lightness` | ⚠️ admin | `lightness($brand-conversion) !default` (calculated) |  |
| `primary-default-saturation` | ⚠️ admin | `designer-value($primary-saturation-designer, $primary-saturation) !default` (calculated) | Color helpers |
| `primary-default-lightness` | ⚠️ admin | `designer-value($primary-lightness-designer, 100%-$lightness-level) !default` (calculated) |  |
| `secondary-default-saturation` | ⚠️ admin | `designer-value($secondary-saturation-designer, $secondary-saturation) !default` (calculated) |  |
| `secondary-default-lightness` | ⚠️ admin | `designer-value($secondary-lightness-designer, $primary-default-lightness) !default` (calculated) |  |
| `conversion-default-saturation` | ⚠️ admin | `designer-value($conversion-saturation-designer, $conversion-saturation) !default` (calculated) |  |
| `conversion-default-lightness` | ⚠️ admin | `designer-value($conversion-lightness-designer, $primary-default-lightness) !default` (calculated) |  |
| `color-bg-primary` | ⚠️ admin | `$brand-primary !default` (calculated) | Background colors |
| `color-bg-primary-light` | ⚠️ admin | `lighten($color-bg-primary, $lightness-level) !default` (calculated) |  |
| `color-bg-primary-dark` | ⚠️ admin | `darken-max($color-bg-primary, $lightness-level) !default` (calculated) |  |
| `color-bg-secondary` | ⚠️ admin | `$brand-secondary !default` (calculated) |  |
| `color-bg-secondary-light` | ⚠️ admin | `lighten($color-bg-secondary, $lightness-level) !default` (calculated) |  |
| `color-bg-secondary-dark` | ⚠️ admin | `darken-max($color-bg-secondary, $lightness-level) !default` (calculated) |  |
| `color-bg-conversion` | ⚠️ admin | `$brand-conversion !default` (calculated) |  |
| `color-bg-conversion-light` | ⚠️ admin | `lighten($color-bg-conversion, $lightness-level) !default` (calculated) |  |
| `color-bg-conversion-dark` | ⚠️ admin | `darken-max($color-bg-conversion, $lightness-level) !default` (calculated) |  |
| `color-fg-primary` | ⚠️ admin | `$brand-primary !default` (calculated) | Foreground colors |
| `color-fg-primary-light` | ⚠️ admin | `lighten($color-fg-primary, $lightness-level) !default` (calculated) |  |
| `color-fg-primary-dark` | ⚠️ admin | `darken-max($color-fg-primary, $lightness-level) !default` (calculated) |  |
| `color-fg-secondary` | ⚠️ admin | `$brand-secondary !default` (calculated) |  |
| `color-fg-secondary-light` | ⚠️ admin | `lighten($color-fg-secondary, $lightness-level) !default` (calculated) |  |
| `color-fg-secondary-dark` | ⚠️ admin | `darken-max($color-fg-secondary, $lightness-level) !default` (calculated) |  |
| `color-fg-conversion` | ⚠️ admin | `$brand-conversion !default` (calculated) |  |
| `color-fg-conversion-light` | ⚠️ admin | `lighten($color-fg-conversion, $lightness-level) !default` (calculated) |  |
| `color-fg-conversion-dark` | ⚠️ admin | `darken-max($color-fg-conversion, $lightness-level) !default` (calculated) |  |
| `color-default` | ⚠️ admin | `hsl($primary-hue, $primary-default-saturation, $primary-default-lightness) !default` (calculated) | Default colors |
| `color-default-light` | ⚠️ admin | `lighten($color-default, ($lightness-level * .5)) !default` (calculated) |  |
| `color-default-dark` | ⚠️ admin | `darken-max($color-default, $lightness-level) !default` (calculated) |  |
| `color-default-s` | ⚠️ admin | `hsl($secondary-hue, $secondary-default-saturation, $secondary-default-lightness) !default` (calculated) | Default colors from secondary |
| `color-default-s-light` | ⚠️ admin | `lighten($color-default-s, ($lightness-level * .5)) !default` (calculated) |  |
| `color-default-s-dark` | ⚠️ admin | `darken-max($color-default-s, $lightness-level) !default` (calculated) |  |
| `color-default-c` | ⚠️ admin | `hsl($conversion-hue, $conversion-default-saturation, $conversion-default-lightness) !default` (calculated) | Default colors from conversion |
| `color-default-c-light` | ⚠️ admin | `lighten($color-default-c, ($lightness-level * .5)) !default` (calculated) |  |
| `color-default-c-dark` | ⚠️ admin | `darken-max($color-default-c, $lightness-level) !default` (calculated) |  |
| `color-text-primary` | ⚠️ admin | `hsl($primary-hue, saturation-max($brand-primary, $text-saturation-max), lightness-max($brand-primary, $text-lightness-max)) !default` (calculated) | Text colors |
| `color-text-primary-light` | ⚠️ admin | `lighten($color-text-primary, $text-lightness-level) !default` (calculated) |  |
| `color-text-primary-dark` | ⚠️ admin | `darken-max($color-text-primary, $text-lightness-level) !default` (calculated) |  |
| `color-text-secondary` | ⚠️ admin | `hsl($secondary-hue, $secondary-saturation, lightness-max($brand-secondary, $text-lightness-max)) !default` (calculated) |  |
| `color-text-secondary-light` | ⚠️ admin | `lighten($color-text-secondary, $text-lightness-level) !default` (calculated) |  |
| `color-text-secondary-dark` | ⚠️ admin | `darken-max($color-text-secondary, $text-lightness-level) !default` (calculated) |  |
| `color-text-conversion` | ⚠️ admin | `hsl($conversion-hue, $conversion-saturation, lightness-max($brand-conversion, $text-lightness-max)) !default` (calculated) |  |
| `color-text-conversion-light` | ⚠️ admin | `lighten($color-text-conversion, $text-lightness-level) !default` (calculated) |  |
| `color-text-conversion-dark` | ⚠️ admin | `darken-max($color-text-conversion, $text-lightness-level) !default` (calculated) |  |
| `color-text-default-p` | ⚠️ admin | `$color-default !default` (calculated) |  |
| `color-text-default-s` | ⚠️ admin | `$color-default-s !default` (calculated) |  |
| `color-text-default-c` | ⚠️ admin | `$color-default-c !default` (calculated) |  |
| `designer-colors` | ⚠️ admin | map[primary, secondary, conversion, primaryLight, secondaryLight, conversionLight, green, red, yellow, cyan, black, white] |  |
| `designer-text-colors` | ⚠️ admin | map[primaryN, primary, secondaryN, secondary, conversionN, conversion, primaryLight, secondaryLight, conversionLight, green, red, yellow, cyan, black, white] |  |
| `designer-class-text-colors` | ⚠️ admin | map[prn, pr, sen, se, con, co, de, des, dec, gr, re, ye, cy, bl, wh] |  |
| `color-required` | ⚠️ admin | `map-get($designer-text-colors, $brand-required) !default` (calculated) | Action colors |
| `color-success` | ⚠️ admin | `map-get($designer-colors, $brand-success) !default` (calculated) |  |
| `color-danger` | ⚠️ admin | `map-get($designer-colors, $brand-danger) !default` (calculated) |  |
| `color-warning` | ⚠️ admin | `map-get($designer-colors, $brand-warning) !default` (calculated) |  |
| `color-info` | ⚠️ admin | `map-get($designer-colors, $brand-info) !default` (calculated) |  |
| `color-facebook-bg` | ✅ slot | #4267b2 !default | Other colors |
| `color-facebook-text` | ✅ slot | #fff !default |  |
| `color-facebook-border-width` | ✅ slot | `0 !default` (calculated) |  |
| `color-facebook-border-color` | ✅ slot | `unset !default` (calculated) |  |
| `color-google-bg` | ✅ slot | #fff !default |  |
| `color-google-text` | ✅ slot | #1f1f1f !default |  |
| `color-google-border-width` | ✅ slot | `1px !default` (calculated) |  |
| `color-google-border-color` | ✅ slot | `#747775 !default` (calculated) |  |
| `color-seznam-bg` | ✅ slot | #CC0000 !default |  |
| `color-seznam-text` | ✅ slot | #fff !default |  |
| `color-seznam-border-width` | ✅ slot | `0 !default` (calculated) |  |
| `color-seznam-border-color` | ✅ slot | `unset !default` (calculated) |  |
| `color-diff-lighten` | ✅ slot | 25% !default | Lighten amount, if element is not visible enough on the |
| `color-theme-interval` | ✅ slot | 8% !default | Set a specific jump point for requesting color jumps |
| `yiq-contrasted-threshold` | ✅ slot | 200 !default | The yiq lightness value that determines when the lightn |
| `yiq-text-light` | ✅ slot | `$color-white !default` (calculated) |  |
| `yiq-text-dark` | ⚠️ admin | `$color-text-primary !default` (calculated) |  |
| `colors-bg` | ⚠️ admin | map[pr, se, co, de, des, dec, gr, re, ye, cy, bl, wh] | Base background and text colors .bg-xxx |
| `color-bg-primary-secondary-diff` | ⚠️ admin | `color-diff($color-bg-primary, $color-bg-secondary, $yiq-contrasted-threshold) !default` (calculated) |  |
| `colors-text` | ⚠️ admin | map[pr, se, co, de, des, dec, gr, re, ye, cy, wh, bl] |  |
| `colors-fg` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] |  |
| `colors-fg-complete` | ⚠️ admin | map[pr, se, co, de, des, dec, gr, re, ye, cy, bl, wh] |  |
| `colors-fg-text` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] |  |
| `colors-section` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] | Section colors .b.bg-xxx |
| `colors-text-separate` | ⚠️ admin | map[pr, prn, se, sen, co, con, de, des, dec, mu, inh, gr, re, ye, cy, bl, wh] | Text colors (for colors without background effects) .c- |
| `colors-text-muted-opacity` | ✅ slot | .6 !default | Text muted (for unimportant texts) .b.bg-xxx .c-mu |
| `text-muted-color-base` | ✅ slot | `rgba($color-white, $colors-text-muted-opacity) !default` (calculated) |  |
| `colors-text-muted` | ⚠️ admin | map[pr, se, co, gr, re, ye, cy, de, des, dec, bl, wh] |  |
| `link-decoration` | ✅ slot | none !default | Links .b.bg-xxx a |
| `link-hover-decoration` | ✅ slot | underline !default |  |
| `link-texts-decoration` | ✅ slot | underline !default |  |
| `link-text-hover-decoration` | ✅ slot | none !default |  |
| `link-hover-bg` | ⚠️ admin | `rgba($color-bg-primary-dark, .075) !default` (calculated) |  |
| `link-hover-bg-dark` | ✅ slot | `rgba($color-black, .2) !default` (calculated) |  |
| `link-cursor` | ✅ slot | pointer !default |  |
| `link-underline-offset` | ✅ slot | .2em !default |  |
| `colors-link-text` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] |  |
| `colors-link-text-hover` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] |  |
| `disabled-opacity` | ✅ slot | .5 !default | Disabled elements .disabled |

## BASE

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `z-indexes` | ✅ slot | map[n10, n1, un, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50] | Z-index .zin-xxx |
| `zindex-dropdown` | ✅ slot | 1000 !default |  |
| `zindex-fixed` | ✅ slot | 1010 !default |  |
| `zindex-tooltip` | ✅ slot | 1020 !default |  |
| `zindex-popover` | ✅ slot | 1030 !default |  |
| `zindex-overlay` | ✅ slot | 1040 !default |  |
| `zindex-sidebar` | ✅ slot | 1050 !default |  |
| `zindex-modal-backdrop` | ✅ slot | 1060 !default |  |
| `zindex-modal` | ✅ slot | 1070 !default |  |
| `zindex-lightbox` | ✅ slot | 1080 !default |  |
| `scroll-bar-width` | ✅ slot | 15px !default | Scrollbar width |
| `body-bg` | ⚠️ admin | `map-get($colors-bg, "wh") !default` (calculated) | Body body |
| `body-color` | ⚠️ admin | `map-get($colors-text-separate, "pr") !default` (calculated) |  |
| `column-width` | ✅ slot | 25vw !default | Column sizes .column |
| `column-max-width` | ✅ slot | 300px !default |  |
| `column-max-width-md` | ✅ slot | 320px !default |  |
| `column-max-width-lg` | ✅ slot | 430px !default |  |
| `column-sticky-position` | ✅ slot | sticky !default |  |

## SIZING

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `min-width-sizes` | ✅ slot | map[0, 1, 2, 3, 4] | Min width .min-w-xxx (responsive) |
| `max-width-sizes` | ✅ slot | map[xxs, xs, sm, md, lg, xl, xxl, fluid] | Max width .max-w-xxx (responsive) |
| `min-height-sizes` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] | Min height .min-h-xxx (responsive) |
| `max-height-sizes` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, fluid] | Max height .max-h-xxx (responsive) |

## SPACERS

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `section-y` | ✅ slot | `3.3334rem * 0.5 * $condensed !default` (calculated) |  |
| `spacers` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6, 7] |  |
| `spacers-negative` | ✅ slot | map[1, 2, 3, 4, 5, 6, 7] |  |
| `space-ico` | ✅ slot | `map-get($spacers, "1") !default` (calculated) |  |
| `space-ico-lg` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `gutters` | ✅ slot | `$spacers !default` (calculated) |  |
| `gaps` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6] |  |
| `px` | ✅ slot | 15px !default | px |
| `sizes` | ✅ slot | map[0, 20, 25, 33, 40, 50, 75, 100, auto] | Width, Height .w-xxx, .h-xxx (responsive) |

## COMPONENTS

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `bg-overlays` | ✅ slot | map[bl, cy, re, gr, ye, wh] | Background overlays .bov-xxx-o-xxx |
| `bg-overlay-opacities` | ✅ slot | map[5, 10, 20, 40, 60, 80, 100] |  |
| `bg-gradient-default-direction` | ✅ slot | 180deg !default | Background gradients .bgr-xxx |
| `bg-gradient-size-md` | ✅ slot | 75% !default |  |
| `bg-gradient-size-lg` | ✅ slot | 100% !default |  |
| `bg-gradient-directions` | ✅ slot | map[l1, l2, l3, l4, l5, l6, l7, l8, r9, r10] |  |
| `background-sizes` | ✅ slot | map[cov, cont, act, str] | Background size .bsi-xxx (responsive) |
| `background-positions` | ✅ slot | map[c, t, b, l, r, tl, bl, tr, br] | Background positions .bpo-xxx (responsive) |
| `background-repeats` | ✅ slot | map[xy, x, y, s, r, n] | Background repeats .bre-xxx (responsive) |
| `blends` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] | Blends .blend-xxx (responsive) |
| `hues` | ✅ slot | map[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 350] | Hues .fil-hu-xxx |
| `saturations` | ✅ slot | map[0, 100] | Saturation .fil-sa-xxx |
| `brightnesses` | ✅ slot | map[0, 100] | Brightness .fil-br-xxx |
| `contrasts` | ✅ slot | map[0, 100] | Contrast .fil-co-xxx |
| `inverts` | ✅ slot | map[0] | Invert .fil-in-xxx |
| `sepias` | ✅ slot | map[0] | Sepia .fil-se-xxx |
| `opacities` | ✅ slot | map[0, 60] | Opacity .fil-op-xxx (responsive) |
| `blurs` | ✅ slot | map[0, 20] |  |
| `visibilities` | ✅ slot | map[h, v] | Visibility .vis-xxx (responsive) |
| `line-height-sizes` | ✅ slot | map[0, xs, sm, md, lg, xl, xxl] | Line height .lh-xxx (responsive) |
| `line-height-heading` | ✅ slot | `map-get($line-height-sizes, "xs") !default` (calculated) |  |
| `border-positions` | ✅ slot | map[t, r, b, l] | Border .bo-xxx-xxx (responsive) |
| `border-sizes` | ✅ slot | map[0, 1, 2, d] |  |
| `border-sizes-reset` | ✅ slot | `-$border-size-base !default` (calculated) |  |
| `border-styles` | ✅ slot | map[so, da, do] | .bos- |
| `border-contrast-ratio` | ✅ slot | `.085 !default` (calculated) | Border colors |
| `border-lightness-max` | ✅ slot | `50% !default` (calculated) |  |
| `radius-positions` | ✅ slot | map[tl, tr, br, bl] | Border radius .ra-xxx-xxx (responsive) |
| `radius-sizes` | ✅ slot | map[0, 1, 2, 3, 4] | .ras-xxx (responsive) |
| `radius-rounded-max` | ✅ slot | 1.3em !default |  |
| `outer-size` | ✅ slot | `map-get($border-sizes, "2") !default` (calculated) | Outer .ou |
| `overlay-bg` | ✅ slot | `rgba($color-black, .5) !default` (calculated) | Overlay |
| `overlay-bg-full` | ✅ slot | `0 0 0 200vw $overlay-bg !default` (calculated) |  |
| `overlay-bg-bottom` | ✅ slot | `0 200vw 0 calc(200vw - 1px) $overlay-bg !default` (calculated) |  |
| `shadows-left` | ✅ slot | map[sm] | Shadow .sh-xxx |
| `shadows-top` | ✅ slot | map[sm] |  |
| `shadows-blur` | ✅ slot | map[sm] |  |
| `shadows-color` | ✅ slot | map[sm] |  |
| `shadows-top-multiple` | ✅ slot | 2 !default |  |
| `shadows-blur-multiple` | ✅ slot | 3 !default |  |
| `shadows` | ✅ slot | map[0, sm, md, lg, xl, xxl] |  |
| `shadow-texts-left` | ✅ slot | map[sm] | Text shadow .sht-xxx |
| `shadow-texts-top` | ✅ slot | map[sm] |  |
| `shadow-texts-blur` | ✅ slot | map[sm] |  |
| `shadow-texts-color` | ✅ slot | map[sm] |  |
| `shadow-texts` | ✅ slot | map[0, sm, md, lg] |  |
| `rotates` | ✅ slot | map[1, 6, 10] | Transform .tra-  Rotate .tra-rox-xxx... |
| `scales` | ✅ slot | map[0, 90, 140] | Scale .tra-scx-xxx, .tra-scy-xxx |
| `translates` | ✅ slot | map[1, 6, 12, 18] | Translate .tra-trx-xxx, .tra-try-xxx |
| `skews` | ✅ slot | map[1, 6, 11] | Skew .tra-skx-xxx, .tra-sky-xxx |
| `origins-x` | ✅ slot | map[l] | Origin .ori-x-xxx, .ori-y-xxx |
| `origins-y` | ✅ slot | map[t] |  |
| `float-sizes` | ✅ slot | map[…] | Float .float-xxx (responsive) |
| `positions` | ✅ slot | map[…] | Position .pos-xxx (responsive) |
| `overflows` | ✅ slot | map[…] | Overflow .ovx-xxx, .ovy-xxx (responsive) |
| `caret-opacity` | ✅ slot | null !default | .caret |
| `hr-border-width` | ✅ slot | `map-get($border-sizes, "1") !default` (calculated) | hr - horizontal rule |
| `hr-border-width-lg` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) |  |
| `hr-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `hr-margin-y` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `duration` | ✅ slot | .25s !default | Effects duration |
| `duration-longer` | ✅ slot | .5s !default |  |
| `duration-longest` | ✅ slot | .75s !default |  |
| `transition-base` | ✅ slot | `all $duration ease-out !default` (calculated) | .trans |
| `transition-fade` | ✅ slot | `opacity $duration linear !default` (calculated) |  |
| `collapse-btn-margin-bottom` | ✅ slot | `map-get($spacers, "5") !default` (calculated) | .collapse |
| `collapse-transition` | ✅ slot | `height $duration ease-out !default` (calculated) |  |
| `collapse-icon-rotate` | ✅ slot | `$duration-longer !default` (calculated) |  |
| `active` | ⚠️ admin | `map-get($designer-colors, $brand-active) !default` (calculated) | .active |
| `active-inverse` | ⚠️ admin | `color-yiq($active) !default` (calculated) |  |
| `active-text-separate` | ⚠️ admin | `$active !default` (calculated) |  |
| `active-label-size-x` | ✅ slot | `map-get($border-sizes, "d") + 2 !default` (calculated) | .active:before |
| `active-label-size-y` | ✅ slot | `map-get($border-sizes, "d") + 3 !default` (calculated) |  |
| `font-family-sans-serif` | ✅ slot | -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !default | Fonts |
| `font-family-monospace` | ✅ slot | SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace !default |  |
| `font-family-icon` | ✅ slot | 'FontAwesome' !default |  |
| `font-families` | ✅ slot | map[base, adv] |  |
| `font-family-break` | ✅ slot | sm !default | Show custom font from breakpoint |
| `font-size-base-max` | ✅ slot | 1.0789 !default | Font size .fs-xxx (responsive) |
| `font-sizes` | ✅ slot | map[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | em |
| `font-size-elastic-multiple` | ✅ slot | .845 !default | Font elastic .fse-xxx |
| `font-size-elastic-expand-elastic` | ✅ slot | .25vw !default |  |
| `font-weight-bold` | ✅ slot | `font-weight-bold($font-weight-base) !default` (calculated) | Font weight .fw-xxx |
| `font-weight-heading-bold` | ✅ slot | `font-weight-bold($font-weight-heading-base) !default` (calculated) |  |
| `font-weights` | ✅ slot | map[l, r, m, b, br] |  |
| `letter-spacing-base` | ✅ slot | 0 !default | Letter spacing .ls-xxx |
| `letter-spacing-heading-base` | ✅ slot | 0 !default |  |
| `letter-spacing-sizes` | ✅ slot | map[n7, n2, 3] |  |
| `paragraph-margin-bottom` | ✅ slot | `map-get($spacers, "3") !default` (calculated) | Type p, ul, ol, small, abbr, address, dt, dd, sub, sup |
| `ul-ol-align` | ✅ slot | left !default |  |
| `small-font-size` | ✅ slot | smaller !default |  |
| `small-font-weight` | ✅ slot | `map-get($font-weights, "r") !default` (calculated) |  |
| `small-letter-spacing` | ✅ slot | `map-get($letter-spacing-sizes, "0") !default` (calculated) |  |
| `abbr-text-decoration` | ✅ slot | underline !default |  |
| `abbr-text-decoration-style` | ✅ slot | dotted !default |  |
| `abbr-decoration-thickness` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) |  |
| `abbr-cursor` | ✅ slot | help !default |  |
| `address-font-style` | ✅ slot | normal !default |  |
| `dt-font-weight` | ✅ slot | `$font-weight-base !default` (calculated) |  |
| `dd-margin-bottom` | ✅ slot | .5rem !default |  |
| `sub-sup-font-size` | ✅ slot | 75% !default |  |
| `sub-bottom` | ✅ slot | -.25em !default |  |
| `sup-top` | ✅ slot | -.5rem !default |  |
| `headings-line-height` | ✅ slot | `$line-height-heading !default` (calculated) | Headings h1..h6, card-header ... |
| `headings-margin-bottom` | ✅ slot | .65em !default |  |
| `headings-small-font-size` | ✅ slot | 65% !default |  |
| `hhg-font-size` | ✅ slot | `2em * $scale-factor !default` (calculated) |  |
| `h1-font-size` | ✅ slot | `1.5em * $scale-factor !default` (calculated) |  |
| `h2-font-size` | ✅ slot | `1.3em * $scale-factor !default` (calculated) |  |
| `h3-font-size` | ✅ slot | `1em * $scale-factor !default` (calculated) |  |
| `h4-font-size` | ✅ slot | `.8em * $scale-factor !default` (calculated) |  |
| `h5-font-size` | ✅ slot | `0.7585em * $scale-factor !default` (calculated) |  |
| `h6-font-size` | ✅ slot | `0.69em * $scale-factor !default` (calculated) |  |
| `hhg-font-size-max` | ✅ slot | `3.5em * $scale-factor !default` (calculated) |  |
| `h1-font-size-max` | ✅ slot | `2.115em * $scale-factor !default` (calculated) |  |
| `h2-font-size-max` | ✅ slot | `1.471em * $scale-factor !default` (calculated) |  |
| `h3-font-size-max` | ✅ slot | `1.15em * $scale-factor !default` (calculated) |  |
| `h4-font-size-max` | ✅ slot | `0.9655em * $scale-factor !default` (calculated) |  |
| `hhg-font-size-grow` | ✅ slot | 1.5 !default |  |
| `h1-font-size-grow` | ✅ slot | 1.25 !default |  |
| `h2-font-size-grow` | ✅ slot | 1.15 !default |  |
| `h3-font-size-grow` | ✅ slot | 1.1 !default |  |
| `h4-font-size-grow` | ✅ slot | 1.1 !default |  |
| `h5-font-size-grow` | ✅ slot | false !default |  |
| `h6-font-size-grow` | ✅ slot | false !default |  |
| `hhg-line-height` | ✅ slot | 1 !default |  |
| `hhg-margin-bottom` | ✅ slot | .3em !default |  |
| `h1-margin-bottom` | ✅ slot | .4em !default |  |
| `ic-size` | ✅ slot | 1em !default | Icons .ic |
| `ic-size-sm` | ✅ slot | .75em !default |  |
| `min-ic-size` | ✅ slot | 1.3em !default |  |
| `ico-border-radius` | ✅ slot | `border-radius-base($rounded: 'circle') !default` (calculated) | .ico-xxx |
| `ico-img-size` | ✅ slot | `map-get($sizes, "50") !default` (calculated) |  |
| `ico-font-sizes` | ✅ slot | map[sm, md, lg, xl] |  |
| `ico-sizes` | ✅ slot | map[sm, md, lg, xl] |  |
| `icon-text-gap` | ✅ slot | `$space-ico !default` (calculated) | .icon-text |
| `icon-text-transition` | ✅ slot | `transform $duration ease-in-out !default` (calculated) |  |
| `icon-text-transform-top` | ✅ slot | 10% !default |  |
| `icon-text-transform-right` | ✅ slot | .25em !default |  |
| `no-item-font-size` | ✅ slot | `map-get($font-sizes, "6") !default` (calculated) | No item .no-item |
| `no-item-padding-y` | ✅ slot | `map-get($spacers, "5") !default` (calculated) |  |
| `no-item-opacity` | ✅ slot | .4 !default |  |
| `no-item-gap` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `text-decorations` | ✅ slot | map[lt, u, n] | Text decoration .td-xxx |
| `text-transforms` | ✅ slot | map[l, u, c] | Text transform .tt-xxx |
| `hlt-border-width` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) | Heading line through .hlt |
| `hlt-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `hlt-gap` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `hlt-line-space-x` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `enable-print-styles` | ✅ slot | true !default | Printing |
| `print-bg-color` | ✅ slot | `$color-white !default` (calculated) |  |
| `print-text-color` | ✅ slot | `$color-black !default` (calculated) |  |
| `print-border` | ⚠️ admin | `map-get($border-sizes, "d") solid desaturate($color-fg-primary-light, 100%) !default` (calculated) |  |
| `print-page-size` | ✅ slot | a3 !default |  |
| `print-body-min-width` | ✅ slot | `map-get($grid-breakpoints, "lg") !default` (calculated) |  |
| `print-img-width` | ✅ slot | 360px !default |  |

## FORMS

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `form-text-margin-top` | ✅ slot | `map-get($spacers, "1") !default` (calculated) |  |
| `form-align-spinner-xs` | ✅ slot | center !default |  |
| `form-align-spinner` | ✅ slot | `$form-align-spinner-xs !default` (calculated) |  |
| `form-width-small-xs` | ✅ slot | 7em !default |  |
| `form-width-small-md` | ✅ slot | 5.5em !default |  |
| `label-space-bottom` | ✅ slot | `map-get($spacers, "3") / 2 !default` (calculated) | label |
| `input-btn-padding-y` | ✅ slot | .75rem !default | Buttons + Forms shared |
| `input-btn-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `input-btn-line-height` | ✅ slot | `map-get($line-height-sizes, "sm") !default` (calculated) |  |
| `input-btn-focus-opacity` | ✅ slot | .5 !default |  |
| `input-btn-focus-width` | ✅ slot | .2rem !default |  |
| `input-btn-focus-color` | ⚠️ admin | `rgba($active, $input-btn-focus-opacity) !default` (calculated) |  |
| `input-btn-focus-box-shadow` | ⚠️ admin | `0 0 0 $input-btn-focus-width $input-btn-focus-color !default` (calculated) |  |
| `input-btn-focus-box-shadow-alternative` | ⚠️ admin | `0 0 0 $input-btn-focus-width rgba($active-inverse, $input-btn-focus-opacity) !default` (calculated) |  |
| `btn-padding-y` | ✅ slot | `$input-btn-padding-y !default` (calculated) | Buttons .btn |
| `btn-padding-x` | ✅ slot | `$input-btn-padding-x !default` (calculated) |  |
| `btn-padding-xl-y` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `btn-padding-xl-x` | ✅ slot | `map-get($spacers, "5") !default` (calculated) |  |
| `btn-gap` | ✅ slot | `$space-ico-lg !default` (calculated) |  |
| `btn-line-height` | ✅ slot | `$input-btn-line-height !default` (calculated) |  |
| `btn-font-weight` | ✅ slot | `map-get($font-weights, "r") !default` (calculated) |  |
| `btn-border-width` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) |  |
| `btn-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `btn-focus-box-shadow` | ⚠️ admin | `0 0 0 $input-btn-focus-width $input-btn-focus-color !default` (calculated) |  |
| `btn-disabled-opacity` | ✅ slot | `$disabled-opacity !default` (calculated) |  |
| `btn-border-radius` | ✅ slot | `border-radius-base() !default` (calculated) |  |
| `btn-hover-bg-darken` | ✅ slot | `$lightness-level !default` (calculated) |  |
| `btn-active-shadow` | ✅ slot | none !default |  |
| `btn-transition` | ✅ slot | `$transition-base !default` (calculated) |  |
| `btn-group-border-radius-reset` | ✅ slot | `0 !default` (calculated) | Button group |
| `btn-block-width-xs` | ✅ slot | 100% !default | .btn-max |
| `btn-block-width` | ✅ slot | 90% !default |  |
| `btn-max-width` | ✅ slot | 19em !default |  |
| `btn-preloader-animation` | ✅ slot | ic-spin 2s infinite linear !default | Button preloader |
| `btn-preloader-cursor` | ✅ slot | not-allowed !default |  |
| `colors-button` | ⚠️ admin | map[pr, se, co, de, des, dec, gr, ye, re, cy, bl, wh] |  |
| `colors-button-text-separate` | ⚠️ admin | map[pr, se, co, gr, ye, re, cy, bl, wh] |  |
| `input-bg` | ⚠️ admin | `$color-default !default` (calculated) | Inputs .form-control |
| `input-color` | ⚠️ admin | `$body-color !default` (calculated) |  |
| `input-padding-y` | ✅ slot | `$input-btn-padding-y !default` (calculated) |  |
| `input-padding-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `input-font-size` | ✅ slot | `map-get($font-sizes, "3") !default` (calculated) |  |
| `input-font-size-sm` | ✅ slot | `map-get($font-sizes, "2") !default` (calculated) |  |
| `input-line-height` | ✅ slot | `$input-btn-line-height !default` (calculated) |  |
| `input-border-width` | ✅ slot | `0 !default` (calculated) |  |
| `input-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `input-border-radius` | ✅ slot | `border-radius-base() !default` (calculated) |  |
| `input-min-width` | ✅ slot | 235px !default |  |
| `input-placeholder-lighten` | ✅ slot | .5 !default |  |
| `input-disabled-style` | ✅ slot | italic !default |  |
| `input-disabled-cursor` | ✅ slot | not-allowed !default |  |
| `input-disabled-opacity` | ✅ slot | `$disabled-opacity !default` (calculated) |  |
| `input-transition` | ✅ slot | `border-color .15s ease-in-out, box-shadow .15s ease-in-out, background-color $duration ease-in-out !default` (calculated) |  |
| `input-focus-width` | ✅ slot | `$input-btn-focus-width !default` (calculated) |  |
| `input-focus-box-shadow` | ⚠️ admin | `0 0 0 $input-focus-width $input-btn-focus-color !default` (calculated) |  |
| `input-icon-size` | ✅ slot | 1em !default | .input-icon |
| `input-icon-margin-right` | ✅ slot | `$input-btn-padding-x !default` (calculated) |  |
| `col-form-label-line-height` | ✅ slot | `map-get($line-height-sizes, "sm") !default` (calculated) | .col-form-label |
| `col-form-label-padding-top` | ✅ slot | `$input-padding-y * 1.2 !default` (calculated) |  |
| `col-form-checkbox-label-padding-top` | ✅ slot | .1rem !default |  |
| `col-form-label-align-base` | ✅ slot | right !default |  |
| `input-group-line-height` | ✅ slot | `$input-line-height !default` (calculated) | Input group .input-group |
| `input-group-right-overlap` | ✅ slot | 2.5em !default |  |
| `input-group-right-overlap-back` | ✅ slot | `-$input-group-right-overlap !default` (calculated) |  |
| `input-group-padding-y` | ✅ slot | `$input-padding-y !default` (calculated) |  |
| `input-group-padding-x` | ✅ slot | `$input-padding-x !default` (calculated) |  |
| `input-group-append-padding-right` | ✅ slot | `$input-group-right-overlap !default` (calculated) |  |
| `input-group-prepend-padding-left` | ✅ slot | `$input-padding-x + 1.8rem !default` (calculated) |  |
| `custom-file-padding-right` | ✅ slot | 7rem !default | File input .custom-file-input |
| `custom-file-cursor` | ✅ slot | default !default |  |
| `select-bg-size` | ✅ slot | 0.9em 0.7em !default | Selects |
| `select-padding-right` | ✅ slot | `$select-indicator-right * 2.5 !default` (calculated) |  |
| `select-option-color` | ⚠️ admin | `rgba(map-get($colors-text, "wh"), .4) !default` (calculated) |  |
| `select-cursor` | ✅ slot | default !default |  |
| `textarea-height` | ✅ slot | auto !default | Textarea |
| `textarea-border-radius` | ✅ slot | `border-radius-base($rounded: 'max') !default` (calculated) |  |
| `spinner-btn-width` | ✅ slot | 2em !default | Spinner .ui-spinner |
| `spinner-btn-cursor` | ✅ slot | pointer !default |  |
| `spinner-btn-padding-x` | ✅ slot | `$spinner-btn-width / 3 !default` (calculated) |  |
| `checkbox-radio-line-height` | ✅ slot | `map-get($line-height-sizes, "sm") !default` (calculated) | Checkboxes and radios .custom-control |
| `checkbox-radio-border-width` | ✅ slot | `2px !default` (calculated) |  |
| `checkbox-radio-border-style` | ✅ slot | `solid !default` (calculated) |  |
| `checkbox-radio-indicator-size` | ✅ slot | 16px !default |  |
| `checkbox-radio-indicator-min-height` | ✅ slot | 1.1em !default |  |
| `checkbox-radio-indicator-gutter` | ✅ slot | `$checkbox-radio-indicator-size * 1.5 !default` (calculated) |  |
| `checkbox-radio-indicator-gutter-sm` | ✅ slot | `$checkbox-radio-indicator-size * 1.35 !default` (calculated) |  |
| `checkbox-radio-indicator-unchecked-color` | ✅ slot | .5 !default |  |
| `checkbox-radio-indicator-border` | ⚠️ admin | `rgba(map-get($colors-text, "wh"), .3) !default` (calculated) |  |
| `checkbox-radio-indicator-border-primary` | ⚠️ admin | `rgba(map-get($colors-text, "pr"), $checkbox-radio-indicator-unchecked-color) !default` (calculated) |  |
| `checkbox-radio-indicator-border-secondary` | ⚠️ admin | `rgba(map-get($colors-text, "se"), $checkbox-radio-indicator-unchecked-color) !default` (calculated) |  |
| `checkbox-radio-indicator-border-conversion` | ⚠️ admin | `rgba(map-get($colors-text, "co"), $checkbox-radio-indicator-unchecked-color) !default` (calculated) |  |
| `checkbox-radio-indicator-bg-inverse` | ✅ slot | `$color-white !default` (calculated) |  |
| `checkbox-radio-indicator-bg-size` | ✅ slot | 50% 50% !default |  |
| `checkbox-radio-indicator-focus-shadow` | ⚠️ admin | `0 0 0 1px $color-default, $input-btn-focus-box-shadow !default` (calculated) |  |
| `checkbox-radio-indicator-transition` | ✅ slot | `background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out !default` (calculated) |  |
| `checkbox-radio-indicator-checked-color` | ✅ slot | `$color-white !default` (calculated) |  |
| `checkbox-radio-indicator-checked-bg-primary` | ⚠️ admin | `$color-fg-primary !default` (calculated) |  |
| `checkbox-radio-indicator-checked-bg-secondary` | ⚠️ admin | `$color-fg-secondary !default` (calculated) |  |
| `checkbox-radio-indicator-checked-bg-conversion` | ⚠️ admin | `$color-fg-conversion !default` (calculated) |  |
| `checkbox-indicator-border-radius` | ✅ slot | `border-radius-base($radius: map-get($radius-sizes, "1"), $rounded: false) !default` (calculated) |  |
| `radio-indicator-border-radius` | ✅ slot | `50% !default` (calculated) |  |
| `form-feedback-required-color` | ⚠️ admin | `$color-required !default` (calculated) | Form validation .has-xxx |
| `form-feedback-success-color` | ⚠️ admin | `$color-success !default` (calculated) |  |
| `form-feedback-danger-color` | ⚠️ admin | `$color-danger !default` (calculated) |  |
| `form-feedback-weight` | ✅ slot | 600 !default |  |
| `form-colors-bg` | ⚠️ admin | map[pr, se, co, de, des, dec] |  |

## MODULES

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `list-group-color` | ✅ slot | inherit !default | List group .list-group |
| `list-group-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `list-group-border-width` | ✅ slot | `map-get($border-sizes, "1") !default` (calculated) |  |
| `list-group-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `list-group-heading-font-weight` | ✅ slot | `$font-weight-bold !default` (calculated) |  |
| `list-group-heading-line-height` | ✅ slot | `map-get($line-height-sizes, "md") !default` (calculated) |  |
| `list-group-font-size-sm` | ✅ slot | `map-get($font-sizes, "2") !default` (calculated) |  |
| `list-group-horizontal-align` | ✅ slot | `$text-align-base !default` (calculated) |  |
| `list-group-item-padding-y` | ✅ slot | `map-get($spacers, "2") !default` (calculated) | .lgi |
| `list-group-item-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `list-group-item-padding-active-left` | ✅ slot | `$list-group-item-padding-x !default` (calculated) |  |
| `list-group-item-padding-active-right` | ✅ slot | `$list-group-item-padding-x !default` (calculated) |  |
| `list-group-item-toggle-right` | ✅ slot | 2.5em !default |  |
| `list-group-item-arrow-top` | ✅ slot | -20% !default |  |
| `list-group-item-text-font-weight` | ✅ slot | `$font-weight-base !default` (calculated) |  |
| `list-group-item-active-weight` | ✅ slot | `$font-weight-bold !default` (calculated) |  |
| `list-group-item-open-weight` | ✅ slot | `$font-weight-bold !default` (calculated) |  |
| `list-group-colors-bg-hover` | ⚠️ admin | map[pr, se, co, de, des, dec, wh] |  |
| `nav-tabs-padding-y` | ✅ slot | `map-get($spacers, "4") !default` (calculated) | Navs .nav / .nav-tabs |
| `nav-tabs-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `nav-tabs-border-width` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) |  |
| `nav-tabs-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `nav-tabs-weight` | ✅ slot | `$font-weight-bold !default` (calculated) |  |
| `nav-tabs-padding` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `nav-tabs-padding-md` | ✅ slot | 0 !default |  |
| `nav-tabs-gap` | ✅ slot | `$space-ico-lg !default` (calculated) |  |
| `nav-item-margin-bottom-md` | ✅ slot | `-$nav-tabs-border-width !default` (calculated) |  |
| `nav-link-color` | ✅ slot | inherit !default |  |
| `nav-link-bg-hover` | ⚠️ admin | `$link-hover-bg !default` (calculated) |  |
| `nav-link-primary-bg-hover` | ✅ slot | `$link-hover-bg-dark !default` (calculated) |  |
| `nav-link-padding-y` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `nav-link-padding-x` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `nav-link-line-height` | ✅ slot | `map-get($line-height-sizes, "lg") !default` (calculated) |  |
| `nav-link-gap` | ✅ slot | `$space-ico !default` (calculated) |  |
| `nav-link-gap-lg` | ✅ slot | `$space-ico-lg !default` (calculated) |  |
| `nav-link-active-min-width` | ✅ slot | null !default |  |
| `nav-link-active-padding-x-sm` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `nav-link-disabled-cursor` | ✅ slot | not-allowed !default |  |
| `nav-link-disabled-opacity` | ✅ slot | `$disabled-opacity !default` (calculated) |  |
| `navbar-padding-y` | ✅ slot | `$list-group-item-padding-y !default` (calculated) | Navbar .navbar |
| `navbar-padding-y-xs` | ✅ slot | `map-get($spacers, "1") !default` (calculated) |  |
| `navbar-padding-x` | ✅ slot | `$list-group-item-padding-x !default` (calculated) |  |
| `navbar-shadow` | ✅ slot | `map-get($shadows, "lg") !default` (calculated) |  |
| `navbar-bg-hover` | ⚠️ admin | `$link-hover-bg !default` (calculated) |  |
| `navbar-height-sm` | ✅ slot | 2.867rem !default |  |
| `navbar-height` | ✅ slot | 3.6rem !default |  |
| `navbar-height-lg` | ✅ slot | 5.33334rem !default |  |
| `navbar-toggler-color` | ✅ slot | inherit !default |  |
| `navbar-toggler-padding-y` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `navbar-toggler-padding-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `navbar-toggler-padding-x-xs` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `navbar-toggler-gap` | ✅ slot | `$space-ico !default` (calculated) |  |
| `navbar-toggler-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `alert-padding-y` | ✅ slot | `map-get($spacers, "4") !default` (calculated) | Alerts .alert |
| `alert-padding-x` | ✅ slot | `$alert-padding-y !default` (calculated) |  |
| `alert-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `alert-link-font-weight` | ✅ slot | `map-get($font-weights, "b") !default` (calculated) |  |
| `alert-link-color` | ✅ slot | inherit !default |  |
| `alert-paragraph-space` | ✅ slot | `$paragraph-margin-bottom !default` (calculated) |  |
| `alert-bg-level` | ✅ slot | -10 !default |  |
| `alert-border-level` | ✅ slot | `-8 !default` (calculated) |  |
| `alert-color-level` | ✅ slot | 6 !default |  |
| `alert-color-darken` | ✅ slot | 5% !default |  |
| `alert-text-muted-lighten` | ✅ slot | 40% !default |  |
| `alert-colors` | ⚠️ admin | map[gr, re, ye, cy] |  |
| `badge-font-family` | ✅ slot | `$font-family-base !default` (calculated) | Badges .badge |
| `badge-font-size` | ✅ slot | `map-get($font-sizes, "2") !default` (calculated) |  |
| `badge-font-weight` | ✅ slot | `map-get($font-weights, "r") !default` (calculated) |  |
| `badge-line-height` | ✅ slot | `map-get($line-height-sizes, "xs") !default` (calculated) |  |
| `badge-letter-spacing` | ✅ slot | `$letter-spacing-base !default` (calculated) |  |
| `badge-padding-y` | ✅ slot | `map-get($spacers, "1") !default` (calculated) |  |
| `badge-padding-x` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `badge-gap` | ✅ slot | `$space-ico !default` (calculated) |  |
| `badge-min-width` | ✅ slot | 2em !default |  |
| `badge-border-radius` | ✅ slot | `border-radius-base() !default` (calculated) |  |
| `badge-sticker-size` | ✅ slot | 1.95em !default |  |
| `badge-sticker-padding-y` | ✅ slot | 0 !default |  |
| `badge-sticker-padding-x` | ✅ slot | .3em !default |  |
| `badge-sticker-top` | ✅ slot | -19% !default |  |
| `badge-sticker-right` | ✅ slot | -1em !default |  |
| `badge-dot-size` | ✅ slot | .6rem !default |  |
| `badge-dot-border-radius` | ✅ slot | `border-radius-base($rounded: 'circle') !default` (calculated) |  |
| `card-padding-y` | ✅ slot | `map-get($spacers, "4") !default` (calculated) | Cards .card |
| `card-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `card-border-width` | ✅ slot | `map-get($border-sizes, "d") !default` (calculated) |  |
| `card-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `card-header-font-size` | ✅ slot | `map-get($font-sizes, "4") !default` (calculated) |  |
| `card-header-weight` | ✅ slot | `$font-weight-heading-bold !default` (calculated) |  |
| `card-header-spacer-y` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `card-header-line-height` | ✅ slot | `map-get($line-height-sizes, "xs") !default` (calculated) |  |
| `card-header-padding-top-uni` | ✅ slot | 0 !default |  |
| `card-header-padding-x-uni` | ✅ slot | `$card-padding-x !default` (calculated) |  |
| `card-header-padding-bottom-uni` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `card-body-padding-top-uni` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `card-body-padding-bottom-uni` | ✅ slot | 0 !default |  |
| `card-item-deck-margin` | ✅ slot | `map-get($spacers, "3") / 2 !default` (calculated) |  |
| `card-item-deck-margin-xs` | ✅ slot | `$card-item-deck-margin / 2 !default` (calculated) |  |
| `card-group-deck-margin` | ✅ slot | `-$card-item-deck-margin !default` (calculated) |  |
| `card-item-border-margin` | ✅ slot | `-$card-border-width !default` (calculated) |  |
| `card-columns-gap` | ✅ slot | `map-get($spacers, "5") !default` (calculated) |  |
| `accordion-border-width` | ✅ slot | `map-get($border-sizes, "1") !default` (calculated) | Accordion .accordion |
| `accordion-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `tile-cursor` | ✅ slot | pointer !default | Tile .tile |
| `tile-horizontal-img-size` | ✅ slot | 50px !default |  |
| `carousel-image-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) | Carousel .carousel |
| `carousel-ico-bottom` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `carousel-nav-size` | ✅ slot | `map-get($ico-sizes, "md") !default` (calculated) |  |
| `carousel-nav-top` | ✅ slot | 50% !default |  |
| `carousel-nav-translate-y` | ✅ slot | -50% !default |  |
| `carousel-nav-font-size` | ✅ slot | 1.4em !default |  |
| `carousel-nav-margin-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `carousel-nav-overlap-x` | ✅ slot | 3rem !default |  |
| `carousel-nav-cont-overlap-x` | ✅ slot | 5rem !default |  |
| `carousel-nav-opacity` | ✅ slot | .4 !default |  |
| `carousel-nav-opacity-hover` | ✅ slot | 1 !default |  |
| `carousel-dot-container-size` | ✅ slot | 2.5em !default |  |
| `carousel-dot-size` | ✅ slot | 1em !default |  |
| `carousel-dot-bg` | ✅ slot | `$color-white !default` (calculated) |  |
| `carousel-dot-inverse-bg` | ⚠️ admin | `$color-text-primary !default` (calculated) |  |
| `carousel-dot-border-radius` | ✅ slot | `border-radius-base($rounded: 'circle') !default` (calculated) |  |
| `carousel-dot-overlap` | ✅ slot | `($carousel-dot-container-size - $carousel-dot-size) / 2 !default` (calculated) |  |
| `carousel-dot-opacity` | ✅ slot | `$carousel-nav-opacity !default` (calculated) |  |
| `carousel-dot-opacity-hover` | ✅ slot | .6 !default |  |
| `carousel-dot-opacity-active` | ✅ slot | 1 !default |  |
| `carousel-indicators-size` | ✅ slot | `map-get($font-sizes, "1") !default` (calculated) |  |
| `carousel-indicators-gap` | ✅ slot | `$carousel-dot-overlap * 2 !default` (calculated) |  |
| `cover-border-radius` | ✅ slot | `$carousel-image-radius !default` (calculated) | Cover .cover |
| `dropdown-top` | ✅ slot | 16px !default | Dropdowns .dropdown-menu |
| `dropdown-width` | ✅ slot | 13.5rem !default |  |
| `dropdown-width-lg` | ✅ slot | 20rem !default |  |
| `dropdown-font-size` | ✅ slot | `$font-size-base !default` (calculated) |  |
| `dropdown-font-weight` | ✅ slot | `map-get($font-weights, "r") !default` (calculated) |  |
| `dropdown-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `dropdown-align` | ✅ slot | left !default |  |
| `dropdown-line-height` | ✅ slot | `map-get($line-height-sizes, "sm") !default` (calculated) |  |
| `dropdown-box-shadow` | ✅ slot | `map-get($shadows, "lg") !default` (calculated) |  |
| `dropdown-animation` | ✅ slot | `anim-dropdown $duration ease-out !default` (calculated) |  |
| `dropdown-text-opacity` | ✅ slot | .5 !default |  |
| `dropdown-toggle-split-padding-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `dropdown-toggle-split-border-left` | ✅ slot | `$btn-border-width !default` (calculated) |  |
| `dropdown-toggle-split-outer-left` | ✅ slot | `-$outer-size !default` (calculated) |  |
| `dropdown-max-height` | ✅ slot | 75vh !default |  |
| `dropdown-arrow-size` | ✅ slot | `$dropdown-top / 2 !default` (calculated) |  |
| `dropdown-arrow-right` | ✅ slot | 1em !default |  |
| `dropdown-link-gap` | ✅ slot | `$space-ico-lg !default` (calculated) |  |
| `dropdown-link-padding-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `dropdown-link-padding-y` | ✅ slot | 0.46667em !default |  |
| `dropdown-link-padding-y-outer` | ✅ slot | `$dropdown-link-padding-y * 2 !default` (calculated) |  |
| `dropdown-link-border-color` | ✅ slot | `map-get($border-colors-default, "wh") !default` (calculated) |  |
| `dropdown-link-justify-content` | ✅ slot | flex-start !default |  |
| `dropdown-link-align-items` | ✅ slot | center !default |  |
| `dropdown-link-hover-bg` | ⚠️ admin | `$link-hover-bg !default` (calculated) |  |
| `dropdown-link-active-bg` | ⚠️ admin | `$active !default` (calculated) |  |
| `dropdown-link-img-shadow` | ✅ slot | none !default |  |
| `alignments` | ✅ slot | map[l, e, a] |  |
| `flex-directions` | ✅ slot | map[row] |  |
| `flex-wraps` | ✅ slot | map[wrap] |  |
| `img-sm-size` | ✅ slot | 60px !default | Image img |
| `img-nopicture-width` | ✅ slot | 5em !default |  |
| `img-nopicture-opacity` | ✅ slot | .1 !default |  |
| `img-nopicture-bg` | ✅ slot | none !default |  |
| `img-nopicture-shadow` | ✅ slot | none !default |  |
| `thumbnail-bg` | ⚠️ admin | `$body-bg !default` (calculated) | Image thumbnails .img-thumbnail |
| `thumbnail-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `thumbnail-sm-border-radius` | ✅ slot | `border-radius-base($rounded: 'circle') !default` (calculated) |  |
| `thumbnail-active-shadow` | ⚠️ admin | `0 0 0 $input-btn-focus-width $active !default` (calculated) |  |
| `thumbnail-caption-font-size` | ✅ slot | `map-get($font-sizes, "2") !default` (calculated) |  |
| `thumbnail-caption-padding-y` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `thumbnail-caption-padding-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `thumbnail-caption-radius` | ✅ slot | `$thumbnail-border-radius !default` (calculated) |  |
| `video-bg` | ✅ slot | `rgba($color-black, .35) !default` (calculated) | Video video |
| `lightbox-bg` | ✅ slot | #171717 !default | Lightbox |
| `lightbox-bg-opacity` | ✅ slot | .96 !default |  |
| `lightbox-content-title-space-b` | ✅ slot | 3rem !default |  |
| `lightbox-content-title-space-b-landscape` | ✅ slot | 5.3rem !default |  |
| `lightbox-thumb-landscape-width` | ✅ slot | 20% !default |  |
| `lightbox-thumb-portrait-height` | ✅ slot | 10.25em !default |  |
| `lightbox-thumb-img-bg` | ⚠️ admin | `$thumbnail-bg !default` (calculated) |  |
| `lightbox-thumb-img-height` | ✅ slot | 8vw !default |  |
| `lightbox-thumb-img-height-sm` | ✅ slot | 5em !default |  |
| `lightbox-thumb-img-space` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `media-align` | ✅ slot | left !default | Media .media |
| `media-margin-top` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `media-indent-size` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `media-indent-border-width` | ✅ slot | `map-get($border-sizes, "d") + 1 !default` (calculated) |  |
| `media-indent-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `media-indent-border-radius` | ✅ slot | `border-radius-base($rounded: 'max') !default` (calculated) |  |
| `media-indent-margin-x` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `modal-backdrop-bg` | ✅ slot | `$color-black !default` (calculated) | Modals .modal |
| `modal-backdrop-opacity` | ✅ slot | .3 !default |  |
| `modal-dialog-width` | ✅ slot | 600px !default |  |
| `modal-dialog-width-lg` | ✅ slot | 900px !default |  |
| `modal-dialog-width-sm` | ✅ slot | 400px !default |  |
| `modal-dialog-font-size` | ✅ slot | false !default |  |
| `modal-dialog-margin` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `modal-dialog-margin-y` | ✅ slot | `map-get($spacers, "3") * 2 !default` (calculated) |  |
| `modal-dialog-margin-y-sm` | ✅ slot | `map-get($spacers, "5") !default` (calculated) |  |
| `modal-dialog-close-out-margin-block` | ✅ slot | `$cross-size-container * 1.5 !default` (calculated) |  |
| `modal-dialog-close-out-transform` | ✅ slot | translate(0, -110%) !default |  |
| `modal-font-size` | ✅ slot | `map-get($font-sizes, "3") !default` (calculated) |  |
| `modal-padding-y` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `modal-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `modal-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `modal-box-shadow` | ✅ slot | `map-get($shadows, "xl") !default` (calculated) |  |
| `modal-header-gap-x` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `modal-header-padding-y` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `modal-title-line-height` | ✅ slot | `map-get($line-height-sizes, "xs") !default` (calculated) |  |
| `pagination-padding-x` | ✅ slot | .5rem !default | Pagination .page-link |
| `pagination-padding-x-xs` | ✅ slot | `map-get($font-sizes, "3") !default` (calculated) |  |
| `popover-font-size` | ✅ slot | 1em !default | Popovers .popover |
| `popover-top` | ✅ slot | -0.75em !default |  |
| `popover-max-width` | ✅ slot | 20em !default |  |
| `popover-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `popover-box-shadow` | ✅ slot | `map-get($shadows, "lg") !default` (calculated) |  |
| `popover-padding-y` | ✅ slot | .7em !default |  |
| `popover-padding-x` | ✅ slot | .8rem !default |  |
| `popover-arrow-width` | ✅ slot | 1em !default |  |
| `popover-arrow-height` | ✅ slot | .5em !default |  |
| `progress-height` | ✅ slot | `map-get($spacers, "1") !default` (calculated) | Progress bars .progress |
| `progress-border-radius` | ✅ slot | `border-radius-base() !default` (calculated) |  |
| `table-border-width` | ✅ slot | `map-get($border-sizes, "1") !default` (calculated) | Tables .table |
| `table-border-style` | ✅ slot | `$border-style !default` (calculated) |  |
| `table-border-top` | ✅ slot | `0 !default` (calculated) |  |
| `table-th-border-width` | ✅ slot | `$table-border-width + 1 !default` (calculated) |  |
| `table-cell-padding-y` | ✅ slot | `map-get($spacers, "2") !default` (calculated) |  |
| `table-cell-padding-y-big` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `table-cell-padding-x` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `table-cell-vertical-align` | ✅ slot | middle !default |  |
| `table-sm-cell-padding-y` | ✅ slot | `map-get($spacers, "1") !default` (calculated) |  |
| `table-sm-cell-padding-x` | ✅ slot | .25rem !default |  |
| `table-elastic-row-gap-md` | ✅ slot | .3em !default |  |
| `table-elastic-tr-padding-y-md` | ✅ slot | 1em !default |  |
| `table-elastic-label-align-md` | ✅ slot | right !default |  |
| `table-elastic-label-width-md` | ✅ slot | 35% !default |  |
| `table-elastic-label-width-xs` | ✅ slot | 30% !default |  |
| `table-elastic-label-main-weight-md` | ✅ slot | `map-get($font-weights, "b") !default` (calculated) |  |
| `table-elastic-label-font-size-md` | ✅ slot | smaller !default |  |
| `table-elastic-label-color` | ✅ slot | `$text-muted-color-base !default` (calculated) |  |
| `table-elastic-label-weight-md` | ✅ slot | normal !default |  |
| `table-elastic-label-style-xs` | ✅ slot | italic !default |  |
| `table-elastic-label-right-md` | ✅ slot | `map-get($spacers, "4") !default` (calculated) |  |
| `table-elastic-label-right-xs` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `table-elastic-addon-gap-md` | ✅ slot | .15em !default |  |
| `table-elastic-heading-bottom-md` | ✅ slot | .5rem !default |  |
| `table-elastic-heading-left-md` | ✅ slot | 0 !default |  |
| `table-elastic-heading-align-md` | ✅ slot | left !default |  |
| `table-elastic-delete-top-md` | ✅ slot | `$table-elastic-tr-padding-y-md - .3em !default` (calculated) |  |
| `table-elastic-delete-right-md` | ✅ slot | -.5em !default |  |
| `tooltip-font-size` | ✅ slot | `map-get($font-sizes, "2") !default` (calculated) | Tooltips .tooltip |
| `tooltip-max-width` | ✅ slot | 18em !default |  |
| `tooltip-border-radius` | ✅ slot | `border-radius-base($rounded: false) !default` (calculated) |  |
| `tooltip-opacity` | ✅ slot | 1 !default |  |
| `tooltip-margin` | ✅ slot | .5em !default |  |
| `tooltip-padding` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `tooltip-align` | ✅ slot | center !default |  |
| `tooltip-box-shadow` | ✅ slot | `map-get($shadows, "lg") !default` (calculated) |  |
| `tooltip-arrow-width` | ✅ slot | `map-get($spacers, "3") !default` (calculated) |  |
| `tooltip-arrow-height` | ✅ slot | `map-get($spacers, "3") / 2 !default` (calculated) |  |
| `tooltip-arrow-color` | ✅ slot | `$tooltip-bg !default` (calculated) |  |
| `tooltip-arrow-left` | ✅ slot | 50% !default |  |
| `typehead-height` | ✅ slot | 18rem !default | Typehead .tt-menu |
| `typehead-max-height` | ✅ slot | 72vh !default |  |
| `typehead-max-height-sm` | ✅ slot | 60vh !default |  |

## TEMPLATES

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `header-alert-height` | ✅ slot | 2.93rem !default | Header .header |
| `header-alert-z-index` | ✅ slot | 15 !default |  |
| `header-navbar-dropdown-1-top` | ✅ slot | 100% !default |  |
| `header-column-search-uni-space-bottom` | ✅ slot | 4.77rem !default |  |
| `header-logo-max-width` | ✅ slot | 400px !default |  |
| `header-item-badge-right` | ✅ slot | .75em !default |  |
| `header-z-index` | ✅ slot | 14 !default |  |
| `header-logo-font-size` | ✅ slot | 4.2em !default |  |
| `header-logo-top` | ✅ slot | .1em !default |  |
| `products-list-img-height` | ✅ slot | 242px !default | Products list .p-i |
| `products-list-img-height-cols` | ✅ slot | 239px !default |  |
| `products-list2-img-height` | ✅ slot | 230px !default |  |
| `products-list2-img-height-cols` | ✅ slot | 227px !default |  |
| `main-z-index` | ✅ slot | 12 !default | Navbar heights |

## THEME

| Variable | Where | Value | Controls (class) |
|---|---|---|---|
| `theme-texture-opacity-white` | ✅ slot | .08 !default |  |
| `theme-texture-opacity-default` | ✅ slot | .6 !default |  |
| `theme-texture-opacity-primary` | ✅ slot | .08 !default |  |
| `theme-texture-opacity-secondary` | ✅ slot | .14 !default |  |
| `theme-texture-opacity-conversion` | ✅ slot | .14 !default |  |
