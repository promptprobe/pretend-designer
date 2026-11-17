# UI copy: say only what the interface needs

Read this file for every page that shows words: homepages, landing pages, dashboards, analytical reports, tools, and operational interfaces. The default is literal, short, and user-led. Do not add an editorial voice merely because the layout has space for a headline and subtitle.

This contract incorporates the fact-preservation and unsupported-claim principles of [Slop Sensor](https://github.com/promptprobe/slop-sensor), then adds a UI-specific necessity test. Slop Sensor finds recurring prose patterns; it does not by itself decide whether a natural-sounding sentence belongs in an interface.

## Order of authority

When choosing visible copy, use this order:

1. The user's requested wording, labels, scope, and language.
2. Verified product terms, metric names, units, filters, and source labels.
3. Text required to operate the interface or avoid a material misreading.
4. Optional interpretation only when the user explicitly requests analysis, narrative, or an executive summary.

Do not add level 4 by default.

## The necessity test

Assign every visible string one job:

- identify the page or object;
- label a metric, chart, filter, state, or action;
- define a term the intended user may not know;
- provide an instruction needed to complete the task;
- warn about a material limitation, risk, or error;
- state a user-requested conclusion with traceable evidence.

Delete the string if it has no job. Then ask: if this line disappears, can the user still understand the page, operate it, and interpret the numbers correctly? If yes, keep it deleted.

Whitespace is not a copy requirement. A design does not need a subtitle because a component template includes a subtitle slot.

## Homepages and landing pages

The same necessity test applies outside dashboards. A homepage is not exempt because it is marketing; most of what reads as machine-written on a homepage is the sentence under each heading.

| Slot | Default |
| --- | --- |
| Hero heading | The product or site name, or one literal sentence saying what it is and for whom. No slogan. |
| Hero lede | Absent. Keep one only when it adds a fact the heading lacks: price, platform, availability, a hard constraint. |
| Eyebrow, badge, or announcement pill above the heading | Absent unless it links to a real, dated announcement the user supplied. |
| Section heading | A noun phrase naming the content. |
| Paragraph under a section heading | Absent. The content below the heading is the explanation. |
| Card or feature text | A name plus facts: a number, a spec, a limit, a supported format. No benefit prose. |
| Button | Verb plus object, named after what happens next. |
| Footer tagline | Absent. |

Rules:

- Do not narrate the layout or the reader's next move: `여기에 모여서, 한번에 확인`, `아래에서 확인하세요`, `필요한 모든 것이 한곳에`, `Everything you need, in one place`. The reader can see where things are.
- Do not describe a heading with a second sentence that says the same thing in more words. `기능` followed by `다양한 기능을 한눈에 살펴보세요` is one string of content and one string of filler.
- Do not invent claims, counts, customers, or benefits to fill a section. When the brief has no content for a section, drop the section. A short page built from real content is the correct output.
- Do not mention how the page was made or what powers it (`Claude 연동 중`, `AI 기반`, `Powered by ...`) unless the user asked for that line or a license requires attribution. Tooling is not content.
- An empty slot stays empty. Do not write to balance a column or fill a card to equal height.

Bad default:

> 흩어진 자료를 한곳에
>
> 여기에 모여서, 한번에 확인하세요. 더 빠르고 스마트한 업무가 시작됩니다.

Better default, using only what the brief states:

> 팀 문서 보관함

If the brief gives a real differentiator, state it as a fact (`PDF·HWP·DOCX 전문 검색`), not as a promise (`어떤 문서든 손쉽게`).

## Korean machine-voice patterns

These are natural Korean and still mark a page as generated. Rewrite as a literal label or delete; do not swap in a synonym.

| Pattern | Examples | Fix |
| --- | --- | --- |
| Comma-split slogan | `여기에 모여서, 한번에 확인` · `더 빠르게, 더 똑똑하게` | Name the thing: `통합 조회` |
| Convenience adverbs | `한눈에` · `한번에` · `한곳에서` · `손쉽게` · `간편하게` · `쉽고 빠르게` | Delete; state the actual step count or time if known |
| Urgency openers | `이제` · `지금 바로` · `오늘부터` | Delete |
| Empty superlatives | `혁신적인` · `스마트한` · `완벽한` · `강력한` · `새로운 경험` · `그 이상` · `차원이 다른` | Replace with the measurable property or delete |
| Totalizers | `모든 것` · `올인원` · `A부터 Z까지` · `처음부터 끝까지` | List the actual scope |
| Second-person intimacy | `당신의` · `당신만의` · `여정` · `함께합니다` | Delete |
| Negation-reveal | `단순한 도구가 아닙니다. 파트너입니다.` | State what it is, once |
| Rhetorical question heading | `왜 OO인가요?` · `아직도 수작업 하시나요?` | `OO 소개`, `도입 효과`, or no heading |
| Staccato triplet | `빠른 설정. 안전한 보관. 쉬운 공유.` | One literal sentence or a spec list |
| Translationese | `~을 통해` · `~을 제공합니다` · `~할 수 있습니다` repeated per sentence | Use the direct verb: `검색합니다`, `내보냅니다` |
| Invitation endings on every block | `~해 보세요` · `~을 만나보세요` · `~을 경험하세요` | Keep the imperative on the button only |
| Decorative punctuation | Em dashes, `→` in body text, `!`, `✨` | Plain punctuation |

English equivalents fall under the same rule: `all in one place`, `at a glance`, `effortlessly`, `meet X`, `say goodbye to`, `built for the way you work`.

## Dashboard header default

Use this hierarchy unless the user asks for narrative reporting:

- **Page title:** the exact product, report, subject, or task name. Prefer a literal noun phrase.
- **Subtitle:** absent by default.
- **Context:** date range, active segment, unit, or freshness only when it is not already clear from nearby controls or metadata.
- **Executive takeaway:** absent unless requested. When requested, distinguish observation from interpretation and keep the underlying evidence visible.

Bad default:

> 검색은 회복했고, 제휴는 새고 있다.
>
> 비용보다 계약을 먼저 봅니다. 모든 수치는 선택한 유료 유입 집단 안에서 비교합니다.

Better default:

> 유료 유입 성과

If the user supplied a more specific dashboard name, use that exact name instead. Do not invent the “better” example as a universal title.

## Subtitles and explanatory copy

A subtitle may stay only when at least one condition is true:

- it states a non-obvious unit, denominator, period, or scope needed to read the numbers;
- it explains an interaction the user cannot reasonably discover;
- it communicates loading, stale data, an error, or another operational state;
- a required legal, compliance, or safety qualification belongs there;
- the user asked for contextual or narrative copy.

Remove a subtitle when it:

- restates the title;
- tells the reader that the dashboard focuses on outcomes, efficiency, or decisions;
- explains how carefully the page was designed or how sections connect;
- announces a conclusion not explicitly requested;
- fills empty space.

## Methodology and exclusions

Accuracy does not require advertising every excluded variable.

- Do not say what the page does not contain when the excluded material is outside the user's requested scope.
- Keep denominator, attribution, source, or comparability notes when omitting them would likely produce a wrong conclusion.
- Put necessary methodology beside the affected metric, in a tooltip, table note, source row, or expandable details section. Do not turn it into the hero subtitle.
- Preserve legally required disclosures and the user's explicit caveats.

Unnecessary by default:

> 인지도·검색량·광고 노출은 분모가 달라 이 전환 흐름에 포함하지 않았습니다.

This may become necessary only when the interface otherwise implies that those measures share a denominator or belong to the same funnel.

## Section labels

Use a section title only when it helps navigation or distinguishes a real group of content. Name the content directly.

| Avoid | Use only if a label is needed |
| --- | --- |
| `B / CHANNEL CHECK` | `채널별 성과` |
| `판단 근거 4개 모두 연결` | `판단 근거`, or no heading |
| `D / CREATIVE SIGNAL` | `소재별 성과` |

Do not mechanically translate decorative labels. Delete them if the chart titles or layout already make the grouping clear. Do not prefix sections with A/B/C/D unless the sequence has a real navigational or procedural function requested by the user.

Match the interface language. Retain English only for real product names, standard abbreviations, codes, tickers, or terms the intended user actually uses.

## Slop Sensor pass

When `slop-sensor` is installed, invoke it in embedded mode with the closest register, normally `business` or `marketing`, and preserve facts, numbers, dates, citations, and user terminology.

After that pass, always run the necessity test. In a 2026-09-04 check, the five dashboard strings above scored `0/20` in Slop Sensor v0.2's business register because they did not match its registered prose patterns. That is expected: a sentence can be natural and still be unnecessary UI copy.

When `slop-sensor` is unavailable, do not block the design. Apply these built-in checks:

- no unsupported claim, significance, authority, or conclusion;
- no mechanical contrast used only to sound insightful;
- no meta narration about the page or its structure;
- no filler introduction, capability phrase, or generic optimistic ending;
- no new fact beyond the user's brief and verified data;
- no paraphrase of a heading immediately below it.

## Final copy check

Before shipping any page:

1. List the job of every title, subtitle, explanatory sentence, note, and section label.
2. Remove every line without a functional job.
3. Confirm that remaining conclusions were requested or are directly supported.
4. Move necessary methodology to the affected metric instead of the hero.
5. Remove decorative English, section letters, and translated template labels.
   On homepages, also remove ledes, eyebrow badges, paragraphs under section headings, and tool or vendor attribution that the user did not supply.
6. Compare the remaining labels with the user's original request and terminology.
7. Render the final interface once with subtitles hidden; restore only the lines whose absence causes a real comprehension or operation failure.
8. Run `python3 scripts/ui_lint.py <files>` from the skill directory and resolve each finding by deleting or rewriting the string, not by rephrasing around the pattern.

The goal is not an artificially terse interface. It is an interface whose words earn their space.
