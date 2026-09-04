# UI copy: say only what the interface needs

Read this file for dashboards, analytical reports, tools, and operational interfaces. The default is literal, short, and user-led. Do not add an editorial voice merely because the layout has space for a headline and subtitle.

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

Before shipping a dashboard or tool:

1. List the job of every title, subtitle, explanatory sentence, note, and section label.
2. Remove every line without a functional job.
3. Confirm that remaining conclusions were requested or are directly supported.
4. Move necessary methodology to the affected metric instead of the hero.
5. Remove decorative English, section letters, and translated template labels.
6. Compare the remaining labels with the user's original request and terminology.
7. Render the final interface once with subtitles hidden; restore only the lines whose absence causes a real comprehension or operation failure.

The goal is not an artificially terse interface. It is an interface whose words earn their space.
