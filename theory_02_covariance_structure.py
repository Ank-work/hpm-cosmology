#!/usr/bin/env python3
"""
Theory 2: Missing covariance / bandpower likelihood structure
[HYPOTHESIS] Chi2 remains large because we assume diagonal errors,
but ratio statistics have correlated errors due to shared C_TT, C_EE denominators.
"""

import numpy as np
import json

base = '/root/obsidian-vault/research/new-research/data/binning_20/combined'
TT = np.loadtxt(base + '/fg_subtracted_TT.dat')
EE = np.loadtxt(base + '/fg_subtracted_EE.dat')
TE = np.loadtxt(base + '/fg_subtracted_TE.dat')

ell = TT[:, 0]
Dl_TT = TT[:, 1]
Dl_EE = EE[:, 1]
Dl_TE = TE[:, 1]
sig_TE = TE[:, 2]

A = np.sqrt(Dl_TT * Dl_EE)
mask = (Dl_TT > 0) & (Dl_EE > 0) & (A > 0) & np.isfinite(Dl_TE) & (sig_TE > 0)

# Extract eta
R_TE = np.full_like(ell, np.nan)
R_TE[mask] = np.abs(Dl_TE[mask]) / A[mask]
eta = R_TE / 2.0

# Train/test split
train = mask & (ell >= 593) & (ell <= 2000)
test = mask & (ell > 2000) & (ell <= 8319)

ell_tr = ell[train]
eta_tr = eta[train]

# Estimate correlation structure in train set
# Fit simple power law
ell_star = 500.0
log_l_tr = np.log(ell_tr / ell_star)
log_eta_tr = np.log(eta_tr[np.isfinite(eta_tr) & (eta_tr > 0)])
valid = np.isfinite(log_eta_tr)
coeffs = np.polyfit(log_l_tr[valid], log_eta_tr, 1)
eta_pred = np.exp(coeffs[1]) * (ell / ell_star) ** coeffs[0]

# Residuals on train
residuals = eta - eta_pred
res_tr = residuals[train]
res_tr = res_tr[np.isfinite(res_tr)]

# Lag-1 autocorrelation
if len(res_tr) > 10:
    lag1_corr = np.corrcoef(res_tr[:-1], res_tr[1:])[0, 1]
else:
    lag1_corr = 0

# Variance inflation needed
var_inflation = np.var(res_tr) / np.mean((sig_TE[train][np.isfinite(sig_TE[train])])**2) if np.any(np.isfinite(sig_TE[train])) else 1.0

results = {
    "theory": "Diagonal chi2 underestimates uncertainty for ratio statistics",
    "lag1_residual_correlation": float(lag1_corr),
    "variance_inflation_factor": float(var_inflation),
    "status": "CONFIRMED" if abs(lag1_corr) > 0.2 else "UNCLEAR",
    "implication": "Need covariance matrix or inflated uncertainties"
}

print(json.dumps(results, indent=2))
