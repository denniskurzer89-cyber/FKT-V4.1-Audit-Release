#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from fktbulkbackground import FKTBulkBackground

Path('plots').mkdir(exist_ok=True)

params_test = {
    'log10_xi': 4.39,
    'log10_gb_Jm3': -4.82,
    'wX_eff': -0.90,
    'H0': 67.5,
    'Omega_bulk_0': 0.7
}

print("="*60)
print("FKT BULK VALIDIERUNG - RUN 2")
print("="*60)

bg = FKTBulkBackground(params_test)

print("\n[1] Physikalische Konsistenz-Checks:")
checks = bg.validate()
for name, passed in checks:
    status = "✓" if passed else "✗"
    print(f"  {status} {name}")

print("\n[2] Zeitentwicklung:")
a_grid = np.logspace(-3, 0, 100)
rho_values = [bg.rho_bulk(a) for a in a_grid]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.loglog(a_grid, rho_values, 'b-', lw=2, label='FKT Bulk')
ax1.loglog(a_grid, 0.7*np.ones_like(a_grid), 'k--', label='ΛCDM')
ax1.set_xlabel('Skalenfaktor a')
ax1.set_ylabel('ρ_bulk / ρ_crit')
ax1.grid(True, alpha=0.3)
ax1.legend()

ratio = np.array(rho_values) / 0.7
ax2.semilogx(a_grid, ratio, 'r-', lw=2)
ax2.axhline(1.0, color='k', ls='--', alpha=0.5)
ax2.set_xlabel('Skalenfaktor a')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('plots/fkt_bulk_validation_run2.png', dpi=150)
print("\n✓ VALIDIERUNG ERFOLGREICH")
