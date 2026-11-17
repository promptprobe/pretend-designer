# Icons and indicators

Read this file before adding any icon, logo, status dot, badge, chip, or "live" marker. The default for all of them is **absent**. Each one that ships must name its source and its job.

## Icons

### Why generated icons look unfinished

A model that writes `<path d="...">` from memory is drawing blind. The result has open contours, uneven stroke weight, off-grid joins, and a metaphor that is almost recognizable. Icons from different remembered sets also get mixed on one page: one 1.5px outline, one 2px outline, one filled glyph. Both failures are visible at a glance and neither is fixed by adjusting the path.

### Rules

1. **Never author icon path data.** Do not write, recall, approximate, or "simplify" SVG paths for an icon. Path data enters the project only by installing a maintained icon package or copying a file verbatim from its published source.
2. **One set per page.** Choose one maintained set and record its name and version in the file (`<!-- icon-set: lucide 0.x -->` or the package entry). Suitable sets include Lucide, Phosphor, Tabler Icons, Heroicons, Remix Icon, and Material Symbols. Any choice is fine; mixing is not.
3. **One style.** Outline or filled, not both. One stroke width across the page. One grid size (normally 24) rendered at 16, 20, or 24px.
4. **No source, no icon.** If the package cannot be installed and the file cannot be fetched, ship a text label. A missing icon is invisible; a malformed icon is the first thing people see.
5. **Do not scale a UI icon into an illustration.** A 24px-grid outline icon rendered at 48px or larger has a stroke that reads as a rough sketch. Large marks need a photograph, type, a diagram, or artwork the user supplied.
6. **Color is `currentColor`.** The icon takes the ink of its label. No gradient fills, no two-tone tinting, no accent-colored icon beside neutral text unless the accent encodes a state.
7. **Align to text.** Icon box equals the text line box or sits on the cap-height center; gap to label is 6–8px. Check at 100% zoom, not in a zoomed crop.
8. **Accessibility.** Decorative icons get `aria-hidden="true"`. Icon-only controls get an accessible name. An icon is never the only carrier of a destructive or irreversible meaning.

### Where an icon has a job

| Has a job | Has no job |
| --- | --- |
| Icon-only controls in a dense toolbar (close, search, menu, copy) | An icon above every feature title |
| File type, platform, or status glyph in a table row | An icon in a tinted rounded square or circle |
| Direction of an action: external link, download, expand | An icon before every nav item or list bullet |
| A recognized object the user must pick among many | A sparkle, wand, robot, or brain meaning "AI" |
| | An arrow after every link and button label |

When in doubt, set the label in type and stop. A page with zero icons is a finished page.

### Logos and brand marks

- The site's own mark is the user's supplied logo file. With no supplied logo, set the name as a wordmark in the page's type family. Do not invent a geometric glyph, monogram tile, or gradient square as a logo.
- Third-party logos (payment methods, integrations, social links, customer logos) come from the brand's official asset or a maintained brand-icon package, unmodified. Do not redraw them, and do not show customer or partner logos the user did not supply.
- Favicon follows the same rule: supplied asset, or the first letter set in the page type on the surface color.

## Indicators

### Status dots and "live" markers

A small colored circle next to a status word claims that the interface is reading a real state right now. When nothing is being read, the dot is decoration pretending to be data.

Remove by default:

- a green dot with `연동 중`, `연결됨`, `동기화 중`, `정상 운영`, `Live`, `Online`, `Connected`, `All systems operational`;
- a pulsing or pinging dot of any color;
- a dot in the header, hero, footer, or nav that never changes;
- tool or vendor attribution dressed as status: `Claude 연동 중`, `AI 연결됨`, `Powered by ...`;
- "last updated just now", fake timers, fake visitor or usage counters.

An indicator may ship only when all of these hold:

1. It is bound to a value the code actually reads (a request state, a health check, a timestamp from data).
2. Every state it can take is designed: ok, in progress, degraded, failed, unknown. A page that can only show green does not have a status indicator.
3. The state is carried by text. Color and shape are secondary; the text must be sufficient in grayscale.
4. It sits beside the thing it describes (the integration row, the data table, the form), not in the masthead as ambience.
5. It does not animate, except a progress indicator during an operation with a known end.

Preferred form is plain text in the mute ink with a timestamp when one exists: `마지막 동기화 14:02`. A failed state uses the danger text token and says what failed.

### Badges, chips, and pills

- No eyebrow pill above the hero heading (`새로운 기능 출시`, `v2.0`, `Beta`, `NEW`) unless the user supplied that announcement and it links somewhere.
- No category chips on cards when every card has the same category or the chip filters nothing.
- No counters, ratings, or "trusted by" rows without supplied data.
- A tag is a filter or a fact. If clicking it does nothing and removing it loses no information, remove it.

## Check

Before shipping:

1. Count icons. For each, state its job from the table above. Remove those without one.
2. Confirm every remaining icon comes from the single recorded set, with one stroke width and one grid.
3. View each icon at its rendered size at 1x and 2x. Any icon that looks drawn by hand is replaced by its label.
4. Search the markup for small circles (`border-radius: 50%`, `rounded-full` at 12px or less) and for pulse or ping animations. Each must pass the five indicator conditions or be deleted.
5. Search visible text for vendor, model, or tool names. Each must be user-supplied content or required attribution.
6. Run `python3 scripts/ui_lint.py <files>` from the skill directory.
