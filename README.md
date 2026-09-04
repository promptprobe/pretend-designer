# pretend-designer

A skill for **Cursor**, **Claude Code**, and **Codex**. It makes landing pages and UI look like a working designer made them, not the default AI template (an unexamined font, purple gradient, three rounded cards, a centered 600px island).

It is not a randomizer. Same brief, same thesis. Different projects pick different references on purpose so they do not all look like one another.

한국어는 [아래](#한국어) · [다운로드](#다운로드) · [Cursor](#cursor-한국어) · [Claude Code](#claude-code-한국어) · [Codex](#codex-한국어)

## Download

One skill folder, including its measured reference library. Three packs, so you drop the matching folder in the right location. Use the full-folder command under each agent; downloading only `SKILL.md` omits the case studies.

| Agent | Download | This project (commit it) | Every project on this machine | Invoke |
| --- | --- | --- | --- | --- |
| **Cursor** | [folder](https://github.com/promptprobe/pretend-designer/tree/main/packs/cursor/pretend-designer) | `.cursor/skills/pretend-designer/` | `~/.cursor/skills/pretend-designer/` | `/pretend-designer` |
| **Claude Code** | [folder](https://github.com/promptprobe/pretend-designer/tree/main/packs/claude/pretend-designer) | `.claude/skills/pretend-designer/` | `~/.claude/skills/pretend-designer/` | `/pretend-designer` |
| **Codex** | [folder](https://github.com/promptprobe/pretend-designer/tree/main/packs/codex/pretend-designer) | `.agents/skills/pretend-designer/` | `~/.agents/skills/pretend-designer/` | `$pretend-designer` |

The three folders contain the same skill and references. Only the destination changes.

---

## Cursor

**This project** (share with the team — commit the folder):

```bash
mkdir -p .cursor/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .cursor/skills/pretend-designer \
      pretend-designer-main/packs/cursor/pretend-designer
```

**Every project on this machine:**

```bash
mkdir -p ~/.cursor/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.cursor/skills/pretend-designer \
      pretend-designer-main/packs/cursor/pretend-designer
```

Cloud Agents, Agents Window, and remote SSH do **not** see `~/.cursor/skills`. For those, put the skill in the repo (`.cursor/skills/`), not only in your home folder.

**From Cursor UI:** Customize → Rules → Add Rule → Remote Rule (GitHub) → paste `https://github.com/promptprobe/pretend-designer`

Restart Agent chat if it does not show up. Type `/` and search `pretend-designer`, or `@pretend-designer`.

```text
/pretend-designer
Build a one-page UTM builder. Korean UI. No login.
```

Docs: [Cursor Agent Skills](https://cursor.com/docs/skills)

---

## Claude Code

**This project** (commit `.claude/skills/` so the team gets it):

```bash
mkdir -p .claude/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .claude/skills/pretend-designer \
      pretend-designer-main/packs/claude/pretend-designer
```

**Every project on this machine:**

```bash
mkdir -p ~/.claude/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.claude/skills/pretend-designer \
      pretend-designer-main/packs/claude/pretend-designer
```

The folder name is the slash command. You want `~/.claude/skills/pretend-designer/SKILL.md`, not an extra nested folder.

If you created `.claude/skills/` while a session was already running, start a new session (or run `/skills`) so Claude picks it up.

Invoke with `/pretend-designer`, or just ask for a restyle — Claude loads it when the description matches.

```text
/pretend-designer
This landing looks AI-generated. Restyle only. Do not change the JS.
```

Docs: [Extend Claude with skills](https://code.claude.com/docs/en/skills)

---

## Codex

Current Codex reads **`.agents/skills`**. Older installs still scan `~/.codex/skills`. Put it in `.agents` unless you already live in `$CODEX_HOME/skills`.

**This project:**

```bash
mkdir -p .agents/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .agents/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

**Every project on this machine:**

```bash
mkdir -p ~/.agents/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.agents/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

If `$skill-installer` is what you use, it may still land in `~/.codex/skills`. That path still works. You can also copy the same file there:

```bash
mkdir -p ~/.codex/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.codex/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

Restart Codex if the skill does not appear. Invoke with `$pretend-designer`, or open `/skills` and pick it. Codex can also match the description on its own.

```text
$pretend-designer
Review this page at 375 and 1280. Fail it if it is still a centered island.
```

Docs: [Build skills (Codex)](https://developers.openai.com/codex/skills)

---

## How to use (any agent)

1. Ask for a site, restyle, or UI review.
2. Invoke the skill (`/pretend-designer` in Cursor and Claude Code, `$pretend-designer` in Codex), or say “use pretend-designer.”
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
- A written px ramp and a deliberate type system; Korean pages use exactly one Hangul family
- Radius as a decision (often 0–4px on tools)
- No unexamined default font / purple / 3-up rounded cards / Get started + Learn more
- Korean text uses Pretendard or Noto Sans KR, generous measured leading, and zero or weak positive tracking; Inter is reserved for Latin-only pages
- **Page vs measure:** prose stays ~60–72 characters. Header, grid, and the tool use the viewport. No centered 560–920px island with empty matching gutters. Do not “fix” that with `max-width: 1200px; margin: auto`.

### What this is not

Not “add noise so it looks handmade.” Not Comic Sans. Not dark mode plus neon. Brand kits still win. Accessibility still wins.

Any other agent that reads [Agent Skills](https://agentskills.io): copy `SKILL.md` into that agent’s skills folder, or paste the file into the chat once and say “follow this skill.”

## Files

| Path | Why |
| --- | --- |
| `SKILL.md` | Canonical skill |
| `references/` | Measured case studies, Korean typography standard, and chart grammar |
| `packs/cursor/pretend-designer/SKILL.md` | Cursor pack |
| `packs/claude/pretend-designer/SKILL.md` | Claude Code pack |
| `packs/codex/pretend-designer/SKILL.md` | Codex pack |
| `.cursor/skills/pretend-designer/SKILL.md` | Same file, Cursor project layout (for this repo) |
| `LICENSE` | MIT |

---

## 한국어

코딩 에이전트가 웹을 만들 때 고민 없는 기본 폰트 + 보라 그라데이션 + 카드 3장 + 가운데 600px 섬으로 수렴하는 걸 막는 스킬입니다. 같은 브리프는 같은 테제로 가고, 프로젝트마다 레퍼런스를 새로 고르라고 해서 **서로 다르게** 나오게 합니다. 복권이 아닙니다. 무드를 고정하려면 레퍼런스 사이트를 지정하세요.

한글 페이지는 Apple Korea의 실측 리듬을 기준으로 합니다. Pretendard 또는 Noto Sans KR 중 하나만 쓰고, 본문은 기본 `17px/27px`, 자간은 `0` 또는 역할별 약한 양수만 허용합니다. Inter는 한글 글리프가 없으므로 영문 전용 페이지에서만 허용합니다.

### 다운로드

스킬은 `SKILL.md`와 실측 레퍼런스 문서가 들어 있는 폴더 단위입니다. 아래 전체 폴더 설치 명령을 사용하세요. `SKILL.md`만 받으면 사례 라이브러리가 빠집니다.

| 에이전트 | 다운로드 | 이 프로젝트 (커밋) | 이 컴퓨터 전부 | 호출 |
| --- | --- | --- | --- | --- |
| **Cursor** | [폴더](https://github.com/promptprobe/pretend-designer/tree/main/packs/cursor/pretend-designer) | `.cursor/skills/pretend-designer/` | `~/.cursor/skills/pretend-designer/` | `/pretend-designer` |
| **Claude Code** | [폴더](https://github.com/promptprobe/pretend-designer/tree/main/packs/claude/pretend-designer) | `.claude/skills/pretend-designer/` | `~/.claude/skills/pretend-designer/` | `/pretend-designer` |
| **Codex** | [폴더](https://github.com/promptprobe/pretend-designer/tree/main/packs/codex/pretend-designer) | `.agents/skills/pretend-designer/` | `~/.agents/skills/pretend-designer/` | `$pretend-designer` |

### Cursor 한국어

이 프로젝트만:

```bash
mkdir -p .cursor/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .cursor/skills/pretend-designer \
      pretend-designer-main/packs/cursor/pretend-designer
```

이 컴퓨터 모든 프로젝트:

```bash
mkdir -p ~/.cursor/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.cursor/skills/pretend-designer \
      pretend-designer-main/packs/cursor/pretend-designer
```

클라우드 에이전트는 홈 폴더 스킬을 못 봅니다. 클라우드에서 돌릴 거면 레포 안 `.cursor/skills/` 에 넣으세요.

Cursor UI: Customize → Rules → Add Rule → Remote Rule (GitHub) → `https://github.com/promptprobe/pretend-designer`

채팅에서 `/` 치고 `pretend-designer` 를 고르거나 `@pretend-designer` 로 부르면 됩니다.

### Claude Code 한국어

이 프로젝트만 (팀에 공유하려면 `.claude/skills/` 를 커밋):

```bash
mkdir -p .claude/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .claude/skills/pretend-designer \
      pretend-designer-main/packs/claude/pretend-designer
```

이 컴퓨터 모든 프로젝트:

```bash
mkdir -p ~/.claude/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.claude/skills/pretend-designer \
      pretend-designer-main/packs/claude/pretend-designer
```

폴더 이름이 슬래시 명령입니다. `~/.claude/skills/pretend-designer/SKILL.md` 가 맞고, 폴더가 한 겹 더 들어가면 안 됩니다. 세션이 이미 켜져 있으면 새 세션을 열거나 `/skills` 로 확인하세요.

호출: `/pretend-designer`. 안 불러도 설명과 맞으면 Claude가 스스로 켭니다.

```text
/pretend-designer
이 랜딩이 AI티 남. JS는 건드리지 말고 다시 칠해.
```

문서: [Claude Code skills](https://code.claude.com/docs/en/skills)

### Codex 한국어

지금 Codex는 **`.agents/skills`** 를 봅니다. 예전 경로는 `~/.codex/skills` 이고, 아직 스캔은 됩니다. 새로 넣으면 `.agents` 쓰세요.

이 프로젝트만:

```bash
mkdir -p .agents/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C .agents/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

이 컴퓨터 모든 프로젝트:

```bash
mkdir -p ~/.agents/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.agents/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

`$skill-installer` 는 아직 `~/.codex/skills` 에 넣을 수 있습니다. 안 보이면 Codex를 재시작하세요.

호출: `$pretend-designer`, 또는 `/skills` 에서 고르기.

```text
$pretend-designer
375 / 1280에서 이 페이지 리뷰해. 가운데 섬이면 실패.
```

문서: [Codex skills](https://developers.openai.com/codex/skills)

### 쓰는 법

1. 페이지를 만들거나, 다시 칠하거나, 리뷰해 달라고 한다.
2. 스킬을 켠다. Cursor / Claude Code 는 `/pretend-designer`, Codex 는 `$pretend-designer`.
3. 에이전트가 픽셀 전에 다섯 줄을 적어야 한다: 직무, 테제, 레퍼런스 하나, 타협 안 할 것, 이번에 안 만들 AI 티.
4. 그다음 디자인. 마지막에 375 / 1280 체크 (페이지가 가운데 섬인지 포함).

무드 고정 예:

```text
/pretend-designer
이 페이지 다시 칠해. 레퍼런스는 GOV.UK Design System. 복사는 그대로. 라운드 0–2px.
```

### 보면 안 되는 것

고민 없는 기본 폰트, 보라 그라데이션, 카드 3장, Get started + Learn more, 배너처럼 둥근 테두리 박스, **양옆이 같이 빈 가운데 `max-width` 섬**. 글줄은 짧아도 되고, 헤더·그리드·툴은 화면 폭을 써야 합니다. 한글에서는 폰트 혼용, 음수 자간, 일괄 700–900 웨이트도 실패입니다.
