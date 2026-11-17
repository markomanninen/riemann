import sys, os, subprocess
from scenes_b import *
from matplotlib.animation import FFMpegWriter
from paths import build_dir
CRED = ("Interview clips: “AI Closes In on the Riemann Hypothesis”, World Science Festival (YouTube), Brian Greene with Alex Kontorovich, 2026.\n"
        "Used for commentary and education with attribution.  Narration: NotebookLM from an original script.  Animations: computed with mpmath/matplotlib.\n"
        "Sources: Quanta Magazine (19 Oct 2026); OEIS A006880; Schoenfeld (1976).")
K = lambda: "Alex Kontorovich", "Professor of Mathematics, Rutgers University"
MAIN = [
 (0, 32, S_title, dict(title="Predicting Primes", sub="How one strange function controls the primes — and what AI proved in 2026")),
 (32, 48, S_text, dict(lines=["Today", "1 · The prime number mystery", "2 · Gauss & the zeta function", "3 · Riemann & the errors", "4 · The AI breakthrough", "5 · Summary"],
                       section=0, starts=[0.2, 3, 7, 8, 11, 13], sizes=[34] + [24] * 5, colors=[INK] + [BLUE] * 5, y0=6.4, dy=0.9)),
 (48, 64, S_section, dict(num=1, title="The prime number mystery", sub="The building blocks")),
 (64, 69.13, S_cue, dict(name="Alex Kontorovich", role="Professor of Mathematics, Rutgers University", section=1)),
 (69.13, 80, S_text, dict(lines=["“Not expecting to live to see it.”", "What happened on 30 September 2026?"], section=1, starts=[0.2, 1.9], sizes=[36, 24], colors=[INK, BLUE], y0=5.0, dy=1.4)),
 (80, 89, S_text, dict(lines=["The one question of this video:", "How accurately can we predict", "how many primes there are up to x?"], section=1,
                       starts=[0.2, 1.0, 1.6], sizes=[22, 40, 40], colors=[MUTED, INK, INK], y0=5.6, dy=1.3)),
 (89, 113, S_primes, dict()), (113, 127, S_gaps, dict()), (127, 140, S_switch, dict()),
 (140, 143.27, S_cue, dict(name="Brian Greene", role="Physicist, Columbia University · host", section=1)),
 (143.27, 149, S_lnx, dict()),
 (149, 156, S_section, dict(num=2, title="Gauss & the zeta function", sub="Connecting primes to a smooth curve")),
 (156, 161, S_text, dict(lines=["Has AI solved the Riemann Hypothesis?"], section=2, sizes=[38], y0=4.6)),
 (161, 164.13, S_cue, dict(name="Brian Greene", role="Physicist, Columbia University · host", section=2)),
 (164.13, 171, S_strip_teaser, dict()),
 (171, 174.68, S_cue, dict(name="Alex Kontorovich", role="Professor of Mathematics, Rutgers University", section=2)),
 (174.68, 182, S_text, dict(lines=["“A moment that can only happen once.”", "To see why it matters, go back to 1795."], section=2, starts=[0.2, 2.4], sizes=[36, 24], colors=[INK, BLUE], y0=5.0, dy=1.4)),
 (182, 185.09, S_cue, dict(name="Alex Kontorovich", role="on Gauss", section=2)),
 (185.09, 210, S_gauss_blocks, dict()), (210, 220, S_density, dict()),
 (220, 237, S_stair, dict()), (237, 247, S_stair, dict(error=True)),
 (247, 255, S_bridge, dict()), (255, 264, S_zsum, dict()), (264, 294, S_euler, dict()), (294, 300, S_log, dict()),
 (300, 318, S_pole, dict()), (318, 325, S_spikes, dict()), (325, 359, S_explicit, dict()), (359, 380.95, S_map, dict()),
 (380.95, 390, S_mirror, dict()),
 (390, 393.17, S_cue, dict(name="Alex Kontorovich", role="on Riemann's 1859 paper", section=2)),
 (393.17, 398, S_quote, dict(line1="The line “real part of s = 1”", line2="Hold on to it — it comes back in 1896.", section=2)),
 (398, 403, S_section, dict(num=3, title="Riemann & the errors", sub="The position of the zeros")),
 (403, 423, S_chain, dict()), (423, 456, S_waves3, dict()), (456, 467, S_four, dict()),
 (467, 470.09, S_cue, dict(name="Alex Kontorovich", role="on Riemann's private notes", section=3)),
 (470.09, 493, S_RH, dict()),
 (493, 495.67, S_cue, dict(name="Alex Kontorovich", role="on what √x means in practice", section=3)),
 (495.67, 538, S_trillion, dict()),
 (538, 556, S_section, dict(num=4, title="The AI breakthrough", sub="Breaking a 130-year wall")),
 (556, 560.83, S_cue, dict(name="Alex Kontorovich", role="on the 19th-century climax", section=4)),
 (560.83, 594, S_timeline, dict()), (594, 636, S_strip, dict()), (636, 653, S_lean, dict()),
 (653, 655.66, S_cue, dict(name="Alex Kontorovich", role="on the Lean proof checker", section=4)),
 (655.66, 662, S_text, dict(lines=["No human in the loop for the checking —", "but a human still confirms the statement is the right one"], section=4,
                           starts=[0.2, 1.5], sizes=[30, 22], colors=[INK, BLUE], y0=5.0, dy=1.3)),
 (662, 668, S_section, dict(num=5, title="Summary of the quest", sub="Scoreboard & future")),
 (668, 694, S_text, dict(lines=["The question: how accurately can we predict the primes?", "Gauss's Li(x) is the smooth average — the game is its error",
                                "The bridge: Euler's product → ζ(s); the pole is the average, every zero a wave",
                                "The rule: the farther east a zero can be, the bigger the error"], section=5,
                         starts=[0.6, 8, 13, 21], sizes=[26, 22, 22, 22], colors=[INK, MUTED, MUTED, BLUE], y0=6.2, dy=1.25)),
 (694, 725, S_score, dict()),
 (725, 742.34, S_end, dict(credits=CRED)),
]
EX = [
 (0, 31, E_puzzle, dict()), (31, 111, E_geo, dict()), (111, 145, E_rigid, dict()), (145, 180, E_eta, dict()),
 (180, 188, S_text, dict(lines=["The rest of the map: the mirror symmetry s ↔ 1 − s"], section=9, sizes=[30], y0=4.6)),
 (188, 228, E_values, dict()), (228, 259, E_zero, dict()),
 (259, 262.9, S_text, dict(lines=["So that's what “extended” means.", "Now, back to Riemann's map."], section=9, starts=[0.2, 1.8],
                             sizes=[34, 26], colors=[INK, BLUE], y0=5.0, dy=1.4)),
]
CRED = [(0, 16, S_credits, dict())]
def render(sched, prefix, idx):
    t0, t1, fn, kw = sched[idx]; f0, f1 = round(t0 * FPS), round(t1 * FPS); T = (f1 - f0) / FPS
    fig = plt.figure(figsize=(W, H), dpi=DPI); up0 = fn(fig, T, **kw)
    _o = fig.add_axes([0, 0, 1, 1], zorder=1000); _o.axis("off"); _o.patch.set_alpha(0); _r = Rectangle((0, 0), 1, 1, color=BG, transform=_o.transAxes); _o.add_patch(_r)
    def up(t): up0(t); _r.set_alpha(float(1 - ease(t / 0.35)))
    out = str(build_dir("seg") / f"{prefix}{idx:03d}.mp4"); tmp = out + ".tmp.mp4"
    w = FFMpegWriter(fps=FPS, codec="libx264", extra_args=["-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p"])
    with w.saving(fig, tmp, DPI):
        for f in range(f1 - f0): up(f / FPS); w.grab_frame()
    os.replace(tmp, out); plt.close(fig)
if __name__ == "__main__":
    which = sys.argv[1]; sched = {"main": MAIN, "ex": EX, "cred": CRED}[which]
    ids = [int(v) for v in sys.argv[2].split(",")] if len(sys.argv) > 2 and sys.argv[2] != "all" else range(len(sched))
    mode = sys.argv[3] if len(sys.argv) > 3 else "video"
    for i in ids:
        if mode == "still":
            t0, t1, fn, kw = sched[i]; T = t1 - t0; fig = plt.figure(figsize=(W, H), dpi=DPI); up = fn(fig, T, **kw)
            for tt in np.arange(0, T, 1 / FPS)[:int(T * FPS * 0.85)]: up(tt)
            fig.savefig(build_dir("still") / f"{which}{i:03d}.png", dpi=50); plt.close(fig)
        else: render(sched, which, i)
