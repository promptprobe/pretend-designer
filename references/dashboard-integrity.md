# Dashboard integrity

Read this for an interactive dashboard or data-heavy mockup. Visual craft must survive changing data, scope and viewport.

## Before styling

- State the monitoring task and the entity, unit, time window and aggregation of each metric.
- Separate page scope, historical interval and fixed-window metrics. A 30-day selector must not silently turn a 24h volume metric into 30-day volume.
- Use one fixture dataset when live data is outside the brief. Disclose synthetic data and its reference date in a reachable data details view. Reserve prominent status for information the user needs at a glance.
- Derive totals, proportions, changes, chart endpoints and exported rows from that dataset. Define the comparison baseline precisely.

## Interaction contract

- Make every enabled control perform its named action. Prefer in-page anchors over navigation to invented pages.
- Apply global scope consistently to linked charts and totals. Label an intentionally fixed comparison universe next to the affected view.
- Keep filtering, sorting, empty states and CSV exports consistent. Include synthetic status and units in exported data.
- Support keyboard focus, chart point inspection, labelled selects and dialog dismissal. Provide chart summaries or adjacent data tables; do not rely on color alone.

## Geometry under stress

- Calculate SVG dimensions from the rendered plot container. Do not shrink desktop labels with an oversized fixed viewBox on mobile.
- Reserve space for axes and direct labels. Test all-positive, all-negative and single-series states; negative bars and labels must stay inside the viewBox.
- On mobile, promote the primary chart to full width, collapse navigation, regroup KPIs and keep a dense comparison table in its own horizontal scroll region.
- Treat usability as a reason to preserve alignment. The core skill's call for one deliberate grid break must never distort chart scales or table columns.

## Verify and report

Inspect actual rendered views at 375px and 1280px. Check font loading, document overflow, chart labels, empty search, scope changes, period changes, sorting, keyboard access and download output. Test reduced-motion behavior only when animation exists. Report unverified checks plainly.

Use `examples/blockchain-dashboard/` as an interaction and data-consistency example, not a house style. Do not reuse its name, copper palette, exact layout or sample market values by default. Its palette seed and fixture methodology belong to that example only.
