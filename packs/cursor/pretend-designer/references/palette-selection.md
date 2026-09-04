# Palette selection: varied, seeded, and independent

Read this file whenever the user has not supplied brand colors, an existing product palette, or exact color requirements.

The goal is variation without arbitrary meaning. A model should not repeatedly reach for a familiar design system, and a structural reference should not silently become the color source.

## Priority

1. User-supplied brand or product palette.
2. Existing colors already present in the product being revised.
3. Exact color requirements explicitly requested by the user.
4. Otherwise, the bundled palette lottery.

Do not use a named company, publication, website, or design system as a fallback at level 4. Do not take colors from a layout reference unless the user explicitly asks for close color matching.

## Run the lottery

From the installed `pretend-designer` directory:

```bash
python3 scripts/palette_lottery.py --mode light
```

Use `--mode dark` only when the brief or existing product calls for a dark surface. Light is the neutral default for an unspecified mode; hue, temperature, accents, and surface tint still vary with every fresh seed.

The output includes:

- a random seed and palette ID;
- surface, ink, muted ink, and line tokens;
- two independently separated accents;
- text-safe `accent-strong` variants;
- `accent-ink` for text placed on the accent fill;
- stable success and danger roles;
- computed contrast ratios.

Copy the seed and tokens into the implementation comment. The seed makes a successful result reproducible without turning it into the next project's default.

For a reproducible rerun:

```bash
python3 scripts/palette_lottery.py --mode light --seed 7d0f46c213bf71aa
```

Use `--format json` when structured output is easier to consume. Run `python3 scripts/palette_lottery.py --self-test` when changing the generator.

If `python3` is not usable in Codex desktop, call its workspace-dependency discovery first and run the script with the returned bundled Python executable. Do not treat a missing system runtime as permission to choose a palette from memory.

## Acceptance rules

- Run the lottery once per new visual direction. Do not ask the language model to name its favorite palette first.
- Do not reroll merely because the result is unfamiliar. That reintroduces model taste and convergence.
- Reroll only when the result conflicts with supplied brand colors, established domain semantics, a required theme, or accessibility. Record the reason.
- Preserve semantics. Success and danger are constrained to their roles; do not randomize them into unrelated meanings.
- Body ink, muted ink, text-safe accents, success, and danger must meet at least `4.5:1` against the primary surface. Primary ink should meet at least `7:1`.
- Use raw `accent` and `accent-2` for fills, rules, selection markers, and charts. Use the corresponding `-strong` token for text on the surface.
- Do not spread the accent across every state. Neutral hierarchy should still do most of the work.
- Do not claim that the generated palette came from a brand or published system. Its evidence is the seed, algorithm, token roles, and contrast report.

## Fallback without any Python 3 runtime

Use a fresh random value supplied by the execution environment, not a hue selected by language-model preference. Preserve that value as the seed, generate the same token roles, and verify the same contrast thresholds. If no environmental randomness or contrast calculation is available, use a neutral accessible surface temporarily and state that palette variation is unverified; do not fall back to a remembered corporate design system.
