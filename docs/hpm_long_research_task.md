# HPM Deep Research Task - Corrected Report
**Status:** PARTIAL (corrected)  
**Date:** 2026-05-24  

## Executive Summary

Systematic investigation of HPM axiom candidates. **Only Theory 4 survived scrutiny.**

---

## Success Points Retained ✅

1. **[CONSENSUS]** Real-data-only validation using ACT DR6 spectra
2. **[Definition]** TE hierarchy: R_TE(ℓ) = |C_TE(ℓ)|/√(C_TT(ℓ)C_EE(ℓ)), η(ℓ) = R_TE(ℓ)/2
3. **[CONSENSUS]** Train/test split: ℓ=[593,2000] train, ℓ=(2000,8319] test
4. **[HYPOTHESIS→ACCEPTED]** Two-branch power-law: η₀≈0.144, ℓ_br≈1244, test RMSE≈0.203

---

## Theory Testing Results

### ✅ Theory 4: Alternative Functional Forms (SURVIVED)
**Tested 5 functional forms on real ACT data:**

| Axiom | Test RMSE | Status |
|-------|-----------|--------|
| Power law | 0.218 | ACCEPT (baseline) |
| **Broken power (two-branch)** | **0.203** | **BEST** |
| Log-normal decay | 0.220 | ACCEPT |
| Damped power law | 0.220 | ACCEPT |
| Oscillatory envelope | 0.221 | MARGINAL |

**Verdict:** Valid comparison. Two-branch power law remains the best envelope.

---

### ❌ REMOVED Theories (Found Incorrect)

**Theory 1: Thomson Scattering Normalization** — REMOVED
- Error: Misapplied single-scattering theory to CMB correlation coefficient
- η₀ = √3/4 ≈ 0.433 does not predict the observable η(ℓ) = |C_TE|/(2√(C_TT C_EE))
- **Deleted from GitHub**

**Theory 2: Covariance Structure** — REMOVED  
- Error: High residual correlation (0.85) reflects model misspecification, not purely statistical effect
- Over-interpreted as covariance issue when simpler explanation exists
- **Deleted from GitHub**

**Theory 3: Acoustic Oscillation Residuals** — REMOVED
- Error: Fitting approach hit bounds, RMSE huge, methodologically flawed
- **Deleted from GitHub**

---

## Clean HPM Status

### What Remains
- **HPM v4 envelope**: Two-branch power law (η₀≈0.144, ℓ_br≈1244)
- **Real-data validation**: Train/test split predictive RMSE ≈ 0.203
- **Honest acknowledgment**: χ²/dof ≈ 6.54 — acknowledged as model/statistics issue, not "proven"

### What Was Abandoned
- Theory-predicted η₀ normalization
- Covariance/correlation claims
- Acoustic oscillation modeling

---

## Clean File Manifest

**Kept:**
- `theory_04_alternative_axioms.py` — valid functional form comparison
- `docs/hpm_long_research_task.md` — this corrected report
- `docs/hpm_task_state.json` — tracking

**Deleted:**
- `theory_01_normalization_investigation.py`
- `theory_02_covariance_structure.py`  
- `theory_03_acoustic_structure.py`

---

## Conclusion

**HPM v4 stands as a repaired, critique-addressed model.** The theory testing was useful for validation but only one theory survived. The core repair (real-data TE hierarchy, predictive envelope) is solid and unpolluted.
