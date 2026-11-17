"""Regenerate data/zeta_data.json: the first 150 zeta zeros, ζ(½ + it) for 0 < t ≤ 52 and Hardy's Z(t) for 0 ≤ t ≤ 62.

Usage: python3 scripts/make_zeta_data.py   (takes a few minutes, needs mpmath and numpy)
"""
import json
from pathlib import Path
import mpmath as mp, numpy as np

OUT = Path(__file__).resolve().parent.parent / "data" / "zeta_data.json"
mp.mp.dps = 20
zeros = [float(mp.zetazero(n).imag) for n in range(1, 151)]
t = np.linspace(0.01, 52, 2600)
z = [mp.zeta(mp.mpc(0.5, ti)) for ti in t]
Zt = np.linspace(0, 62, 2500)
Z = [float(mp.siegelz(ti)) for ti in Zt]
json.dump({"zeros": zeros, "t": t.tolist(), "re": [float(v.real) for v in z], "im": [float(v.imag) for v in z],
           "Zt": Zt.tolist(), "Z": Z}, open(OUT, "w"))
print("wrote", OUT, "first zeros", [round(v, 3) for v in zeros[:3]])
