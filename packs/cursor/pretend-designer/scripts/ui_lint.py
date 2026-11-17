#!/usr/bin/env python3
"""Flag generated-UI tells in markup and styles.

Covers the mechanical part of references/ui-copy.md and
references/icons-and-indicators.md: fake status indicators, tool attribution,
hand-authored or inconsistent inline SVG icons, emoji, filler copy, and a
paragraph placed directly under a heading. Dependency-free.

Exit status: 0 clean, 1 findings at error level (or any finding with --strict),
2 usage error.
"""

import argparse
import os
import re
import sys


EXTENSIONS = {
    ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte",
    ".astro", ".css", ".scss", ".mdx", ".php", ".erb", ".njk", ".liquid",
}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "vendor"}
MARKUP_FREE = {".css", ".scss"}

ERROR = "error"
WARN = "warn"

VENDOR = r"(?:Claude|ChatGPT|GPT(?:-\w+)?|Gemini|OpenAI|Anthropic|Copilot|LLM|AI)"

LINE_RULES = [
    (
        "tool-attribution", ERROR,
        re.compile(
            VENDOR + r"\s*(?:와|과|에|로|으로)?\s*(?:연동|연결|기반|탑재|구동)"
            r"|[Pp]owered\s+by\s+" + VENDOR
            + r"|(?:[Bb]uilt|[Mm]ade|[Gg]enerated)\s+(?:with|by)\s+" + VENDOR
        ),
        "tool or vendor attribution shown as content; delete unless the user supplied it",
    ),
    (
        "status-text", WARN,
        re.compile(
            r"연동\s*중|연결\s*중|연결됨|동기화\s*중|정상\s*운영|정상\s*작동"
            r"|All\s+systems\s+operational|\bOperational\b|\bOnline\b|\bConnected\b"
            r"|>\s*(?:LIVE|Live)\s*<"
        ),
        "status wording; keep only if bound to a state the code reads, with every state designed",
    ),
    (
        "status-pulse", ERROR,
        re.compile(r"\banimate-(?:ping|pulse)\b|@keyframes\s+(?:pulse|ping|blink|glow)\b"),
        "pulsing indicator; remove (progress during a real operation is the only exception)",
    ),
    (
        "status-dot", WARN,
        re.compile(
            r"(?=[^\n]*\brounded-full\b)(?=[^\n]*\b(?:w|h|size)-(?:1|1\.5|2|2\.5|3)\b)"
            r"(?=[^\n]*\bbg-(?:green|emerald|lime|teal|red|amber|yellow|orange|sky|blue)-\d)"
        ),
        "small colored dot; keep only as a real, text-labelled state indicator",
    ),
    (
        "emoji", ERROR,
        re.compile(
            "[\U0001F300-\U0001FAFF\U00002600-\U000026FF\U0001F1E6-\U0001F1FF\u2B50\u2705\u274C\u2728]"
        ),
        "emoji in the interface; remove or use the label alone",
    ),
    (
        "filler-ko", WARN,
        re.compile(
            r"한눈에|한\s?번에|한\s?곳에서?|손쉽게|간편하게|쉽고\s*빠르게|지금\s*바로"
            r"|혁신적인?|스마트한|완벽한|강력한|새로운\s*경험|차원이\s*다른|올인원"
            r"|모든\s*것을?|당신의|당신만의|여정|만나보세요|경험하세요|경험해\s*보세요"
            r"|[가-힣]+이?\s*아닙니다\.\s*[가-힣 ]+입니다"
        ),
        "filler phrasing; replace with a literal label or a stated fact, or delete",
    ),
    (
        "filler-en", WARN,
        re.compile(
            r"\b(?:unlock|seamless(?:ly)?|effortless(?:ly)?|supercharge|reimagine|elevate"
            r"|next-gen|all[- ]in[- ]one|at a glance|in one place|say goodbye to"
            r"|game[- ]chang\w+|cutting[- ]edge)\b",
            re.IGNORECASE,
        ),
        "filler phrasing; replace with a literal label or a stated fact, or delete",
    ),
    (
        "slogan-comma", WARN,
        re.compile(r"[가-힣]{1,8}(?:서|고|게|며|면|히),\s?[가-힣 ]{2,14}(?<![다요])(?=\s*(?:<|$|[\"'`.]))"),
        "comma-split slogan; name the thing instead",
    ),
]

HEADING_PARAGRAPH = re.compile(r"</h[1-3]>\s*<p[\s>]", re.IGNORECASE)
CSS_BLOCK = re.compile(r"\{([^{}]*)\}")
ROUND = re.compile(r"border-radius\s*:\s*(?:50%|9{3,}px|100%)")
SMALL = re.compile(r"(?:^|[;\s])(?:width|height|inline-size|block-size)\s*:\s*(\d+(?:\.\d+)?)px")
SVG_OPEN = re.compile(r"<svg\b[^>]*>", re.IGNORECASE)
PATH_DATA = re.compile(r"<path\b[^>]*\bd\s*=\s*[\"'{]", re.IGNORECASE)
STROKE_WIDTH = re.compile(r"stroke-?[wW]idth\s*=\s*[\"'{]\s*[\"']?([\d.]+)")
VIEWBOX = re.compile(r"viewBox\s*=\s*[\"']([^\"']+)[\"']")
ICON_SET = re.compile(r"icon-set\s*:\s*\S+", re.IGNORECASE)
IGNORE = "ui-lint-ignore"


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def lint_text(text, extension=".html"):
    findings = []
    lines = text.split("\n")
    ignored = {number for number, line in enumerate(lines, 1) if IGNORE in line}

    def add(line, rule, level, message):
        if line not in ignored:
            findings.append((line, rule, level, message))

    for number, line in enumerate(lines, 1):
        for rule, level, pattern, message in LINE_RULES:
            match = pattern.search(line)
            if match:
                add(number, rule, level, "{} ({!r})".format(message, match.group(0).strip()[:40]))

    for match in CSS_BLOCK.finditer(text):
        body = match.group(1)
        sizes = [float(value) for value in SMALL.findall(body)]
        if ROUND.search(body) and sizes and max(sizes) <= 12:
            add(
                line_of(text, match.start()), "status-dot", WARN,
                "round element of 12px or less; keep only as a real, text-labelled state indicator",
            )

    if extension in MARKUP_FREE:
        return sorted(findings)

    for match in HEADING_PARAGRAPH.finditer(text):
        add(
            line_of(text, match.start()), "heading-paragraph", WARN,
            "paragraph directly under a heading; keep only for scope, unit, state, or a required instruction",
        )

    if not ICON_SET.search(text):
        for match in PATH_DATA.finditer(text):
            add(
                line_of(text, match.start()), "inline-icon", ERROR,
                "inline SVG path with no recorded source; use one icon set verbatim and add "
                "an `icon-set: <name> <version>` comment, or use a text label",
            )

    if SVG_OPEN.search(text):
        widths = sorted(set(STROKE_WIDTH.findall(text)))
        if len(widths) > 1:
            add(
                line_of(text, SVG_OPEN.search(text).start()), "icon-consistency", WARN,
                "mixed icon stroke widths in one file: {}".format(", ".join(widths)),
            )
        boxes = sorted(set(" ".join(box.split()) for box in VIEWBOX.findall(text)))
        if len(boxes) > 1:
            add(
                line_of(text, SVG_OPEN.search(text).start()), "icon-consistency", WARN,
                "mixed SVG viewBox grids in one file: {}".format("; ".join(boxes)),
            )

    return sorted(findings)


def collect(paths):
    for path in paths:
        if os.path.isfile(path):
            yield path
            continue
        for root, directories, names in os.walk(path):
            directories[:] = [name for name in directories if name not in SKIP_DIRS]
            for name in sorted(names):
                if os.path.splitext(name)[1].lower() in EXTENSIONS:
                    yield os.path.join(root, name)


SELF_TEST_BAD = """<header>
  <span class="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
  <span>Claude 연동 중</span>
</header>
<h2>흩어진 자료를 한곳에</h2>
<p>여기에 모여서, 한번에 확인</p>
<svg viewBox="0 0 24 24" stroke-width="2"><path d="M3 12l4 4"/></svg>
<svg viewBox="0 0 20 20" stroke-width="1.5"><path d="M2 2h9"/></svg>
<button>시작하기 🚀</button>
<style>.dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e; }</style>
"""

SELF_TEST_GOOD = """<!-- icon-set: lucide 0.4 -->
<header><a href="/">팀 문서 보관함</a></header>
<h2>지원 형식</h2>
<ul><li>PDF</li><li>HWP</li><li>DOCX</li></ul>
<p class="sync">마지막 동기화 14:02</p>
<svg viewBox="0 0 24 24" stroke-width="1.5"><path d="M21 21l-4.3-4.3"/></svg>
<button>문서 올리기</button>
<style>.avatar { width: 32px; height: 32px; border-radius: 50%; }</style>
"""


def self_test():
    bad = {rule for _, rule, _, _ in lint_text(SELF_TEST_BAD)}
    expected = {
        "tool-attribution", "status-text", "status-pulse", "status-dot", "emoji",
        "filler-ko", "slogan-comma", "heading-paragraph", "inline-icon", "icon-consistency",
    }
    missing = expected - bad
    good = lint_text(SELF_TEST_GOOD)
    if missing or good:
        print("self-test failed")
        if missing:
            print("  not detected:", ", ".join(sorted(missing)))
        for finding in good:
            print("  false positive:", finding)
        return 1
    print("self-test passed: {} rules detected, clean sample has no findings".format(len(expected)))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="*", help="files or directories to check")
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings as well as errors")
    parser.add_argument("--self-test", action="store_true", help="run the built-in samples")
    arguments = parser.parse_args()

    if arguments.self_test:
        return self_test()
    if not arguments.paths:
        parser.print_usage()
        return 2

    errors = warnings = files = 0
    for path in collect(arguments.paths):
        files += 1
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            print("{}: skipped ({})".format(path, problem))
            continue
        for line, rule, level, message in lint_text(text, os.path.splitext(path)[1].lower()):
            print("{}:{}: {} [{}] {}".format(path, line, level, rule, message))
            if level == ERROR:
                errors += 1
            else:
                warnings += 1

    print("{} file(s), {} error(s), {} warning(s)".format(files, errors, warnings))
    return 1 if errors or (arguments.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
