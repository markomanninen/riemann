import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt, numpy as np, json
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import glob as _g, os as _os
from paths import DATA, FONTS
for f in fm.findSystemFonts():
    if "Inter" in f: fm.fontManager.addfont(f)
for f in _g.glob(str(FONTS / "*.ttf")): fm.fontManager.addfont(f)
mpl.rcParams.update({"font.family": ["Inter", "DejaVu Sans"], "mathtext.fontset": "stix", "axes.unicode_minus": True})
# Output height in pixels: 1080 by default, RIEMANN_HEIGHT=720 for a faster draft render
HEIGHT = int(_os.environ.get("RIEMANN_HEIGHT", 1080))
W, H, DPI, FPS = 12.8, 7.2, round(HEIGHT / 7.2), 24
BG = "#101418"; INK = "#EDE8DA"; MUTED = "#8C9199"; FAINT = "#2A313A"; CARD = "#171C22"; AXIS = "#5A626D"
BLUE = "#58C4DD"; ORANGE = "#FFD866"; GREEN = "#7BD88F"; RED = "#FF7A6B"; PURPLE = "#B79CF2"; SOFT = "#1B2733"
HEAD = ["EB Garamond SemiBold", "Inter", "DejaVu Sans"]
mpl.rcParams.update({"text.color": INK, "legend.labelcolor": INK, "axes.labelcolor": MUTED, "savefig.facecolor": BG, "figure.facecolor": BG})
_rng = np.random.default_rng(7); GRAIN = _rng.normal(0.5, 0.5, (180, 320)).clip(0, 1)
D = json.load(open(DATA))
ZEROS = np.array(D["zeros"])
SECTIONS = {0: "", 1: "Part 1 · The prime number mystery", 2: "Part 2 · Gauss & the zeta function",
            3: "Part 3 · Riemann & the errors", 4: "Part 4 · The AI breakthrough", 5: "Part 5 · Summary",
            9: "Excursion · Analytic continuation"}
def spaced(s): return "\u200a".join(s.upper())

def ease(u):
    u = np.clip(u, 0, 1); return u * u * (3 - 2 * u)

def ramp(t, a, d=0.6):
    return float(ease((t - a) / d))

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]

def canvas(fig, section=0):
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 16, 9, color=BG, zorder=-10))
    ax.imshow(GRAIN, extent=(0, 16, 0, 9), cmap="gray", alpha=0.035, zorder=-9, aspect="auto", interpolation="bilinear")
    if SECTIONS.get(section):
        ax.text(0.8, 8.42, spaced(SECTIONS[section]), fontsize=10.5, color=MUTED, weight="semibold", va="center")
        cur = 2 if section == 9 else section
        for k in range(5):
            ax.add_patch(FancyBboxPatch((12.72 + k * 0.52, 8.39), 0.42, 0.05, boxstyle="round,pad=0,rounding_size=0.025",
                                        fc=(PURPLE if section == 9 else ORANGE) if k + 1 == cur else FAINT, ec="none"))
    return ax

def txt(ax, x, y, s, size=26, color=INK, weight="normal", ha="left", va="center", alpha=1, **kw):
    if weight == "bold" and size >= 24 and "family" not in kw:
        kw["family"] = HEAD; weight = "normal"; size = size * 1.12
    return ax.text(x, y, s, fontsize=size, color=color, weight=weight, ha=ha, va=va, alpha=alpha, **kw)

def plot_ax(fig, rect, xlabel="", ylabel=""):
    a = fig.add_axes(rect); a.set_facecolor(CARD)
    for sp in ("top", "right"): a.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): a.spines[sp].set_color(AXIS)
    a.tick_params(colors=MUTED, labelsize=12)
    a.grid(color=FAINT, lw=0.8)
    if xlabel: a.set_xlabel(xlabel, fontsize=14, color=MUTED)
    if ylabel: a.set_ylabel(ylabel, fontsize=14, color=MUTED)
    return a

def fade_overlay(ax):
    r = Rectangle((0, 0), 16, 9, color=BG, zorder=100, alpha=0); ax.add_patch(r); return r

def chip(ax, x, y, w, h, s, fc=CARD, ec=BLUE, size=18, color=INK, alpha=1, weight="semibold"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.18", fc=fc, ec=ec, lw=1.5, alpha=alpha)
    ax.add_patch(p)
    t = ax.text(x + w / 2, y + h / 2, s, ha="center", va="center", fontsize=size, color=color, weight=weight, alpha=alpha)
    return p, t
