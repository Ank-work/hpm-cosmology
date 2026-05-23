"""
Test 5: Leave-One-Out Jackknife Prediction
===========================================
Training: Fit to 14/15 ℓ-bins (leave one out)
Prediction: Predict the left-out bin
Repeat: For all 15 bins
Validation: RMS prediction error vs expected scatter
Success: χ²/DOF ≈ 1 for predictions
"""

import numpy as np
import json
from hpm_base import HierarchicalPhaseModel, load_planck_data

def run_leave_one_out_jackknife():
    print("=" * 70)
    print("TEST 5: LEAVE-ONE-OUT JACKKNIFE PREDICTION")
    print("=" * 70)
    
    # Load Planck data
    print("\n[1] Loading Planck 2018 data...")
    data = load_planck_data()
    l = data['l']
    c_tt = data['C_TT']
    c_ee = data['C_EE']
    c_te = data['C_TE']
    sigma_te = data['sigma_TE']
    
    # Select representative ℓ-bins (15 bins spread across range)
    print("\n[2] Selecting 15 representative ℓ-bins...")
    
    # Get 15 bins across the range
    n_bins = 15
    # Ensure we don't exceed array bounds
    max_index = len(l) - 1
    start_index = min(10, max_index // 4)  # Start a bit into the array
    indices = np.linspace(start_index, max_index, n_bins, dtype=int)
    indices = np.clip(indices, 0, max_index)  # Ensure within bounds
    
    print(f"    Selected {len(indices)} bins: ℓ = {l[indices[0]]:.0f} to {l[indices[-1]]:.0f}")
    
    # Jackknife loop
    print("\n[3] Running leave-one-out jackknife...")
    
    predictions = []
    observations = []
    uncertainties = []
    residuals = []
    pulls = []
    
    for i, idx in enumerate(indices):
        l_test = l[idx]
        c_te_obs = c_te[idx]
        sigma_test = sigma_te[idx]
        
        # Training set: all bins except idx
        train_mask = np.ones(len(l), dtype=bool)
        train_mask[idx] = False
        
        l_train = l[train_mask]
        c_tt_train = c_tt[train_mask]
        c_ee_train = c_ee[train_mask]
        c_te_train = c_te[train_mask]
        sigma_te_train = sigma_te[train_mask]
        
        # Fit on training set
        hpm = HierarchicalPhaseModel()
        fit_result = hpm.fit(l_train, c_tt_train, c_ee_train, c_te_train, sigma_te_train)
        
        # Predict on left-out bin
        c_te_pred = hpm.predict_te(np.array([l_test]), 
                                   np.array([c_tt[idx]]), 
                                   np.array([c_ee[idx]]))
        
        # Store results
        predictions.append(c_te_pred[0])
        observations.append(c_te_obs)
        uncertainties.append(sigma_test)
        
        residual = c_te_obs - c_te_pred[0]
        residuals.append(residual)
        
        pull = residual / sigma_test if sigma_test > 0 else 0
        pulls.append(pull)
        
        if (i + 1) % 5 == 0:
            print(f"    Completed {i+1}/{n_bins} jackknife iterations")
    
    # Analyze results
    print("\n[4] Analyzing prediction accuracy...")
    
    predictions = np.array(predictions)
    observations = np.array(observations)
    uncertainties = np.array(uncertainties)
    residuals = np.array(residuals)
    pulls = np.array(pulls)
    
    # RMS prediction error
    rms_error = np.sqrt(np.mean(residuals**2))
    rms_expected = np.sqrt(np.mean(uncertainties**2))
    
    # Chi2 for predictions
    chi2 = np.sum((residuals / uncertainties)**2)
    chi2_dof = chi2 / n_bins
    
    print(f"    RMS prediction error: {rms_error:.3f}")
    print(f"    Expected scatter: {rms_expected:.3f}")
    print(f"    Prediction χ²: {chi2:.2f}")
    print(f"    χ²/DOF: {chi2_dof:.3f}")
    print(f"    Mean pull: {np.mean(pulls):.3f}")
    print(f"    Pull std: {np.std(pulls):.3f}")
    
    # Check individual predictions
    within_1sigma = np.sum(np.abs(pulls) < 1) / n_bins
    within_2sigma = np.sum(np.abs(pulls) < 2) / n_bins
    
    print(f"    Predictions within 1σ: {within_1sigma*100:.1f}%")
    print(f"    Predictions within 2σ: {within_2sigma*100:.1f}%")
    
    # Step 5: Pass/Fail criteria
    chi2_ok = 0.5 < chi2_dof < 2.0  # χ²/DOF ≈ 1
    pulls_ok = np.abs(np.mean(pulls)) < 0.5 and 0.7 < np.std(pulls) < 1.3
    
    passed = chi2_ok and pulls_ok
    
    print(f"\n[5] PASS/FAIL CRITERIA (χ²/DOF ≈ 1):")
    print(f"    0.5 < χ²/DOF < 2.0: {chi2_dof:.3f} {'✅ PASS' if chi2_ok else '❌ FAIL'}")
    print(f"    Pull distribution OK: {'✅ PASS' if pulls_ok else '❌ FAIL'}")
    print(f"\n    OVERALL: {'✅ PASSED' if passed else '❌ FAILED'}")
    
    results = {
        'test_name': 'Leave-One-Out Jackknife Prediction',
        'test_id': 5,
        'status': 'PASSED' if passed else 'FAILED',
        'n_bins': n_bins,
        'rms_prediction_error': float(rms_error),
        'rms_expected': float(rms_expected),
        'chi2': float(chi2),
        'chi2_dof': float(chi2_dof),
        'chi2_ok': chi2_ok,
        'pulls': {
            'mean': float(np.mean(pulls)),
            'std': float(np.std(pulls)),
            'within_1sigma': float(within_1sigma),
            'within_2sigma': float(within_2sigma),
            'ok': pulls_ok
        },
        'individual_predictions': [
            {
                'ell': float(l[indices[i]]),
                'predicted': float(predictions[i]),
                'observed': float(observations[i]),
                'sigma': float(uncertainties[i]),
                'pull': float(pulls[i])
            }
            for i in range(n_bins)
        ],
        'criteria': {
            'chi2_ok': chi2_ok,
            'pulls_ok': pulls_ok
        }
    }
    
    return results


if __name__ == "__main__":
    results = run_leave_one_out_jackknife()
    
    # Save results
    with open('test5_leave_one_out_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "=" * 70)
    print("Results saved to: test5_leave_one_out_results.json")
    print("=" * 70)
