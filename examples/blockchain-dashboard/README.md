# STRATUM blockchain dashboard

A buildless Korean-language interactive mockup. All numbers are synthetic and are anchored to 2026-11-17, not current market values.

Open `index.html` directly, or serve this directory with a static HTTP server (for example `python3 -m http.server 4173`). No install or build step is required. Pretendard is bundled under its SIL Open Font License in `assets/OFL.txt`.

## Design brief

- Job: compare chain-level capital, activity and bridge flows.
- Thesis: a continuous research desk with ruled sections and a narrow navigation index.
- Reference: Blockworks Analytics' separation of navigation, analytical scope and chart controls. Its brand, dark palette, ticker and actual market data are not copied.
- Constraints: one Hangul family; no card grid or shadows; charts and table use the available width; 0px structural radius and 2–3px controls.
- Avoided tell: dark neon crypto tiles with disconnected KPI numbers.
- Type ramp: display 40/52, heading 19/29, label 13/20, prose 17/27, main number 44/54, caption 12/18, with compact operational metadata where needed.

The environment could not run Python or load the bundled dependency runtime. `palette.json` records the one-time, environment-random seed, an LCG fallback, role tokens and calculated contrast. Do not rerun the Python generator with that seed expecting identical output: its random algorithm differs. The stored token file is the reproduction source.

## Behavior

7/30/90-day ranges update historical TVL, comparison changes and bridge flows. 24h volume and fees remain fixed. Chain scope updates every data panel. Search and sorting apply to the comparison table and CSV export. Chart points support pointer inspection and left/right arrow keys. Dataset definitions open in a native dialog.

Totals: TVL $128.42B, DEX volume $8.76B, stablecoin supply $214.60B and fees $6.82M. TVL shares and changes are calculated from the same fixtures, not independently authored labels. The 30-day TVL change is 12.9% after rounding. Synthetic histories use deterministic functions; no random data changes on reload.

## QA

Rendered at 1280×1000 and 375×812. Checked period and scope changes, search empty state, TVL sorting, methodology dialog and font loading. Final QA details are recorded in `qa.json`. This is a design example with browser-local interactions, not a wallet-connected application.
