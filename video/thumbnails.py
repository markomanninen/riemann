"""Render the YouTube thumbnails (1280x720 JPEG) into build/thumbnails/.

  python3 video/thumbnails.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from paths import ART, FONTS, build_dir

W, H = 1280, 720
INK = (237, 232, 218); MUTED = (170, 175, 183); GOLD = (255, 216, 102); BLUE = (88, 196, 221); BG = (16, 20, 24)
SERIF = lambda s: ImageFont.truetype(str(FONTS / "EBGaramond-SemiBold.ttf"), s)
SANS = lambda s, w="SemiBold": ImageFont.truetype(str(FONTS / f"Inter-{w}.ttf"), s)


def base(name, shade, dy=0):
    """Artwork scaled to 1280x720, moved down by dy pixels, with a dark gradient over the side that carries the text."""
    art = Image.open(ART / f"{name}.jpg").convert("RGB").resize((W, H), Image.LANCZOS)
    im = Image.new("RGB", (W, H), BG); im.paste(art, (0, dy))
    g = Image.new("L", (W, H))
    px = g.load()
    for y in range(H):
        for x in range(W):
            px[x, y] = shade(x / W, y / H)
    return Image.composite(Image.new("RGB", (W, H), BG), im, g)


def spaced(d, xy, s, font, fill, gap=3):
    x, y = xy
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + gap
    return x


def chip(d, x, y, s, font, fg, bg):
    w = d.textlength(s, font=font)
    d.rounded_rectangle((x, y, x + w + 36, y + 52), 26, fill=bg)
    d.text((x + 18, y + 26), s, font=font, fill=fg, anchor="lm")


def main():
    # Upper band darkened, the primes and the density curve stay visible below
    im = base("title", lambda u, v: int(255 * max(0.0, min(1.0, 1.4 - v * 2.2))), dy=130)
    d = ImageDraw.Draw(im)
    spaced(d, (72, 58), "THE RIEMANN HYPOTHESIS", SANS(30), GOLD, 4)
    d.text((66, 100), "Predicting Primes", font=SERIF(150), fill=INK)
    d.text((72, 290), "What AI proved in 2026", font=SANS(52, "Medium"), fill=BLUE)
    return im


def podcast():
    # Left side darkened, the narrowing strip of zeros stays on the right
    im = base("part4", lambda u, v: int(255 * max(0.0, min(1.0, 1.5 - u * 2.1))))
    d = ImageDraw.Draw(im)
    chip(d, 72, 92, "PODCAST EDITION", SANS(28), BG, GOLD)
    d.text((66, 180), "Predicting\nPrimes", font=SERIF(140), fill=INK, spacing=-10)
    d.text((72, 500), "The Riemann Hypothesis", font=SANS(44, "Medium"), fill=MUTED)
    d.text((72, 560), "and the AI result", font=SANS(44, "Medium"), fill=BLUE)
    return im


if __name__ == "__main__":
    out = build_dir("thumbnails")
    for name, fn in (("main", main), ("podcast", podcast)):
        p = out / f"thumb_{name}.jpg"
        fn().save(p, quality=90, optimize=True)
        print(p, round(p.stat().st_size / 1e3), "kB")
