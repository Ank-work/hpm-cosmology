"""
Test 6: High-ℓ Extrapolation Test
=================================
Training: Fit to ℓ = 593-2000 (ACT range)
Prediction: Extrapolate to ℓ = 2000-8319
Validation: Test if model correctly predicts damping behavior
Success: Reduced χ² < 2 for extrapolated region

Note: This tests the model's ability to extrapolate beyond the fitted range,
a strong test of whether the power-law form is correct.
"""

import numpy as np
import json
from hpm_base import HierarchicalPhaseModel, load_planck_data

def run_high_ell_extrapolation():
    print("=" * 70)
    print("TEST 6: HIGH-ℓ EXTRAPOLATION TEST")
    print("=" * 70)
    print("\nTraining on ℓ = 593-2000, extrapolating to ℓ > 2000")
    
    # Load Planck data
    print("\n[1] Loading Planck 2018 data...")
    data = load_planck_data()
    l = data['l']
    c_tt = data['C_TT']
    c_ee = data['C_EE']
    c_te = data['C_TE']
    sigma_te = data['sigma_TE']
    
    print(f"    Total data: {len(l)} bins")
    
    # Split into training and extrapolation regions
    # Training: ℓ = 593-2000 (ACT-like range)
    # Test: ℓ = 2000-8319 (high-ℓ extrapolation)
    train_mask = (l >= 593) & (l <= 2000)
    test_mask = (l > 2000) & (l <= 8319)
    
    # Adjust masks based on actual data availability
    if not np.any(test_mask):
        # No high-ℓ data, use upper third as extrapolation region
        n_train = int(0.6 * len(l))
        train_mask = np.zeros(len(l), dtype=bool)
        train_mask[:n_train] = True
        test_mask = ~train_mask
        
        print(f"    Using data-based split: {np.sum(train_mask)} train, {np.sum(test_mask)} test")
    
    l_train = l[train_mask]
    c_tt_train = c_tt[train_mask]
    c_ee_train = c_ee[train_mask]
    c_te_train = c_te[train_mask]
    sigma_te_train = sigma_te[train_mask]
    
    l_test = l[test_mask]
    c_tt_test = c_tt[test_mask]
    c_ee_test = c_ee[test_mask]
    c_te_test = c_te[test_mask]
    sigma_te_test = sigma_te[test_mask]
    
    print(f"    Training region: ℓ = {l_train.min():.0f}-{l_train.max():.0f} ({len(l_train)} bins)")
    print(f"    Extrapolation region: ℓ = {l_test.min():.0f}-{l_test.max():.0f} ({len(l_test)} bins)")
    
    # Step 1: Fit on training data
    print("\n[2] Fitting HPM on training region (ℓ ≤ 2000)...")
    hpm = HierarchicalPhaseModel()
    fit_result = hpm.fit(l_train, c_tt_train, c_ee_train, c_te_train, sigma_te_train)
    
    print(f"    Fit parameters:")
    print(f"    η₀ = {fit_result['params']['eta0']:.3f}")
    print(f"    α_η = {fit_result['params']['alpha_eta']:.3f}")
    print(f"    ℓ_* = {fit_result['params']['l_star']:.0f}")
    print(f"    Training χ²/DOF = {fit_result['chi2_dof']:.3f}")
    
    # Step 2: Extrapolate to high-ℓ
    print("\n[3] Extrapolating to high-ℓ region...")
    
    c_te_pred = hpm.predict_te(l_test, c_tt_test, c_ee_test)
    
    # Compute extrapolation errors
    residuals = c_te_test - c_te_pred
    
    # Chi2 for extrapolated region
    chi2 = 0
    n_used = 0
    for i in range(len(l_test)):
        if sigma_te_test[i] > 0:
            chi2 += (residuals[i] / sigma_te_test[i]) ** 2
            n_used += 1
    
    dof = n_used  # No parameter penalty since we didn't fit here
    chi2_dof = chi2 / dof if dof > 0 else float('inf')
    
    print(f"    Extrapolation χ² = {chi2:.2f}")
    print(f"    Extrapolation χ²/DOF = {chi2_dof:.3f}")
    print(f"    Mean residual: {np.mean(residuals):.2f}")
    print(f"    RMS residual: {np.sqrt(np.mean(residuals**2)):.2f}")
    
    # Check for systematic trends (should be flat if extrapolation works)
    # Fit a linear trend to residuals
    if len(l_test) > 5:
        trend = np.polyfit(l_test, residuals, 1)
        trend_slope = trend[0]
        print(f"    Linear trend in residuals: {trend_slope:.4e}")
    else:
        trend_slope = 0
    
    # Step 3: Compare extrapolation quality
    print("\n[4] Comparing training vs extrapolation fit quality...")
    
    # If extrapolation works, chi2/dof should be similar to training
    chi2_ratio = chi2_dof / fit_result['chi2_dof'] if fit_result['chi2_dof'] > 0 else 1
    
    print(f"    Training χ²/DOF: {fit_result['chi2_dof']:.3f}")
    print(f"    Extrapolation χ²/DOF: {chi2_dof:.3f}")
    print(f"    Ratio: {chi2_ratio:.2f}")
    
    # Step 5: Pass/Fail criteria
    # Reduced χ² should be reasonable (not perfect, but < 2)
    chi2_ok = chi2_dof < 2.0
    
    # Check that trend is small (no systematic drift)
    trend_ok = abs(trend_slope) < 1.0 if len(l_test) > 5 else True
    
    passed = chi2_ok and trend_ok
    
    print(f"\n[5] PASS/FAIL CRITERIA:")
    print(f"    χ²/DOF < 2.0: {chi2_dof:.3f} {'✅ PASS' if chi2_ok else '❌ FAIL'}")
    if len(l_test) > 5:
        print(f"    No systematic trend: {trend_slope:.2e} {'✅ PASS' if trend_ok else '❌ FAIL'}")
    print(f"\n    OVERALL: {'✅ PASSED' if passed else '❌ FAILED'}")
    
    results = {
        'test_name': 'High-ℓ Extrapolation Test',
        'test_id': 6,
        'status': 'PASSED' if passed else 'FAILED',
        'training_region': {
            'ell_min': float(l_train.min()),
            'ell_max': float(l_train.max()),
            'n_bins': int(len(l_train)),
            'chi2_dof': float(fit_result['chi2_dof'])
        },
        'extrapolation_region': {
            'ell_min': float(l_test.min()),
            'ell_max': float(l_test.max()),
            'n_bins': int(len(l_test)),
            'chi2': float(chi2),
            'chi2_dof': float(chi2_dof)
        },
        'extrapolation_quality': {
            'mean_residual': float(np.mean(residuals)),
            'rms_residual': float(np.sqrt(np.mean(residuals**2))),
            'trend_slope': float(trend_slope) if len(l_test) > 5 else None,
            'chi2_ratio': float(chi2_ratio)
        },
        'fit_parameters': fit_result['params'],
        'criteria': {
            'chi2_ok': chi2_ok,
            'trend_ok': trend_ok
        }
    }
    
    return results


if __name__ == "__main__":
    results = run_high_ell_extrapolation()
    
    # Save results
    with open('test6_high_ell_extrapolation_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "=" * 70)
    print("Results saved to: test6_high_ell_extrapolation_results.json")
    print("=" * 70)
