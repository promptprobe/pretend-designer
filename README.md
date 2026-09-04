# pretend-designer

코딩 에이전트가 웹을 만들 때 반복하는 **AI 기본 디자인**을 피하게 만드는 디자인 스킬입니다.

보라 그라데이션, 둥근 카드 3장, 가운데 모인 히어로, 근거 없는 폰트와 색상 대신 먼저 디자인의 목적·테제·레퍼런스를 정하고 작업하게 합니다. Cursor, Claude Code, Codex에서 같은 규칙과 사례 라이브러리를 사용할 수 있습니다.

**[전체 저장소 ZIP 다운로드](https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.zip)** · **[스킬 원문](SKILL.md)** · **[한글 타이포 기준](references/korean-typography.md)** · **[레퍼런스 라이브러리](references/reference-workflow.md)**

## 1분 설치

이 스킬은 `SKILL.md` 하나가 아니라 `references/`까지 포함한 **폴더 단위**입니다. 에이전트에 맞는 `pretend-designer` 폴더 전체를 설치해야 실측 사례와 한글 타이포 규칙이 함께 작동합니다.

| 에이전트 | 받을 폴더 | 프로젝트에 설치 | 내 컴퓨터 전체에 설치 | 호출 |
| --- | --- | --- | --- | --- |
| Cursor | [Cursor pack](packs/cursor/pretend-designer) | `.cursor/skills/pretend-designer/` | `~/.cursor/skills/pretend-designer/` | `/pretend-designer` |
| Claude Code | [Claude pack](packs/claude/pretend-designer) | `.claude/skills/pretend-designer/` | `~/.claude/skills/pretend-designer/` | `/pretend-designer` |
| Codex | [Codex pack](packs/codex/pretend-designer) | `.agents/skills/pretend-designer/` | `~/.agents/skills/pretend-designer/` | `$pretend-designer` |

### macOS / Linux: 내 컴퓨터 전체에 설치

Codex:

```bash
mkdir -p ~/.agents/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.agents/skills/pretend-designer \
      pretend-designer-main/packs/codex/pretend-designer
```

Claude Code:

```bash
mkdir -p ~/.claude/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.claude/skills/pretend-designer \
      pretend-designer-main/packs/claude/pretend-designer
```

Cursor:

```bash
mkdir -p ~/.cursor/skills/pretend-designer
curl -fsSL https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.cursor/skills/pretend-designer \
      pretend-designer-main/packs/cursor/pretend-designer
```

설치 후 실행 중이던 에이전트 세션을 다시 시작하세요. Cursor에서는 **Customize → Rules → Add Rule → Remote Rule (GitHub)**에 이 저장소 주소를 넣는 방법도 사용할 수 있습니다.

### 프로젝트에만 설치

[ZIP 파일](https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.zip)을 풀고 사용하는 에이전트의 pack 폴더를 프로젝트 안의 다음 위치로 복사합니다.

```text
Cursor       packs/cursor/pretend-designer  → .cursor/skills/pretend-designer
Claude Code  packs/claude/pretend-designer  → .claude/skills/pretend-designer
Codex        packs/codex/pretend-designer   → .agents/skills/pretend-designer
```

프로젝트 설치는 해당 폴더를 저장소에 커밋하면 팀원과 클라우드 에이전트도 같은 규칙을 사용한다는 장점이 있습니다.

### 업데이트

위 설치 명령을 다시 실행하면 같은 경로의 스킬과 레퍼런스가 최신 `main` 버전으로 갱신됩니다. 갱신 후에는 새 에이전트 세션에서 확인하세요.

## 이렇게 사용합니다

Codex:

```text
$pretend-designer
이 랜딩 페이지가 AI로 만든 것처럼 보인다. 현재 기능은 유지하고 디자인만 다시 잡아줘.
```

Cursor 또는 Claude Code:

```text
/pretend-designer
375px과 1280px에서 검토해. 가운데 섬 형태면 실패로 판단해.
```

원하는 방향을 고정하려면 실제 레퍼런스를 같이 지정합니다.

```text
/pretend-designer
이 페이지를 다시 디자인해.
레퍼런스: Visa Onchain Analytics의 차트 구조.
브랜드 색상과 문구는 우리 것을 유지해.
```

## 무엇이 달라지나

스킬이 활성화되면 에이전트는 픽셀을 만들기 전에 다음 다섯 가지를 먼저 정합니다.

1. 이 페이지를 누가, 어떤 일을 끝내기 위해 사용하는가
2. 페이지를 관통하는 하나의 시각적 테제는 무엇인가
3. 구조와 태도를 빌릴 실제 레퍼런스는 무엇인가
4. 끝까지 지킬 타입·재질·레이아웃 제약은 무엇인가
5. 이번 작업에서 제거할 AI 기본 패턴은 무엇인가

그다음 폰트, 색상, 페이지 폭, 라운드, 이미지, 차트, 모션을 같은 테제 아래에서 결정하고 375px과 1280px에서 다시 검사합니다.

## 한글 페이지는 더 엄격하게

[Apple Korea iPhone 페이지](https://www.apple.com/kr/iphone/)의 데스크톱·모바일 실측 리듬을 참고하되 Apple의 브랜드나 SF Pro KR을 복제하지 않습니다.

| 항목 | 기본 규칙 |
| --- | --- |
| 폰트 | Pretendard 또는 Noto Sans KR 중 하나만 사용 |
| Inter | 한글 글리프가 없으므로 영문 전용 페이지에서만 사용 |
| 본문 | 기본 `17px / 27px`, 짧은 카드 문구는 `17px / 23px` |
| 제목 웨이트 | 먼저 600을 사용하고, 이유 없이 700–900으로 올리지 않음 |
| 자간 | 기본 `0`; 음수 자간 금지; 역할에 따라 약한 양수만 허용 |
| 줄바꿈 | `word-break: keep-all`; 문단에 스크린샷용 `<br>` 금지 |
| 검수 | 실제 한글 문장으로 375px과 1280px 렌더링 확인 |

전체 수치, 색상 토큰, CSS 예제와 검수표는 [한글 타이포그래피 표준](references/korean-typography.md)에 있습니다.

## 실측 레퍼런스 라이브러리

사례는 외형을 복사하기 위한 템플릿이 아닙니다. 측정한 타입·색상·페이지 구조·차트 문법을 현재 제품의 목적에 맞게 번역하기 위한 근거입니다.

| 작업 | 참고 사례 |
| --- | --- |
| 한글 제품 페이지와 타이포 | [Apple Korea iPhone](references/cases/apple-korea-iphone.md) |
| 빌더 행사, 터미널형 에디토리얼 | [BUIDL CTC](references/cases/buidl-creditcoin.md) |
| 공개 분석 리포트, 단일 질문 차트 | [Visa Onchain Analytics](references/cases/visa-onchain-analytics.md) |
| 모니터링 대시보드, 다중 비교 차트 | [Blockworks Analytics](references/cases/blockworks-analytics.md) |
| 대형 타이포와 사진 중심 포트폴리오 | [Dots & Lines](references/cases/dots-and-lines.md) |
| 실제 제품 UI를 이용한 마케팅 | [Stripe](references/cases/stripe.md) |
| 금융 흐름과 다이어그램 스토리텔링 | [Spark Finance](references/cases/spark-finance.md) |

차트를 만들 때는 [Chart grammar](references/chart-grammar.md)에서 설명형 리포트와 모니터링 터미널 중 하나를 먼저 선택합니다.

## 저장소 구조

```text
pretend-designer/
├── SKILL.md                  # 기준 스킬
├── references/               # 실측 사례와 세부 규칙
│   ├── korean-typography.md
│   ├── chart-grammar.md
│   └── cases/
├── packs/
│   ├── cursor/pretend-designer/
│   ├── claude/pretend-designer/
│   └── codex/pretend-designer/
└── .cursor/skills/pretend-designer/
```

각 pack의 `SKILL.md`와 `references/`는 같은 내용입니다. 루트 파일은 검토용 기준본이고, 설치할 때는 사용하는 에이전트의 pack 폴더 전체를 받으면 됩니다.

## 범위

- 웹사이트, 랜딩 페이지, 대시보드, 포트폴리오, UI의 신규 디자인·리디자인·리뷰에 사용합니다.
- 백엔드 작업이나 문서 작성만 필요한 요청에는 사용하지 않습니다.
- 브랜드 가이드와 접근성 요구사항이 있다면 그것이 우선합니다.
- 레퍼런스의 로고, 카피, 이미지, 데이터, 고유 브랜드 표현은 복제하지 않습니다.

MIT License. 자세한 내용은 [LICENSE](LICENSE)를 확인하세요.

<details>
<summary>English</summary>

## What it is

`pretend-designer` is a design skill for Cursor, Claude Code, and Codex. It pushes coding agents away from the recurring AI-template look—unexamined fonts, purple gradients, three rounded cards, centered heroes—and toward a page with a job, a visual thesis, a real reference, and explicit constraints.

Download the [complete repository ZIP](https://github.com/promptprobe/pretend-designer/archive/refs/heads/main.zip), then copy the matching `pretend-designer` pack folder to your agent's skill directory:

| Agent | Source folder | Project install | Global install | Invoke |
| --- | --- | --- | --- | --- |
| Cursor | [`packs/cursor/pretend-designer`](packs/cursor/pretend-designer) | `.cursor/skills/pretend-designer/` | `~/.cursor/skills/pretend-designer/` | `/pretend-designer` |
| Claude Code | [`packs/claude/pretend-designer`](packs/claude/pretend-designer) | `.claude/skills/pretend-designer/` | `~/.claude/skills/pretend-designer/` | `/pretend-designer` |
| Codex | [`packs/codex/pretend-designer`](packs/codex/pretend-designer) | `.agents/skills/pretend-designer/` | `~/.agents/skills/pretend-designer/` | `$pretend-designer` |

Install the complete folder, not only `SKILL.md`; the skill routes to measured references in `references/`.

```text
$pretend-designer
Restyle this landing page without changing its behavior.
Use Visa Onchain Analytics for chart structure, but keep our brand and copy.
```

Korean pages use exactly one Hangul-capable family—Pretendard or Noto Sans KR—with the measured size, leading, tracking, and line-breaking rules in the [Korean typography standard](references/korean-typography.md). Inter is reserved for Latin-only pages because it does not contain Hangul glyphs.

The reference library includes Apple Korea iPhone, BUIDL CTC, Visa Onchain Analytics, Blockworks Analytics, Dots & Lines, Stripe, and Spark Finance. It transfers structural decisions, not brand identity.

MIT License.

</details>
