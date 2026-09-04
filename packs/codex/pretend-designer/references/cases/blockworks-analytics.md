# Blockworks Analytics

- References: https://blockworks.com/ and https://blockworks.com/analytics/chain-comparison
- Observed: 2026-09-04 at 1440×1000 and 375×812
- Direction: monitoring terminal + market editorial
- Confidence: high for visible layout and computed styles; live market values and available sectors are transient.

## Job and thesis

The public homepage builds authority around onchain capital markets; the analytics product lets a repeat user scan, compare, and diagnose many market series. Its thesis is a research terminal with editorial taste, not a collection of isolated dashboard cards.

## Measured evidence

- Homepage body uses Söhne; the analytics heading sampled at 22px/32px, weight 600, used Inter.
- Dashboard body is 16px/24px on a dark surface around `rgb(26,27,30)`.
- Common structural radii were 2px, 4px, and 6px.
- The observed analytics view contained 76 SVGs and two canvas charts.
- The two visible canvas plots were approximately 361×294 and 372×294.
- Prominent semantic colors included white and several cool grays, with categorical chart colors and status accents such as coral, violet, green, yellow, and blue.

## Chart grammar

- A persistent left taxonomy answers “where am I?” before the plot loads.
- Page-level tabs choose the analytical lens; chart-level controls choose representation and interval.
- Chart headers combine a specific title with a one-line definition.
- Multiple charts share the viewport for cross-reading.
- Dense categorical legends are placed beside the plot rather than encoded only through tooltips.
- Range brushes sit below the plots for repeated time-window comparison.
- The homepage uses compact sparkline tiles as ambient market evidence; the analytics product expands the same vocabulary into full diagnostic plots.

## Loaded-state observation

One chart initially showed a spinner and resolved after several seconds. The page emitted a React hydration error and repeated PostHog initialization warnings during observation. These are runtime observations, not endorsements or direct evidence of poor visual design. A replica should reserve chart height and verify the final series rather than capture the spinner.

## Page geometry and mobile

Desktop combines a global header, horizontal market ticker, left navigation, compact tabs, and a two-column chart grid. At 375px, the taxonomy collapses to a select-like control, tabs wrap into compact rows, and each chart becomes a full-width vertical module. The plot remains legible because it is not squeezed beside a persistent sidebar.

## Why it works

Density follows the user's monitoring job. Repetition creates speed: each chart has the same title/control/plot/legend/range anatomy. Small radii and dark tonal steps preserve hierarchy without making every chart float.

## Transferable rules

- Build a stable dashboard grammar before styling individual charts.
- Keep global scope, page lens, and chart settings as three visibly different control levels.
- Reserve multiple categorical colors for genuine multi-series comparison.
- Use small radii and tonal surfaces for operational density.
- On mobile, collapse taxonomy and stack charts; preserve plot width before side navigation.

## Do not copy

Do not reuse the Blockworks wordmark, exact ticker, sector taxonomy, market data, categorical palette, or homepage point-cloud artwork. A dark chart grid without the navigation and control hierarchy becomes generic crypto chrome.
