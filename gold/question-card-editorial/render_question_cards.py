from PIL import Image, ImageDraw, ImageFont
import argparse
import subprocess
from pathlib import Path

W, H = 1920, 1080
FPS = 30
DURATION = 4
FRAMES = FPS * DURATION

QUESTIONS = [
    "第一条示例问题是什么？",
    "第二条示例问题是什么？",
    "第三条示例问题是什么？",
    "第四条示例问题是什么？",
]

DEFAULT_LABEL = "INTERVIEW"

# Pure typography / editorial treatment. No illustrations and no logo.
BG = (255, 255, 255)
INK = (17, 24, 39)
MUTED = (111, 129, 153)
HAIR = (218, 228, 240)
NAVY = (47, 62, 102)
ACCENT = (49, 134, 255)
PALE = (232, 242, 255)

DEFAULT_SERIF_FONT = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
DEFAULT_SANS_FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
DEFAULT_MONO_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def ease_out_cubic(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def ease_in_cubic(t):
    t = max(0.0, min(1.0, t))
    return t ** 3


def segment(frame, a, b):
    if b == a:
        return 1.0
    return max(0.0, min(1.0, (frame - a) / (b - a)))


def alpha_color(rgb, a):
    return (*rgb, int(max(0, min(1, a)) * 255))


def draw_text_alpha(base, xy, text, font, fill, opacity=1.0, anchor=None):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text(xy, text, font=font, fill=alpha_color(fill, opacity), anchor=anchor)
    return Image.alpha_composite(base.convert("RGBA"), layer)


def load_fonts(serif_path, sans_path, mono_path):
    return {
        "question": ImageFont.truetype(serif_path, 86),
        "number_big": ImageFont.truetype(mono_path, 240),
        "number_small": ImageFont.truetype(mono_path, 26),
        "label": ImageFont.truetype(mono_path, 25),
        "sub": ImageFont.truetype(sans_path, 27),
    }


def render_frame(question, index, frame, label, fonts):
    img = Image.new("RGBA", (W, H), (*BG, 255))
    draw = ImageDraw.Draw(img)

    # Intro / outro opacity envelope
    intro = ease_out_cubic(segment(frame, 3, 20))
    outro = 1 - ease_in_cubic(segment(frame, 101, 119))
    global_a = min(intro, outro)

    # Top metadata line
    line_p = ease_out_cubic(segment(frame, 5, 24))
    line_x2 = int(145 + (1630 - 145) * line_p)
    draw.line((145, 145, line_x2, 145), fill=alpha_color(HAIR, global_a), width=2)

    # Accent tick
    tick_p = ease_out_cubic(segment(frame, 8, 20))
    draw.line(
        (145, 145, 145 + int(150 * tick_p), 145),
        fill=alpha_color(ACCENT, global_a),
        width=5,
    )

    # Small labels
    img = draw_text_alpha(img, (145, 96), label, fonts["label"], NAVY, global_a)
    img = draw_text_alpha(
        img,
        (1630, 96),
        f"{index:02d} / 04",
        fonts["number_small"],
        ACCENT,
        global_a,
        anchor="ra",
    )

    # Big editorial number: text only, deliberately pale
    num_p = ease_out_cubic(segment(frame, 0, 25))
    num_y = int(330 + (300 - 330) * num_p)
    img = draw_text_alpha(
        img,
        (1535, num_y),
        f"{index:02d}",
        fonts["number_big"],
        PALE,
        0.88 * global_a,
        anchor="ra",
    )

    # Kicker / section label
    kicker_p = ease_out_cubic(segment(frame, 12, 28))
    kicker_x = int(145 + (185 - 145) * kicker_p)
    img = draw_text_alpha(
        img,
        (kicker_x, 360),
        f"QUESTION {index:02d}",
        fonts["label"],
        ACCENT,
        kicker_p * global_a,
    )

    # Question text entrance: slight horizontal travel + fade
    q_p = ease_out_cubic(segment(frame, 16, 34))
    q_x = int(145 + (190 - 145) * q_p)
    q_y = 450

    # Fit longest question without wrapping too aggressively.
    max_width = 1370
    bbox = fonts["question"].getbbox(question)
    text_width = bbox[2] - bbox[0]
    if text_width <= max_width:
        lines = [question]
    else:
        # Natural split near punctuation / middle for long Chinese lines.
        if "，" in question:
            parts = question.split("，", 1)
            lines = [parts[0] + "，", parts[1]]
        else:
            mid = len(question) // 2
            lines = [question[:mid], question[mid:]]

    for li, line in enumerate(lines):
        line_delay = li * 3
        lp = ease_out_cubic(segment(frame, 16 + line_delay, 34 + line_delay))
        line_y = q_y + li * 132 + int((1 - lp) * 24)
        img = draw_text_alpha(
            img,
            (q_x, line_y),
            line,
            fonts["question"],
            INK,
            lp * global_a,
        )

    # Bottom descriptor + rule, keeping it deliberately quiet
    bottom_p = ease_out_cubic(segment(frame, 25, 42))
    bottom_y = int(870 + (850 - 870) * bottom_p)
    draw = ImageDraw.Draw(img)
    draw.line(
        (190, 820, 560, 820),
        fill=alpha_color(HAIR, bottom_p * global_a),
        width=2,
    )
    img = draw_text_alpha(
        img,
        (190, bottom_y),
        "人物 · 收入 · 经验 · 平台",
        fonts["sub"],
        MUTED,
        bottom_p * global_a,
    )

    # Final exit: content lifts a touch while fading
    if frame >= 101:
        lift = int(18 * ease_in_cubic(segment(frame, 101, 119)))
        shifted = Image.new("RGBA", (W, H), (*BG, 255))
        shifted.alpha_composite(img, (0, -lift))
        img = shifted

    return img


def render_question(question, index, outfile, label, fonts):
    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        str(outfile),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for frame in range(FRAMES):
        img = render_frame(question, index, frame, label, fonts)
        proc.stdin.write(img.convert("RGB").tobytes())

    proc.stdin.close()
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"ffmpeg failed for {outfile.name}")


def render_stills(stills_dir, label, fonts):
    stills_dir.mkdir(parents=True, exist_ok=True)
    for frame, name in [
        (18, "still_018_intro.png"),
        (60, "still_060_hold.png"),
        (110, "still_110_outro.png"),
    ]:
        img = render_frame(QUESTIONS[0], 1, frame, label, fonts)
        preview = img.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
        preview.quantize(colors=32, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(
            stills_dir / name, optimize=True
        )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default=DEFAULT_LABEL)
    parser.add_argument("--output-dir", default="renders")
    parser.add_argument("--stills-dir", default="stills")
    parser.add_argument("--stills-only", action="store_true")
    parser.add_argument("--serif-font", default=DEFAULT_SERIF_FONT)
    parser.add_argument("--sans-font", default=DEFAULT_SANS_FONT)
    parser.add_argument("--mono-font", default=DEFAULT_MONO_FONT)
    return parser.parse_args()


def main():
    args = parse_args()
    fonts = load_fonts(args.serif_font, args.sans_font, args.mono_font)

    render_stills(Path(args.stills_dir), args.label, fonts)

    if args.stills_only:
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for i, question in enumerate(QUESTIONS, 1):
        path = output_dir / f"Question_{i:02d}.mp4"
        render_question(question, i, path, args.label, fonts)
        print(f"Rendered: {path}")


if __name__ == "__main__":
    main()
