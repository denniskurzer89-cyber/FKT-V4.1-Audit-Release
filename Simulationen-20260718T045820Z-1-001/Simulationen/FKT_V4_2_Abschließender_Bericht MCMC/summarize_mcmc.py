#!/usr/bin/env python3
import numpy as np
import json
import matplotlib.pyplot as plt
from pathlib import Path
from getdist import MCSamples, plots

CHAIN_ROOT = 'chains/fkt_bulk_p2_run2'
PLOT_DIR = 'plots'
RESULTS_DIR = 'results'

for d in [PLOT_DIR, RESULTS_DIR]:
    Path(d).mkdir(exist_ok=True)

print("="*60)
print("POST-MCMC DIAGNOSTIK - RUN 2")
print("="*60)

try:
    samples = MCSamples(CHAIN_ROOT)
    print(f"\n✓ Chain geladen: {samples.numrows} Samples")
except Exception as e:
    print(f"\n❌ Fehler: {e}")
    exit(1)

print("\n[1] Corner Plot...")
g = plots.get_subplot_plotter(width_inch=10)
params = ['H0', 'ombh2', 'omch2', 'log10_xi', 'log10_gb_Jm3', 'wX_eff', 'Omega_bulk_0']
g.triangle_plot(samples, params, filled=True)
plt.savefig(f'{PLOT_DIR}/corner_plot_run2.png', dpi=150)
print(f"    ✓ {PLOT_DIR}/corner_plot_run2.png")
plt.close()

print("\n✓ DIAGNOSTIK ABGESCHLOSSEN")
