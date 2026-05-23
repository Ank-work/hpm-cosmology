#!/usr/bin/env python3
"""
Theory 4: Alternative axiom formulations
Test different functional forms for eta(l) envelope
"""

import numpy as np
import json
from scipy.optimize import curve_fit

# Load ACT
base = '/root/obsidian-vault/research/new-research/data/binning_20/combined'
TT = np.loadtxt(base + '/fg_subtracted_TT.dat')
EE = np.loadtxt(base + '/fg_subtracted_EE.dat')
TE = np.loadtxt(base + '/fg_subtracted_TE.dat')

ell = TT[:, 0]
Dl_TT, sig_TT = TT[:, 1], TT[:, 2]
Dl_EE, sig_EE = EE[:, 1], EE[:, 2]
Dl_TE, sig_TE = TE[:, 1], TE[:, 2]

A = np.sqrt(Dl_TT * Dl_EE)
mask = (Dl_TT > 0) & (Dl_EE > 0) & (A > 0) & np.isfinite(Dl_TE)
R_TE = np.full_like(ell, np.nan)
R_TE[mask] = np.abs(Dl_TE[mask]) / A[mask]
eta = R_TE / 2.0

# Outlier cut
mask = mask & np.isfinite(eta) & (eta < 5)

# Train/test
train = mask & (ell >= 593) & (ell <= 2000)
test = mask & (ell > 2000) & (ell <= 8319)

ell_tr, eta_tr = ell[train], eta[train]
ell_te, eta_te = ell[test], eta[test]

ell_star = 500.0

# Axiom candidates
axioms = {}

# 1. Power law (baseline)
def power(l, eta0, alpha):
    return eta0 * (l / ell_star) ** (-alpha)

try:
    popt, _ = curve_fit(power, ell_tr, eta_tr, p0=[0.15, 0.2], 
                        bounds=([0.01, -5], [10, 5]), maxfev=200000)
    pred = power(ell_te, *popt)
    rmse = np.sqrt(np.mean((eta_te - pred)**2))
    axioms['power_law'] = {'params': popt.tolist(), 'rmse': float(rmse)}
except:
    axioms['power_law'] = {'error': 'fit failed'}

# 2. Broken power law (continuous)
def broken_power(l, eta0, alpha1, alpha2, l_br):
    eta1 = eta0 * (l / ell_star) ** (-alpha1)
    eta2 = eta0 * (l_br / ell_star) ** (-alpha1) * (l / l_br) ** (-alpha2)
    return np.where(l <= l_br, eta1, eta2)

try:
    popt, _ = curve_fit(broken_power, ell_tr, eta_tr, p0=[0.15, 0.2, 0.2, 1200],
                        bounds=([0.01, -5, -5, 800], [10, 5, 5, 2500]), maxfev=200000)
    pred = broken_power(ell_te, *popt)
    rmse = np.sqrt(np.mean((eta_te - pred)**2))
    axioms['broken_power'] = {'params': popt.tolist(), 'rmse': float(rmse)}
except:
    axioms['broken_power'] = {'error': 'fit failed'}

# 3. Log-normal decay
def lognormal(l, eta0, mu, sigma):
    x = np.log(l / ell_star)
    return eta0 * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

try:
    popt, _ = curve_fit(lognormal, ell_tr, eta_tr, p0=[0.2, 1, 1],
                        bounds=([0.01, -5, 0.1], [10, 5, 5]), maxfev=200000)
    pred = lognormal(ell_te, *popt)
    rmse = np.sqrt(np.mean((eta_te - pred)**2))
    axioms['lognormal'] = {'params': popt.tolist(), 'rmse': float(rmse)}
except:
    axioms['lognormal'] = {'error': 'fit failed'}

# 4. Damped power law
def damped(l, eta0, alpha, l_damp):
    return eta0 * (l / ell_star) ** (-alpha) * np.exp(-l / l_damp)

try:
    popt, _ = curve_fit(damped, ell_tr, eta_tr, p0=[0.2, 0.2, 5000],
                        bounds=([0.01, -5, 1000], [10, 5, 50000]), maxfev=200000)
    pred = damped(ell_te, *popt)
    rmse = np.sqrt(np.mean((eta_te - pred)**2))
    axioms['damped'] = {'params': popt.tolist(), 'rmse': float(rmse)}
except:
    axioms['damped'] = {'error': 'fit failed'}

# 5. Oscillatory envelope
def oscillatory(l, eta0, alpha, A, period, phi):
    env = eta0 * (l / ell_star) ** (-alpha)
    osc = 1 + A * np.sin(2 * np.pi * l / period + phi)
    return env * osc

try:
    popt, _ = curve_fit(oscillatory, ell_tr, eta_tr, p0=[0.15, 0.2, 0.1, 300, 0],
                        bounds=([0.01, -5, 0, 100, -np.pi], [10, 5, 1, 1000, np.pi]), maxfev=200000)
    pred = oscillatory(ell_te, *popt)
    rmse = np.sqrt(np.mean((eta_te - pred)**2))
    axioms['oscillatory'] = {'params': popt.tolist(), 'rmse': float(rmse)}
except Exception as e:
    axioms['oscillatory'] = {'error': str(e)[:50]}

# Find best
best_axiom = min([(k, v.get('rmse', 1e9)) for k, v in axioms.items()], key=lambda x: x[1])

results = {
    "axioms_tested": len(axioms),
    "results": axioms,
    "best_axiom": best_axiom[0],
    "best_rmse": float(best_axiom[1]),
    "status": "COMPLETE"
}

print(json.dumps(results, indent=2))
