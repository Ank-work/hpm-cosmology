"""
HPM Base Module for Prediction Tests
Shared functionality for all cross-validation tests
"""

import numpy as np
from pathlib import Path
from scipy.optimize import minimize
import json

# Data directory
DATA_DIR = Path("/root/obsidian-vault/research/new-research/new-theory-v2/external_data")

class HierarchicalPhaseModel:
    """
    HPM: C_TE / sqrt(C_TT * C_EE) = eta0 * (l/l_star)^(-alpha_eta)
    """
    
    def __init__(self, eta0=2.5, alpha_eta=0.5, l_star=500):
        self.eta0 = eta0
        self.alpha_eta = alpha_eta
        self.l_star = l_star
        
    def hierarchy_ratio(self, l):
        """R_H(l) = C_TE / sqrt(C_TT * C_EE)"""
        return self.eta0 * (l / self.l_star) ** (-self.alpha_eta)
    
    def predict_te(self, l, c_tt, c_ee):
        """Predict C_TE from C_TT and C_EE using HPM"""
        r_h = self.hierarchy_ratio(l)
        return r_h * np.sqrt(c_tt * c_ee)
    
    def chi2(self, params, l_data, c_tt_data, c_ee_data, c_te_data, sigma_te_data):
        """Chi-squared for TE prediction"""
        self.eta0, self.alpha_eta, self.l_star = params
        
        chi2_val = 0.0
        n_dof = 0
        
        for i in range(len(l_data)):
            if sigma_te_data[i] <= 0 or c_tt_data[i] <= 0 or c_ee_data[i] <= 0:
                continue
            
            c_te_pred = self.predict_te(l_data[i], c_tt_data[i], c_ee_data[i])
            chi2_val += ((c_te_data[i] - c_te_pred) / sigma_te_data[i]) ** 2
            n_dof += 1
        
        return chi2_val, max(1, n_dof - 3)
    
    def fit(self, l_data, c_tt_data, c_ee_data, c_te_data, sigma_te_data, 
            initial_guess=(2.5, 0.5, 500)):
        """Fit HPM parameters to data"""
        
        def objective(params):
            chi2_val, _ = self.chi2(params, l_data, c_tt_data, c_ee_data, 
                                      c_te_data, sigma_te_data)
            return chi2_val
        
        bounds = [(1.0, 5.0), (0.0, 1.5), (100, 2000)]
        
        result = minimize(objective, initial_guess, method='L-BFGS-B', bounds=bounds)
        
        self.eta0, self.alpha_eta, self.l_star = result.x
        
        chi2_final, dof = self.chi2(result.x, l_data, c_tt_data, c_ee_data,
                                     c_te_data, sigma_te_data)
        
        return {
            'params': {'eta0': self.eta0, 'alpha_eta': self.alpha_eta, 'l_star': self.l_star},
            'chi2': chi2_final,
            'dof': dof,
            'chi2_dof': chi2_final / dof if dof > 0 else float('inf'),
            'success': result.success
        }


def load_planck_data():
    """Load Planck 2018 data files"""
    planck_dir = DATA_DIR / "planck"
    
    data = {'l': [], 'C_TT': [], 'C_EE': [], 'C_TE': [],
            'sigma_TT': [], 'sigma_EE': [], 'sigma_TE': []}
    
    # Load TT
    with open(planck_dir / "COM_PowerSpect_CMB-TT-full_R3.01.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['l'].append(float(parts[0]))
                data['C_TT'].append(float(parts[1]))
                data['sigma_TT'].append(float(parts[2]))
    
    # Load EE
    with open(planck_dir / "COM_PowerSpect_CMB-EE-full_R3.01.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['C_EE'].append(float(parts[1]))
                data['sigma_EE'].append(float(parts[2]))
    
    # Load TE
    with open(planck_dir / "COM_PowerSpect_CMB-TE-full_R3.01.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['C_TE'].append(float(parts[1]))
                data['sigma_TE'].append(float(parts[2]))
    
    # Convert to numpy arrays
    min_len = min(len(data['l']), len(data['C_EE']), len(data['C_TE']))
    for key in data:
        data[key] = np.array(data[key][:min_len])
    
    return data


def load_wmap_data():
    """Load WMAP 9-year data files"""
    wmap_dir = DATA_DIR / "wmap"
    
    data = {'l': [], 'C_TT': [], 'C_EE': [], 'C_TE': [],
            'sigma_TT': [], 'sigma_EE': [], 'sigma_TE': []}
    
    # Load TT
    with open(wmap_dir / "wmap_tt_spectrum_9yr_v5.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['l'].append(float(parts[0]))
                data['C_TT'].append(float(parts[1]))
                data['sigma_TT'].append(float(parts[2]))
    
    # Load EE
    with open(wmap_dir / "wmap_ee_spectrum_9yr_v5.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['C_EE'].append(float(parts[1]))
                data['sigma_EE'].append(float(parts[2]))
    
    # Load TE
    with open(wmap_dir / "wmap_te_spectrum_9yr_v5.txt", 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                data['C_TE'].append(float(parts[1]))
                data['sigma_TE'].append(float(parts[2]))
    
    # Convert to numpy arrays
    min_len = min(len(data['l']), len(data['C_EE']), len(data['C_TE']))
    for key in data:
        data[key] = np.array(data[key][:min_len])
    
    return data


def compute_hierarchy_ratio(c_te, c_tt, c_ee):
    """Compute R_H = C_TE / sqrt(C_TT * C_EE)"""
    return c_te / np.sqrt(c_tt * c_ee)


def compute_pull(observed, predicted, sigma):
    """Compute pull = (observed - predicted) / sigma"""
    return (observed - predicted) / sigma


if __name__ == "__main__":
    print("HPM Base Module - test loading...")
    planck = load_planck_data()
    wmap = load_wmap_data()
    print(f"Planck: {len(planck['l'])} bins")
    print(f"WMAP: {len(wmap['l'])} bins")
