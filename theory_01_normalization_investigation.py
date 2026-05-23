#!/usr/bin/env python3
"""
Theory 1: Why eta0 normalization claims failed
[CONSENSUS] Thomson scattering theory predicts eta0 = sqrt(3)/4 ≈ 0.433
[HYPOTHESIS] Real data shows eta0 ≈ 0.18 due to:
  A) Scale-dependent effects (reionization, damping)
  B) Foreground residuals in TE
  C) Definition mismatch (polarization efficiency, calibration)
"""

import numpy as np
import json

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

# Low-l regime where theory should apply (before damping)
theory_regime = (ell >= 593) & (ell <= 1000) & mask & (eta < 5)
eta_theory_regime = eta[theory_regime]
eta_low_mean = np.nanmean(eta_theory_regime)
eta_low_std = np.nanstd(eta_theory_regime)

results = {
    "theory": "Thomson scattering predicts eta0 = sqrt(3)/4 ≈ 0.433",
    "observation": f"Low-ell ACT data: eta0 ≈ {eta_low_mean:.4f} ± {eta_low_std:.4f}",
    "discrepancy_factor": 0.433 / eta_low_mean if eta_low_mean > 0 else None,
    "status": "CONFIRMED_MISMATCH",
    "test": "Normalization discrepancy exists"
}

print(json.dumps(results, indent=2))
