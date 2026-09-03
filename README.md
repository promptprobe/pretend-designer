# pretend-designer

A skill for coding agents. It makes landing pages and UI look like a working designer made them, not the default AI template (Inter, purple gradient, three rounded cards, a centered 600px island).

It is not a randomizer. Same brief, same thesis. Different projects pick different references on purpose so they do not all look like one another.

한국어 사용법은 아래 [한국어](#한국어) 를 보세요.

## Install (Cursor) — 30 seconds

**This project only** (commit it so the whole team gets it):

```bash
mkdir -p .cursor/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/.cursor/skills/pretend-designer/SKILL.md \
  -o .cursor/skills/pretend-designer/SKILL.md
```

Or copy the folder from this repo:

```text
.cursor/skills/pretend-designer/SKILL.md
```

**Every project on this machine:**

```bash
mkdir -p ~/.cursor/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/.cursor/skills/pretend-designer/SKILL.md \
  -o ~/.cursor/skills/pretend-designer/SKILL.md
```

Cloud Agents and remote SSH do **not** see `~/.cursor/skills`. If the agent runs in the cloud, put the skill in the repo (`.cursor/skills/`), not only in your home folder.

**From Cursor UI:** Customize → Rules → Add Rule → Remote Rule (GitHub) → paste `https://github.com/promptprobe/pretend-designer`

Restart Agent chat if it does not show up. Type `/` and search `pretend-designer`.

## Install (Claude Code / Codex / other Agent Skills)

Same file, different folder:

```bash
# Claude Code
mkdir -p ~/.claude/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/SKILL.md \
  -o ~/.claude/skills/pretend-designer/SKILL.md

# Codex
mkdir -p ~/.codex/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/SKILL.md \
  -o ~/.codex/skills/pretend-designer/SKILL.md
```

Project copies: `.claude/skills/pretend-designer/SKILL.md` or `.codex/skills/pretend-designer/SKILL.md` in the repo.

Any other agent that reads Agent Skills: point it at `SKILL.md`. You can also paste the file into the chat once and say “follow this skill.”

## How to use

1. Ask for a site, restyle, or UI review.
2. Invoke the skill: `/pretend-designer` or `@pretend-designer`, or just say “use pretend-designer.”
3. The agent must write five lines **before pixels**: job, thesis, one real reference, non-negotiables, the AI tell it will not make.
4. Then it designs. Then it runs the ship check (including page width at 1280px).

### Pin a look (not a lottery)

If you do not name a reference, the agent picks one that fits the job. That is how two toys stop looking like twins. It is a commit, not a dice roll.

To lock a mood, name the reference:

```text
/pretend-designer
Restyle this page.
Reference: GOV.UK Design System. Keep our copy. Radius 0–2px.
```

Same page, same brief, second run should stay in that thesis.

### What you should see

- A named palette (FT Origami, IBM Carbon, MTA, GDS, a foundry specimen) — not four invented hex codes
- Two typefaces with a written px ramp
- Radius as a decision (often 0–4px on tools)
- No Inter / purple / 3-up rounded cards / Get started + Learn more
- **Page vs measure:** prose stays ~60–72 characters. Header, grid, and the tool use the viewport. No centered 560–920px island with empty matching gutters. Do not “fix” that with `max-width: 1200px; margin: auto`.

### Example prompts

```text
/pretend-designer
Build a one-page UTM builder. Korean UI. No login.
```

```text
/pretend-designer
This landing looks AI-generated. Restyle only. Do not change the JS.
```

```text
/pretend-designer
Review this page at 375 and 1280. Fail it if it is still a centered island.
```

## What this is not

Not “add noise so it looks handmade.” Not Comic Sans. Not dark mode plus neon. Brand kits still win. Accessibility still wins.

## Files

| Path | Why |
| --- | --- |
| `SKILL.md` | Canonical skill (copy this) |
| `.cursor/skills/pretend-designer/SKILL.md` | Same file, Cursor project layout |
| `LICENSE` | MIT |

---

## 한국어

코딩 에이전트가 웹을 만들 때 Inter + 보라 그라데이션 + 카드 3장 + 가운데 600px 섬으로 수렴하는 걸 막는 스킬입니다. 같은 브리프는 같은 테제로 가고, 프로젝트마다 레퍼런스를 새로 고르라고 해서 **서로 다르게** 나오게 합니다. 복권이 아닙니다. 무드를 고정하려면 레퍼런스 사이트를 지정하세요.

### Cursor에 넣기 (30초)

이 프로젝트만 (팀에 공유하려면 커밋):

```bash
mkdir -p .cursor/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/.cursor/skills/pretend-designer/SKILL.md \
  -o .cursor/skills/pretend-designer/SKILL.md
```

이 컴퓨터 모든 프로젝트:

```bash
mkdir -p ~/.cursor/skills/pretend-designer
curl -fsSL https://raw.githubusercontent.com/promptprobe/pretend-designer/main/.cursor/skills/pretend-designer/SKILL.md \
  -o ~/.cursor/skills/pretend-designer/SKILL.md
```

클라우드 에이전트는 홈 폴더 스킬을 못 봅니다. 클라우드에서 돌릴 거면 레포 안 `.cursor/skills/` 에 넣으세요.

Cursor UI: Customize → Rules → Add Rule → Remote Rule (GitHub) → `https://github.com/promptprobe/pretend-designer`

채팅에서 `/` 치고 `pretend-designer` 를 고르거나 `@pretend-designer` 로 부르면 됩니다.

### 쓰는 법

1. 페이지를 만들거나, 다시 칠하거나, 리뷰해 달라고 한다.
2. 스킬을 켜다.
3. 에이전트가 픽셀 전에 다섯 줄을 적어야 한다: 직무, 테제, 레퍼런스 하나, 타협 안 할 것, 이번에 안 만들 AI 티.
4. 그다음 디자인. 마지막에 375 / 1280 체크 (페이지가 가운데 섬인지 포함).

무드 고정 예:

```text
/pretend-designer
이 페이지 다시 칠해. 레퍼런스는 GOV.UK Design System. 복사는 그대로. 라운드 0–2px.
```

### 보면 안 되는 것

Inter, 보라 그라데이션, 카드 3장, Get started + Learn more, 배너처럼 둥근 테두리 박스, **양옆이 같이 빈 가운데 `max-width` 섬**. 글줄은 짧아도 되고, 헤더·그리드·툴은 화면 폭을 써야 합니다.
