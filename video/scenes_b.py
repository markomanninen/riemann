from scenes_ex import *

def card(ax, x, y, w, h):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.18", fc=CARD, ec=FAINT, lw=1.2, zorder=0); ax.add_patch(p); return p
def chart(fig, ax, x, y, w, h, xlabel="", ylabel="", pad=(0.75, 0.9, 0.3, 0.3)):
    card(ax, x, y, w, h); l, b, r, t = pad
    a = fig.add_axes([(x + l) / 16, (y + b) / 9, (w - l - r) / 16, (h - b - t) / 9]); a.patch.set_alpha(0)
    for sp in ("top", "right"): a.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): a.spines[sp].set_color(AXIS)
    a.tick_params(colors=MUTED, labelsize=11); a.grid(color=FAINT, lw=0.8)
    if xlabel: a.set_xlabel(xlabel, fontsize=12, color=MUTED, labelpad=6)
    if ylabel: a.set_ylabel(ylabel, fontsize=12, color=MUTED)
    return a
def panel(ax, x, y, color, title, body, tsize=17, bsize=13.5):
    n = body.count("\n") + 1; h = 0.5 + 0.36 * n
    bar = FancyBboxPatch((x, y - h + 0.12), 0.07, h, boxstyle="round,pad=0,rounding_size=0.035", fc=color, ec="none"); ax.add_patch(bar)
    a = ax.text(x + 0.28, y, title, fontsize=tsize, color=INK, weight="semibold", va="center")
    b = ax.text(x + 0.28, y - 0.42, body, fontsize=bsize, color=MUTED, va="top", linespacing=1.45)
    return [bar, a, b]
def show(arts, a):
    for o in arts: o.set_alpha(a)
def row(fig, ax, x, y, pieces, size):
    out = []; r = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    for s, c in pieces:
        t = ax.text(x, y, s, fontsize=size, color=c, va="center"); out.append(t)
        bb = t.get_window_extent(r); x = inv.transform((bb.x1, 0))[0] + 0.12
    return out
def kicker(ax, x, y, s, c=MUTED): return ax.text(x, y, spaced(s), fontsize=10, color=c, weight="semibold", va="center")
def head(ax, title, sub=None):
    t = txt(ax, 0.8, 7.55, title, 30, weight="bold"); s = txt(ax, 0.8, 6.85, sub, 15.5, MUTED) if sub else None; return t, s

def S_zsum(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "The zeta function: a sum over all whole numbers", "Add up one fraction for every whole number n. The exponent s is the dial we get to turn.")
    p = chart(fig, ax, 0.8, 0.7, 8.6, 5.6, "number of terms added", "running total")
    n = np.arange(1, 61); s2 = np.cumsum(1 / n ** 2); s1 = np.cumsum(1 / n); p.set_xlim(0, 60); p.set_ylim(0, 5)
    p.axhline(np.pi ** 2 / 6, color=BLUE, ls=(0, (4, 4)), lw=1)
    a, = p.plot([], [], "-", color=BLUE, lw=2.6); b, = p.plot([], [], "-", color=ORANGE, lw=2.6)
    la = p.text(61, s2[-1], "", color=BLUE, fontsize=12, va="center"); lb = p.text(40, 4.55, "keeps growing", color=ORANGE, fontsize=12)
    kicker(ax, 10.0, 6.0, "Definition")
    f = ax.text(10.0, 5.35, r"$\zeta(s)=1+\dfrac{1}{2^{s}}+\dfrac{1}{3^{s}}+\dfrac{1}{4^{s}}+\cdots$", fontsize=25, color=INK, va="center")
    P1 = panel(ax, 10.0, 4.0, BLUE, "s = 2: the total settles", "1 + 1/4 + 1/9 + 1/16 + …\napproaches π²/6 ≈ 1.645 (Euler)")
    P2 = panel(ax, 10.0, 2.2, ORANGE, "s = 1: the total never settles", "1 + 1/2 + 1/3 + 1/4 + …\npasses every number, slowly")
    def up(t):
        k = int(ramp(t, 0.6, T * 0.35) * 60); a.set_data(n[:k], s2[:k]); j = int(ramp(t, T * 0.45, T * 0.4) * 60); b.set_data(n[:j], s1[:j])
        f.set_alpha(ramp(t, 0.2)); show(P1, ramp(t, 1.0)); show(P2, ramp(t, T * 0.45)); lb.set_alpha(ramp(t, T * 0.8))
    return up

def S_euler(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "Euler's product: the primes are hiding inside ζ")
    f1 = row(fig, ax, 0.8, 6.55, [(r"$\zeta(s)\;=\;\sum_{n}\dfrac{1}{n^{s}}$", INK), (r"$=\;\prod_{p\ \mathrm{prime}}\left(1+\dfrac{1}{p^{s}}+\dfrac{1}{p^{2s}}+\cdots\right)$", ORANGE)], 22)
    PR = [2, 3, 5, 7]; rows = 5; cells = {}; cards = []
    for i, p_ in enumerate(PR):
        x0 = 0.8 + i * 2.55; c = card(ax, x0, 2.75, 2.2, 3.0); cards.append(c)
        cards.append(ax.text(x0 + 1.1, 5.5, f"bracket for {p_}", fontsize=11, color=MUTED, ha="center", va="center"))
        for e in range(rows):
            lab = "1" if e == 0 else (rf"$1/{p_ ** e}^{{s}}$" if p_ ** e <= 30 else "…")
            cells[(p_, e)] = ax.text(x0 + 1.1, 5.05 - e * 0.5, lab, fontsize=15, color=INK, ha="center", va="center")
        if i < 3: cards.append(ax.text(x0 + 2.375, 4.25, "×", fontsize=22, color=MUTED, ha="center", va="center"))
    cards.append(ax.text(11.1, 4.25, "×  …", fontsize=22, color=MUTED, ha="center", va="center"))
    k1 = kicker(ax, 11.9, 5.5, "One term per bracket")
    rd1 = ax.text(11.9, 4.75, "", fontsize=30, color=ORANGE, va="center", family=HEAD)
    rd2 = ax.text(11.9, 3.95, "", fontsize=17, color=INK, va="center")
    rd3 = ax.text(11.9, 3.3, "", fontsize=12, color=MUTED, va="center")
    nums = []; 
    for n in range(1, 31):
        x = 0.8 + (n - 1) * 0.485; c = Circle((x + 0.2, 1.75), 0.2, fc=CARD, ec=FAINT, lw=1.2); ax.add_patch(c)
        nums.append((c, ax.text(x + 0.2, 1.75, str(n), fontsize=10.5, color=MUTED, ha="center", va="center")))
    kn = kicker(ax, 0.8, 2.3, "Every whole number is produced exactly once")
    fin = ax.text(0.8, 0.85, "A sum over all whole numbers  =  a product over all primes.   ζ knows the primes because it is built from them.", fontsize=15.5, color=INK, weight="semibold", va="center")
    def fac(n):
        e = {}
        for p_ in PR:
            while n % p_ == 0: e[p_] = e.get(p_, 0) + 1; n //= p_
        return e, n
    smooth = [n for n in range(1, 31) if fac(n)[1] == 1]
    sup = {1: "", 2: "²", 3: "³", 4: "⁴"}
    t0, t1 = 12.0, 18.5
    def up(t):
        f1[0].set_alpha(ramp(t, 1.0)); f1[1].set_alpha(ramp(t, 6)); show(cards, ramp(t, 9.5)); k1.set_alpha(ramp(t, t0 - 0.5)); 
        for o in cells.values(): o.set_alpha(ramp(t, 9.5))
        u = np.clip((t - t0) / (t1 - t0), 0, 1); k = int(u * len(smooth)); done = set(smooth[:k]); cur = smooth[min(k, len(smooth)) - 1] if k else None
        rest = t > t1 + 0.4
        for n, (c, lab) in enumerate(nums, 1):
            on = n in done or rest; iscur = (n == cur and not rest)
            c.set_facecolor(ORANGE if iscur else (SOFT if on else CARD)); c.set_edgecolor(ORANGE if on else FAINT); lab.set_color(BG if iscur else (INK if on else MUTED))
        e = fac(cur)[0] if cur and not rest else {}
        for (p_, ex), o in cells.items():
            pick = bool(cur) and not rest and e.get(p_, 0) == ex
            o.set_color(ORANGE if pick else INK); o.set_weight("bold" if pick else "normal")
            if t > 9.5: o.set_alpha(1 if (pick or not cur or rest) else 0.3)
        if cur and not rest:
            rd1.set_text(f"n = {cur}"); rd2.set_text(" × ".join(f"{p_}{sup[x]}" for p_, x in e.items()) if e else "1 (pick “1” everywhere)")
            rd3.set_text("no other choice gives this number")
        elif rest: rd1.set_text("11, 13, 17 …"); rd2.set_text("have their own brackets"); rd3.set_text("so every number is covered")
        kn.set_alpha(ramp(t, t0 - 0.5)); fin.set_alpha(ramp(t, 20.0))
        for c, lab in nums: c.set_alpha(ramp(t, t0 - 0.5)); lab.set_alpha(ramp(t, t0 - 0.5))
    return up

def S_pole(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "Where Gauss's average hides: the pole at s = 1", "Turn the dial s down toward 1 and watch ζ(s) climb without limit.")
    p = chart(fig, ax, 0.8, 0.7, 8.6, 5.6, "s", "")
    s = np.linspace(1.012, 4, 500); z = np.array([float(mp.zeta(v)) for v in s]); p.set_xlim(0.8, 4); p.set_ylim(0, 25)
    p.axvline(1, color=RED, lw=1.4, ls=(0, (2, 3))); p.text(1.05, 23.5, "s = 1", color=RED, fontsize=12)
    l2, = p.plot(s, 1 / (s - 1), color=MUTED, lw=1.4, ls=(0, (5, 4))); l1, = p.plot([], [], color=BLUE, lw=3)
    dot, = p.plot([], [], "o", color=BLUE, ms=9)
    p.text(2.6, 2.6, "ζ(s)", color=BLUE, fontsize=15, weight="semibold"); p.text(2.2, 5.2, "1/(s − 1)", color=MUTED, fontsize=12)
    P1 = panel(ax, 10.0, 6.05, BLUE, "A pole at s = 1", "ζ(s) blows up like 1/(s − 1).")
    P2 = panel(ax, 10.0, 4.85, MUTED, "Take the logarithm of the product", "It becomes a sum over primes only:\n1/2ˢ + 1/3ˢ + 1/5ˢ + 1/7ˢ + …\nwhich blows up like ln 1/(s − 1).")
    P3 = panel(ax, 10.0, 2.75, BLUE, "That speed is a fingerprint", "It is exactly what you get if primes\nnear x have density 1 / ln x.")
    fin = ax.text(10.0, 1.0, "Gauss's average lives in the pole.", fontsize=16, color=BLUE, weight="semibold", va="center")
    def up(t):
        k = int(ramp(t, 0.3, 5.5) * len(s)); l1.set_data(s[::-1][:k], z[::-1][:k])
        if k: dot.set_data([s[::-1][k - 1]], [min(z[::-1][k - 1], 25)])
        show(P1, ramp(t, 4.5)); show(P2, ramp(t, 7.0)); show(P3, ramp(t, 9.5)); fin.set_alpha(ramp(t, 13.5))
    return up

def S_explicit(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "The zeros draw the primes", "Riemann's explicit formula: the true prime count is a smooth average minus one wave for every zero of ζ.")
    p = chart(fig, ax, 0.8, 0.7, 9.2, 5.75, "", "", pad=(0.6, 0.9, 0.3, 0.3))
    x = np.linspace(1.5, 40, 1600); PRM = primes_upto(50); true = np.zeros_like(x)
    for q in PRM:
        k = q
        while k <= 40: true += np.log(q) * (x >= k); k *= q
    base = x - np.log(2 * np.pi) - 0.5 * np.log(1 - x ** -2); rho = 0.5 + 1j * ZEROS
    waves = np.array([2 * np.real(x ** r / r) for r in rho]); cum = np.vstack([np.zeros_like(x), np.cumsum(waves, axis=0)])
    p.set_xlim(1.5, 40); p.set_ylim(-1, 42); p.grid(axis="x", visible=False); p.set_xticks([q for q in PRM if q < 40]); p.tick_params(axis="x", labelsize=9.5, colors=INK)
    p.set_xlabel("the primes — the staircase jumps by ln p at each one (and at p², p³ …)", fontsize=11, color=MUTED)
    st, = p.step(x, true, where="post", color=INK, lw=2.0); av, = p.plot(x, x, color=BLUE, lw=2, ls=(0, (5, 4))); ln, = p.plot([], [], color=ORANGE, lw=2.6)
    leg = [p.text(3, 39.5 - i * 2.6, s_, color=c, fontsize=11.5, weight="semibold", va="center") for i, (s_, c) in enumerate(
        [("━  ψ(x): the true (weighted) prime count", INK), ("╍  x: the smooth average", BLUE), ("━  average − waves from N zeros", ORANGE)])]
    nlab = p.text(30.5, 3.2, "", fontsize=15, color=BG, weight="bold", bbox=dict(boxstyle="round,pad=0.4,rounding_size=0.9", fc=ORANGE, ec="none"))
    k1 = kicker(ax, 10.6, 6.15, "Explicit formula")
    F = row(fig, ax, 10.6, 5.5, [(r"$\psi(x)\,=$", INK), (r"$x$", BLUE), (r"$-\ \sum_{\rho}\ \dfrac{x^{\rho}}{\rho}$", ORANGE), (r"$-\ \cdots$", MUTED)], 27)
    P1 = panel(ax, 10.6, 4.5, BLUE, "The smooth average", "comes from the pole of ζ at s = 1.\nThis is Gauss's part.")
    P2 = panel(ax, 10.6, 3.0, ORANGE, "One wave for every zero ρ", "Each place where ζ(ρ) = 0 adds a wave.")
    card(ax, 10.6, 0.7, 4.6, 1.3); w = fig.add_axes([10.75 / 16, 0.76 / 9, 4.3 / 16, 0.8 / 9]); w.axis("off"); w.set_xlim(1.5, 40); w.set_ylim(-1.1, 1.1)
    wl, = w.plot([], [], color=ORANGE, lw=2); wt = ax.text(10.75, 1.78, "the wave from the first zero, ρ = ½ + 14.13 i", fontsize=10, color=MUTED, va="center")
    def up(t):
        k1.set_alpha(ramp(t, 5)); st.set_alpha(ramp(t, 0.3)); av.set_alpha(ramp(t, 12.5)); leg[0].set_alpha(ramp(t, 0.3)); leg[1].set_alpha(ramp(t, 12.5)); leg[2].set_alpha(ramp(t, 17))
        for i, o in enumerate(F): o.set_alpha(ramp(t, [5, 12.5, 17, 17][i]))
        show(P1, ramp(t, 13)); show(P2, ramp(t, 17))
        u = np.clip((t - 18) / (T - 21), 0, 1); N = int(round(150 ** u)) if t > 18 else 0
        if t > 17.5: ln.set_data(x, base - cum[N]); nlab.set_text(f"N = {N} zero" + ("" if N == 1 else "s"))
        k = int(ramp(t, 17.5, 4) * len(x)); wl.set_data(x[:k], waves[0][:k] / np.abs(waves[0]).max()); wt.set_alpha(ramp(t, 17.5))
    return up

def S_map(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "Riemann's map: letting s be a complex number", "The puzzle: the sum only works for s bigger than 1 — and there it is never zero.")
    card(ax, 0.8, 0.7, 9.2, 5.75); X = lambda s: 4.2 + s * 1.5; Y = lambda t: 3.55 + t * 0.085
    ax.plot([X(-2.1), X(3.7)], [Y(0), Y(0)], color=AXIS, lw=1.2, zorder=2); ax.plot([X(0), X(0)], [Y(-30), Y(31)], color=AXIS, lw=1.2, zorder=2)
    for v in (-2, -1, 1, 2, 3): ax.text(X(v), Y(0) - 0.22, str(v), fontsize=10, color=MUTED, ha="center", zorder=3)
    ax.text(X(3.7), Y(0) + 0.2, "σ  (east–west)", fontsize=11, color=MUTED, ha="right"); ax.text(X(0) + 0.12, Y(31) - 0.1, "t  (north–south)", fontsize=11, color=MUTED, va="top")
    good = Rectangle((X(1), Y(-30)), X(3.7) - X(1), Y(31) - Y(-30), color=GREEN, alpha=0, zorder=1); ax.add_patch(good)
    gl = ax.text(X(2.35), Y(-22), "the sum works here\nζ is never zero", fontsize=11.5, color=GREEN, ha="center", va="center")
    cont = Rectangle((X(1), Y(-30)), 0, Y(31) - Y(-30), color=BLUE, alpha=0.13, zorder=1); ax.add_patch(cont)
    cl = ax.text(X(-0.9), Y(-22), "analytic continuation\nextends ζ here", fontsize=11.5, color=BLUE, ha="center", va="center")
    pole = ax.plot([X(1)], [Y(0)], "x", color=RED, ms=11, mew=3, zorder=5)[0]; pl = ax.text(X(1) + 0.12, Y(0) + 0.3, "pole", fontsize=10.5, color=RED)
    s0 = (2.4, 17); pt = ax.plot([X(s0[0])], [Y(s0[1])], "o", color=ORANGE, ms=10, zorder=6)[0]
    d1 = ax.plot([X(s0[0]), X(s0[0])], [Y(0), Y(s0[1])], color=ORANGE, lw=1.2, ls=(0, (3, 3)))[0]; d2 = ax.plot([X(0), X(s0[0])], [Y(s0[1]), Y(s0[1])], color=ORANGE, lw=1.2, ls=(0, (3, 3)))[0]
    sl = ax.text(X(s0[0]) + 0.15, Y(s0[1]) + 0.3, r"$s=\sigma+i\,t$", fontsize=17, color=ORANGE)
    P1 = panel(ax, 10.6, 5.9, GREEN, "Where the formula works", "For σ > 1 the sum settles, and a product\nof non-zero brackets is never zero.\nSo the zeros must be somewhere else.")
    P2 = panel(ax, 10.6, 3.7, ORANGE, "Move 1: a complex dial", "s = σ + i·t is a point on a map:\nσ east–west, t north–south.")
    P3 = panel(ax, 10.6, 1.95, BLUE, "Move 2: extend ζ everywhere", "Analytic continuation — the only\nsmooth way to carry ζ past σ = 1.")
    def up(t):
        u = ramp(t, 1.0); good.set_alpha(0.14 * u); gl.set_alpha(u); show(P1, u); pole.set_alpha(u); pl.set_alpha(u)
        v = ramp(t, 9.0); show([pt, d1, d2, sl], v); show(P2, v)
        w = ramp(t, 15.5, 3.5); cont.set_x(X(1) - w * (X(1) - X(-2.1))); cont.set_width(w * (X(1) - X(-2.1))); cl.set_alpha(ramp(t, 17.5)); show(P3, ramp(t, 15.5))
    return up

def S_gauss_blocks(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "Gauss, around 1795: counting primes in blocks of a thousand", "Each dot is one block of 1 000 consecutive numbers, up to three million.")
    p = chart(fig, ax, 0.8, 0.7, 9.6, 5.75, "x  (each step to the right is ten times bigger)", "primes in the block")
    N = 3_000_000; P = primes_upto(N); blocks = np.bincount(P // 1000, minlength=N // 1000)[:N // 1000]; mid = np.arange(N // 1000) * 1000 + 500
    p.set_xscale("log"); p.set_xlim(400, 3.5e6); p.set_ylim(0, 180)
    sc, = p.plot([], [], "o", ms=2.6, color="#8fa3b8", alpha=.8); cur, = p.plot([], [], color=BLUE, lw=3)
    hl, = p.plot([], [], "o", ms=11, mfc="none", mec=ORANGE, mew=2.2)
    cl = p.text(2.2e4, 122, "1000 / ln x", fontsize=17, color=BLUE, weight="semibold")
    P1 = panel(ax, 11.0, 5.9, ORANGE, "First block, 1 – 1 000", "168 primes")
    P2 = panel(ax, 11.0, 4.6, ORANGE, "Near three million", "only about 65 – 70 primes per block")
    P3 = panel(ax, 11.0, 3.3, BLUE, "They thin out — predictably", "Block by block the count wobbles,\nbut the average follows one\nsmooth curve.")
    cnt = ax.text(11.0, 1.1, "", fontsize=11.5, color=MUTED, va="center", linespacing=1.5)
    def up(t):
        xm = 1000 * 3000 ** ramp(t, 0.5, 15); k = int(np.searchsorted(mid, xm)); sc.set_data(mid[:k], blocks[:k])
        cnt.set_text(f"counted so far: {int(blocks[:k].sum()):,} primes\nup to {max(k,1)*1000:,}".replace(",", " "))
        u = ramp(t, 20, 3.5)
        if u > 0: xx = np.logspace(np.log10(500), np.log10(500 + u * 3e6), 300); cur.set_data(xx, 1000 / np.log(xx))
        cl.set_alpha(u); show(P1, ramp(t, 11.5)); show(P2, ramp(t, 15.5)); show(P3, ramp(t, 20.5))
        hl.set_data([mid[0]], [blocks[0]]) if 11.5 < t < 15.5 else (hl.set_data([mid[-1]], [blocks[-1]]) if 15.5 <= t < 20 else hl.set_data([], []))
    return up

def S_density(fig, T, section=2):
    ax = canvas(fig, section); head(ax, "Gauss's rule: near x, about one number in every ln x is prime")
    rows = [("near 1 000", "ln x ≈ 6.9", 7), ("near 1 000 000", "ln x ≈ 13.8", 14), ("near 10¹²", "ln x ≈ 27.6", 28)]; arts = []
    for i, (a, b, n) in enumerate(rows):
        y = 5.6 - i * 1.45; g = [ax.text(0.8, y + 0.12, a, fontsize=17, color=INK, weight="semibold", va="center"), ax.text(0.8, y - 0.3, b, fontsize=13, color=MUTED, va="center")]
        for k in range(44):
            on = k % n == n // 2; r = FancyBboxPatch((4.0 + k * 0.2, y - 0.2), 0.14, 0.4, boxstyle="round,pad=0,rounding_size=0.04", fc=ORANGE if on else FAINT, ec="none"); ax.add_patch(r); g.append(r)
        g.append(ax.text(15.2, y, f"about 1 in {n}", fontsize=14, color=ORANGE, ha="right", va="center", weight="semibold")); arts.append(g)
    fin = ax.text(0.8, 1.2, r"density of primes near $x$  $\approx$  $\dfrac{1}{\ln x}$", fontsize=30, color=BLUE, va="center")
    def up(t):
        for i, g in enumerate(arts): show(g, ramp(t, 1.0 + i * 1.6))
        fin.set_alpha(ramp(t, 6.5))
    return up

def S_stair(fig, T, section=2, error=False):
    ax = canvas(fig, section)
    head(ax, "How big can the error get?" if error else "Two ways to count the primes", "The whole story is about the gap between the staircase and the curve." if error else "The true count is a staircase. Gauss's estimate is a smooth curve that tracks it closely.")
    p = chart(fig, ax, 0.8, 0.7, 9.6, 5.75, "x", "number of primes up to x")
    N = 200; P = primes_upto(N); x = np.linspace(2, N, 1400); pi = np.searchsorted(P, x, side="right"); Li = np.array([float(mp.li(v) - mp.li(2)) for v in x])
    p.set_xlim(0, N); p.set_ylim(0, 50); st, = p.step([], [], where="post", color=INK, lw=2.2); li, = p.plot([], [], color=BLUE, lw=3)
    if error: p.fill_between(x, pi, Li, color=RED, alpha=.28, step=None, lw=0)
    P1 = panel(ax, 11.0, 5.9, INK, "π(x) — the true count", "Steps up by one at every prime.\n(π is just a name here, not 3.14.)")
    P2 = panel(ax, 11.0, 4.1, BLUE, "Li(x) — Gauss's estimate", "Adds up the density 1 / ln t up to x.\nHere it runs slightly above the stairs.")
    P3 = panel(ax, 11.0, 2.35, RED, "The error:  π(x) − Li(x)", "Gauss could not say how large\nit can become. The answer hides\nin one function.")
    def up(t):
        if error: st.set_data(x, pi); li.set_data(x, Li); show(P1, 1); show(P2, 1); show(P3, ramp(t, 0.6))
        else:
            k = int(ramp(t, 0.3, 8) * len(x)); st.set_data(x[:k], pi[:k]); j = int(ramp(t, 9.5, 5) * len(x)); li.set_data(x[:j], Li[:j])
            show(P1, ramp(t, 1.0)); show(P2, ramp(t, 9.5)); show(P3, 0)
    return up

def S_strip(fig, T, section=4):
    ax = canvas(fig, section); head(ax, "Autumn 2026: an AI proves a quasi-Riemann hypothesis", "Not “all zeros on the line ½” — but all zeros inside a narrower band. Shown here: where zeros are allowed.")
    card(ax, 0.8, 0.7, 9.2, 5.75); X = lambda s: 1.6 + s * 7.6
    ax.plot([X(0), X(1)], [1.55, 1.55], color=AXIS, lw=1.2)
    for v, l in ((0, "0"), (1 / 8, "1/8"), (.5, "½"), (7 / 8, "7/8"), (1, "1")): ax.text(X(v), 1.2, l, fontsize=12, color=MUTED, ha="center"); ax.plot([X(v), X(v)], [1.48, 1.62], color=AXIS, lw=1.2)
    ax.text(X(.5), 0.88, "σ — the east–west position of a zero", fontsize=10.5, color=MUTED, ha="center")
    def band(y, a, b, c, lab, sub):
        r = FancyBboxPatch((X(a), y), X(b) - X(a), 0.62, boxstyle="round,pad=0,rounding_size=0.1", fc=c, ec="none", alpha=0.9); ax.add_patch(r)
        return [r, ax.text(X(.5), y + 0.31, lab, fontsize=12.5, color=BG, weight="bold", ha="center", va="center"), ax.text(X(.5), y + 0.86, sub, fontsize=10.5, color=MUTED, ha="center", va="center", bbox=dict(fc=CARD, ec="none", pad=2))]
    B0 = band(4.9, 0, 1, "#6f7a88", "0 ≤ σ ≤ 1", "known since Riemann, 1859")
    B1 = band(3.55, 1 / 8, 7 / 8, PURPLE, "1/8 ≤ σ ≤ 7/8", "Version 1 · 30 Sep 2026 · 199 pages · verified in Lean")
    B2 = band(2.2, 1 / 12, 11 / 12, ORANGE, "1/12 ≤ σ ≤ 11/12", "Version 2 · a week later · 49 pages · not yet in Lean")
    mid = ax.plot([X(.5), X(.5)], [1.62, 5.6], color=BLUE, lw=1.6, ls=(0, (4, 4)))[0]; ml = ax.text(X(.5) + 0.12, 1.85, "RH: all on ½", fontsize=10.5, color=BLUE, va="center")
    P1 = panel(ax, 10.6, 6.05, PURPLE, "Version 1 — machine-checked", "Every zero has σ between 1/8 and 7/8.")
    P2 = panel(ax, 10.6, 4.85, ORANGE, "Version 2 — shorter, weaker", "A wider band, so a weaker result.\nEasier to read, so mathematicians\nstudy this one.")
    P3 = panel(ax, 10.6, 2.95, BLUE, "What it means for primes", "The error in Gauss's estimate\nis at most about")
    big = ax.text(10.88, 1.5, r"$x^{7/8}$", fontsize=30, color=BLUE, va="center"); fin = ax.text(10.88, 0.82, "the first fixed power below x, ever", fontsize=12.5, color=INK, weight="semibold", va="center")
    def up(t):
        show(B0, ramp(t, 0.5)); show([mid, ml], ramp(t, 0.5)); show(B1, ramp(t, 6.5) * 0.95); show(P1, ramp(t, 6.5)); show(B2, ramp(t, 13.5) * 0.95); show(P2, ramp(t, 17.5))
        show(P3, ramp(t, 29)); big.set_alpha(ramp(t, 32)); fin.set_alpha(ramp(t, 37))
    return up

# ================= v6: section cards, narration-synced scenes =================
def _art(ax, name, crop=0.47):
    im = mpimg.imread(ART / f"{name}.jpg"); w = im.shape[1]; x0 = 16 * crop
    if name.startswith("part") or name == "title":
        ax.imshow(im, extent=(0, 16, 0, 9), zorder=-5, aspect="auto", interpolation="bilinear"); ax.set_xlim(0, 16); ax.set_ylim(0, 9); return
    ax.imshow(im[:, int(w * crop):], extent=(x0, 16, 0, 9), zorder=-5, aspect="auto", interpolation="bilinear")
    g = np.zeros((2, 256, 4)); g[..., :3] = mpl.colors.to_rgb(BG); g[..., 3] = np.clip(1.15 - np.linspace(0, 1, 256) * 1.15, 0, 1)[None, :]
    ax.imshow(g, extent=(x0, x0 + 3.2, 0, 9), zorder=-4, aspect="auto", interpolation="bilinear"); ax.set_xlim(0, 16); ax.set_ylim(0, 9)
def _parts(ax, cur):
    names = ["Primes", "Gauss", "Errors", "AI result", "Summary"]
    for k in range(5):
        ax.add_patch(FancyBboxPatch((0.8 + k * 1.04, 1.3), 0.92, 0.05, boxstyle="round,pad=0,rounding_size=0.025", fc=ORANGE if k + 1 == cur else "#4a515b", ec="none"))
        ax.text(0.8 + k * 1.04, 1.02, f"{k+1} {names[k]}", fontsize=8.5, color=INK if k + 1 == cur else MUTED, va="center")
def S_title(fig, T, title, sub, section=0):
    ax = canvas(fig, 0); _art(ax, "title", 0.34)
    k = txt(ax, 0.8, 7.75, spaced("An explainer in five parts"), 12, ORANGE, "semibold")
    t1 = ax.text(0.8, 6.65, title, fontsize=80, color=INK, family=HEAD, va="center")
    t2 = txt(ax, 0.8, 5.55, "How one strange function controls the primes", 18, MUTED)
    A = panel(ax, 0.8, 4.2, ORANGE, "What an AI did in autumn 2026", "Narrowed down where the zeros\nof the zeta function can be.", 15, 12.5)
    B = panel(ax, 0.8, 2.55, RED, "What it did not do", "Prove the Riemann Hypothesis.\nIt is a historic step toward it.", 15, 12.5)
    def up(t):
        k.set_alpha(ramp(t, 0.3)); t1.set_alpha(ramp(t, 0.5, 0.9)); t2.set_alpha(ramp(t, 1.5, 0.9)); show(A, ramp(t, 16)); show(B, ramp(t, 23))
    return up
def S_section(fig, T, num, title, sub):
    ax = canvas(fig, 0); _art(ax, f"part{num}")
    k = txt(ax, 0.8, 6.5, spaced(f"Part {num} of 5"), 13, ORANGE, "semibold")
    words = title.split(); half = (len(words) + 1) // 2
    two = " ".join(words[:half]) + "\n" + " ".join(words[half:]) if len(title) > 14 else title
    t1 = ax.text(0.8, 5.0, two, fontsize=50, color=INK, family=HEAD, va="center", linespacing=1.05)
    t2 = txt(ax, 0.8, 3.45, sub, 17, MUTED); _parts(ax, num)
    def up(t): k.set_alpha(ramp(t, 0.15)); t1.set_alpha(ramp(t, 0.3, 0.8)); t2.set_alpha(ramp(t, 1.5, 0.8))
    return up

def S_primes(fig, T, section=1):
    ax = canvas(fig, section); head(ax, "Primes: the atoms of arithmetic", "A prime is a whole number bigger than 1 that is not a product of two smaller whole numbers.")
    card(ax, 0.8, 0.7, 8.8, 5.75); P = set(primes_upto(30)); cells = {}
    for n in range(1, 31):
        cx = 1.45 + ((n - 1) % 10) * 0.8; cy = 5.45 - ((n - 1) // 10) * 0.95
        r = FancyBboxPatch((cx - 0.3, cy - 0.3), 0.6, 0.6, boxstyle="round,pad=0,rounding_size=0.1", fc=CARD, ec=FAINT, lw=1.2); ax.add_patch(r)
        cells[n] = (r, ax.text(cx, cy, str(n), fontsize=14, color=MUTED, ha="center", va="center"))
    eq = ax.text(5.2, 1.75, r"$12 \;=\; 2 \times 2 \times 3$", fontsize=34, color=INK, ha="center", va="center"); eq2 = ax.text(5.2, 1.05, "and there is no other way", fontsize=13, color=MUTED, ha="center")
    P1 = panel(ax, 10.2, 5.9, ORANGE, "The primes", "2, 3, 5, 7, 11, 13, …")
    P2 = panel(ax, 10.2, 4.55, BLUE, "Unique factorisation", "Every whole number is built from\nprimes in exactly one way.")
    P3 = panel(ax, 10.2, 2.85, MUTED, "Remember this", "It is the reason a function about\nall numbers can know about primes.")
    order = sorted(P)
    def up(t):
        for n, (r, lab) in cells.items():
            on = n in P and t > 6 + order.index(n) * 0.5 if n in P else False
            r.set_facecolor(ORANGE if on else CARD); r.set_edgecolor(ORANGE if on else FAINT); lab.set_color(BG if on else MUTED); lab.set_weight("bold" if on else "normal")
        if t > 18: cells[12][0].set_edgecolor(BLUE); cells[12][0].set_linewidth(2.5); cells[12][1].set_color(BLUE)
        show(P1, ramp(t, 6)); show(P2, ramp(t, 14)); eq.set_alpha(ramp(t, 18.5)); eq2.set_alpha(ramp(t, 21)); show(P3, ramp(t, 21.5))
    return up

def S_gaps(fig, T, section=1):
    ax = canvas(fig, section); head(ax, "One at a time, primes look random", "Where each one falls on the number line, up to 120.")
    card(ax, 0.8, 2.9, 14.4, 3.2); P = primes_upto(120); X = lambda n: 1.4 + n / 120 * 13.2
    ax.plot([X(0), X(120)], [4.0, 4.0], color=AXIS, lw=1.5)
    for v in range(0, 121, 10): ax.plot([X(v), X(v)], [3.92, 4.08], color=AXIS, lw=1); ax.text(X(v), 3.5, str(v), fontsize=10.5, color=MUTED, ha="center")
    sc = ax.scatter([], [], s=60, color=ORANGE, zorder=3)
    def brace(a, b, c, lab):
        return [ax.plot([X(a), X(a), X(b), X(b)], [4.3, 4.6, 4.6, 4.3], color=c, lw=2)[0], ax.text((X(a) + X(b)) / 2, 5.2, lab, fontsize=13, color=c, ha="center", va="center", weight="semibold")]
    B1 = brace(11, 13, GREEN, "11 and 13\nneighbours"); B2 = brace(89, 97, RED, "89 → 97\na gap of 8")
    P1 = panel(ax, 0.8, 2.0, MUTED, "No practical formula", "Nothing simply hands you the next prime.")
    P2 = panel(ax, 6.2, 2.0, GREEN, "Sometimes close together", "like 11 and 13")
    P3 = panel(ax, 11.0, 2.0, RED, "Sometimes far apart", "a long stretch with none")
    def up(t):
        k = int(ramp(t, 0.3, 4.5) * len(P)); sc.set_offsets(np.c_[[X(p) for p in P[:k]], [4.0] * k] if k else np.empty((0, 2)))
        show(P1, ramp(t, 2)); show(B1, ramp(t, 7)); show(P2, ramp(t, 7)); show(B2, ramp(t, 9.5)); show(P3, ramp(t, 9.5))
    return up

def S_switch(fig, T, section=1):
    ax = canvas(fig, section); kicker(ax, 0.8, 6.6, "Changing the question")
    a = txt(ax, 0.8, 5.6, "Where exactly is the next prime?", 34, MUTED, "bold"); strike = ax.plot([], [], color=RED, lw=4, zorder=10, solid_capstyle="round")[0]
    b = txt(ax, 0.8, 3.9, "How many primes are there,\non average, near a number x?", 40, INK, "bold"); bar = Rectangle((0.8, 2.3), 0, 0.07, fc=ORANGE, ec="none"); ax.add_patch(bar)
    def up(t):
        a.set_alpha(ramp(t, 0.8)); strike.set_data([0.75, 0.75 + 9.1 * ramp(t, 7, 0.7)] if t > 7 else [[], []], [5.5, 5.5] if t > 7 else [[], []]); b.set_alpha(ramp(t, 9)); bar.set_width(6 * ramp(t, 9.5, 1.2))
    return up

def S_chain(fig, T, section=3):
    ax = canvas(fig, section); head(ax, "Checkpoint: the chain of logic")
    items = [("primes", INK, "the atoms", 4), ("unique\nfactorisation", INK, "one way to\nbuild each number", 5.5), ("Euler product\n= ζ(s)", INK, "primes written\nas a function", 8),
             ("pole at s = 1", BLUE, "Gauss's\naverage density", 10.3), ("zeros of ζ", ORANGE, "waves around the\naverage = the error", 13.3)]
    G = []
    for i, (s, c, sub, t0) in enumerate(items):
        x = 0.8 + i * 3.0; p_, t_ = chip(ax, x, 4.0, 2.5, 1.5, s, fc=CARD, ec=c, size=15, color=c)
        g = [p_, t_, ax.text(x + 1.25, 3.3, sub, fontsize=12, color=MUTED, ha="center", va="center", linespacing=1.4)]
        if i: g.append(ax.annotate("", xy=(x - 0.05, 4.75), xytext=(x - 0.45, 4.75), arrowprops=dict(arrowstyle="->", color=MUTED, lw=2)))
        G.append((g, t0))
    fin = ax.text(0.8, 1.6, "The error in Gauss's estimate is made of waves — one for each zero.", fontsize=18, color=INK, weight="semibold", va="center")
    def up(t):
        for g, t0 in G: show(g, ramp(t, t0))
        fin.set_alpha(ramp(t, 16))
    return up

def S_waves3(fig, T, section=3):
    ax = canvas(fig, section); head(ax, "The position of a zero sets the size of its wave", r"A zero at $\sigma + i\,t$:  the east–west position $\sigma$ sets the height, about $x^{\sigma}$;  $t$ sets how fast it wiggles.")
    x = np.linspace(1, 400, 1500); cfg = [(1.0, RED, r"$\sigma = 1$", "as big as x itself:\nGauss's estimate would fail", 13), (7 / 8, ORANGE, r"$\sigma = 7/8$", r"height about $x^{7/8}$", 27.5), (0.5, BLUE, r"$\sigma = 1/2$", "only about √x:\nthe smallest possible", 22)]
    L = []
    for i, (sg, c, lab, sub, t0) in enumerate(cfg):
        x0 = 0.8 + i * 4.9; a = chart(fig, ax, x0, 2.2, 4.6, 4.1, "x", "", pad=(0.75, 0.8, 0.2, 0.75)); a.set_ylim(-420, 420); a.set_xlim(1, 400)
        l, = a.plot([], [], color=c, lw=1.7); env = a.fill_between(x, -x ** sg, x ** sg, color=c, alpha=0)
        g = [ax.text(x0 + 0.3, 5.9, lab, fontsize=20, color=c, va="center"), ax.text(x0 + 0.3, 1.6, sub, fontsize=12.5, color=MUTED, va="center", linespacing=1.4)]
        L.append((l, env, sg, g, t0))
    fin = ax.text(8, 0.62, "To know how big the error can be, you must know how far east the zeros can be.", fontsize=15.5, color=INK, weight="semibold", ha="center", va="center")
    def up(t):
        for l, env, sg, g, t0 in L:
            k = int(ramp(t, t0, 4) * len(x)); xx = x[:k]; l.set_data(xx, xx ** sg * np.cos(14.13 * np.log(xx))); env.set_alpha(0.1 * ramp(t, t0)); show(g, ramp(t, t0))
        fin.set_alpha(ramp(t, 28))
    return up

def S_four(fig, T, section=3):
    ax = canvas(fig, section); head(ax, "The mirror symmetry pins down the centre line", "Zeros come in mirror images: left–right across σ = ½, and top–bottom.")
    card(ax, 0.8, 0.7, 8.8, 5.75); X = lambda s: 2.2 + s * 6; Y = lambda t: 3.55 + t * 0.1
    ax.add_patch(Rectangle((X(0), Y(-26)), 6, Y(26) - Y(-26), color=SOFT)); ax.plot([X(.5), X(.5)], [Y(-26), Y(26)], color=BLUE, lw=2.5)
    for v, l in ((0, "0"), (.5, "½"), (1, "1")): ax.text(X(v), 0.92, l, fontsize=12, color=MUTED, ha="center")
    pts = [(0.74, 18), (0.26, 18), (0.74, -18), (0.26, -18)]
    sc = [ax.scatter([X(a)], [Y(b)], s=190, facecolors="none", edgecolors=RED, linewidths=2.5, zorder=4) for a, b in pts]
    ar = [ax.annotate("", xy=(X(0.3), Y(18)), xytext=(X(0.7), Y(18)), arrowprops=dict(arrowstyle="<->", color=RED, lw=1.5)), ax.annotate("", xy=(X(0.74), Y(-15)), xytext=(X(0.74), Y(15)), arrowprops=dict(arrowstyle="<->", color=RED, lw=1.5, ls="--"))]
    on = ax.scatter([X(.5), X(.5)], [Y(9), Y(-9)], s=110, color=BLUE, zorder=4)
    P1 = panel(ax, 10.2, 5.9, RED, "Off the centre line", "A zero there would never be alone:\nit would come in a group of four.")
    P2 = panel(ax, 10.2, 4.0, BLUE, "On the centre line, σ = ½", "A zero is its own mirror image.")
    def up(t):
        for i, s in enumerate(sc): s.set_alpha(ramp(t, 0.6 + i * 0.7))
        show(ar, ramp(t, 2.5)); show(P1, ramp(t, 0.6)); on.set_alpha(ramp(t, 5)); show(P2, ramp(t, 5))
    return up

def S_RH(fig, T, section=3):
    ax = canvas(fig, section); kicker(ax, 0.8, 7.6, "The Riemann Hypothesis, 1859", BLUE)
    t1 = txt(ax, 0.8, 6.7, "Every non-trivial zero of ζ lies exactly\non the line σ = ½.", 36, INK, "bold", va="top")
    card(ax, 11.6, 0.7, 3.6, 6.2); X = lambda s: 12.2 + s * 2.4; Y = lambda t: 1.1 + t * 0.108
    ax.add_patch(Rectangle((X(0), Y(0)), 2.4, Y(50) - Y(0), color=SOFT)); ax.plot([X(.5), X(.5)], [Y(0), Y(50)], color=BLUE, lw=2)
    z = ZEROS[ZEROS < 50]; sc = ax.scatter([], [], s=46, color=ORANGE, zorder=4); labs = [ax.text(X(.5) - 0.2, Y(v), f"{v:.2f}", fontsize=11, color=INK, ha="right", va="center") for v in z[:4]]
    for v, l in ((0, "0"), (.5, "½"), (1, "1")): ax.text(X(v), 0.88, l, fontsize=11, color=MUTED, ha="center")
    P1 = panel(ax, 0.8, 4.3, ORANGE, "The first zeros", "at heights t ≈ 14.13, 21.02, 25.01, 30.42 …")
    P2 = panel(ax, 0.8, 3.0, GREEN, "Checked by computer", "more than 12 trillion zeros — every one on the line")
    P3 = panel(ax, 0.8, 1.7, RED, "But checking is not a proof", "There are infinitely many zeros.  Clay Millennium Prize: $1 000 000")
    def up(t):
        t1.set_alpha(ramp(t, 2.5)); k = int(ramp(t, 3.5, 7) * len(z)); sc.set_offsets(np.c_[np.full(k, X(.5)), Y(z[:k])] if k else np.empty((0, 2)))
        for i, l in enumerate(labs): l.set_alpha(1 if k > i else 0)
        show(P1, ramp(t, 4)); show(P2, ramp(t, 13)); show(P3, ramp(t, 19))
    return up

def S_trillion(fig, T, section=3):
    ax = canvas(fig, section); head(ax, "Checking it: how many primes are there up to a trillion?", "A trillion is 10¹².  (Kontorovich's quick guess was 100 billion; the true count is about 37.6 billion.)")
    card(ax, 0.8, 3.3, 14.4, 3.0); p_, l_ = "37607912018", "37607950281"; k = 6
    def rowd(y, label, s):
        ax.text(1.2, y, label, fontsize=15, color=MUTED, va="center")
        return [ax.text(6.0 + i * 0.78 + (i // 3 + (1 if i >= 2 else 0) * 0) * 0.0 + (0.25 * ((i + 1) // 3)), y, ch, fontsize=42, color=INK, weight="bold", ha="center", va="center", family="DejaVu Sans Mono") for i, ch in enumerate(s)]
    r1 = rowd(5.45, "true count  π(10¹²)", p_); r2 = rowd(4.15, "Gauss's estimate  Li(10¹²)", l_)
    P1 = panel(ax, 0.8, 2.55, ORANGE, "Difference: 38 263", "tiny next to 37.6 billion")
    P2 = panel(ax, 5.6, 2.55, MUTED, "If RH is true", "the error must be below\n√x · ln x / 8π ≈ 1.1 million")
    P3 = panel(ax, 10.4, 2.55, BLUE, "Roughly half the digits", "√x has about half as many\ndigits as x")
    def up(t):
        for i, a in enumerate(r1): a.set_alpha(ramp(t, 13.3 + i * 0.45, 0.3))
        for i, a in enumerate(r2): a.set_alpha(ramp(t, 19.3 + i * 0.45, 0.3))
        if t > 25.3:
            for i, a in enumerate(r1 + r2): a.set_color(BLUE if (i % 11) < k else ORANGE)
        show(P1, ramp(t, 25.3)); show(P2, ramp(t, 29.3)); show(P3, ramp(t, 35.3))
    return up

def S_timeline(fig, T, section=4):
    ax = canvas(fig, section); head(ax, "What was proved after Riemann")
    ev = [(1859, "Riemann", "zeros lie somewhere in 0 ≤ σ ≤ 1", INK, 0.3), (1896, "Hadamard · de la Vallée Poussin", "no zeros on σ = 1  →  the prime number theorem: Gauss was right on average", GREEN, 5),
          (1914, "Hardy", "infinitely many zeros lie on σ = ½", MUTED, 13), (1942, "Selberg", "a positive proportion of zeros lie on the line", MUTED, 14.6), (1958, "Vinogradov · Korobov", "a wider zero-free region near σ = 1", MUTED, 16.2),
          (1974, "Levinson", "at least one third of the zeros are on the line", MUTED, 17.8), (1989, "Conrey", "at least two fifths", MUTED, 19.4)]
    ax.plot([2.05, 2.05], [1.9, 6.75], color=FAINT, lw=2); G = []
    for i, (y, who, what, c, t0) in enumerate(ev):
        yy = 6.5 - i * 0.72; d = ax.scatter([2.05], [yy], s=70, color=c if c != MUTED else AXIS, zorder=3)
        G.append(([d, ax.text(0.8, yy, str(y), fontsize=17, color=c if c != MUTED else INK, weight="bold", va="center"), ax.text(2.45, yy, who, fontsize=14, color=INK, weight="semibold", va="center"), ax.text(6.6, yy, what, fontsize=13.5, color=MUTED, va="center")], t0))
    W = panel(ax, 0.8, 1.35, RED, "The wall", "For 130 years nobody could prove that all zeros stay a fixed distance away from σ = 1 — until 2026.")
    def up(t):
        for g, t0 in G: show(g, ramp(t, t0))
        show(W, ramp(t, 22.5))
    return up

def S_lean(fig, T, section=4):
    ax = canvas(fig, section); head(ax, "Why a machine-checked proof matters")
    A = [card(ax, 0.8, 2.6, 6.9, 3.7), kicker(ax, 1.2, 5.85, "Language model", ORANGE), ax.text(1.2, 5.1, "predicts the next word", fontsize=22, color=INK, family=HEAD, va="center"),
         ax.text(1.2, 4.2, "Fluent, but in mathematics a single\nwrong step breaks the whole proof.", fontsize=13.5, color=MUTED, va="center", linespacing=1.45)]
    B = [card(ax, 8.3, 2.6, 6.9, 3.7), kicker(ax, 8.7, 5.85, "Lean proof checker", GREEN), ax.text(8.7, 5.1, "checks every logical step", fontsize=22, color=INK, family=HEAD, va="center"),
         ax.text(8.7, 4.2, "Version 1 (199 pages) was verified\nmechanically, step by tiny step.", fontsize=13.5, color=MUTED, va="center", linespacing=1.45)]
    wr = [ax.scatter([1.3 + i * 0.42], [3.15], s=110, marker="s", color=(RED if i == 9 else "#59616c")) for i in range(14)]
    st = ax.scatter([], [], s=110, marker="s", color=GREEN)
    def up(t):
        show(A, ramp(t, 0.5)); show(wr, ramp(t, 4)); show(B, ramp(t, 9)); k = int(ramp(t, 13.5, 3) * 14); st.set_offsets(np.c_[8.8 + np.arange(k) * 0.42, np.full(k, 3.15)] if k else np.empty((0, 2)))
    return up

def S_score(fig, T, section=5):
    ax = canvas(fig, section); head(ax, "The scoreboard")
    rows = [("1859", "zeros somewhere in 0 ≤ σ ≤ 1", "no error bound yet", MUTED, 2, 0, 1), ("1896", "no zeros on σ = 1", "prime number theorem", GREEN, 6, 0.02, 0.98),
            ("2026", "zeros in 1/8 ≤ σ ≤ 7/8  (Lean-verified)", r"error $\leq$ about $x^{7/8}$", PURPLE, 10, 1 / 8, 7 / 8), ("RH", "all zeros on σ = ½  — still open", "error ≈ √x: about half the digits", BLUE, 18, 0.49, 0.51)]
    HK = [kicker(ax, x_, 6.7, s_) for x_, s_ in ((0.8, "when"), (2.4, "where the zeros can be"), (9.2, "what it means for primes"), (13.4, "allowed band"))]
    G = []
    for i, (a, b, c, col, t0, lo, hi) in enumerate(rows):
        y = 5.75 - i * 1.25; X = lambda s: 13.4 + s * 1.8
        g = [ax.text(0.8, y, a, fontsize=22, color=col, weight="bold", va="center"), ax.text(2.4, y, b, fontsize=15, color=INK, va="center"), ax.text(9.2, y, c, fontsize=15, color=col, weight="semibold", va="center"),
             ax.add_patch(FancyBboxPatch((X(0), y - 0.13), 1.8, 0.26, boxstyle="round,pad=0,rounding_size=0.05", fc=FAINT, ec="none")),
             ax.add_patch(FancyBboxPatch((X(lo), y - 0.13), X(hi) - X(lo), 0.26, boxstyle="round,pad=0,rounding_size=0.05", fc=col, ec="none")), ax.plot([0.8, 15.2], [y - 0.62, y - 0.62], color=FAINT, lw=1)[0]]
        G.append((g, t0))
    def up(t):
        show(HK, ramp(t, 1.5))
        for g, t0 in G: show(g, ramp(t, t0))
    return up

# ================= v7: excursion in the same visual system =================
def E_puzzle(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "How can you extend a sum that doesn't even add up?", "The zeros that control the primes sit exactly where the sum stops working.")
    card(ax, 0.8, 0.7, 8.8, 5.75); X = lambda s: 3.6 + s * 1.7; Y = lambda t: 3.55 + t * 0.085
    ax.plot([X(-1.5), X(3.4)], [Y(0), Y(0)], color=AXIS, lw=1.2, zorder=2); ax.plot([X(0), X(0)], [Y(-30), Y(31)], color=AXIS, lw=1.2, zorder=2)
    for v in (0, 1, 2, 3): ax.text(X(v), Y(0) - 0.25, str(v), fontsize=10, color=MUTED, ha="center")
    good = Rectangle((X(1), Y(-30)), X(3.4) - X(1), Y(31) - Y(-30), color=GREEN, alpha=0, zorder=1); ax.add_patch(good)
    strip = Rectangle((X(0), Y(-30)), X(1) - X(0), Y(31) - Y(-30), color=RED, alpha=0, zorder=1); ax.add_patch(strip)
    z = ZEROS[ZEROS < 30]; sc = ax.scatter(np.full(2 * len(z), X(.5)), np.r_[Y(z), Y(-z)], s=42, color=ORANGE, zorder=4)
    P1 = panel(ax, 10.2, 5.9, GREEN, "Where the sum settles", "1 + 1/2ˢ + 1/3ˢ + … only adds up\nwhen s is bigger than 1.")
    P2 = panel(ax, 10.2, 4.2, ORANGE, "Where the zeros live", "In the strip between 0 and 1.")
    P3 = panel(ax, 10.2, 2.85, RED, "The catch", "That is exactly where the sum fails.\nSo how can ζ have a value there?")
    def up(t):
        u = ramp(t, 7); good.set_alpha(.15 * u); show(P1, u); sc.set_alpha(ramp(t, 15)); show(P2, ramp(t, 15)); v = ramp(t, 21); strip.set_alpha(.13 * v); show(P3, v)
    return up

def E_geo(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "A simpler sum first:  1 + x + x² + x³ + …", "The geometric series, and the curve 1 / (1 − x).")
    p = chart(fig, ax, 0.8, 0.7, 8.8, 5.75, "x", ""); xs = np.linspace(-2.5, 3, 2200); p.set_xlim(-2.5, 3); p.set_ylim(-4, 8); p.axhline(0, color=AXIS, lw=1); p.axvline(0, color=AXIS, lw=1)
    zone = p.axvspan(-1, 1, color=GREEN, alpha=0); zl = p.text(0, 7.3, "the sum settles here", fontsize=11, color=GREEN, ha="center")
    f = 1 / (1 - xs); f[np.abs(1 - xs) < 0.02] = np.nan
    curve, = p.plot([], [], color=BLUE, lw=3); part, = p.plot([], [], color=ORANGE, lw=2.2); pt, = p.plot([], [], "o", color=ORANGE, ms=10, zorder=5); p2, = p.plot([], [], "o", color=RED, ms=11, zorder=5)
    cl = p.text(-2.3, 0.75, "1 / (1 − x)", fontsize=13, color=BLUE, weight="semibold"); nl = p.text(1.25, 6.9, "", fontsize=12, color=ORANGE, weight="semibold")
    P1 = panel(ax, 10.2, 6.0, GREEN, "Between −1 and 1 they agree", "x = ½:  1 + ½ + ¼ + ⅛ + … = 2\nand  1 / (1 − ½) = 2")
    P2 = panel(ax, 10.2, 4.3, BLUE, "The curve does not stop at 1", "At x = 2 it gives 1 / (1 − 2) = −1.")
    P3 = panel(ax, 10.2, 3.0, RED, "The sum does", "1 + 2 + 4 + 8 + … just blows up.")
    P4 = panel(ax, 10.2, 1.7, INK, "So “1 + 2 + 4 + 8 + … = −1” means", "the function this sum describes\nnear 0 has the value −1 at x = 2.")
    def up(t):
        k = int(ramp(t, 5, 6) * len(xs)); curve.set_data(xs[:k], f[:k]); cl.set_alpha(ramp(t, 8)); u = ramp(t, 5); zone.set_alpha(0.12 * u); zl.set_alpha(u)
        show(P1, ramp(t, 16)); show(P2, ramp(t, 42)); show(P3, ramp(t, 49)); show(P4, ramp(t, 57))
        if 16 <= t < 28:
            N = int(np.clip((t - 16) / 0.9, 1, 9)); pt.set_data([0.5], [sum(0.5 ** i for i in range(N))]); nl.set_text(f"{N} terms"); part.set_data([], [])
        elif t >= 28:
            pt.set_data([], []); N = int(np.clip(2 + (t - 28) * 0.8, 2, 14)); y = sum(xs ** i for i in range(N)); y[np.abs(y) > 50] = np.nan; y[xs < -1.0] = np.nan
            part.set_data(xs, y); nl.set_text(f"partial sum, {N} terms")
        p2.set_data([2.0], [-1.0]) if t > 42 else p2.set_data([], [])
    return up

def E_rigid(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "Analytic continuation: only one way to go on", "Know a complex-smooth function on a small patch, and you know it everywhere.")
    p = chart(fig, ax, 0.8, 0.7, 8.8, 5.75, "", ""); p.set_xticks([]); p.set_yticks([]); x = np.linspace(-3, 3, 900); y = np.sin(1.3 * x) * np.exp(-0.15 * x ** 2) + 0.2 * x; p.set_xlim(-3, 3); p.set_ylim(-1.7, 1.7)
    alts = [p.plot([], [], color=MUTED, lw=1.4, ls=(0, (4, 4)))[0] for _ in range(4)]
    p.axvspan(-0.3, 0.3, color=GREEN, alpha=.15); m0 = np.abs(x) < 0.3; p.plot(x[m0], y[m0], color=GREEN, lw=5); p.text(0, 1.45, "the patch we know", fontsize=11, color=GREEN, ha="center")
    cont, = p.plot([], [], color=BLUE, lw=2.8)
    P1 = panel(ax, 10.2, 5.9, MUTED, "Ordinary curves", "can be continued however you like.")
    P2 = panel(ax, 10.2, 4.55, BLUE, "Analytic functions cannot", "Smooth in the complex sense:\na tiny patch fixes the function\neverywhere it can be extended.")
    P3 = panel(ax, 10.2, 2.4, GREEN, "Like a rigid road", "See one stretch, and there is exactly\none way it can continue.\nNot a trick, and not a choice.")
    xr = x[x >= 0.3]
    def up(t):
        a = ramp(t, 6) * (1 - ramp(t, 14, 2))
        for i, l in enumerate(alts): l.set_data(xr, y[x >= 0.3][0] + (xr - 0.3) * [0.9, -0.5, 0.2, -1.1][i] + [0.25, 0.1, -0.3, 0.2][i] * np.sin(3 * (xr - 0.3))); l.set_alpha(a)
        u = ramp(t, 16, 7); m = np.abs(x) < 0.3 + 2.7 * u; cont.set_data(x[m], y[m]); show(P1, ramp(t, 6)); show(P2, ramp(t, 10)); show(P3, ramp(t, 23))
    return up

def E_eta(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "Reaching the strip: flip every second sign", "The plus and minus terms partly cancel, so the alternating sum settles for every σ > 0.")
    p = chart(fig, ax, 0.8, 0.7, 8.8, 5.75, "number of terms added", "running total at s = ½"); n = np.arange(1, 81); a = np.cumsum((-1) ** (n + 1) / np.sqrt(n)); p.set_xlim(0, 80); p.set_ylim(0, 1.1)
    eta = float(mp.altzeta(0.5)); hl = p.axhline(eta, color=BLUE, ls=(0, (4, 4)), lw=1.2); l, = p.plot([], [], "-", color=ORANGE, lw=1.8); el = p.text(52, 0.2, f"settles at {eta:.4f}", fontsize=13, color=BLUE, weight="semibold")
    f1 = ax.text(10.2, 6.0, r"$1-\dfrac{1}{2^{s}}+\dfrac{1}{3^{s}}-\dfrac{1}{4^{s}}+\cdots$", fontsize=22, color=ORANGE, va="center")
    P1 = panel(ax, 10.2, 5.0, ORANGE, "Step 1: the alternating sum", f"At s = ½ it settles at {eta:.4f},\ninside the strip.")
    f2 = ax.text(10.2, 3.1, r"$\zeta(s)=\dfrac{\mathrm{alternating\ sum}}{1-2^{\,1-s}}$", fontsize=21, color=INK, va="center")
    P2 = panel(ax, 10.2, 2.05, BLUE, "Step 2: divide", f"ζ(½) = {eta:.4f} / (1 − √2) = {float(mp.zeta(0.5)):.4f}\nA value where the original sum fails.")
    def up(t):
        f1.set_alpha(ramp(t, 8)); k = int(ramp(t, 9, 9) * len(n)); l.set_data(n[:k], a[:k]); show([hl, el], ramp(t, 14)); show(P1, ramp(t, 12)); f2.set_alpha(ramp(t, 20)); show(P2, ramp(t, 27))
    return up

def E_values(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "The famous “crazy sums”", "Once ζ is continued it has a value everywhere except s = 1.")
    p = chart(fig, ax, 0.8, 0.7, 8.8, 5.75, "s", "ζ(s)"); s = np.linspace(-4.5, 4, 1000); z = np.array([float(mp.zeta(v)) if abs(v - 1) > 0.04 else np.nan for v in s])
    p.set_xlim(-4.5, 4); p.set_ylim(-2, 3); p.axhline(0, color=AXIS, lw=1); p.axvline(1, color=RED, ls=(0, (2, 3)), lw=1.2); l, = p.plot([], [], color=BLUE, lw=3)
    pts = [(-1, -1 / 12, "−1/12", (-0.1, -0.45)), (0, -0.5, "−½", (0.45, -0.3)), (-2, 0, "0", (0, 0.35))]
    M = [[p.plot([a], [b], "o", color=ORANGE, ms=10)[0], p.text(a + o[0], b + o[1], lab, fontsize=13, color=ORANGE, ha="center", weight="semibold")] for a, b, lab, o in pts]
    P = [panel(ax, 10.2, 6.0, ORANGE, "ζ(−1) = −1/12", "written as  1 + 2 + 3 + 4 + … = −1/12"), panel(ax, 10.2, 4.75, ORANGE, "ζ(0) = −½", "“1 + 1 + 1 + … = −½”"),
         panel(ax, 10.2, 3.5, ORANGE, "ζ(−2) = 0", "“1 + 4 + 9 + … = 0”: the first trivial zero")]
    P4 = panel(ax, 10.2, 2.1, RED, "None of these sums adds up", "Each line means: the one continued\nfunction takes this value here.")
    def up(t):
        k = int(ramp(t, 4, 5) * len(s)); l.set_data(s[:k], z[:k])
        for i, t0 in enumerate([13, 23, 25]): show(M[i], ramp(t, t0)); show(P[i], ramp(t, t0))
        show(P4, ramp(t, 29))
    return up

def E_zero(fig, T, section=9):
    ax = canvas(fig, section); head(ax, "ζ(ρ) = 0 never means the sum adds up to zero", "At a zero in the strip the original sum does not settle at all.")
    p = chart(fig, ax, 0.8, 0.7, 8.8, 5.75, "real part", "imaginary part"); rho = mp.mpc(0.5, ZEROS[0]); n = np.arange(1, 400); ps = np.cumsum([complex(mp.power(int(k), -rho)) for k in n])
    p.set_xlim(-2.6, 2.6); p.set_ylim(-1.7, 1.7); p.axhline(0, color=AXIS, lw=1); p.axvline(0, color=AXIS, lw=1); l, = p.plot([], [], color=ORANGE, lw=1.2); h, = p.plot([], [], "o", color=ORANGE, ms=6)
    o = [p.plot([0], [0], "o", color=BLUE, ms=13, zorder=5)[0], p.text(1.3, 1.35, "ζ(ρ) = 0 is the centre", fontsize=13, color=BLUE, weight="semibold")]
    P1 = panel(ax, 10.2, 5.9, ORANGE, "The sum keeps wandering", f"Partial sums of the original series\nat ρ = ½ + {ZEROS[0]:.3f} i circle the\norigin and never settle.")
    P2 = panel(ax, 10.2, 3.8, BLUE, "The continued function", "has the exact value 0 there —\na value like −1/12, not a total.")
    P3 = panel(ax, 10.2, 2.1, INK, "Without continuation", "no zeros in the strip, no waves in\nthe prime count, no Riemann Hypothesis.")
    def up(t):
        k = int(ramp(t, 6, 14) * len(n)); l.set_data(ps[:k].real, ps[:k].imag)
        if k: h.set_data([ps[k - 1].real], [ps[k - 1].imag])
        show(P1, ramp(t, 6)); show(o, ramp(t, 14)); show(P2, ramp(t, 14)); show(P3, ramp(t, 20))
    return up

def clip_bg(fig, section, people, topic):
    ax = canvas(fig, section); kicker(ax, 0.8, 7.75, "From the interview", ORANGE)
    card(ax, 0.72, 1.695, 10.16, 5.785)
    ax.add_patch(FancyBboxPatch((0.8, 1.38), 10, 0.05, boxstyle="round,pad=0,rounding_size=0.025", fc=FAINT, ec="none"))
    y = 7.0
    for name, role in people:
        ax.add_patch(FancyBboxPatch((11.4, y - 1.0), 0.07, 1.2, boxstyle="round,pad=0,rounding_size=0.035", fc=ORANGE, ec="none"))
        ax.text(11.7, y, name, fontsize=24, color=INK, family=HEAD, va="center"); ax.text(11.7, y - 0.6, role, fontsize=11.5, color=MUTED, va="center", linespacing=1.4); y -= 1.75
    kicker(ax, 11.4, y - 0.1, "Topic"); ax.text(11.4, y - 0.6, topic, fontsize=14, color=INK, va="top", linespacing=1.4, weight="semibold")
    kicker(ax, 11.4, 2.0, "Source"); ax.text(11.4, 1.65, "World Science Festival, 2026\n“AI Closes In on the\nRiemann Hypothesis”", fontsize=10.5, color=MUTED, va="top", linespacing=1.45)

def S_end(fig, T, credits=""):
    ax = canvas(fig, 0); kicker(ax, 8, 5.9, "The open question", ORANGE).set_ha("center")
    q = ax.text(8, 4.5, "Will the last step — from 7/8 to ½ — come from AI,\nfrom human insight, or from both?", fontsize=34, color=INK, family=HEAD, ha="center", va="center", linespacing=1.3)
    def up(t): q.set_alpha(ramp(t, 3))
    return up

def S_credits(fig, T):
    ax = canvas(fig, 0); ax.text(0.8, 7.7, "Predicting Primes", fontsize=40, color=INK, family=HEAD, va="center")
    def block(x, y, k, lines, t0):
        g = [kicker(ax, x, y, k, ORANGE)]
        for i, (s, c, w) in enumerate(lines): g.append(ax.text(x, y - 0.5 - i * 0.42, s, fontsize=13, color=c, weight=w, va="center"))
        return g, t0
    B = [block(0.8, 6.5, "Interview excerpts", [("“AI Closes In on the Riemann Hypothesis”", INK, "semibold"), ("World Science Festival, YouTube, 2026", MUTED, "normal"), ("Brian Greene, Columbia University", MUTED, "normal"),
                                               ("Alex Kontorovich, Rutgers University", MUTED, "normal"), ("Excerpts used for commentary and education.", MUTED, "normal"), ("All rights remain with World Science Festival.", MUTED, "normal")], 0.5),
         block(8.4, 6.5, "Sources", [("Quanta Magazine, 19 October 2026", INK, "semibold"), ("“AI Proved the Quasi-Riemann Hypothesis. What Happens Now?”", MUTED, "normal"), ("OEIS A006880 — the prime counts π(10ⁿ)", MUTED, "normal"),
                                     ("L. Schoenfeld (1976) — error bound under RH", MUTED, "normal"), ("B. Riemann (1859)", MUTED, "normal")], 2.0),
         block(0.8, 3.0, "Narration", [("AI-generated voice (NotebookLM), from an original script", MUTED, "normal")], 3.5),
         block(8.4, 3.0, "Status", [("Verification of the quasi-Riemann proofs was still", MUTED, "normal"), ("in progress in November 2026.", MUTED, "normal")], 5.0)]
    c = ax.text(0.8, 0.9, "© 2026 Marko T. Manninen", fontsize=15, color=INK, weight="semibold", va="center")
    def up(t):
        for g, t0 in B: show(g, ramp(t, t0))
        c.set_alpha(ramp(t, 6.5))
    return up
