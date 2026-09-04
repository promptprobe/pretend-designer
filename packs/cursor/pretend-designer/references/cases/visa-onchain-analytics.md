# Visa Onchain Analytics

- Reference: https://visaonchainanalytics.com/
- Observed: 2026-09-04 at 1440×1000 and 375×812
- Direction: explanatory report + institutional dashboard
- Confidence: high for visible layout and computed styles; metric values and navigation contents may change.

## Job and thesis

The dashboard helps a broad audience understand fiat-backed stablecoin activity through definitions, key metrics, and auditable charts. Its thesis is a public statistical report inside a strong institutional frame, not a trading terminal.

## Measured evidence

- Desktop: a fixed left rail is about 288px; the content begins around x=320.
- Body: custom `visaDialectFont`, 16px with 24px line height.
- Hero heading: 36px with 40px line height, weight 500, normal tracking.
- Structural radius: 0px across the sampled navigation, controls, metric blocks, and chart regions.
- Palette observed in the interface: near-black `rgb(10,10,10)`, cool grays, white/off-white, Visa blue `rgb(20,51,204)`, and a yellow contact accent around `rgb(251,191,24)`.
- The loaded overview contained 59 SVGs and no canvas elements.
- The main supply chart was a roughly 1024×384 SVG with 96 rectangular marks, 28 line elements, and 29 text labels.

## Chart grammar

- A title names the metric; a subtitle defines it in plain language.
- Time-range and aggregation controls sit above the plot, outside the data field.
- One dark-blue series carries the data while pale horizontal gridlines provide scale.
- Axes, units, date labels, reset/download controls, and a source line remain visible.
- KPI blocks precede the detailed chart, giving the reader a summary before exploration.
- Definitions follow the plot, so terminology is resolved near the evidence.

## Page geometry and mobile

The desktop rail creates a clear institutional shell while the main canvas remains spacious and rectangular. Metric blocks form a compact matrix without elevated card chrome. At 375px, the rail becomes a hamburger; the blue hero becomes a full-width vertical band; explanatory copy follows in a single reading column. The mobile page changes order and measure instead of shrinking the desktop dashboard.

## Why it works

The visual language is stable enough to feel official but not so branded that it obscures the data. The chart is large, single-purpose, and sourced. Definitions and navigation make the dashboard usable by non-specialists.

## Transferable rules

- For public analytics, optimize for explanation and auditability before density.
- Use rectangular KPI blocks and whitespace before adding shadows or large radii.
- Give charts a title, definition, unit, range, aggregation, source, and reset path.
- Keep the plot visually dominant; controls should not compete with marks.
- Treat mobile as a report sequence: context, metric, chart, definition.

## Do not copy

Do not reuse the Visa logo, exact corporate blue/yellow pairing, navigation taxonomy, Allium branding, or stablecoin copy. The transferable idea is institutional clarity, not the Visa identity.
