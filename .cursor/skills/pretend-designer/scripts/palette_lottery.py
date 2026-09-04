#!/usr/bin/env python3

import argparse
import colorsys
import hashlib
import json
import random
import secrets


AA = 4.5
AAA = 7.0


def seeded_random(seed):
    digest = hashlib.sha256(str(seed).encode("utf-8")).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


def hsl_to_hex(hue, saturation, lightness):
    red, green, blue = colorsys.hls_to_rgb(
        (hue % 360) / 360,
        max(0, min(100, lightness)) / 100,
        max(0, min(100, saturation)) / 100,
    )
    return "#{:02x}{:02x}{:02x}".format(
        round(red * 255), round(green * 255), round(blue * 255)
    )


def hex_to_rgb(value):
    clean = value.lstrip("#")
    return tuple(int(clean[offset : offset + 2], 16) for offset in (0, 2, 4))


def relative_luminance(value):
    channels = []
    for channel in hex_to_rgb(value):
        normalized = channel / 255
        channels.append(
            normalized / 12.92
            if normalized <= 0.04045
            else ((normalized + 0.055) / 1.055) ** 2.4
        )
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(first, second):
    brighter = max(relative_luminance(first), relative_luminance(second))
    darker = min(relative_luminance(first), relative_luminance(second))
    return (brighter + 0.05) / (darker + 0.05)


def contrasting_text(hue, saturation, initial_lightness, background, direction, target=AA):
    lightness = initial_lightness
    for _ in range(101):
        color = hsl_to_hex(hue, saturation, lightness)
        if contrast(color, background) >= target:
            return color
        lightness = max(0, min(100, lightness + direction))
    raise RuntimeError("Unable to create a contrasting text color")


def best_ink(background):
    black = "#000000"
    white = "#ffffff"
    return black if contrast(black, background) >= contrast(white, background) else white


def mix(first, second, first_weight):
    first_rgb = hex_to_rgb(first)
    second_rgb = hex_to_rgb(second)
    mixed = tuple(
        round(first_rgb[index] * first_weight + second_rgb[index] * (1 - first_weight))
        for index in range(3)
    )
    return "#{:02x}{:02x}{:02x}".format(*mixed)


def build_palette(seed, mode):
    rng = seeded_random(seed)
    surface_hue = rng.randint(0, 359)
    surface_saturation = rng.randint(3, 18)
    accent_hue = rng.randint(0, 359)
    accent_two_hue = (accent_hue + rng.randint(95, 205)) % 360
    accent_saturation = rng.randint(58, 88)
    accent_two_saturation = rng.randint(48, 82)
    is_light = mode == "light"

    background = hsl_to_hex(
        surface_hue,
        surface_saturation,
        rng.randint(96, 99) if is_light else rng.randint(5, 9),
    )
    surface = hsl_to_hex(
        surface_hue,
        max(2, surface_saturation - 2),
        100 if is_light else rng.randint(11, 15),
    )
    ink = contrasting_text(
        surface_hue,
        rng.randint(4, 14),
        12 if is_light else 92,
        background,
        -1 if is_light else 1,
        AAA,
    )
    ink_muted = contrasting_text(
        surface_hue,
        rng.randint(5, 18),
        44 if is_light else 66,
        background,
        -1 if is_light else 1,
    )
    line = hsl_to_hex(
        surface_hue,
        rng.randint(3, 16),
        rng.randint(78, 88) if is_light else rng.randint(25, 34),
    )

    accent = hsl_to_hex(
        accent_hue,
        accent_saturation,
        rng.randint(46, 62) if is_light else rng.randint(48, 65),
    )
    accent_two = hsl_to_hex(
        accent_two_hue,
        accent_two_saturation,
        rng.randint(44, 60) if is_light else rng.randint(50, 68),
    )
    accent_strong = contrasting_text(
        accent_hue,
        accent_saturation,
        42 if is_light else 64,
        background,
        -1 if is_light else 1,
    )
    accent_two_strong = contrasting_text(
        accent_two_hue,
        accent_two_saturation,
        42 if is_light else 64,
        background,
        -1 if is_light else 1,
    )
    success = contrasting_text(
        rng.randint(126, 154),
        rng.randint(45, 72),
        38 if is_light else 62,
        background,
        -1 if is_light else 1,
    )
    danger_hue = rng.randint(0, 12) if rng.random() < 0.5 else rng.randint(348, 359)
    danger = contrasting_text(
        danger_hue,
        rng.randint(62, 82),
        45 if is_light else 64,
        background,
        -1 if is_light else 1,
    )

    tokens = {
        "bg": background,
        "surface": surface,
        "ink": ink,
        "ink-muted": ink_muted,
        "line": line,
        "accent": accent,
        "accent-strong": accent_strong,
        "accent-ink": best_ink(accent),
        "accent-tint": mix(accent, background, 0.14 if is_light else 0.22),
        "accent-2": accent_two,
        "accent-2-strong": accent_two_strong,
        "success": success,
        "danger": danger,
    }
    ratios = {
        "ink/bg": contrast(tokens["ink"], tokens["bg"]),
        "ink-muted/bg": contrast(tokens["ink-muted"], tokens["bg"]),
        "accent-strong/bg": contrast(tokens["accent-strong"], tokens["bg"]),
        "accent-2-strong/bg": contrast(tokens["accent-2-strong"], tokens["bg"]),
        "accent-ink/accent": contrast(tokens["accent-ink"], tokens["accent"]),
        "success/bg": contrast(tokens["success"], tokens["bg"]),
        "danger/bg": contrast(tokens["danger"], tokens["bg"]),
    }
    palette_id = hashlib.sha256(str(seed).encode("utf-8")).hexdigest()[:8]
    return {
        "id": f"{mode}-{palette_id}",
        "mode": mode,
        "seed": str(seed),
        "tokens": tokens,
        "contrast": {name: round(value, 2) for name, value in ratios.items()},
    }


def css_output(palette):
    ratios = "; ".join(
        f"{name} {value}:1" for name, value in palette["contrast"].items()
    )
    lines = [
        f"/* Generated palette {palette['id']}. Seed: {palette['seed']}. Independent from visual references.",
        f"   Contrast: {ratios}. */",
        ":root {",
    ]
    lines.extend(f"  --{name}: {value};" for name, value in palette["tokens"].items())
    lines.append("}")
    return "\n".join(lines)


def self_test():
    accents = set()
    for index in range(1000):
        mode = "light" if index % 2 == 0 else "dark"
        palette = build_palette(f"self-test-{index}", mode)
        accents.add((palette["tokens"]["accent"], palette["tokens"]["accent-2"]))
        if palette["contrast"]["ink/bg"] < AAA:
            raise RuntimeError(f"ink contrast failed at {index}")
        for name, ratio in palette["contrast"].items():
            if name != "ink/bg" and ratio < AA:
                raise RuntimeError(f"{name} contrast failed at {index}")

    if build_palette("deterministic", "light") != build_palette("deterministic", "light"):
        raise RuntimeError("seeded output is not deterministic")
    if len(accents) < 950:
        raise RuntimeError(f"palette diversity too low: {len(accents)}/1000")
    print(
        f"Self-test passed: 1000 palettes, {len(accents)} unique accent pairs, deterministic seeds."
    )


def main():
    parser = argparse.ArgumentParser(description="Generate a seeded, contrast-checked UI palette.")
    parser.add_argument("--mode", choices=("light", "dark"), default="light")
    parser.add_argument("--seed")
    parser.add_argument("--format", choices=("css", "json"), default="css")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    seed = args.seed or secrets.token_hex(8)
    palette = build_palette(seed, args.mode)
    print(json.dumps(palette, indent=2) if args.format == "json" else css_output(palette))


if __name__ == "__main__":
    main()
