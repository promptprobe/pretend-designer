---
name: pretend-designer
description: >-
  Use when designing, restyling, or reviewing a website, landing page, or UI so
  it looks like a working designer made it, not a generic AI template.
---
# pretend-designer

Act like a working web designer with a brief, a thesis, and taste. Do not average the internet. The default output of a coding model is already a genre: an unexamined default font, indigo/purple, three rounded cards, centered hero. People clock that in three seconds. This skill exists to refuse that genre.

Use this for new pages, restyles, and design reviews. Skip it for pure backend, docs-only, or when the user named a specific existing system to copy exactly.

## 0. Before pixels (mandatory)

Write these five lines to yourself, then design. If you cannot fill them, you do not have a design yet.

1. **Job.** One sentence: who this is for, what they do on this page, what “done” looks like.
2. **Thesis.** One visual idea, not a moodboard dump. Examples: “a typesetter’s shop sign, not a SaaS dashboard”; “a field notebook with one controlled signal”; “a 90s catalog grid with contemporary spacing.”
3. **One real reference.** A specific existing site, magazine, album cover, wayfinding system, or product UI. Name it. Steal structure and attitude from that one thing, not from “modern SaaS.” If the user did not give a reference, pick one that fits the job and say which.
4. **Non-negotiables.** Two or three constraints that hurt: a type system, a dominant material (paper, CRT, metal, newsprint), a layout rule (no centered hero, no 3-up cards, full-bleed type, etc.).
5. **The tell you will not make.** Name the AI default this page would have fallen into, then ban it.

Do not start in Tailwind defaults. Do not start in shadcn. Those are implementation later, after the thesis is visible in type, color, and page geometry.

## 1. Hard bans (AI visual signature)

If any of these appear without a written reason that serves the thesis, rip them out.

**Type**
- An unexamined default font with no written reason
- Geist / Geist Mono as the “interesting” substitute (it is the new Inter)
- Space Grotesk, Poppins, Montserrat as the display face
- Headlines at weight 700 with `letter-spacing: -0.02em` as a reflex
- Negative tracking on Korean text as a reflex
- Mixing type families inside one Korean page
- Inter assigned to Korean text: Inter has no Hangul glyphs, so the browser silently mixes in a fallback
- The default type ramp (`3rem / 2.25rem / 1.5rem / 1rem`)

**Color**
- Tailwind `blue-500` / `indigo-500` / `purple-500` (`#3b82f6`, `#6366f1`, `#8b5cf6`)
- `from-purple-500 to-pink-500`, blue-to-purple, blue-to-cyan hero gradients
- `#F9FAFB` / `gray-50` page background
- Palettes of 3–4 invented hex codes with no named source
- Purple-on-white “AI startup” chrome

**Layout**
- Centered hero, one headline, two CTAs, then a row of three equal rounded cards
- `grid-cols-3 gap-6 rounded-2xl shadow-md` feature sections
- Perfect 8px-grid symmetry with no overlap, crop, or tension
- Everything max-width 1200px, everything padded the same
- The **centered island**: `max-width: 560px`–`920px; margin: 0 auto` with equal empty gutters and no full-bleed chrome. That is not “readable measure.” That is a form tutorial. Replacing it with `max-width: 1200px; margin: auto` is the same tell, one step wider.
- Sticky glass nav with blur over a gradient

**Chrome / radius / banners**
- `border-radius: 12px`–`24px` on every panel
- Pill buttons (`999px`) as the default
- Alert, note, peek, hero, or masthead as a rounded rectangle with a 1px stroke (a “banner in a card”)
- Box-shadow as a substitute for hierarchy

**Motion / decoration**
- Fade-up-on-scroll for every block
- Cards that `scale(1.05)` on hover
- Floating blobs, mesh gradients, particle fields, aurora backgrounds
- Emoji as icons or in CTAs
- Fake 3D abstract shapes from the same six stock packs

**Copy / chrome**
- Unlock / seamless / elevate / reimagine / supercharge / next-gen
- “Get started” + “Learn more” as the only two buttons
- Three-feature lists that say nothing
- Placeholder testimonials, fake avatars, 4.9 stars
- Gradient “Most popular” pricing pill
- Dashboard headlines that dramatize an inferred takeaway the user did not request
- An automatic subtitle that paraphrases the title or explains the page's own existence
- Decorative English section codes such as `B / CHANNEL CHECK` inside a Korean UI
- Meta headings that narrate the composition, count the evidence, or announce that sections are connected
- Scope-exclusion disclaimers in the hero when the excluded data is irrelevant to the requested view

Banning is not the design. After the bans, you still have to choose.

## 2. Choose like a designer

A real designer commits. Pick **one** of these directions and go deep. Mixing three of them is how you get another average.

- **Typographic.** The page is a typesetting job. A deliberate type system does 80% of the work. Latin pages may pair display and text faces; Korean pages use one Hangul family with scale and weight doing the hierarchy. Color is 2–3 notes. Layout follows measure and crop.
- **Editorial.** Magazine or newspaper geometry: columns, pull quotes, rules, folios, running feet, image that breaks the grid.
- **Material.** The screen is a surface (paper, plaster, steel, thermal print, CRT). Texture, edge, ink spread. Not a PNG overlay of “paper.”
- **Product-index.** Like a catalog, parts list, or wayfinding: dense, tabular, labeled, utilitarian. Beauty from order, not from hero.
- **Brutal / cheap.** Default system chrome used on purpose. Ugly-pretty. Few fonts, hard corners, one deliberately weighted accent.
- **Historical cut.** Steal from a decade that is not 2024-SaaS (Swiss, Dutch postmodern, Japanese retail, 70s sci-fi paperback, early web). Translate, do not costume.

If the product is actually a tool, it can still have a thesis. Linear did. Craigslist did. A docs site can be typeset. Do not use “it’s a tool so the default is fine.”

## 3. Craft rules

### Korean typography (mandatory when Hangul is present)

Read and apply [references/korean-typography.md](references/korean-typography.md) before styling any Korean page. Its font-family, size, line-height, tracking, line-breaking, and QA rules override generic type advice in this skill.

- Use exactly one Hangul-capable family for the page: **Pretendard** or **Noto Sans KR**. Do not assign different families to headings, body, numbers, or controls.
- Use **Inter only for Latin-only pages**. It has no Hangul glyphs and cannot satisfy the one-family rule on a Korean page.
- Build hierarchy with size and weight, normally 400 and 600, before introducing 700 or 800.
- Default Korean tracking to `0`. Never apply negative tracking automatically. Use only the small positive values in the reference scale when that role calls for them.
- Default Korean body copy to `17px/27px`; compact cards may use `17px/23px`. Do not squeeze explanatory Korean into a generic `16px/24px` preset without evidence.
- Use `word-break: keep-all`. Let paragraphs wrap naturally; insert manual line breaks only in short, deliberately composed display copy.

### Color palette (do this first)

Read [references/palette-selection.md](references/palette-selection.md). Color must vary without collapsing into the model's favorite named system.

- If the user supplied brand colors, an existing product palette, or exact color requirements, use them and do not run the lottery.
- Otherwise run `python3 scripts/palette_lottery.py --mode light` once from the skill directory. Use `--mode dark` only when the brief calls for a dark surface. The dependency-free script uses a fresh random seed and emits the seed, role-based tokens, text-safe accent variants, and contrast ratios.
- A layout or visual reference is **not** a color reference by default. Do not inherit its palette unless the user explicitly asks for a close color match.
- Do not choose a named design system, company, publication, or website as the fallback palette source. That turns a familiar example into a repeated house style.
- Do not reroll because another result feels more tasteful or familiar. Reroll only for a documented conflict with the user's brand, domain semantics, or accessibility requirements.
- Keep semantic roles stable: success stays success and danger stays danger. Randomize the visual palette, not meaning.
- Use `accent` for fills, rules, and data marks; use `accent-strong` for text. An accent is not permission to tint every selected row, KPI, icon, and chart.

If the script cannot run, obtain a fresh random seed from the environment and follow the same reference. Do not substitute a color system recalled from model memory.

### Type size and ink color

Write the ramp in px **before** CSS: display, lede, label, body, number, caption. Different jobs get different sizes, not one 16px body with a bold 32px title.

- On Latin-only pages, two faces may take different jobs when the thesis needs it. On Korean pages, one Hangul family uses weight and scale for every role.
- Prefer fonts with a body: oldstyle or tabular figures when numbers matter; a real italic; optical sizes if they exist.
- Self-host or use a specific foundry CSS, not “whatever Google Fonts listed first.”
- **Measure is for prose, not for the page.** Reading text: 60–72 characters. Headlines can break it. Tools, tables, mastheads, and grids use the viewport.
- Tracking: choose by script and role. Latin display may be tighter; Korean display defaults to zero or weak positive tracking, never reflexively negative.
- **Ink is a palette token, not leftover gray.** Mute text uses the system’s mute (a named gray/mix), not a muddy brown that almost matches the paper. Headlines, labels, and numbers should not all be the same hex.

### Radius (first-order, not a polish pass)

Radius is a decision you write down. Default for tools and editorial: `0`–`4px`. One reserved pill is allowed if the thesis needs a single action to look like a pill. Mixed radii need a reason. `12px`–`24px` on every card is a tell. `border-radius: 999px` on chips *and* buttons *and* inputs is a tell.

### Banners and panels

Alert, peek, note, hero, masthead, “result banner”: **no rounded rectangle with a 1px border**. That outline-card is the AI banner. Separate regions with a background shift, a hairline rule, or a 3–4px left rule. Fields (inputs) may keep a 1px hairline because they are fields. Hierarchy by type and placement, not box-shadow.

### Layout (page vs measure)

The page is a surface that meets the edges of the window. A lonely centered column with matching leftover margins is the AI default, even when the type is good.

- Header, rules, background, and at least one structural band are **full-bleed**.
- Put the tool on a real grid: 12-col, 2/3+1/3, left-aligned with a folio/rail, or a named system’s layout (GDS two-thirds, FT article+rail). Do not optically center a 600px stack “because it’s a form.”
- If something stays narrow (a receipt, a ticket, a caption), **pin it** (left, top, a column) so the leftover space is a decision, not leftover.
- Side space needs a job (rail, running footer, empty on purpose) or should not exist.
- Start with a grid, then break it once on purpose: overlap, full-bleed crop, a column that is too narrow, a title that collides with an image.
- Whitespace is uneven. A huge top margin and a tight cluster is more designed than even padding everywhere.
- Nav can be ugly, tiny, or over to the side. It does not have to be a floating pill.
- Mobile is a re-sequence, not “stack the desktop.”

### Image / mark
- Prefer type as image, a single photograph, or a diagram. Do not generate decorative 3D blobs.
- If you generate an image, it must obey the thesis (grain, lens, era). One image, not a set of matching illustrations.
- Favicon and og:image should look like the same studio, not a gradient square.

### Motion
- Default is none.
- If motion exists, it has a job: a page-turn, a tick, a counter, a hover that reveals a layer. One family of easing. No scroll-fade catalog.
- Respect `prefers-reduced-motion`.

### Copy
- Write like the people who will use the page. Specific nouns. No filler adjectives.
- One primary action, named after the outcome (“Send the invoice”, “Book Tuesday”), not “Get started.”
- Headlines can be dry. Dry is designed. Hype is a template.

### UI copy (mandatory for dashboards and tools)

Read and apply [references/ui-copy.md](references/ui-copy.md). User-requested content and terminology outrank an agent's urge to make the page sound editorial.

- Use the user's exact page name or a literal subject label as the title. Do not turn an inferred data pattern into a slogan or executive conclusion unless the user explicitly asked for one.
- Default to **no subtitle**. Keep one only when it adds scope, unit, state, instruction, or risk that is necessary to use or interpret the page and is not already visible.
- Give every visible string a job: identify, label, define, filter, instruct, warn, or enable action. If deleting it changes none of those, delete it.
- Do not announce which unrelated data was excluded. Add a methodology note only when omission would cause a material misreading, the user requested it, or compliance requires it; place it next to the affected metric or in details, not in the hero.
- Match the user's language. Do not invent alphabetical section folios, all-caps English labels, `SIGNAL`, `CHECK`, `OVERVIEW`, or `INSIGHT` as decoration. Preserve only real domain terms the user needs.
- If `slop-sensor` is available, use its embedded mode with the appropriate register before finalizing Korean UI copy. Then run the UI necessity check above; prose-pattern detection alone cannot decide whether a sentence belongs in the interface.

## 4. Implementation (so the code does not undo the design)

- CSS variables for the tokens, named by role (`--surface`, `--ink`, `--accent`, `--danger`) rather than a borrowed brand.
- If you use Tailwind, treat it as a compiler, not a look. Custom theme, custom font, custom radius (including `0` or `2px`).
- Avoid shadcn defaults unless you restyle every token. A restyled button is fine; a page of default `Card` is not.
- Semantic HTML. Real labels. Focus states that match the thesis (ink ring, accent underline, fat outline), not a framework-default glow.
- On Korean pages, load one family and only the weights needed. On Latin-only pages, use at most two families and two to four files.
- No autoplay video backgrounds.

## Reference cases (conditional)

When the user supplies a design reference, asks for a reference breakdown, or needs analytical charts, read [references/reference-workflow.md](references/reference-workflow.md). Select only the one or two cases that fit the current job; do not load the full case library by default. For chart work, also read [references/chart-grammar.md](references/chart-grammar.md). For any page containing Korean, read [references/korean-typography.md](references/korean-typography.md) regardless of visual direction. For dashboards and tools, read [references/ui-copy.md](references/ui-copy.md).

Reuse structure and decision logic, not outcome-specific fonts, colors, copy, imagery, or brand identity. State what principle is being borrowed, what recognizable feature is being rejected, and why the chosen case fits the current user's job.

## 5. Ship check (run before you call it done)

Look at the page at 375px and 1280px, and answer:

1. If you grayscale it, does hierarchy still hold?
2. Could you identify the studio without the logo? (Type + color + geometry.)
3. Is there a single element a coworker would argue about? If everything is agreeable, it is still average.
4. Count unexamined default fonts / purple / 3-up cards / dual CTAs / fade-up / 16px+ radius on panels / outlined banners / centered 600–900px islands. Score must be zero unless justified in the thesis.
5. Does every dashboard title name the user's requested subject, metric, or task instead of manufacturing a takeaway?
6. Would a designer from the reference you named recognize the theft? If not, you only vibe-copied.
7. Can you point at the user-supplied palette or the lottery seed, token roles, contrast results, and type ramp in the file?
8. At 1280px, does chrome use the width, or is there a puddle of UI in the middle of the background?
9. If Korean is present: is there exactly one Hangul family, no negative tracking, `word-break: keep-all`, and a measured line-height from the Korean reference scale?
10. Delete every subtitle, explanatory sentence, section code, and methodology note once. If the page still works and means the same thing, keep it deleted.

If 3, 4, 5, 7, 8, 9, or 10 fail, redo copy, type, radius, color, and **page geometry** before adding more components.

## 6. What this skill is not

- Not “add noise and typos so it looks handmade.” That is another template.
- Not “use Comic Sans” or random fonts as personality.
- Not dark mode plus neon equals original.
- Not a request to ignore accessibility, performance, or the user’s actual brand rules. If they gave a brand kit, interpret it with craft. Do not ignore it.
- Not a reason to delay shipping with infinite moodboards. Thesis, then one tight pass, then the checklist.
- Not “make everything full-width soup.” Prose still has a measure. Tools still have alignment. The ban is the *island*, not density.

When the user already has a design they like, match that, then apply the bans only where their design is accidentally generic.
