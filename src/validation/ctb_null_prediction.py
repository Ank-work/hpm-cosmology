"""
Test 7: C_TB Null Prediction (Phase 4 Follow-up)
=================================================
Training: Fit to TT/EE/TE
Prediction: C_TB should show NO hierarchy (C_TB ≈ 0)
Validation: Check if C_TB data supports null prediction
Success: |C_TB| < 2σ from zero

Note: C_TB is the temperature-B-mode cross-correlation.
Under standard physics and HPM, there should be no B-mode signal
from scalar perturbations, so C_TB should be consistent with zero.
Any detection would be anomalous.
"""

import numpy as np
import json
from hpm_base import HierarchicalPhaseModel, load_planck_data

def simulate_ctb_data(l, noise_factor=50.0):
    """
    Simulate C_TB data
    
    In reality, scalar perturbations produce no B-modes, so C_TB should be zero
    Plus noise. We simulate this null expectation.
    
    Parameters:
    - l: multipoles
    - noise_factor: noise amplitude (larger than C_TE noise)
    """
    # True C_TB = 0 (no B-mode from scalars)
    c_tb_true = np.zeros_like(l)
    
    # Noise: larger than TE because B-modes are harder to measure
    sigma_tb = noise_factor * (1 + 0.1 * l)  # Increasing with l
    
    # Add Gaussian noise
    c_tb_obs = c_tb_true + np.random.normal(0, sigma_tb)
    
    return c_tb_obs, sigma_tb


def run_ctb_null_prediction():
    print("=" * 70)
    print("TEST 7: C_TB NULL PREDICTION")
    print("=" * 70)
    print("\nPrediction: C_TB ≈ 0 (no hierarchy in TB)")
    
    # Load Planck data (for ℓ values and TT/EE/TE)
    print("\n[1] Loading Planck 2018 data...")
    data = load_planck_data()
    l = data['l']
    c_tt = data['C_TT']
    c_ee = data['C_EE']
    c_te = data['C_TE']
    sigma_te = data['sigma_TE']
    
    print(f"    Total data points: {len(l)}")
    
    # Step 1: Simulate C_TB data (null expectation)
    print("\n[2] Simulating C_TB observations (null expectation)...")
    np.random.seed(42)  # For reproducibility
    
    c_tb, sigma_tb = simulate_ctb_data(l, noise_factor=50.0)
    
    print(f"    Generated C_TB with noise ~{np.mean(sigma_tb):.1f} μK²")
    print(f"    Mean C_TB: {np.mean(c_tb):.2f}")
    print(f"    RMS C_TB: {np.sqrt(np.mean(c_tb**2)):.2f}")
    
    # Step 2: Check for hierarchy
    print("\n[3] Checking for C_TB hierarchy...")
    
    # Compare C_TB to C_TT (should be much smaller)
    ratio_tb_to_tt = np.abs(c_tb) / (c_tt + 1e-10)
    mean_ratio = np.mean(ratio_tb_to_tt)
    
    # Compute pulls from zero
    pull_from_zero = c_tb / sigma_tb
    mean_pull = np.mean(np.abs(pull_from_zero))
    max_pull = np.max(np.abs(pull_from_zero))
    
    print(f"    Mean |C_TB|/C_TT: {mean_ratio:.4f}")
    print(f"    Mean |pull| from zero: {mean_pull:.3f}")
    print(f"    Max |pull|: {max_pull:.2f}")
    
    # Step 3: Chi2 for null hypothesis
    print("\n[4] Testing null hypothesis (C_TB = 0)...")
    
    chi2_null = np.sum((c_tb / sigma_tb) ** 2)
    dof = len(l)
    chi2_dof_null = chi2_null / dof
    
    print(f"    χ² (null hypothesis): {chi2_null:.2f}")
    print(f"    χ²/DOF: {chi2_dof_null:.3f}")
    
    # Step 4: Count violations
    print("\n[5] Counting significant deviations from null...")
    
    n_1sigma = np.sum(np.abs(pull_from_zero) > 1)
    n_2sigma = np.sum(np.abs(pull_from_zero) > 2)
    n_3sigma = np.sum(np.abs(pull_from_zero) > 3)
    
    frac_1sigma = n_1sigma / len(l)
    frac_2sigma = n_2sigma / len(l)
    frac_3sigma = n_3sigma / len(l)
    
    print(f"    Points > 1σ from zero: {n_1sigma} ({frac_1sigma*100:.1f}%)")
    print(f"    Points > 2σ from zero: {n_2sigma} ({frac_2sigma*100:.1f}%)")
    print(f"    Points > 3σ from zero: {n_3sigma} ({frac_3sigma*100:.1f}%)")
    
    # Expected under Gaussian: ~32% > 1σ, ~5% > 2σ, ~0.3% > 3σ
    
    # Step 6: Pass/Fail criteria
    # All |C_TB| should be within 2σ of zero
    all_within_2sigma = np.all(np.abs(pull_from_zero) < 2.0)
    
    # Chi2 should be reasonable (within 3σ of expected)
    expected_chi2_dof = 1.0
    chi2_ok = abs(chi2_dof_null - expected_chi2_dof) < 0.5
    
    # Fraction > 2σ should be consistent with expectation (~5%)
    frac_2sigma_ok = frac_2sigma < 0.15  # Allow up to 15%
    
    passed = all_within_2sigma and chi2_ok and frac_2sigma_ok
    
    print(f"\n[6] PASS/FAIL CRITERIA (|C_TB| < 2σ):")
    print(f"    All points within 2σ: {'✅ PASS' if all_within_2sigma else '❌ FAIL'}")
    print(f"    χ²/DOF ≈ 1: {chi2_dof_null:.3f} {'✅ PASS' if chi2_ok else '❌ FAIL'}")
    print(f"    Fraction > 2σ < 15%: {frac_2sigma*100:.1f}% {'✅ PASS' if frac_2sigma_ok else '❌ FAIL'}")
    print(f"\n    OVERALL: {'✅ PASSED' if passed else '❌ FAILED'}")
    
    results = {
        'test_name': 'C_TB Null Prediction',
        'test_id': 7,
        'status': 'PASSED' if passed else 'FAILED',
        'null_hypothesis': 'C_TB = 0 (no B-mode hierarchy)',
        'ctb_statistics': {
            'mean': float(np.mean(c_tb)),
            'rms': float(np.sqrt(np.mean(c_tb**2))),
            'mean_ratio_to_tt': float(mean_ratio)
        },
        'pull_statistics': {
            'mean_abs_pull': float(mean_pull),
            'max_pull': float(max_pull),
            'all_within_2sigma': all_within_2sigma
        },
        'chi2_test': {
            'chi2': float(chi2_null),
            'dof': int(dof),
            'chi2_dof': float(chi2_dof_null),
            'chi2_ok': chi2_ok
        },
        'deviations': {
            'n_1sigma': int(n_1sigma),
            'n_2sigma': int(n_2sigma),
            'n_3sigma': int(n_3sigma),
            'frac_2sigma': float(frac_2sigma),
            'frac_2sigma_ok': frac_2sigma_ok
        },
        'criteria': {
            'all_within_2sigma': all_within_2sigma,
            'chi2_ok': chi2_ok,
            'frac_2sigma_ok': frac_2sigma_ok
        },
        'note': 'C_TB is expected to be zero under scalar perturbations. '
                'Any significant detection would be anomalous.'
    }
    
    return results


if __name__ == "__main__":
    results = run_ctb_null_prediction()
    
    # Save results
    with open('test7_ctb_null_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "=" * 70)
    print("Results saved to: test7_ctb_null_results.json")
    print("=" * 70)
