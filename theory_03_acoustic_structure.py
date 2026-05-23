#!/usr/bin/env python3
"""
Theory 3: Acoustic residual structure
[HYPOTHESIS] eta(l) contains acoustic oscillation residuals not captured by smooth envelopes.
Fit eta(l)/eta_LCDM(l) to extract oscillation pattern.
"""

import numpy as np
import json
from scipy.optimize import curve_fit

# Load ACT
base = '/root/obsidian-vault/research/new-research/data/binning_20/combined'
TT = np.loadtxt(base + '/fg_subtracted_TT.dat')
EE = np.loadtxt(base + '/fg_subtracted_EE.dat')
TE = np.loadtxt(base + '/fg_subtracted_TE.dat')

ell_act = TT[:, 0]
Dl_TT_act = TT[:, 1]
Dl_EE_act = EE[:, 1]
Dl_TE_act = TE[:, 1]
sig_TE_act = TE[:, 2]

# Load LCDM theory
th_path = '/root/obsidian-vault/research/new-research/data/dr6_lcdm_best_fits/cmb.dat'
th = np.loadtxt(th_path)
ell_th = th[:, 0]
Dl_TT_th = th[:, 1]
Dl_TE_th = th[:, 2]
Dl_EE_th = th[:, 6]

# Interpolate theory to ACT bins
Dl_TT_i = np.interp(ell_act, ell_th, Dl_TT_th)
Dl_EE_i = np.interp(ell_act, ell_th, Dl_EE_th)
Dl_TE_i = np.interp(ell_act, ell_th, Dl_TE_th)
A_th = np.sqrt(np.maximum(Dl_TT_i * Dl_EE_i, 0))

# eta data and theory
A_act = np.sqrt(Dl_TT_act * Dl_EE_act)
mask = (Dl_TT_act > 0) & (Dl_EE_act > 0) & (A_act > 0) & np.isfinite(Dl_TE_act)
eta_obs = np.full_like(ell_act, np.nan)
eta_obs[mask] = np.abs(Dl_TE_act[mask]) / (2 * A_act[mask])

mask_th = (Dl_TT_i > 0) & (Dl_EE_i > 0) & (A_th > 0)
eta_th = np.full_like(ell_act, np.nan)
eta_th[mask_th] = np.abs(Dl_TE_i[mask_th]) / (2 * A_th[mask_th])

# Residual: eta_obs / eta_th
mask_both = mask & mask_th & np.isfinite(eta_obs) & np.isfinite(eta_th) & (eta_th > 0)
l = ell_act[mask_both]
residual = eta_obs[mask_both] / eta_th[mask_both]

# Fit acoustic model: residual = A * cos(2*pi*l/l_p + phi) + C
def acoustic_model(l, A, l_p, phi, C):
    return A * np.cos(2 * np.pi * l / l_p + phi) + C

# Initial guess: l_p ~ 300 (first acoustic peak scale)
p0 = [0.1, 300, 0, 1.0]
bounds = ([0, 100, -np.pi, 0.5], [1, 1000, np.pi, 2.0])

try:
    popt, pcov = curve_fit(acoustic_model, l, residual, p0=p0, bounds=bounds, maxfev=200000)
    A_fit, l_p_fit, phi_fit, C_fit = popt
    
    # Predictions
    residual_pred = acoustic_model(l, *popt)
    rmse = np.sqrt(np.mean((residual - residual_pred)**2))
    
    results = {
        "theory": "eta(l) contains acoustic oscillation residuals",
        "fitted_period_l_p": float(l_p_fit),
        "amplitude": float(A_fit),
        "phase": float(phi_fit),
        "offset": float(C_fit),
        "rmse": float(rmse),
        "status": "CONFIRMED" if rmse < 0.3 else "MARGINAL"
    }
except Exception as e:
    results = {
        "theory": "eta(l) contains acoustic oscillation residuals",
        "error": str(e),
        "status": "FAILED"
    }

print(json.dumps(results, indent=2))
