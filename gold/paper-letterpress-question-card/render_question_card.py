from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse
import subprocess
from pathlib import Path

W, H = 1920, 1080
FPS = 30
N = 120

SURFACE = (242, 245, 245)
INK = (27, 33, 39)
BLUE = (49, 134, 255)
BLUE_INK = (46, 74, 104)

SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"

DEFAULT_NUMBER = "01"
DEFAULT_LINES = ["一个核心问题？", "我们如何回答它？"]
DEFAULT_SIZES = [136, 136]
DEFAULT_TOPS = [418, 590]
STILL_FRAMES = {
    13: "f013-entry-mid.webp",
    62: "f062-hold.webp",
    112: "f112-exit.webp",
}


def clamp(v, a=0, b=1):
    return max(a, min(b, v))


def ease(t):
    t = clamp(t)
    return 1 - (1 - t) ** 4


def smooth(t):
    t = clamp(t)
    return t * t * (3 - 2 * t)


def make_base():
    base = Image.new("RGBA", (W, H), SURFACE + (255,))
    light = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(light)
    ld.ellipse((390, 60, 1540, 1060), fill=(255, 255, 255, 95))
    light = light.filter(ImageFilter.GaussianBlur(210))
    return Image.alpha_composite(base, light)


def make_small_text_layer(text, font, pos, fill):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad = 20
    img = Image.new("RGBA", (tw + pad * 2, th + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((pad - bbox[0], pad - bbox[1]), text, font=font, fill=fill)
    return img, (pos[0] - pad + bbox[0], pos[1] - pad + bbox[1])


def precompute_title_frames(text, size, pos):
    font = ImageFont.truetype(SERIF, size)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad = 40
    raw = Image.new("RGBA", (tw + pad * 2, th + pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(raw)
    d.text((pad - bbox[0], pad - bbox[1]), text, font=font, fill=INK + (255,))
    states = []
    for k in range(11):
        t = ease(k / 10)
        sc = 1.28 - 0.28 * t
        blur = 7 * (1 - t)
        nw = max(1, int(raw.width * sc))
        nh = max(1, int(raw.height * sc))
        im = raw.resize((nw, nh), Image.Resampling.LANCZOS)
        if blur > 0.25:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        if t < 0.999:
            a = im.getchannel("A").point(lambda p, tt=t: int(p * tt))
            im.putalpha(a)
        x = pos[0] - pad + bbox[0]
        center_y = pos[1] + th / 2
        y = int(center_y - nh / 2)
        states.append((im, (int(x), y)))
    return states


def render_frame(frame, base, num_img, num_pos, label, label_pos, title_states, underline_y):
    im = base.copy()

    na = clamp((frame - 2) / 10)
    if na > 0:
        n = num_img.copy()
        if na < 1:
            n.putalpha(n.getchannel("A").point(lambda p, aa=na: int(p * aa)))
        im.alpha_composite(n, num_pos)

    la = ease((frame - 2) / 9)
    if la > 0:
        l = label.copy()
        if la < 1:
            l.putalpha(l.getchannel("A").point(lambda p, aa=la: int(p * aa)))
        im.alpha_composite(l, label_pos)

    for i, states in enumerate(title_states):
        delay = 6 + i * 5
        k = int(round(clamp((frame - delay) / 10) * 10))
        if frame >= delay:
            layer, pos = states[k]
            im.alpha_composite(layer, pos)

    u = smooth((frame - 20) / 18)
    if u > 0:
        d = ImageDraw.Draw(im)
        x1 = 170 + int(225 * u)
        d.rounded_rectangle(
            (170, underline_y, x1, underline_y + 6),
            radius=3,
            fill=BLUE + (235,),
        )

    out = smooth((frame - 106) / 14)
    if out > 0:
        overlay = Image.new("RGBA", (W, H), SURFACE + (int(255 * out),))
        im = Image.alpha_composite(im, overlay)

    return im


def main():
    global SERIF, SANS_BOLD
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", default=DEFAULT_NUMBER)
    parser.add_argument("--line-1", default=DEFAULT_LINES[0])
    parser.add_argument("--line-2", default=DEFAULT_LINES[1])
    parser.add_argument("--out", default="question-card-placeholder.mp4")
    parser.add_argument("--stills-dir", default=None)
    parser.add_argument("--serif-font", default=SERIF)
    parser.add_argument("--sans-font", default=SANS_BOLD)
    args = parser.parse_args()

    # Defaults are Linux container paths; override on other platforms.
    SERIF = args.serif_font
    SANS_BOLD = args.sans_font

    lines = [args.line_1, args.line_2]
    sizes = DEFAULT_SIZES
    tops = DEFAULT_TOPS
    underline_y = 772

    font_label = ImageFont.truetype(SANS_BOLD, 27)
    font_num = ImageFont.truetype(SERIF, 470)
    base = make_base()
    num_img, num_pos = make_small_text_layer(
        args.number,
        font_num,
        (1265, 246),
        BLUE + (24,),
    )
    label, label_pos = make_small_text_layer(
        f"QUESTION {args.number}",
        font_label,
        (170, 265),
        BLUE_INK + (255,),
    )
    title_states = [
        precompute_title_frames(text, size, (170, top))
        for text, size, top in zip(lines, sizes, tops)
    ]

    if args.stills_dir:
        stills_dir = Path(args.stills_dir)
        stills_dir.mkdir(parents=True, exist_ok=True)
        for frame, filename in STILL_FRAMES.items():
            image = render_frame(
                frame,
                base,
                num_img,
                num_pos,
                label,
                label_pos,
                title_states,
                underline_y,
            )
            image.convert("RGB").resize(
                (240, 135),
                Image.Resampling.LANCZOS,
            ).save(
                stills_dir / filename,
                "WEBP",
                quality=60,
                method=6,
            )

    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "rawvideo",
        "-vcodec",
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
        "-movflags",
        "+faststart",
        args.out,
    ]
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for frame in range(N):
        image = render_frame(
            frame,
            base,
            num_img,
            num_pos,
            label,
            label_pos,
            title_states,
            underline_y,
        )
        proc.stdin.write(image.convert("RGB").tobytes())

    proc.stdin.close()
    proc.wait()


if __name__ == "__main__":
    main()
