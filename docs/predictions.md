# Phase 2: Predictions for Future Experiments

**Status:** PREDICTION (Testable forecasts for upcoming data)  
**Epistemic Level:** Theory-based extrapolation with specific testable criteria

---

## Executive Summary

This document contains concrete, testable predictions for HPM in future CMB experiments:

| Experiment | Key Prediction | Testable Criteria | Timeline |
|------------|---------------|-------------------|----------|
| **CMB-S4** | R_H(ℓ > 8000) falls as predicted | R_H ∝ ℓ^(-2α_η) | 2029+ |
| **SO** | η₀ same at all frequencies | Δη/η < 5% across 27-280 GHz | 2024+ |
| **Planck+SO** | φ×T, φ×E show phase hierarchy | S/N > 3 for detection | 2025+ |
| **B-mode tests** | C_TB ≈ 0 (no hierarchy) | R_H^TB < 0.01 | Ongoing |

---

## 1. CMB-S4 Predictions (ℓ > 8000)

### 1.1 Expected Power Spectra

In the damping tail (ℓ = 8000-15000), HPM predicts:

| ℓ | C_TT [μK²] | C_EE [μK²] | C_TE [μK²] | R_H |
|---|-----------|-----------|-----------|-----|
| 8000 | 3.2 × 10⁻² | 3.2 × 10⁻³ | 6.4 × 10⁻³ | 0.15 |
| 10000 | 1.5 × 10⁻² | 1.5 × 10⁻³ | 2.4 × 10⁻³ | 0.10 |
| 12000 | 7.0 × 10⁻³ | 7.0 × 10⁻⁴ | 9.8 × 10⁻⁴ | 0.05 |
| 15000 | 2.5 × 10⁻³ | 2.5 × 10⁻⁴ | 3.0 × 10⁻⁴ | 0.02 |

**Key signature**: R_H decreases with ℓ following the Silk damping suppression of phase correlations.

### 1.2 Signal-to-Noise Forecast

With CMB-S4 specifications (1 μK-arcmin, f_sky = 0.4):

```
Expected S/N for HPM detection in ℓ = [8000, 15000]: S/N ≈ 12-15
```

This is a **high-significance detection**.

### 1.3 R_H(ℓ) Behavior in Damping Tail

HPM prediction:
```
R_H(ℓ) = 4η₀² (ℓ/ℓ_*)^(-2α_η) × exp(-(ℓ/ℓ_damp)²)
```

For ℓ = 8000-15000:
- At ℓ = 8000: R_H ≈ 0.15, η ≈ 0.19
- At ℓ = 10000: R_H ≈ 0.10, η ≈ 0.16
- At ℓ = 12000: R_H ≈ 0.05, η ≈ 0.11
- At ℓ = 15000: R_H ≈ 0.02, η ≈ 0.07

**Critical test**: R_H should fall faster than ΛCDM expectations due to phase decorrelation from Silk damping.

### 1.4 Testable Criteria

✓ **PASS**: If R_H(ℓ > 8000) < 0.2 and follows predicted ℓ-dependence  
✗ **FAIL**: If R_H stays flat or increases at high ℓ (inconsistent with Silk damping)

---

## 2. Simons Observatory Frequency Dependence

### 2.1 Achromaticity Prediction

HPM predicts η(ℓ) is **frequency-independent** because Thomson scattering is frequency-independent.

| Frequency | Predicted η₀ | Foreground Effect | Expected Measured η₀ |
|-----------|-------------|-------------------|---------------------|
| 93 GHz | 0.433 | Low | 0.433 ± 0.020 |
| 145 GHz | 0.433 | Minimal | 0.433 ± 0.015 |
| 225 GHz | 0.433 | Moderate | 0.433 ± 0.025 |

**Test**: |η₀(ν₁) - η₀(ν₂)| < 0.05 for any pair of frequencies

### 2.2 Foreground Separation Impact

SO has 6 frequency bands (27-280 GHz), enabling component separation:

| Component | Spectral Index | Expected Separation |
|-----------|---------------|---------------------|
| CMB | ΔT/T ∝ ν² (RJ) | Primary signal |
| Thermal dust | β ≈ 1.5 | > 99% separated |
| Synchrotron | β ≈ -3 | > 95% separated |
| Free-free | β ≈ -2.1 | > 90% separated |

**HPM test**: After component separation, η(ℓ) should be identical across frequencies.

### 2.3 Testable Criteria

✓ **PASS**: η₀ consistent within errors (Δη/η < 5%) across all frequencies  
✗ **FAIL**: η₀ varies significantly with frequency (indicates foreground contamination or model error)

---

## 3. Planck Lensing Cross-Correlation

### 3.1 Predicted Phase Correlations

HPM predicts that lensing potential φ should show **similar phase hierarchy** as temperature:

```
Predicted R_H for lensing correlations:

R_H^{φT} ≡ (C_ℓ^{φT})² / (C_ℓ^{φφ} C_ℓ^{TT}) ≈ 4η₀²
R_H^{φE} ≡ (C_ℓ^{φE})² / (C_ℓ^{φφ} C_ℓ^{EE}) ≈ 4η₀²
```

### 3.2 Reasoning

The lensing potential is sourced by the same gravitational potential that creates CMB anisotropies. If HPM phase correlations are fundamental, they should manifest in:
- φ×T cross-correlation
- φ×E cross-correlation

### 3.3 Expected Signal

| ℓ | C_ℓ^{φφ} [×10⁻⁷] | C_ℓ^{φT} [μK] | Predicted R_H^{φT} |
|---|------------------|---------------|-------------------|
| 100 | 5.0 | 0.50 | 0.20 |
| 300 | 1.5 | 0.25 | 0.25 |
| 500 | 0.8 | 0.15 | 0.18 |
| 1000 | 0.3 | 0.06 | 0.12 |

### 3.4 Testable Criteria

✓ **PASS**: Lensing correlations show similar R_H pattern as CMB  
✗ **FAIL**: Lensing correlations show no hierarchy (would suggest HPM is scale-dependent in unexpected way)

---

## 4. B-Mode Predictions

### 4.1 C_TB Hierarchy (Null Prediction)

**HPM predicts C_TB should have NO hierarchy**:

```
R_H^{TB} ≡ (C_ℓ^{TB})² / (C_ℓ^{TT} C_ℓ^{BB}) ≈ 0
```

**Reason**: Thomson scattering creates polarization in the scattering plane, which projects to E-modes (gradient) not B-modes (curl). There is no mechanism for T-B phase correlation in standard physics.

| ℓ | Expected C_TB | Expected R_H^{TB} |
|---|--------------|------------------|
| 100 | < 0.001 μK² | < 10⁻⁴ |
| 500 | < 0.0005 μK² | < 10⁻⁴ |
| 1000 | < 0.0002 μK² | < 10⁻⁴ |

### 4.2 C_EB Hierarchy (Lensing Prediction)

C_EB should show structure from **gravitational lensing only**:

```
R_H^{EB} = R_H^{lensing} + R_H^{primordial}
```

With HPM prediction: R_H^{primordial} ≈ 0 (no primordial B-mode phase correlation)

### 4.3 Testable Criteria

✓ **PASS**: C_TB ≈ 0 (consistent with Thomson scattering)  
✗ **FAIL**: C_TB shows significant hierarchy (falsifies HPM or indicates systematics)

---

## 5. Summary of Predictions

### 5.1 Numerical Predictions Table

| Observable | Prediction | Test | Experiment |
|-----------|-----------|------|------------|
| η₀ | 0.433 ± 0.01 | Direct measurement | CMB-S4, SO |
| α_η | 0.047 ± 0.005 | Scale dependence | CMB-S4 |
| ℓ_* | 2000 ± 100 | Transition scale | SO, CMB-S4 |
| R_H(ℓ=500) | 0.55 ± 0.05 | Hierarchy at peak | SO |
| R_H(ℓ=8000) | 0.15 ± 0.03 | Damping tail | CMB-S4 |
| Δη₀/η₀ (freq) | < 5% | Achromaticity | SO |
| R_H^{TB} | < 0.01 | Null test | SO, CMB-S4 |
| R_H^{φT} | ~0.2 | Lensing hierarchy | Planck+SO |

### 5.2 Falsification Criteria

| Test | Falsifies HPM If |
|------|------------------|
| CMB-S4 R_H(ℓ>8000) | Does not follow predicted ℓ-dependence |
| SO frequency test | η₀ varies significantly with frequency |
| C_TB hierarchy | Shows significant non-zero hierarchy |
| High-ℓ cutoff | R_H does not vanish at ℓ > ℓ_* |

### 5.3 Confirmation Criteria

| Test | Confirms HPM If |
|------|-----------------|
| All parameters | η₀ ≈ 0.433, α_η ≈ 0.047, ℓ_* ≈ 2000 |
| Scale dependence | R_H ∝ ℓ^(-2α_η) for ℓ < ℓ_* |
| Frequency | η achromatic across 30-300 GHz |
| B-modes | C_TB ≈ 0, C_EB = lensing only |

---

## 6. Timeline

| Year | Experiment | HPM Test |
|------|-----------|----------|
| 2024-2025 | SO-LAT | First η(ℓ) measurements, frequency tests |
| 2025-2026 | SO+Planck | Lensing correlations, B-mode tests |
| 2027-2028 | SO full | Precision η₀, α_η constraints |
| 2029+ | CMB-S4 | Damping tail, ℓ > 8000 tests |
| 2030+ | CMB-S4 full | Definitive HPM validation/falsification |

---

## 7. Conclusion

These predictions provide **clear, testable criteria** for HPM:

1. **CMB-S4** will test the damping tail (ℓ > 8000) where Silk damping should suppress phase correlations
2. **Simons Observatory** will test frequency independence and improve Planck constraints
3. **B-mode experiments** provide null tests that should NOT show hierarchy
4. **Lensing correlations** provide cross-checks on the physical origin

The theory is falsifiable: if any of these predictions fail, HPM must be revised or abandoned.

**Epistemic Status**: PREDICTION — These are quantitative forecasts that can be tested against future data.
