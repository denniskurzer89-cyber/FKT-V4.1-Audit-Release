from cobaya.likelihood import Likelihood
import numpy as np

class FKTPrecisionConstraint(Likelihood):
    Z_target = 114
    A_target = 289
    N_target = 175
    BE_measured = 0.0
    BE_sigma = 0.050
    hbar_c = 197.3269804
    m_proton_MeV = 938.27208816
    alpha_em = 1.0 / 137.035999084
    R0 = 1.25
    
    def initialize(self):
        self.log_info("FKT Precision Constraint initialisiert")
        self.log_info(f"Target: Z={self.Z_target}, A={self.A_target}")
    
    def compute_fkt_shift(self, xi, gb_Jm3):
        Z = self.Z_target
        A = self.A_target
        N = self.N_target
        
        R = self.R0 * A**(1.0/3.0)
        E_coulomb = (3.0/5.0) * self.alpha_em * self.hbar_c * Z**2 / R
        f_shell = 1.0 + 0.15 * np.exp(-(Z - 114.0)**2 / 20.0)
        
        try:
            v_over_c = Z * self.alpha_em
            if v_over_c < 1.0:
                gamma_rel = 1.0 / np.sqrt(1.0 - v_over_c**2)
            else:
                gamma_rel = 1.0
        except:
            gamma_rel = 1.0
        
        f_asymmetry = 1.0 - 0.05 * ((N - Z) / A)**2
        S = xi * gb_Jm3
        
        Delta_BE_MeV = (S * (E_coulomb / self.m_proton_MeV) * 
                        f_shell * gamma_rel * f_asymmetry * 1e-6)
        
        return Delta_BE_MeV
    
    def get_requirements(self):
        return {'log10_xi': None, 'log10_gb_Jm3': None}
    
    def logp(self, **params_values):
        xi = 10**params_values['log10_xi']
        gb_Jm3 = 10**params_values['log10_gb_Jm3']
        
        Delta_BE_pred = self.compute_fkt_shift(xi, gb_Jm3)
        chi2 = ((Delta_BE_pred - self.BE_measured) / self.BE_sigma)**2
        
        return -0.5 * chi2
