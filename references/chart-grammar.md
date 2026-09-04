# Chart grammar: explanatory report vs monitoring terminal

Read this file when a page contains analytical charts. Select one dominant chart mode before choosing colors or a chart library.

## Mode A — explanatory report

Use the Visa Onchain Analytics case when the reader needs to understand one metric, its definition, and its development over time.

- One primary question per chart.
- Plain-language title followed by a short definitional subtitle.
- A restrained series palette; neutral gridlines carry the scale.
- Visible source, unit, date range, and aggregation control.
- Large plot area with controls kept outside the marks.
- Prefer direct comparison and stable axes over ornamental animation.
- Provide definitions close to the chart, not in a distant glossary.

This mode should feel printable and auditable.

## Mode B — monitoring terminal

Use the Blockworks Analytics case when the reader compares many assets, diagnoses movement, or repeatedly changes scope.

- Persistent category navigation and a compact control rail.
- Multiple charts visible at once when cross-reading matters.
- Dense legends and categorical colors are acceptable only when series identity is the task.
- Small chart cards may share a consistent internal grammar: title, definition, interval, plot, legend, and range control.
- Dark surfaces reduce glare but require stronger axis and label contrast than decorative dashboards usually provide.
- Loading states must reserve final chart dimensions to prevent layout shift.

This mode should feel operational rather than editorial.

## Shared chart rules

1. State the analytical question before selecting a chart type.
2. Put title, definition, unit, time range, source, and freshness in the visual hierarchy.
3. Use one visual channel per meaning: position for magnitude, color for series identity, and texture or dash only when it adds a second necessary distinction.
4. Do not connect incompatible denominators or imply a funnel when stages do not share a population.
5. Keep gridlines quieter than the data and labels quieter than the title.
6. On mobile, enlarge one chart to the content width; do not shrink a desktop dashboard until labels become illegible.
7. SVG supports crisp labels and accessible structure. Canvas is viable for dense or high-frequency rendering, but add a text summary, table, or equivalent accessible representation.
8. Verify the loaded chart, not only the container. Record spinners, missing series, hydration errors, or stale timestamps as runtime evidence rather than silently treating them as design.

## Do not merge the modes by default

A printable public report and a monitoring terminal optimize for different reading behavior. Combining Visa's spacious single-series plot with Blockworks' full categorical legend often produces a chart that is neither calm nor operational. Choose the mode from the user's decision task.
