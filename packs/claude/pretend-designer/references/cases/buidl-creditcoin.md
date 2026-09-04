# BUIDL CTC

- Reference: https://buidl.creditcoin.org/
- Observed: 2026-09-04
- Direction: typographic + product-index + terminal editorial
- Confidence: high for the live landing page observed at desktop and mobile; event copy and dates are transient.

## Job and thesis

The page helps builder teams understand the program, tracks, deadline, prize, and application path. Its visual thesis is a launch terminal crossed with an editorial event poster, not a generic Web3 landing page.

## Measured and observed evidence

- Display type: Tektur. Reading and navigation roles use Inter and Source Code Pro.
- Dominant surface: near-black `#0C0E10`, white, muted gray, and electric blue around `#4976FF`.
- Structural radius is mostly 0. Browser-like frames use about 8px; tags about 20px; the primary CTA is the reserved pill.
- Large display type uses tight tracking and compact line height. Small operational labels use wider tracking.
- The desktop composition uses full-width rules, browser chrome, an oversized topology/diagram field, and a dense section index.
- Mobile reorders the hero, diagram, and metadata rather than merely scaling the desktop grid.

## Why it works

The typeface, language, diagram, and grid all describe the same technical-builder world. The large claim provides emotional scale while the small labels, coordinates, deadlines, and track indices provide operational credibility. Rounded geometry is scarce enough that the primary action remains distinctive.

## Transferable rules

- Pair one expressive operational display face with a calmer reading face.
- Let metadata and numbering become part of the composition, not footer debris.
- Use a single diagram as the visual argument instead of several decorative illustrations.
- Reserve pills and soft geometry for actions that truly need contrast.
- For event pages, expose date, deadline, prize, and next action in the first two screens.

## Do not copy

Do not reuse the Creditcoin name, exact blue, terminal labels, track names, orbit diagram, or event copy. “Dark plus neon plus monospace” without the operational information architecture is costume rather than a thesis.

## Implementation lesson from the reconstruction exercise

A fixed mobile menu placed inside an animated, transformed header can use the header as its containing block and fail to cover the viewport. Prefer an explicit viewport-height layer under the header, then verify open, close, Escape, and body scroll lock at 375px.
