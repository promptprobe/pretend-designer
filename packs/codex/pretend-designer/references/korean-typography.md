# Korean typography standard

Read this file for every page that contains Korean. It is the default Korean type contract for this skill, derived from the live [Apple Korea iPhone page](https://www.apple.com/kr/iphone/) at 1440×1000 and 375×812 on 2026-09-04.

The source uses the proprietary `SF Pro KR`. Do not imitate the family name or depend on an Apple system font. Transfer its sizing, leading, tracking discipline, weights, line breaking, and neutral palette to one permitted Hangul family.

## Non-negotiable font rule

Choose exactly one family per Korean page:

1. **Pretendard** — default for product, editorial, dashboard, and mixed Korean/Latin UI.
2. **Noto Sans KR** — use when broad language coverage, Google Fonts delivery, or a slightly more neutral public-service tone matters.
3. **Inter** — allowed only when the page is Latin-only. Inter contains no Hangul glyphs; a Korean browser will silently render Hangul with another font and break the one-family rule.

One family may use multiple weights. Do not set a different `font-family` for headings, body, buttons, charts, or numbers. Load only the weights that appear, normally 400 and 600.

## Measured Apple baseline

These are observed computed styles, not guesses. Use the roles that the page actually needs; do not force every tier into every page.

| Role | Desktop size / line-height | Mobile size / line-height | Weight | Letter spacing |
| --- | --- | --- | --- | --- |
| Large section display | `56px / 66px` | `48px / 57px` when it becomes the page title | 600 | `0` (`normal`) |
| Section heading | `32px / 39px` | `28px / 35px` | 600 | `+0.004em` desktop; `0` mobile |
| Feature statement | `28px / 35px` | `28px / 35px` | 600 | `0` to `+0.007em` |
| Component heading | `19px / 29px` | `19px / 29px` | 600 | `+0.012em` |
| Explanatory body | `17px / 27px` | `17px / 27px` | 400 | `0` |
| Compact card copy | `17px / 23px` | `17px / 23px` | 400 or 600 | `0` |
| Promo / secondary action | `14px / 22px` | `14px / 22px` | 400 | `0` |
| Legal / footnote | `12px / 16px` | `12px / 16px` | 400 | `0` |

The essential pattern is not simply “large type.” Korean leading stays generous, body text remains 17px, and large Hangul is not compressed with fashionable negative tracking.

## Required application rules

- Start Korean tracking at `0`. Negative tracking is prohibited unless the user supplies a different Korean brand system with measured evidence.
- Use the weak positive tracking only for the measured role: about `0.004em` at 32px, `0.007em` at 28px feature statements, and `0.012em` at 19px component headings.
- Use 600 for strong Korean headings before reaching for 700 or 800. Heavy weight plus tight tracking is a common AI-generated tell.
- Keep explanatory paragraphs at `17px/27px` by default. Use `17px/23px` only for short card copy, never for long prose.
- Use `word-break: keep-all` on Korean. Add `overflow-wrap: break-word` only as an emergency guard for URLs and long tokens.
- Do not insert `<br>` into body paragraphs to make one screenshot look balanced. Manual line breaks are allowed only in short display copy whose composition is deliberate at each breakpoint.
- Give prose a readable measure. Begin around `28–36rem` and adjust after checking real Korean copy; do not use character-count assumptions copied from English.
- Check actual glyph rendering in the browser. A CSS declaration is not proof that the requested webfont loaded.

## Neutral color baseline

Use this only when the user has not supplied a brand palette. A brand system may replace it, but preserve the contrast roles.

| Token | Value | Use |
| --- | --- | --- |
| `--ko-ink` | `#1d1d1f` | Primary headings and body |
| `--ko-ink-strong` | `#333336` | Alternate dark surface or dense UI ink |
| `--ko-ink-muted` | `#6e6e73` | Secondary explanation |
| `--ko-ink-subtle` | `#86868b` | Tertiary metadata |
| `--ko-bg` | `#ffffff` | Primary surface |
| `--ko-bg-soft` | `#f5f5f7` | Section separation |
| `--ko-link` | `#0066cc` | Inline links |
| `--ko-control` | `#0071e3` | Primary control |
| `--ko-legal` | `rgba(0, 0, 0, 0.56)` | Legal and footnotes on white |

Do not turn this neutral palette into an Apple imitation. It is a readability baseline; product color, grid, imagery, and interaction must still come from the user's own brief.

## Reference CSS

```css
/* Korean type contract: Apple Korea rhythm translated to Pretendard. */
:root {
  --font-ko: "Pretendard";
  --ko-ink: #1d1d1f;
  --ko-ink-muted: #6e6e73;
  --ko-bg: #fff;
  --ko-bg-soft: #f5f5f7;
  --ko-link: #06c;
}

html[lang="ko"] {
  font-family: var(--font-ko), sans-serif;
  color: var(--ko-ink);
  background: var(--ko-bg);
  word-break: keep-all;
  overflow-wrap: break-word;
  font-synthesis: none;
}

.ko-display {
  font-size: 56px;
  line-height: 66px;
  font-weight: 600;
  letter-spacing: 0;
}

.ko-heading {
  font-size: 32px;
  line-height: 39px;
  font-weight: 600;
  letter-spacing: 0.004em;
}

.ko-body {
  font-size: 17px;
  line-height: 27px;
  font-weight: 400;
  letter-spacing: 0;
  max-width: 34rem;
}

@media (max-width: 734px) {
  .ko-display {
    font-size: 48px;
    line-height: 57px;
  }

  .ko-heading {
    font-size: 28px;
    line-height: 35px;
    letter-spacing: 0;
  }
}
```

The `sans-serif` fallback is resilience, not permission to mix a second designed family. Verify that the chosen webfont loads before accepting the page.

## Korean typography QA

At 375px and 1280px, fail the page if any answer is no:

1. Is every visible Hangul glyph rendered by one chosen family, Pretendard or Noto Sans KR?
2. Are body paragraphs at least 17px with the appropriate 27px explanatory leading?
3. Is all Korean tracking zero or one of the small positive, role-specific values above?
4. Does Korean wrap by phrase without arbitrary syllable breaks?
5. Do paragraphs wrap naturally without screenshot-specific `<br>` tags?
6. Are headings primarily 600 weight rather than uniformly 700–900?
7. Does muted text remain readable on its actual background?
8. Have font loading and both breakpoints been inspected in the rendered page, not only in source code?

Confidence: **high** for the measured Apple computed styles and colors at the two recorded viewports; **moderate** for visual equivalence after translating from SF Pro KR to Pretendard or Noto Sans KR, so rendered QA remains mandatory.
