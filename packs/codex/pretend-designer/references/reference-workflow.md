# Reference-led design workflow

Read this file only when the user supplies a design reference, asks for a reference breakdown, or wants an existing design language translated into a new page.

## The purpose of a case study

A case study is evidence for a decision, not a template to reproduce. Reuse the observed relationship between type, color, geometry, content, and interaction. Do not reuse outcome-specific fonts, brand colors, copy, imagery, or component arrangements unless the user explicitly asks for close matching.

Treat a reference selected for structure, density, typography, charts, or interaction as color-neutral. When the user has not supplied a palette, use the independent [palette selection protocol](palette-selection.md); do not import the reference brand's colors or replace them with another familiar company's design system.

## Observation protocol

1. Open the live reference at a fixed desktop viewport, normally 1440×1000.
2. Wait for fonts, images, charts, and other data-driven regions to reach a loaded state.
3. Capture the first screen and at least one content-dense section.
4. Repeat at 375×812. Record whether mobile is a re-sequence, a reduction, or merely a stack.
5. Measure, when available: font families, display/body sizes, line heights, tracking, common radii, dominant colors, grid geometry, media type, and chart rendering mode.
6. Separate observed facts from interpretation. Mark runtime defects or incomplete loading separately from design criticism.

## Case-study schema

Each case should contain:

- reference URL and observation date;
- best-fit design direction;
- job and visual thesis;
- measured evidence;
- page geometry and hierarchy;
- type, color, radius, imagery, motion, and mobile behavior;
- why the system works;
- transferable rules;
- outcome-specific details that must not be copied;
- confidence and any observation limits.

Do not preserve current business metrics, article titles, or transient data values as design rules.

## Current case routing

Choose the smallest useful set. Do not load every case by default.

- For typographic launch pages, terminal/editorial density, or event sites: [BUIDL CTC](cases/buidl-creditcoin.md).
- For public analytical reports and single-question charts: [Visa Onchain Analytics](cases/visa-onchain-analytics.md).
- For monitoring dashboards, dense comparison charts, or market terminals: [Blockworks Analytics](cases/blockworks-analytics.md).
- For agency portfolios, oversized type, cropping, and photographic pacing: [Dots & Lines](cases/dots-and-lines.md).
- For product marketing built from interface evidence and modular composition: [Stripe](cases/stripe.md).
- For institutional finance storytelling, capital-flow diagrams, and split-screen product narratives: [Spark Finance](cases/spark-finance.md).
- For Korean product pages, Hangul hierarchy, line height, tracking, and neutral readability: [Apple Korea iPhone](cases/apple-korea-iphone.md), then apply the mandatory [Korean typography standard](korean-typography.md).
- For chart-specific choices, read [Chart grammar](chart-grammar.md) after selecting either the Visa or Blockworks case.

## Cross-case findings

These patterns recur across the current set and may guide future work:

1. **The page has a strong surface.** Full-width bands, side rails, crop, or structural rules make the viewport part of the composition.
2. **Type carries hierarchy before containers do.** The strongest pages use scale, weight, measure, and line breaks before adding cards or shadows.
3. **Proof is visualized.** Charts, interface states, live metrics, photographs, or diagrams do the explanatory work; decoration does not stand in for evidence.
4. **Radii are restrained.** Observed structural radii are commonly 0–8px. Pills are reserved for a particular control or action.
5. **Mobile edits the story.** Navigation collapses, copy is shortened, charts become full-width, and content order changes. Desktop is not simply scaled down.
6. **A brand exception needs structural support.** Stripe's color field and Spark's gradient work because type, grid, product imagery, and motion all reinforce the same system. A gradient alone is not art direction.
7. **Dense and spacious are both valid.** Visa and Blockworks are information-dense; Dots & Lines is intentionally sparse. The correct density follows the user's job.
8. **Korean needs script-specific spacing.** Apple Korea relies on generous leading, normal or weak positive tracking, and restrained 600 weights. Latin display habits—especially automatic negative tracking—do not transfer safely to Hangul.

## Anti-overfitting rule

Before borrowing from a case, write:

- the structural principle being reused;
- at least one outcome-specific feature being rejected;
- why the selected case fits the current job better than the other cases.

If the answer is only “it looks good,” the case has not been interpreted.
