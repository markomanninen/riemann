from scenes import *

def E_puzzle(fig, T, section=9):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "How can you extend a sum that doesn't even add up?", 28, weight="bold")
    X = lambda s: 6.5 + s * 2.4; Y = lambda t: 3.9 + t * 0.08
    ax.plot([X(-2), X(3.2)], [Y(0), Y(0)], color=AXIS, lw=1); ax.plot([X(0), X(0)], [Y(-30), Y(34)], color=AXIS, lw=1)
    good = Rectangle((X(1), Y(-30)), X(3.2) - X(1), Y(34) - Y(-30), color=GREEN, alpha=0); ax.add_patch(good)
    strip = Rectangle((X(0), Y(-30)), X(1) - X(0), Y(34) - Y(-30), color=RED, alpha=0); ax.add_patch(strip)
    g = txt(ax, X(2.1), Y(22), "σ > 1\nthe sum settles ✓", 16, GREEN, ha="center")
    r = txt(ax, X(0.5), Y(-22), "0 < σ < 1\nzeros live here\nbut the sum fails ✗", 15, RED, ha="center")
    z = ZEROS[ZEROS < 32]; sc = ax.scatter(np.full(len(z), X(.5)), Y(z), s=40, color=BLUE, zorder=4, alpha=0)
    def up(t):
        u = ramp(t, 7); good.set_alpha(.15 * u); g.set_alpha(u)
        v = ramp(t, 15); strip.set_alpha(.12 * v); r.set_alpha(v); sc.set_alpha(v)
    return up

def E_geo(fig, T, section=9):
    ax = canvas(fig, section)
    head = txt(ax, 1.0, 7.3, "A simpler sum:  1 + x + x² + x³ + …", 28, weight="bold")
    p = plot_ax(fig, [0.07, 0.12, 0.56, 0.62], "x", "")
    xs = np.linspace(-2.5, 3, 2000); p.set_xlim(-2.5, 3); p.set_ylim(-4, 8); p.axhline(0, color=AXIS, lw=1); p.axvline(0, color=AXIS, lw=1)
    zone = p.axvspan(-1, 1, color=GREEN, alpha=0)
    f = 1 / (1 - xs); f[np.abs(1 - xs) < 0.02] = np.nan
    curve, = p.plot([], [], color=BLUE, lw=3, label="1 / (1 − x)")
    part, = p.plot([], [], color=ORANGE, lw=2, label="partial sum, N terms")
    pt, = p.plot([], [], "o", color=RED, ms=10)
    p.legend(loc="upper left", fontsize=13, frameon=False)
    notes = [txt(ax, 10.6, 6.2, "x = ½:  1 + ½ + ¼ + … = 2", 18, INK, "semibold"),
             txt(ax, 10.6, 5.5, "and 1/(1 − ½) = 2  ✓", 18, BLUE),
             txt(ax, 10.6, 4.5, "Partial sums hug the curve", 17, ORANGE), txt(ax, 10.6, 4.0, "only for −1 < x < 1", 17, ORANGE),
             txt(ax, 10.6, 3.0, "x = 2: the sum 1 + 2 + 4 + 8 + … → ∞", 17, RED),
             txt(ax, 10.6, 2.5, "but the curve gives 1/(1 − 2) = −1", 17, BLUE),
             txt(ax, 10.6, 1.4, "The sum only described the", 17, INK, "semibold"), txt(ax, 10.6, 0.9, "function near 0 — not the function", 17, INK, "semibold")]
    sched = [16, 23, 28, 28.6, 49, 42, 74, 74.6]
    nl = txt(ax, 6.0, 1.55, "", 15, ORANGE)
    def up(t):
        for n, s0 in zip(notes, sched): n.set_alpha(ramp(t, s0))
        k = int(ramp(t, 5, 6) * len(xs)); curve.set_data(xs[:k], f[:k])
        if t < 28:   # x = 1/2 example: partial sums as dots
            N = int(np.clip((t - 16) / 1.0, 0, 8)); pt.set_data([0.5], [sum(0.5 ** i for i in range(N))] if N else [np.nan])
            part.set_data([], [])
        else:
            pt.set_data([2.0], [-1.0] if t > 42 else [np.nan])
            N = int(np.clip(1 + (t - 28) * 0.8, 1, 14)); y = sum(xs ** i for i in range(N)); y[np.abs(y) > 50] = np.nan; y[xs < -1.0] = np.nan
            part.set_data(xs, y); nl.set_text(f"N = {N}"); zone.set_alpha(0.12 * ramp(t, 28))
    return up

def E_rigid(fig, T, section=9):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Analytic continuation: there is only one way to continue", 26, weight="bold")
    p = plot_ax(fig, [0.07, 0.16, 0.56, 0.56], "", ""); p.set_xticks([]); p.set_yticks([])
    x = np.linspace(-3, 3, 800); y = np.sin(1.3 * x) * np.exp(-0.15 * x ** 2) + 0.2 * x
    p.set_xlim(-3, 3); p.set_ylim(-1.6, 1.6)
    p.axvspan(-0.3, 0.3, color=GREEN, alpha=.15)
    known, = p.plot(x[(x > -0.3) & (x < 0.3)], y[(x > -0.3) & (x < 0.3)], color=GREEN, lw=5)
    cont, = p.plot([], [], color=BLUE, lw=2.5)
    notes = [txt(ax, 10.6, 5.6, "Ordinary curves: continue", 18, MUTED), txt(ax, 10.6, 5.1, "however you like", 18, MUTED),
             txt(ax, 10.6, 4.0, "Complex-smooth (analytic):", 18, INK, "semibold"), txt(ax, 10.6, 3.5, "a small patch fixes it", 18, INK, "semibold"),
             txt(ax, 10.6, 3.0, "everywhere", 18, INK, "semibold"),
             txt(ax, 10.6, 1.8, "Like a rigid road:", 18, BLUE), txt(ax, 10.6, 1.3, "one stretch → one route", 18, BLUE)]
    def up(t):
        u = ramp(t, 16, 7); m = np.abs(x) < 0.3 + 2.7 * u; cont.set_data(x[m], y[m])
        for i, n in enumerate(notes): n.set_alpha(ramp(t, [6, 6, 10, 10, 16, 23, 23][i]))
    return up

def E_eta(fig, T, section=9):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "Reaching the strip: flip every second sign", 28, weight="bold")
    txt(ax, 1.0, 6.5, "1 − 1/2ˢ + 1/3ˢ − 1/4ˢ + …   settles for every σ > 0", 20, INK)
    p = plot_ax(fig, [0.07, 0.12, 0.52, 0.54], "number of terms", "partial sum at s = ½")
    n = np.arange(1, 81); a = np.cumsum((-1) ** (n + 1) / np.sqrt(n)); p.set_xlim(0, 80); p.set_ylim(0, 1.1)
    eta = float(mp.altzeta(0.5)); p.axhline(eta, color=BLUE, ls="--", lw=1)
    l, = p.plot([], [], "o-", color=ORANGE, ms=3, lw=1.5)
    notes = [txt(ax, 10.2, 5.0, f"→ {eta:.4f}", 26, BLUE, "bold"),
             txt(ax, 10.2, 3.9, "ζ(s) = alternating sum / (1 − 2^(1−s))", 17, INK),
             txt(ax, 10.2, 3.0, f"ζ(½) = {eta:.4f} / (1 − √2)", 17, INK),
             txt(ax, 10.2, 2.2, f"     = {float(mp.zeta(0.5)):.4f}", 24, BLUE, "bold"),
             txt(ax, 10.2, 1.2, "a value inside the strip,\nwhere the original sum fails", 15, MUTED)]
    def up(t):
        k = int(ramp(t, 8, 9) * len(n)); l.set_data(n[:k], a[:k])
        for i, o in enumerate(notes): o.set_alpha(ramp(t, [14, 22, 25, 28, 29][i]))
    return up

def E_values(fig, T, section=9):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "The famous “crazy sums” are values of the continued ζ", 26, weight="bold")
    p = plot_ax(fig, [0.07, 0.12, 0.55, 0.62], "s (real)", "ζ(s)")
    s = np.linspace(-4.5, 4, 900); z = np.array([float(mp.zeta(v)) if abs(v - 1) > 0.04 else np.nan for v in s])
    p.set_xlim(-4.5, 4); p.set_ylim(-2, 3); p.axhline(0, color=AXIS, lw=1); p.axvline(1, color=RED, ls=":", lw=1.2)
    l, = p.plot([], [], color=BLUE, lw=3)
    pts = [(-1, -1 / 12, "ζ(−1) = −1/12"), (0, -0.5, "ζ(0) = −½"), (-2, 0, "ζ(−2) = 0")]
    marks = [p.plot([a], [b], "o", color=ORANGE, ms=10, alpha=0)[0] for a, b, _ in pts]
    offs = [(-0.2, -0.55), (0.9, -0.35), (-0.4, 0.4)]
    labs = [p.text(a + offs[i][0], b + offs[i][1], s_, fontsize=13, color=ORANGE, ha="center", alpha=0) for i, (a, b, s_) in enumerate(pts)]
    notes = [txt(ax, 10.4, 5.8, "ζ(−1) = −1/12", 20, INK, "bold"), txt(ax, 10.4, 5.3, "read as  1 + 2 + 3 + 4 + …", 16, MUTED),
             txt(ax, 10.4, 4.4, "ζ(0) = −½", 20, INK, "bold"), txt(ax, 10.4, 3.9, "read as  1 + 1 + 1 + …", 16, MUTED),
             txt(ax, 10.4, 3.0, "ζ(−2) = 0", 20, INK, "bold"), txt(ax, 10.4, 2.5, "read as  1 + 4 + 9 + …  (first trivial zero)", 16, MUTED),
             txt(ax, 10.4, 1.3, "None of these sums really adds up", 17, RED, "semibold")]
    def up(t):
        k = int(ramp(t, 4, 5) * len(s)); l.set_data(s[:k], z[:k])
        for i in range(3):
            a = ramp(t, [13, 23, 25][i]); marks[i].set_alpha(a); labs[i].set_alpha(a)
            notes[2 * i].set_alpha(a); notes[2 * i + 1].set_alpha(a)
        notes[6].set_alpha(ramp(t, 29))
    return up

def E_zero(fig, T, section=9):
    ax = canvas(fig, section)
    txt(ax, 1.0, 7.3, "ζ(ρ) = 0 never means the sum adds up to zero", 28, weight="bold")
    p = plot_ax(fig, [0.07, 0.12, 0.5, 0.62], "real part", "imaginary part")
    rho = mp.mpc(0.5, ZEROS[0]); n = np.arange(1, 400)
    ps = np.cumsum([complex(mp.power(int(k), -rho)) for k in n])
    p.set_xlim(-4, 6); p.set_ylim(-5, 5); p.axhline(0, color=FAINT, lw=1); p.axvline(0, color=FAINT, lw=1)
    l, = p.plot([], [], color=ORANGE, lw=1.2); h, = p.plot([], [], "o", color=ORANGE, ms=6)
    o, = p.plot([0], [0], "o", color=BLUE, ms=14, alpha=0)
    notes = [txt(ax, 9.8, 5.8, "Partial sums of 1 + 1/2^ρ + 1/3^ρ + …", 16, ORANGE, "semibold"),
             txt(ax, 9.8, 5.3, f"at ρ = ½ + {ZEROS[0]:.3f} i  keep wandering", 16, ORANGE),
             txt(ax, 9.8, 4.1, "The continued function:", 18, BLUE, "semibold"),
             txt(ax, 9.8, 3.6, "ζ(ρ) = 0  exactly", 22, BLUE, "bold"),
             txt(ax, 9.8, 2.4, "No continuation → no zeros in the strip", 16, INK),
             txt(ax, 9.8, 1.9, "→ no waves → no Riemann Hypothesis", 16, INK)]
    def up(t):
        k = int(ramp(t, 6, 14) * len(n)); l.set_data(ps[:k].real, ps[:k].imag)
        if k: h.set_data([ps[k - 1].real], [ps[k - 1].imag])
        o.set_alpha(ramp(t, 14))
        for i, x in enumerate(notes): x.set_alpha(ramp(t, [6, 6, 14, 14, 20, 25][i]))
    return up
