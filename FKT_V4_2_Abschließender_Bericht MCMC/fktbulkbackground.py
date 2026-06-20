import numpy as np

# Physikalische Konstanten (SI)
G_SI = 6.67430e-11      # m^3/(kg*s^2)
c_SI = 2.99792458e8     # m/s
Mpc_to_m = 3.085677581e22  # m

class FKTBulkBackground:
    """FKT Bulk-Dichte Implementierung für Cobaya/CLASS."""
    
    def __init__(self, params):
        self.params = params
        self.H0_SI = self._get_H0_SI()
        self.rho_crit_today = self._compute_rho_crit()
        
    def _get_H0_SI(self):
        """Konvertiert H0 von km/s/Mpc zu 1/s."""
        H0_kms_Mpc = self.params.get('H0', 67.5)
        return H0_kms_Mpc * 1e3 / Mpc_to_m
    
    def _compute_rho_crit(self):
        """Berechnet kritische Dichte heute in kg/m^3."""
        return 3 * self.H0_SI**2 / (8 * np.pi * G_SI)
    
    def rho_bulk(self, a):
        """Berechnet FKT Bulk-Energiedichte als Funktion von a."""
        log10_xi = self.params['log10_xi']
        log10_gb_Jm3 = self.params['log10_gb_Jm3']
        wX_eff = self.params['wX_eff']
        
        xi = 10**log10_xi
        gb_Jm3 = 10**log10_gb_Jm3
        
        gb_kg_m3 = gb_Jm3 / c_SI**2
        gb_norm = gb_kg_m3 / self.rho_crit_today
        
        gamma = 1.0
        g0_norm = 1.0 
        S = xi * (gb_norm / g0_norm)**gamma
        
        Omega_bulk_0 = self.params.get('Omega_bulk_0', 0.7)
        rho_bulk_norm = S * Omega_bulk_0 * a**(-3 * (1 + wX_eff))
        
        return rho_bulk_norm
    
    def w_bulk(self, a):
        return self.params['wX_eff']
    
    def validate(self):
        checks = []
        a_test = np.array([0.01, 0.1, 0.5, 1.0])
        rho_test = [self.rho_bulk(a) for a in a_test]
        checks.append(("Positive Dichte", all(r > 0 for r in rho_test)))
        
        rho_early = self.rho_bulk(0.001)
        checks.append(("Frühe Dichte < 10", rho_early < 10.0))
        
        rho_today = self.rho_bulk(1.0)
        checks.append(("Heutige Dichte ~0.7", 0.5 < rho_today < 1.5))
        
        return checks

def rho_bulk(a, params):
    bg = FKTBulkBackground(params)
    return bg.rho_bulk(a)

def w_bulk(a, params):
    bg = FKTBulkBackground(params)
    return bg.w_bulk(a)
