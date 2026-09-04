# Apple Korea iPhone

- Reference: [apple.com/kr/iphone](https://www.apple.com/kr/iphone/)
- Observed: 2026-09-04
- Viewports: 1440×1000 desktop, 375×812 mobile
- Best fit: Korean product marketing, editorial product explainers, consumer landing pages
- Confidence: high for computed typography and sampled colors; moderate for animation behavior outside the inspected states

## Job and visual thesis

The page helps Korean consumers scan the iPhone family, understand product differences, and move toward comparison or purchase. Its thesis is disciplined product theatre: large, calm Korean type establishes hierarchy while full-width navigation, horizontal product rails, photography, and spacious sections carry the spectacle.

## Measured evidence

The live page used `SF Pro KR` with SF Pro and Apple Gothic fallbacks. Because SF Pro KR is proprietary, this skill transfers the metrics to Pretendard or Noto Sans KR rather than prescribing Apple's font.

| Element | Desktop computed style | Mobile computed style |
| --- | --- | --- |
| Major section heading | `56px / 66px`, 600, tracking `normal` | Section heading `28px / 35px`, 600, tracking `normal` |
| Page title | — | `48px / 57px`, 600, tracking `normal` |
| Feature-card statement | `28px / 35px`, 600, `0.196px` (`0.007em`) | same role remains open rather than tightly tracked |
| Section subheading | `32px / 39px`, 600, `0.128px` (`0.004em`) | reduces by role |
| Component heading | `19px / 29px`, 600, `0.228px` (`0.012em`) | consistent compact hierarchy |
| Explanatory paragraph | `17px / 27px`, 400, tracking `normal` | same readable body rhythm |
| Compact card copy | `17px / 23px`, 400 or 600, tracking `normal` | same compact rhythm |
| Promotion | `14px / 22px`, 400, tracking `normal` | two lines fit into a 44px block |
| Legal footnote | `12px / 16px`, 400, tracking `normal` | compact but readable |

The recurring text colors were `#1d1d1f`, `#333336`, `#6e6e73`, and `#86868b`. Primary surfaces were `#ffffff`, `#f5f5f7`, and `#fafafc`; links used `#0066cc`, primary controls `#0071e3`, and legal copy used black at 56% opacity.

## Geometry, radius, and mobile behavior

- Global chrome and content bands meet the viewport rather than sitting inside one floating card.
- Product navigation and lineup cards use horizontal rails. On mobile they remain rails, preserving browsing behavior instead of collapsing into a long generic stack.
- Reading text stays narrow inside much larger visual modules. The page distinguishes prose measure from page width.
- Several large editorial/product modules use about 28px corner radii. This works because the radius belongs to a few photograph-led surfaces; it is not sprayed onto every field, button, and panel.
- Mobile is a reduction and re-sequence: navigation becomes horizontally scrollable, headings step down by role, and content remains image-led.

## Why the Korean typography works

1. **Leading does more than tracking.** A 17px paragraph gets 27px leading, so Hangul remains calm and legible without artificial spacing tricks.
2. **Large Hangul is not crushed.** Major headings use normal tracking; smaller strong roles use only weak positive spacing.
3. **Weight is restrained.** 600 creates authority without turning every Korean heading into a dense 800-weight block.
4. **Color has four text levels.** Hierarchy is not reduced to black versus one generic gray.
5. **Line breaks follow composition.** Short display phrases can be composed, while paragraphs wrap naturally within a deliberate measure.

## Transferable rules

- For Korean product pages, use one Hangul family and let 400/600 weights plus the measured size-and-leading scale do the hierarchy.
- Default Korean body text to `17px/27px`, not a reflexive `16px/24px` UI preset.
- Default Korean letter spacing to zero. Treat negative tracking as an exception requiring measured brand evidence.
- Use `word-break: keep-all` and check real Korean strings at 375px.
- Separate the full-width composition from the narrower text measure.
- Reserve a large radius for a small class of image-led modules; do not infer that all UI should be rounded.

## Do not copy

- Do not use Apple's trademarks, product names, photography, navigation labels, or proprietary SF Pro KR files.
- Do not reproduce the exact product-card sequence or Apple-specific controls.
- Do not import the 28px radius as a universal token. It is an observed exception supported by Apple's photographic card system.
- Do not use the neutral palette as a substitute for the user's brand direction.

For the mandatory implementation scale and QA checklist, read [Korean typography standard](../korean-typography.md).
