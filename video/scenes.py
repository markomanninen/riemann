from lib import *
import mpmath as mp

# ---------- generic scenes ----------
import matplotlib.image as mpimg
from paths import ART
def _art(ax, name, SH=2.4):
    im = mpimg.imread(ART / f"{name}.jpg")
    a = ax.imshow(im, extent=(SH, 16 + SH, 0, 9), zorder=-5, aspect="auto", interpolation="bilinear")
    g = np.zeros((2, 256, 4)); c = mpl.colors.to_rgb(BG); g[..., :3] = c
    g[..., 3] = np.clip(1.5 - np.linspace(0, 1, 256) * 2.1, 0, 1)[None, :]
    ax.imshow(g, extent=(0, 16, 0, 9), zorder=-4, aspect="auto", interpolation="bilinear")
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)
    return a
def _parts(ax, cur):
    names = ["1 Primes", "2 Gauss & zeta", "3 Riemann & errors", "4 The AI result", "5 Summary"]
    for k in range(5):
        ax.add_patch(FancyBboxPatch((0.8 + k * 2.0, 1.22), 1.8, 0.05, boxstyle="round,pad=0,rounding_size=0.025", fc=ORANGE if k + 1 == cur else "#4a515b", ec="none"))
        ax.text(0.8 + k * 2.0, 0.95, names[k], fontsize=9.5, color=INK if k + 1 == cur else MUTED, va="center")
def S_title(fig, T, title, sub, section=0):
    ax = canvas(fig, 0); a = _art(ax, "title", 0); SH = 0
    k = txt(ax, 0.8, 7.75, spaced("An explainer in five parts"), 12, ORANGE, "semibold")
    t1 = ax.text(0.8, 6.65, title, fontsize=84, color=INK, family=HEAD, va="center")
    t2 = txt(ax, 0.8, 5.5, sub, 19, MUTED)
    def up(t):
        z = 0.25 * t / max(T, 1); a.set_extent((SH - z, SH + 16 + z, -z * 9 / 16, 9 + z * 9 / 16)); ax.set_xlim(0, 16); ax.set_ylim(0, 9)
        k.set_alpha(ramp(t, 0.3)); t1.set_alpha(ramp(t, 0.5, 0.9)); t2.set_alpha(ramp(t, 1.3, 0.9))
    return up

def S_section(fig, T, num, title, sub):
    ax = canvas(fig, 0); a = _art(ax, f"part{num}"); SH = 2.4
    k = txt(ax, 0.8, 6.45, spaced(f"Part {num} of 5"), 13, ORANGE, "semibold")
    words = title.split(); half = (len(words) + 1) // 2
    two = " ".join(words[:half]) + "\n" + " ".join(words[half:]) if len(title) > 14 else title
    t1 = ax.text(0.8, 4.85, two, fontsize=64, color=INK, family=HEAD, va="center", linespacing=1.0)
    t2 = txt(ax, 0.8, 3.05, sub, 22, MUTED); _parts(ax, num)
    def up(t):
        z = 0.3 * t / max(T, 1); a.set_extent((SH - z, SH + 16 + z, -z * 9 / 16, 9 + z * 9 / 16)); ax.set_xlim(0, 16); ax.set_ylim(0, 9)
        k.set_alpha(ramp(t, 0.15)); t1.set_alpha(ramp(t, 0.3, 0.8)); t2.set_alpha(ramp(t, 0.8, 0.8))
    return up

def S_text(fig, T, lines, section, starts=None, sizes=None, colors=None, y0=5.6, dy=1.25, x=1.2, ha="left"):
    """lines appear one by one at given start times (local seconds)."""
    ax = canvas(fig, section); starts = starts or [0.3 + i * 1.2 for i in range(len(lines))]
    sizes = sizes or [34] + [24] * (len(lines) - 1); colors = colors or [INK] + [MUTED] * (len(lines) - 1)
    arts = [txt(ax, x, y0 - i * dy, s, sizes[i], colors[i], "bold" if i == 0 else "normal", ha=ha) for i, s in enumerate(lines)]
    def up(t):
        for a, s0 in zip(arts, starts): a.set_alpha(ramp(t, s0, 0.5))
    return up

def S_cue(fig, T, name, role, section):
    ax = canvas(fig, section)
    txt(ax, 1.2, 5.2, "From the interview", 18, MUTED)
    a = txt(ax, 1.2, 4.3, name, 40, weight="bold"); b = txt(ax, 1.2, 3.4, role, 20, MUTED)
    bar = Rectangle((1.2, 2.7), 0, 0.08, color=ORANGE); ax.add_patch(bar)
    def up(t):
        a.set_alpha(ramp(t, 0.1)); b.set_alpha(ramp(t, 0.4)); bar.set_width(6 * ramp(t, 0.2, T))
    return up

# ---------- section 1 ----------
def S_primes(fig, T, section=1):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "A prime is a whole number > 1 that is not a product of two smaller ones", 22, weight="semibold")
    xs = 1.0 + (np.arange(1, 31) - 1) * 0.48
    P = set(primes_upto(30))
    circ = []; lab = []
    for i, n in enumerate(range(1, 31)):
        c = Circle((xs[i], 5.6), 0.2, fc=BG, ec=FAINT, lw=1.5); ax.add_patch(c); circ.append(c)
        lab.append(txt(ax, xs[i], 5.6, str(n), 12, MUTED, ha="center"))
    # factor tree for 12
    tree = [txt(ax, 8, 3.6, "12", 34, weight="bold", ha="center"),
            txt(ax, 6.6, 2.3, "2", 30, BLUE, "bold", ha="center"), txt(ax, 9.4, 2.3, "6", 30, weight="bold", ha="center"),
            txt(ax, 8.6, 1.0, "2", 30, BLUE, "bold", ha="center"), txt(ax, 10.2, 1.0, "3", 30, BLUE, "bold", ha="center")]
    lines = [ax.plot([7.8, 6.8], [3.2, 2.7], color=MUTED)[0], ax.plot([8.2, 9.2], [3.2, 2.7], color=MUTED)[0],
             ax.plot([9.2, 8.7], [1.9, 1.4], color=MUTED)[0], ax.plot([9.6, 10.1], [1.9, 1.4], color=MUTED)[0]]
    note = txt(ax, 11.2, 2.3, "12 = 2 × 2 × 3\nin exactly one way", 22, INK)
    ov = fade_overlay(ax)
    def up(t):
        ov.set_alpha(1 - ramp(t, 0, 0.3))
        for i, n in enumerate(range(1, 31)):
            on = (n in P) and t > 1 + n * 0.12
            circ[i].set_facecolor(BLUE if on else BG); circ[i].set_edgecolor(BLUE if on else FAINT)
            lab[i].set_color(BG if on else MUTED)
        a = ramp(t, T * 0.45)
        for o in tree + lines + [note]: o.set_alpha(a)
    return up

def S_gaps(fig, T, section=1):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "One by one, primes look random", 30, weight="bold")
    P = primes_upto(120)
    X = lambda n: 1.0 + n / 120 * 14
    ax.plot([1, 15], [4.5, 4.5], color=FAINT, lw=2)
    for v in (0, 20, 40, 60, 80, 100, 120): txt(ax, X(v), 3.9, str(v), 12, MUTED, ha="center")
    sc = ax.scatter([], [], s=70, color=BLUE, zorder=3)
    a1 = txt(ax, X(12), 5.6, "11 and 13:\nneighbours", 16, GREEN, ha="center")
    br1 = ax.plot([X(11), X(11), X(13), X(13)], [4.8, 5.0, 5.0, 4.8], color=GREEN, lw=2)[0]
    a2 = txt(ax, X(93), 5.6, "89 → 97:\na gap of 8", 16, ORANGE, ha="center")
    br2 = ax.plot([X(89), X(89), X(97), X(97)], [4.8, 5.0, 5.0, 4.8], color=ORANGE, lw=2)[0]
    q = txt(ax, 8, 2.0, "No practical formula gives the next prime.", 24, INK, ha="center")
    def up(t):
        k = int(np.clip(t / (T * 0.4), 0, 1) * len(P)); sc.set_offsets(np.c_[[X(p) for p in P[:k]], [4.5] * k] if k else np.empty((0, 2)))
        for o in (a1, br1): o.set_alpha(ramp(t, T * 0.42))
        for o in (a2, br2): o.set_alpha(ramp(t, T * 0.55))
        q.set_alpha(ramp(t, T * 0.7))
    return up

def S_switch(fig, T, section=1):
    ax = canvas(fig, section)
    a = txt(ax, 8, 5.6, "Where is the next prime?", 36, MUTED, ha="center")
    strike = ax.plot([3.2, 12.8], [5.6, 5.6], color=RED, lw=4)[0]
    b = txt(ax, 8, 3.8, "How many primes are there, on average, near x?", 36, BLUE, "bold", ha="center")
    def up(t):
        strike.set_data([3.2, 3.2 + 9.6 * ramp(t, T * 0.35, 0.6)], [5.6, 5.6]); b.set_alpha(ramp(t, T * 0.5))
    return up

def S_lnx(fig, T, section=1):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "The natural logarithm ln x grows very slowly", 28, weight="bold")
    p = plot_ax(fig, [0.08, 0.12, 0.55, 0.62], "x", "ln x")
    x = np.logspace(0, 12, 400); p.set_xscale("log"); p.set_xlim(1, 1e12); p.set_ylim(0, 30)
    ln, = p.plot([], [], color=BLUE, lw=3)
    rows = [("x = 1 000", "ln x ≈ 6.9"), ("x = 1 000 000", "ln x ≈ 13.8"), ("x = 10¹²", "ln x ≈ 27.6")]
    arts = []
    for i, (a, b) in enumerate(rows):
        arts += [txt(ax, 10.6, 5.4 - i * 1.2, a, 19, MUTED), txt(ax, 13.5, 5.4 - i * 1.2, b, 19, INK, "semibold")]
    def up(t):
        k = int(ramp(t, 0, T * 0.6) * len(x)); ln.set_data(x[:k], np.log(x[:k]))
        for i, o in enumerate(arts): o.set_alpha(ramp(t, 0.6 + (i // 2) * 0.9))
    return up

def S_quote(fig, T, line1, line2, section):
    return S_text(fig, T, [line1, line2], section, starts=[0.2, 1.5], sizes=[36, 24], colors=[INK, BLUE], y0=5.0, dy=1.4)

def S_strip_teaser(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Not yet — but AI narrowed down where the zeros can be", 26, weight="bold")
    X = lambda s: 3 + s * 10
    ax.plot([X(0), X(0)], [1.5, 6.3], color=FAINT, lw=2); ax.plot([X(1), X(1)], [1.5, 6.3], color=FAINT, lw=2)
    ax.plot([X(.5), X(.5)], [1.5, 6.3], color=BLUE, lw=2, ls="--")
    band = Rectangle((X(0), 1.5), 10, 4.8, color=ORANGE, alpha=.18); ax.add_patch(band)
    for z in ZEROS[ZEROS < 48]: ax.scatter([X(.5)], [1.5 + z / 48 * 4.8], s=40, color=BLUE, zorder=4)
    for v, l in ((0, "0"), (.5, "½"), (1, "1")): txt(ax, X(v), 1.0, l, 18, MUTED, ha="center")
    lab = txt(ax, 13.6, 4.0, "", 20, ORANGE, "semibold")
    def up(t):
        u = ramp(t, 1.0, T * 0.5); a = u / 8; band.set_x(X(a)); band.set_width(10 * (1 - 2 * a))
        lab.set_text("1/8 ≤ σ ≤ 7/8" if u > 0.95 else "0 ≤ σ ≤ 1"); lab.set_position((X(1 - a) + 0.3, 4.0))
    return up

# ---------- section 2: Gauss ----------
def S_gauss_blocks(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Gauss, c. 1795: counting primes in blocks of 1000", 28, weight="bold")
    N = 3_000_000; P = primes_upto(N); blocks = np.bincount(P // 1000, minlength=N // 1000)[:N // 1000]; mid = np.arange(N // 1000) * 1000 + 500
    p = plot_ax(fig, [0.08, 0.12, 0.86, 0.62], "x (log scale)", "primes per block")
    p.set_xscale("log"); p.set_xlim(400, 3.5e6); p.set_ylim(0, 180)
    sc, = p.plot([], [], "o", ms=2.5, color="#8fa3b8", alpha=.8)
    cur, = p.plot([], [], color=BLUE, lw=3)
    lab = p.text(1.2e5, 150, "1000 / ln x", fontsize=20, color=BLUE, weight="bold")
    n1 = p.text(600, 172, "1–1000: 168 primes", fontsize=14, color=INK)
    n2 = p.text(4e5, 25, "near 3 million: about 65–70", fontsize=14, color=INK)
    def up(t):
        xm = 1000 * 3000 ** ramp(t, 0, T * 0.6); k = int(np.searchsorted(mid, xm)); sc.set_data(mid[:k], blocks[:k])
        u = ramp(t, T * 0.62, T * 0.2)
        if u > 0:
            xx = np.logspace(np.log10(500), np.log10(500 + u * 3e6), 300); cur.set_data(xx, 1000 / np.log(xx))
        lab.set_alpha(u); n1.set_alpha(ramp(t, 0.5)); n2.set_alpha(ramp(t, T * 0.55))
    return up

def S_density(fig, T, section=2):
    return S_text(fig, T, ["Near x, about one number in every ln x is prime",
                           "near 1 000: about 1 in 7",
                           "near 1 000 000: about 1 in 14",
                           "near 10¹²: about 1 in 28",
                           "density of primes ≈ 1 / ln x"], section,
                  starts=[0.2, 2.0, 3.3, 4.6, 6.5], sizes=[32, 24, 24, 24, 30], colors=[INK, MUTED, MUTED, MUTED, BLUE])

def S_stair(fig, T, section=2, error=False):
    ax = canvas(fig, section)
    head = txt(ax, 1.0, 7.3, "π(x): true count — a jagged staircase.   Li(x): Gauss's smooth guess", 22, weight="semibold")
    p = plot_ax(fig, [0.08, 0.12, 0.86, 0.64], "x", "number of primes up to x")
    N = 200; P = primes_upto(N); x = np.linspace(2, N, 1200); pi = np.searchsorted(P, x, side="right")
    Li = np.array([float(mp.li(v) - mp.li(2)) for v in x])
    p.set_xlim(0, N); p.set_ylim(0, 50)
    st, = p.step([], [], where="post", color=INK, lw=2.2, label="π(x)")
    li, = p.plot([], [], color=BLUE, lw=3, label="Li(x)")
    p.legend(loc="upper left", fontsize=14, frameon=False)
    q = txt(ax, 8, 6.4, "How big can the error  π(x) − Li(x)  get?", 30, RED, "bold", ha="center")
    fill = [None]
    def up(t):
        k = int(ramp(t, 0, T * 0.45 if not error else 0.1) * len(x)); st.set_data(x[:k], pi[:k])
        j = int(ramp(t, T * (0.35 if not error else 0), T * 0.3 if not error else 0.1) * len(x)); li.set_data(x[:j], Li[:j])
        if error:
            head.set_text("How big can the error  π(x) − Li(x)  get?"); head.set_color(RED); head.set_fontsize(26); head.set_weight("bold"); q.set_alpha(0)
            if fill[0] is None and t > 1.0: fill[0] = p.fill_between(x, pi, Li, color=RED, alpha=.18, step=None)
        else: q.set_alpha(0)
    return up

def S_bridge(fig, T, section=2):
    return S_text(fig, T, ["The answer hides in one strange function", "ζ(s) — the Riemann zeta function", "a bridge from all whole numbers to the primes"],
                  section, starts=[0.2, 1.8, 3.4], sizes=[32, 40, 24], colors=[INK, BLUE, MUTED], y0=5.4, dy=1.4)

def S_zsum(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "ζ(s) = 1 + 1/2ˢ + 1/3ˢ + 1/4ˢ + …   a sum over all whole numbers", 24, weight="semibold")
    p = plot_ax(fig, [0.08, 0.12, 0.86, 0.62], "number of terms", "partial sum")
    n = np.arange(1, 61); s2 = np.cumsum(1 / n ** 2); s1 = np.cumsum(1 / n)
    p.set_xlim(0, 60); p.set_ylim(0, 5)
    a, = p.plot([], [], "o-", color=BLUE, ms=4, lw=2, label="s = 2:  1 + 1/4 + 1/9 + …  → π²/6 ≈ 1.645")
    b, = p.plot([], [], "o-", color=ORANGE, ms=4, lw=2, label="s = 1:  1 + 1/2 + 1/3 + …  grows forever")
    p.axhline(np.pi ** 2 / 6, color=BLUE, ls="--", lw=1)
    p.legend(loc="upper left", fontsize=15, frameon=False)
    def up(t):
        k = int(ramp(t, 0.3, T * 0.4) * 60); a.set_data(n[:k], s2[:k])
        j = int(ramp(t, T * 0.5, T * 0.4) * 60); b.set_data(n[:j], s1[:j])
    return up

def S_euler(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Euler: the same sum is a product — one bracket for each prime", 24, weight="semibold")
    br = [("2", ["1", "1/2ˢ", "1/4ˢ", "1/8ˢ"]), ("3", ["1", "1/3ˢ", "1/9ˢ", "1/27ˢ"]), ("5", ["1", "1/5ˢ", "1/25ˢ", "…"]), ("7", ["1", "1/7ˢ", "1/49ˢ", "…"])]
    cells = {}
    for i, (p_, terms) in enumerate(br):
        x0 = 1.0 + i * 3.4
        txt(ax, x0 + 1.3, 6.4, f"prime {p_}", 16, MUTED, ha="center")
        ax.add_patch(FancyBboxPatch((x0, 3.3), 2.6, 2.7, boxstyle="round,pad=0.02,rounding_size=0.2", fc=CARD, ec=FAINT))
        for j, tm in enumerate(terms):
            cells[(i, j)] = txt(ax, x0 + 1.3, 5.6 - j * 0.65, tm, 20, INK, ha="center")
        if i < 3: txt(ax, x0 + 3.0, 4.65, "×", 30, MUTED, ha="center")
    txt(ax, 14.7, 4.65, "× …", 30, MUTED, ha="center")
    pick = {(0, 2): BLUE, (1, 1): BLUE, (2, 0): BLUE, (3, 0): BLUE}
    res = txt(ax, 8, 2.3, "1/4ˢ × 1/3ˢ × 1 × 1 × …  =  1/12ˢ", 30, BLUE, "bold", ha="center")
    con = txt(ax, 8, 1.1, "every whole number appears exactly once  ⇒  sum over all numbers = product over all primes", 19, INK, ha="center")
    def up(t):
        on = t > T * 0.35
        for k, a in cells.items():
            a.set_color(pick.get(k, INK) if on else INK); a.set_weight("bold" if (on and k in pick) else "normal")
            a.set_alpha(0.35 if (on and k not in pick) else 1)
        res.set_alpha(ramp(t, T * 0.42)); con.set_alpha(ramp(t, T * 0.7))
    return up

def S_log(fig, T, section=2):
    return S_text(fig, T, ["Take the logarithm:","the product becomes a sum over primes",
                           "log ζ(s)  ≈  1/2ˢ + 1/3ˢ + 1/5ˢ + 1/7ˢ + 1/11ˢ + …"], section,
                  starts=[0.2, 0.8, 2.0], sizes=[30, 26, 30], colors=[INK, MUTED, BLUE], y0=5.6, dy=1.3)

def S_pole(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "The pole at s = 1: ζ(s) blows up like 1/(s − 1)", 26, weight="bold")
    p = plot_ax(fig, [0.08, 0.12, 0.5, 0.62], "s (real)", "")
    s = np.linspace(1.03, 4, 300); z = np.array([float(mp.zeta(v)) for v in s])
    p.set_xlim(0.8, 4); p.set_ylim(0, 25); p.axvline(1, color=RED, lw=1.5, ls=":")
    l1, = p.plot([], [], color=BLUE, lw=3, label="ζ(s)"); l2, = p.plot([], [], color=MUTED, lw=1.5, ls="--", label="1/(s − 1)")
    p.legend(fontsize=14, frameon=False)
    notes = [txt(ax, 9.9, 5.6, "Sum over primes  Σ 1/pˢ", 20, INK, "semibold"),
             txt(ax, 9.9, 4.9, "blows up like  log 1/(s − 1)", 20, INK),
             txt(ax, 9.9, 3.7, "That speed is exactly what", 20, MUTED),
             txt(ax, 9.9, 3.1, "density 1/ln x would give:", 20, MUTED),
             txt(ax, 9.9, 2.1, "Gauss's average lives in the pole", 19, BLUE, "bold"),
             txt(ax, 9.9, 1.2, "Bonus (Euler): it blows up ⇒ infinitely many primes", 14, MUTED)]
    def up(t):
        k = int(ramp(t, 0.2, T * 0.35) * len(s)); l1.set_data(s[::-1][:k], z[::-1][:k]); l2.set_data(s[::-1][:k], 1 / (s[::-1][:k] - 1))
        for i, o in enumerate(notes): o.set_alpha(ramp(t, T * (0.3 + i * 0.1)))
    return up

def S_spikes(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "−ζ′/ζ: a list of primes, each weighted by ln p  →  ψ(x)", 24, weight="semibold")
    p = plot_ax(fig, [0.08, 0.12, 0.86, 0.62], "x", "ψ(x)")
    N = 40; P = primes_upto(N); pts = []
    for q in P:
        k = q
        while k <= N: pts.append((k, np.log(q))); k *= q
    pts.sort(); xs = [a for a, _ in pts]; hs = [b for _, b in pts]
    p.set_xlim(0, N); p.set_ylim(0, 40)
    sp = p.vlines([], 0, [], color=ORANGE, lw=3)
    stp, = p.step([], [], where="post", color=INK, lw=2.2)
    p.plot([0, N], [0, N], color=BLUE, ls="--", lw=1.5); p.text(30, 33, "$x$", color=BLUE, fontsize=20)
    def up(t):
        k = int(ramp(t, 0.2, T * 0.5) * len(xs))
        sp.set_segments([[(xs[i], 0), (xs[i], hs[i])] for i in range(k)])
        u = ramp(t, T * 0.45, T * 0.4); m = int(u * len(xs))
        cx = [0] + xs[:m]; cy = [0] + list(np.cumsum(hs[:m])); stp.set_data(cx + ([N] if m == len(xs) else []), cy + ([cy[-1]] if m == len(xs) else []))
    return up

def S_explicit(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.4, "Explicit formula:   $\\psi(x) = x - \\sum_{\\rho} x^{\\rho}/\\rho - \\ln 2\\pi - \\frac{1}{2}\\ln(1 - x^{-2})$", 22, weight="semibold")
    tag1 = txt(ax, 10.4, 6.95, "pole at s = 1  →  x  (the average)", 17, BLUE, "semibold")
    tag2 = txt(ax, 10.4, 6.45, "each zero ρ  →  one wave", 17, ORANGE, "semibold")
    p = plot_ax(fig, [0.08, 0.12, 0.86, 0.55], "x", "")
    x = np.linspace(1.5, 40, 1600); P = primes_upto(50)
    true = np.zeros_like(x)
    for q in P:
        k = q
        while k <= 40: true += np.log(q) * (x >= k); k *= q
    base = x - np.log(2 * np.pi) - 0.5 * np.log(1 - x ** -2)
    rho = 0.5 + 1j * ZEROS
    cum = np.vstack([np.zeros_like(x), np.cumsum(np.array([2 * np.real(x ** r / r) for r in rho]), axis=0)])
    p.set_xlim(1.5, 40); p.set_ylim(-1, 44)
    p.step(x, true, where="post", color=INK, lw=1.8, label="ψ(x): true weighted prime count")
    p.plot(x, base, color=BLUE, ls="--", lw=1.8, label="smooth average x")
    ln, = p.plot([], [], color=ORANGE, lw=2.4, label="average − waves from N zeros")
    p.legend(loc="upper left", fontsize=13, frameon=False)
    nlab = p.text(30, 4, "", fontsize=18, color=BG, weight="bold", bbox=dict(boxstyle="round,pad=0.45,rounding_size=0.9", fc=ORANGE, ec="none"))
    def up(t):
        u = np.clip((t - 1) / (T - 3), 0, 1); N = int(round(150 ** u)) if t > 1 else 0
        ln.set_data(x, base - cum[N]); nlab.set_text(f"N = {N}")
        tag1.set_alpha(ramp(t, 0.2)); tag2.set_alpha(ramp(t, 1.2))
    return up

def S_map(fig, T, section=2):
    ax = canvas(fig, section)
    head = txt(ax, 1.0, 7.3, "Riemann's map: s = σ + i·t", 28, weight="bold")
    X = lambda s: 6.5 + s * 2.2; Y = lambda t: 3.9 + t * 0.075
    ax.plot([X(-2.4), X(3.6)], [Y(0), Y(0)], color=AXIS, lw=1); ax.plot([X(0), X(0)], [Y(-28), Y(36)], color=AXIS, lw=1)
    txt(ax, X(3.6), Y(0) - 0.35, "σ (east–west)", 14, MUTED, ha="right"); txt(ax, X(0) + 0.15, Y(36), "t (north–south)", 14, MUTED, va="top")
    right = Rectangle((X(1), Y(-28)), X(3.6) - X(1), Y(36) - Y(-28), color=GREEN, alpha=0); ax.add_patch(right)
    rl = txt(ax, X(2.3), Y(24), "the sum works here\n(σ > 1)\n— no zeros here", 15, GREEN, ha="center")
    left = Rectangle((X(-2.4), Y(-28)), X(1) - X(-2.4), Y(36) - Y(-28), color=BLUE, alpha=0); ax.add_patch(left)
    ll = txt(ax, X(-1.2), Y(24), "analytic\ncontinuation\nextends ζ here", 15, BLUE, ha="center")
    arr = ax.annotate("", xy=(X(-0.5), Y(-15)), xytext=(X(1.6), Y(-15)), arrowprops=dict(arrowstyle="->", color=BLUE, lw=3))
    for v, l in ((0, "0"), (1, "1")): txt(ax, X(v), Y(0) - 0.35, l, 14, MUTED, ha="center")
    def up(t):
        u1 = ramp(t, T * 0.25); right.set_alpha(0.15 * u1); rl.set_alpha(u1)
        u2 = ramp(t, T * 0.62); left.set_alpha(0.10 * u2); ll.set_alpha(u2); arr.set_alpha(u2)
    return up

def S_mirror(fig, T, section=2):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "A mirror symmetry s ↔ 1 − s  →  all interesting zeros in the critical strip", 22, weight="semibold")
    X = lambda s: 5.0 + s * 6.0; Y = lambda t: 4.0 + t * 0.085
    strip = Rectangle((X(0), Y(-32)), X(1) - X(0), Y(36) - Y(-32), color=SOFT, alpha=0); ax.add_patch(strip)
    for v in (0, 1): ax.plot([X(v), X(v)], [Y(-32), Y(36)], color=FAINT, lw=1.5)
    mid, = ax.plot([X(.5), X(.5)], [Y(-32), Y(36)], color=BLUE, lw=2.5, alpha=0)
    for v, l in ((0, "0"), (.5, "½"), (1, "1")): txt(ax, X(v), 0.6, l, 16, MUTED, ha="center")
    z = ZEROS[ZEROS < 34]; sc = ax.scatter(np.full(2 * len(z), X(.5)), np.r_[Y(z), Y(-z)], s=45, color=BLUE, zorder=4, alpha=0)
    tl = [txt(ax, 2.6, Y(0), "trivial zeros\n−2, −4, −6 …", 14, MUTED, ha="center")]
    lab = txt(ax, X(1) + 0.4, Y(20), "critical strip\n0 < σ < 1", 16, BLUE)
    def up(t):
        u = ramp(t, 0.6); strip.set_alpha(u); mid.set_alpha(ramp(t, 1.5)); sc.set_alpha(ramp(t, 2.2)); lab.set_alpha(u); tl[0].set_alpha(ramp(t, 3))
    return up

# ---------- section 3 ----------
def S_chain(fig, T, section=3):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "The chain of logic", 30, weight="bold")
    items = [("primes", INK), ("unique\nfactorisation", INK), ("Euler product\n= ζ(s)", INK), ("pole at s = 1\n→ average density", BLUE), ("zeros of ζ\n→ waves = error", ORANGE)]
    arts = []
    for i, (s, c) in enumerate(items):
        x = 0.8 + i * 3.05
        p_, t_ = chip(ax, x, 3.5, 2.6, 1.8, s, fc=CARD, ec=c, size=16, color=c); arts.append((p_, t_))
        if i < 4: arts.append((ax.annotate("", xy=(x + 3.0, 4.4), xytext=(x + 2.65, 4.4), arrowprops=dict(arrowstyle="->", color=MUTED, lw=2)),))
    def up(t):
        for k, grp in enumerate(arts):
            a = ramp(t, 0.3 + k * T * 0.09)
            for o in grp: o.set_alpha(a)
    return up

def S_waves3(fig, T, section=3):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "A zero at $\\sigma + i\\,t$ makes a wave of height about $x^{\\sigma}$", 26, weight="bold")
    x = np.linspace(1, 400, 1500)
    cfg = [(1.0, RED, "σ = 1: as big as x itself — Gauss fails"), (7 / 8, ORANGE, "$\\sigma = 7/8$:  $x^{7/8}$"), (0.5, BLUE, "σ = ½: only √x")]
    axs = []
    for i, (sg, c, lab) in enumerate(cfg):
        a = plot_ax(fig, [0.07 + i * 0.31, 0.16, 0.27, 0.55], "x", ""); a.set_ylim(-420, 420); a.set_xlim(1, 400)
        l, = a.plot([], [], color=c, lw=1.6); env = a.fill_between(x, -x ** sg, x ** sg, color=c, alpha=.08)
        a.set_title(lab, fontsize=13, color=c, loc="left"); axs.append((a, l, sg))
    rule = txt(ax, 8, 0.55, "To know how big the error can be, you must know how far east the zeros can be.", 18, INK, "semibold", ha="center")
    def up(t):
        for i, (a, l, sg) in enumerate(axs):
            k = int(ramp(t, 0.3 + i * 1.2, T * 0.35) * len(x)); xx = x[:k]
            l.set_data(xx, xx ** sg * np.cos(14.13 * np.log(xx)))
        rule.set_alpha(ramp(t, T * 0.7))
    return up

def S_four(fig, T, section=3):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Off the centre line, zeros would come in groups of four", 26, weight="bold")
    X = lambda s: 4.5 + s * 7; Y = lambda t: 3.9 + t * 0.11
    ax.add_patch(Rectangle((X(0), Y(-26)), 7, Y(26) - Y(-26), color=SOFT))
    ax.plot([X(.5), X(.5)], [Y(-26), Y(26)], color=BLUE, lw=2.5)
    pts = [(0.72, 20), (0.28, 20), (0.72, -20), (0.28, -20)]
    sc = [ax.scatter([X(a)], [Y(b)], s=200, facecolors="none", edgecolors=RED, linewidths=2.5, zorder=4, alpha=0) for a, b in pts]
    on = ax.scatter([X(.5), X(.5)], [Y(14.13), Y(-14.13)], s=90, color=BLUE, zorder=4, alpha=0)
    l1 = txt(ax, X(1) + 0.3, Y(20), "imagined zero\noff the line", 15, RED)
    l2 = txt(ax, X(1) + 0.3, Y(10), "a zero on σ = ½ is\nits own mirror image", 15, BLUE)
    for v, l in ((0, "0"), (.5, "½"), (1, "1")): txt(ax, X(v), 0.5, l, 16, MUTED, ha="center")
    def up(t):
        for i, s in enumerate(sc): s.set_alpha(ramp(t, 0.4 + i * 0.6))
        l1.set_alpha(ramp(t, 0.4)); on.set_alpha(ramp(t, T * 0.6)); l2.set_alpha(ramp(t, T * 0.6))
    return up

def S_RH(fig, T, section=3):
    ax = canvas(fig, section)
    t1 = txt(ax, 1.0, 7.0, "The Riemann Hypothesis", 40, BLUE, "bold")
    t2 = txt(ax, 1.0, 6.0, "Every non-trivial zero lies exactly on the line σ = ½", 26, INK)
    X = lambda s: 12.4 + s * 3; Y = lambda t: 0.6 + t * 0.11
    ax.add_patch(Rectangle((X(0), Y(0)), 3, Y(48) - Y(0), color=SOFT)); ax.plot([X(.5), X(.5)], [Y(0), Y(48)], color=BLUE, lw=2)
    z = ZEROS[ZEROS < 48]; sc = ax.scatter([], [], s=50, color=BLUE, zorder=4)
    labs = [txt(ax, X(.5) - 0.3, Y(v), f"{v:.2f}", 13, INK, ha="right") for v in z[:4]]
    notes = [txt(ax, 1.0, 4.4, "First zeros: t ≈ 14.13, 21.02, 25.01, 30.42 …", 20, MUTED),
             txt(ax, 1.0, 3.5, "Over 12 trillion zeros checked by computer — all on the line", 20, MUTED),
             txt(ax, 1.0, 2.6, "But infinitely many need a proof.  Clay Millennium Prize: $1 000 000", 20, INK, "semibold")]
    def up(t):
        k = int(ramp(t, 0.5, T * 0.4) * len(z)); sc.set_offsets(np.c_[np.full(k, X(.5)), Y(z[:k])] if k else np.empty((0, 2)))
        for i, l in enumerate(labs): l.set_alpha(1 if k > i else 0)
        notes[0].set_alpha(ramp(t, 1.5)); notes[1].set_alpha(ramp(t, T * 0.5)); notes[2].set_alpha(ramp(t, T * 0.7))
        t2.set_alpha(ramp(t, 0.4))
    return up

def S_trillion(fig, T, section=3):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "How many primes up to a trillion (10¹²)?", 28, weight="bold")
    p, l = "37607912018", "37607950281"; k = 6
    def row(y, label, s):
        txt(ax, 1.0, y, label, 18, MUTED)
        return [txt(ax, 6.2 + i * 0.72, y, ch, 40, BLUE if i < k else ORANGE, "bold", ha="center", family="DejaVu Sans Mono") for i, ch in enumerate(s)]
    r1 = row(5.6, "true count π(10¹²)", p); r2 = row(4.4, "Gauss's Li(10¹²)", l)
    notes = [txt(ax, 1.0, 3.0, "Difference: 38 263", 22, INK, "semibold"),
             txt(ax, 1.0, 2.2, "If RH is true: error < √x · ln x / 8π ≈ 1.1 million (Schoenfeld 1976)", 20, MUTED),
             txt(ax, 1.0, 1.4, "√x has about half as many digits as x  →  roughly half the digits are reliable", 20, BLUE, "semibold"),
             txt(ax, 1.0, 0.6, "(Kontorovich's on-the-fly guess was ~100 billion; the true count is ~37.6 billion)", 14, MUTED)]
    def up(t):
        for i, a in enumerate(r1 + r2): a.set_alpha(ramp(t, 0.3 + (i % 11) * 0.12))
        for i, n in enumerate(notes): n.set_alpha(ramp(t, T * (0.3 + i * 0.15)))
    return up

# ---------- section 4 ----------
def S_timeline(fig, T, section=4):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "What was proved after Riemann", 28, weight="bold")
    ev = [(1859, "Riemann: zeros somewhere in 0 ≤ σ ≤ 1"), (1896, "Hadamard & de la Vallée Poussin: none on σ = 1 → prime number theorem"),
          (1914, "Hardy: infinitely many zeros on σ = ½"), (1942, "Selberg: a positive proportion on the line"),
          (1958, "Vinogradov & Korobov: wider zero-free region near σ = 1"), (1974, "Levinson: at least one third"),
          (1989, "Conrey: at least two fifths")]
    arts = []
    for i, (y, s) in enumerate(ev):
        yy = 6.3 - i * 0.78
        arts.append((txt(ax, 1.2, yy, str(y), 20, BLUE, "bold"), txt(ax, 2.7, yy, s, 18, INK)))
    wall = txt(ax, 1.2, 0.75, "But nobody could prove all zeros stay a fixed distance from σ = 1 — the wall stood until 2026", 18, RED, "semibold")
    def up(t):
        for i, g in enumerate(arts):
            for o in g: o.set_alpha(ramp(t, 0.3 + i * T * 0.08))
        wall.set_alpha(ramp(t, T * 0.75))
    return up

def S_strip(fig, T, section=4):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Autumn 2026: an OpenAI model proves a quasi-Riemann hypothesis", 24, weight="bold")
    X = lambda s: 1.5 + s * 8
    for v in (0, 1): ax.plot([X(v), X(v)], [1.4, 6.4], color=FAINT, lw=2)
    ax.plot([X(.5), X(.5)], [1.4, 6.4], color=BLUE, lw=2, ls="--")
    for v, l in ((0, "0"), (1 / 12, "1/12"), (1 / 8, "1/8"), (.5, "½"), (7 / 8, "7/8"), (11 / 12, "11/12"), (1, "1")):
        txt(ax, X(v), 1.0 if v not in (1 / 12, 11 / 12) else 0.55, l, 13, MUTED, ha="center")
    b1 = Rectangle((X(1 / 8), 4.2), X(7 / 8) - X(1 / 8), 1.6, color=PURPLE, alpha=0); ax.add_patch(b1)
    b2 = Rectangle((X(1 / 12), 2.0), X(11 / 12) - X(1 / 12), 1.6, color=ORANGE, alpha=0); ax.add_patch(b2)
    l1 = txt(ax, X(.5), 5.0, "Version 1 · 30 Sep 2026\n199 pages · Lean-verified\n1/8 ≤ σ ≤ 7/8", 12, BG, "bold", ha="center")
    l2 = txt(ax, X(.5), 2.8, "Version 2 · ~a week later · 49 pages\nnot yet in Lean · wider band = weaker\n1/12 ≤ σ ≤ 11/12", 12, BG, "bold", ha="center")
    side = [txt(ax, 10.4, 5.4, "Error in predicting primes", 18, INK, "semibold"),
            txt(ax, 10.4, 4.7, "$\\leq$ about $x^{7/8}$", 26, PURPLE, "bold"),
            txt(ax, 10.4, 3.7, "First time ever: a fixed power", 17, INK),
            txt(ax, 10.4, 3.2, "saved below x", 17, INK),
            txt(ax, 10.4, 2.2, "Radziwiłł: most consequences of RH", 15, MUTED),
            txt(ax, 10.4, 1.75, "already follow from quasi-RH", 15, MUTED)]
    def up(t):
        u1 = ramp(t, 1.0); b1.set_alpha(0.85 * u1); l1.set_alpha(u1)
        u2 = ramp(t, T * 0.33); b2.set_alpha(0.85 * u2); l2.set_alpha(u2)
        for i, s in enumerate(side): s.set_alpha(ramp(t, T * (0.62 + i * 0.05)))
    return up

def S_lean(fig, T, section=4):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Why a machine-checked proof matters", 28, weight="bold")
    chip(ax, 1.0, 3.6, 6.6, 2.6, "Language model\npredicts the next word\n— one wrong step breaks a proof", fc=CARD, ec=ORANGE, size=17, color=INK)
    chip(ax, 8.4, 3.6, 6.6, 2.6, "Lean proof checker\nchecks every tiny logical step\nmechanically", fc=CARD, ec=GREEN, size=17, color=INK)
    steps = [ax.scatter([], [], s=120, marker="s", color=GREEN)]
    n = txt(ax, 8, 2.2, "A human still checks that the statement Lean verified is the one we care about", 18, BLUE, "semibold", ha="center")
    def up(t):
        k = int(ramp(t, 1.0, T * 0.6) * 14); steps[0].set_offsets(np.c_[8.9 + np.arange(k) * 0.42, np.full(k, 3.2)] if k else np.empty((0, 2)))
        n.set_alpha(ramp(t, T - 2.5))
    return up

# ---------- section 5 ----------
def S_score(fig, T, section=5):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "The scoreboard", 30, weight="bold")
    rows = [("1859", "zeros somewhere in 0 ≤ σ ≤ 1", "no error bound yet", MUTED),
            ("1896", "no zeros on σ = 1", "prime number theorem", GREEN),
            ("2026", "zeros in 1/8 ≤ σ ≤ 7/8 (Lean)", "error $\\leq$ about $x^{7/8}$", PURPLE),
            ("RH", "all zeros on σ = ½  (OPEN)", "error ≈ √x: about half the digits", BLUE)]
    hdr = [txt(ax, 1.0, 6.3, "when", 15, MUTED), txt(ax, 2.8, 6.3, "where the zeros are", 15, MUTED), txt(ax, 8.6, 6.3, "what it means for primes", 15, MUTED)]
    arts = []
    for i, (a, b, c, col) in enumerate(rows):
        y = 5.4 - i * 1.15
        arts.append([txt(ax, 1.0, y, a, 22, col, "bold"), txt(ax, 2.8, y, b, 19, INK), txt(ax, 8.6, y, c, 19, col, "semibold")])
    def up(t):
        for i, g in enumerate(arts):
            for o in g: o.set_alpha(ramp(t, 0.5 + i * T * 0.18))
    return up

def S_end(fig, T, credits):
    ax = canvas(fig, 0)
    q = txt(ax, 8, 6.2, "Will the last step — from 7/8 to ½ — come from AI,\nfrom human insight, or from both?", 30, INK, "bold", ha="center")
    c = txt(ax, 8, 2.6, credits, 13, MUTED, ha="center")
    def up(t):
        q.set_alpha(ramp(t, 0.3)); c.set_alpha(ramp(t, T * 0.45))
    return up
