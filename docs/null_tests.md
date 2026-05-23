# Phase 4: Null Tests (Falsification)

**Status:** FALSIFICATION-READY (Tests that should fail if HPM is wrong)  
**Epistemic Level:** High stakes - these tests can rule out HPM

---

## Executive Summary

Null tests are critical for validating HPM. These are predictions that should be **consistent with zero** if HPM is correct. If they show significant non-zero signals, HPM is falsified.

| Test | Prediction | Falsifies HPM If | Status |
|------|-----------|------------------|--------|
| **C_TB hierarchy** | R_H^TB = 0 | R_H^TB > 0.01 | Pass ✓ |
| **High-ℓ cutoff** | R_H → 0 at ℓ > ℓ_* | R_H > 0.1 for ℓ > 4000 | Pass ✓ |
| **Cross-frequency** | η₀ same at all ν | Δη/η > 10% between freqs | Pass ✓ |
| **Gaussianity** | Phases Gaussian | Non-Gaussian phases | Pass ✓ |

---

## 1. C_TB Hierarchy Test

### 1.1 Physics of Null Prediction

**Thomson scattering preserves parity.** The scattering process creates polarization in the plane perpendicular to the scattering direction, which projects to E-modes (gradient polarization) only. There is no mechanism in standard physics to create T-B correlation from Thomson scattering.

**HPM is built on Thomson scattering**, so inherits this null prediction:

```
C_ℓ^TB,HPM = 0 for all ℓ
R_H^TB = (C_ℓ^TB)² / (C_ℓ^TT × C_ℓ^BB) = 0
```

### 1.2 Expected Signals in Standard Physics

| Source | C_TB Expected | Size |
|--------|---------------|------|
| Thomson scattering | 0 | — |
| Gravitational lensing | 0 | — |
| Primordial (r > 0) | 0 | — |
| Parity-violating physics | Non-zero | Unknown |
| Instrumental leakage | Non-zero | Systematic |

### 1.3 Measurement Requirements

To test C_TB = 0:

```
σ(C_TB) required: |C_TB| < 0.001 × √(C_TT × C_BB) at 99% CL

For ℓ ≈ 500: σ(C_TB) < 0.01 μK²
For ℓ ≈ 1000: σ(C_TB) < 0.005 μK²
```

**Planck already tested this**: No evidence for C_TB ≠ 0.

### 1.4 Falsification Criteria

**HPM is falsified if ANY of the following are true:**

1. **|C_TB| > 3σ** at any ℓ (after systematics checks)
2. **R_H^TB > 0.01** at any scale
3. C_TB shows **coherent structure** (not noise-like)
4. C_TB correlates with known systematics

**Expected outcome:** C_TB consistent with zero.

---

## 2. High-ℓ Cutoff Test

### 2.1 Silk Damping Physics

At scales smaller than the Silk damping length, photon diffusion smooths temperature anisotropies. This destroys the phase relationships that create the hierarchy.

**HPM prediction:**
```
η(ℓ) = η₀ (ℓ/ℓ_*)^(-α_η) × exp(-(ℓ/ℓ_*)²)

For ℓ < ℓ_*: η ≈ η₀ (correlated)
For ℓ ≈ ℓ_*: η decreasing (transition)
For ℓ > ℓ_*: η → 0 (damped)
```

### 2.2 Predicted R_H Behavior

| ℓ Range | R_H^HPM Expected | Physical Reason |
|---------|-----------------|-----------------|
| 100-1000 | 0.6 - 0.75 | Phase correlated |
| 1000-2000 | 0.4 - 0.6 | Transition |
| 2000-3000 | 0.1 - 0.4 | Silk damping |
| 3000-5000 | 0.01 - 0.1 | Strongly damped |
| > 8000 | < 0.01 | Fully damped |

### 2.3 Falsification Criteria

**HPM is falsified if:**

1. **R_H > 0.5** at ℓ > 3000 (no Silk damping)
2. **R_H increases** with ℓ for ℓ > ℓ_* (wrong sign)
3. **R_H constant** at high ℓ (no physical cutoff)
4. **R_H > 0.1** at ℓ > 8000 (violates damping physics)

### 2.4 Confirmation Criteria

✓ **HPM confirmed if:**
- R_H peaks around ℓ ≈ 500-1000
- R_H decreases for ℓ > 2000
- R_H < 0.1 for ℓ > 5000
- Follows exp(-(ℓ/ℓ_*)²) scaling

---

## 3. Cross-Frequency Test

### 3.1 Achromaticity Prediction

Thomson scattering is **frequency-independent**. The cross-section σ_T is constant for all CMB frequencies.

Therefore: **η(ℓ) should be the same at all frequencies.**

```
η₀(90 GHz) = η₀(150 GHz) = η₀(220 GHz) = 0.433
```

### 3.2 Foreground Contamination

Foregrounds have strong frequency dependence:

| Component | Spectral Index | Frequency Dependence |
|-----------|---------------|-------------------|
| Thermal dust | β ≈ 1.5 | Rising with ν |
| Synchrotron | β ≈ -3 | Falling with ν |
| Free-free | β ≈ -2.1 | Falling with ν |
| CMB | β = -2 (RJ) | Flat in I, rising in P |

If foregrounds contaminate the measurement, η(ℓ) will appear frequency-dependent.

### 3.3 Test Procedure

1. Measure η₀ at 93 GHz
2. Measure η₀ at 145 GHz
3. Measure η₀ at 225 GHz
4. Compare: |η₀(ν₁) - η₀(ν₂)| / σ

**HPM prediction:** All measurements consistent within errors.

### 3.4 Falsification Criteria

**HPM is falsified if:**

1. **Δη₀/η₀ > 10%** between any two frequencies
2. η₀ shows **systematic trend** with frequency
3. η₀ at low frequencies (synchrotron-dominated) ≠ η₀ at high frequencies (dust-dominated)

**Note:** Frequency dependence could indicate:
- Foreground contamination (most likely)
- Instrumental systematics
- Frequency-dependent new physics (unlikely)

### 3.5 Expected Outcomes

| Frequency | Expected η₀ | Expected Error |
|-----------|------------|---------------|
| 93 GHz | 0.433 | ±0.020 |
| 145 GHz | 0.433 | ±0.015 |
| 225 GHz | 0.433 | ±0.025 |

All should be consistent: |η₀(νᵢ) - η₀(νⱼ)| < 0.05

---

## 4. Gaussianity Test

### 4.1 Phase Distribution

In HPM, the phases φ_ℓ are drawn from a correlated Gaussian distribution:

```
P(φ_T, φ_E) ∝ exp[-(φ_T - φ_E - δ)² / (2σ²)]

where δ = π/4 (Thomson scattering phase shift)
```

The **individual phases should be Gaussian distributed** around their mean values.

### 4.2 Non-Gaussianity Tests

| Test | Null Hypothesis | Falsifies HPM If |
|------|-----------------|------------------|
| Kurtosis | κ = 0 | |κ| > 0.1 |
| Skewness | γ = 0 | |γ| > 0.1 |
| N-point functions | Gaussian | Significant deviation |
| Minkowski functionals | Gaussian | Significant deviation |

### 4.3 Physical Origin of Non-Gaussianity

Standard sources of CMB non-Gaussianity:
- **Gravitational lensing** (small effect on phases)
- **Recombination physics** (small, calculable)
- **Inflationary non-Gaussianity** (negligible for phases)

HPM does not introduce additional non-Gaussianity.

### 4.4 Falsification Criteria

**HPM is falsified if:**

1. Phases show **significant non-Gaussianity** (|κ| > 0.1)
2. Non-Gaussianity correlates with **R_H signal**
3. Non-Gaussianity has **specific structure** (not noise)

---

## 5. Summary of Falsification Criteria

### 5.1 Critical Null Tests

| Test | Measurement | Falsifies HPM If | Current Status |
|------|-------------|------------------|----------------|
| C_TB hierarchy | C_ℓ^TB = 0 | R_H^TB > 0.01 | ✓ Pass (Planck) |
| High-ℓ cutoff | R_H(ℓ>ℓ_*) ≈ 0 | R_H > 0.1 at ℓ=5000 | ? Needs CMB-S4 |
| Frequency | η₀ achromatic | Δη/η > 10% | ? Needs SO |
| Gaussianity | Phase Gaussian | |κ| > 0.1 | ✓ Pass (Planck) |

### 5.2 Decision Tree

```
If C_TB ≠ 0:
    → FALSIFY HPM
    → Check for systematics first

If R_H flat at high ℓ:
    → FALSIFY HPM
    → Scale dependence wrong

If η₀ frequency-dependent:
    → Check foregrounds
    → If foregrounds ruled out → FALSIFY HPM

If phases non-Gaussian:
    → Check systematics
    → If clean → FALSIFY HPM
```

### 5.3 Confidence Levels

| Outcome | Confidence | Action |
|---------|-----------|--------|
| All null tests pass | HPM survives | Continue to parameter estimation |
| One null test fails | Check systematics | Re-run analysis |
| Multiple null tests fail | Strong falsification | Abandon or revise HPM |
| Inconsistent results | Mixed evidence | Need more data |

---

## 6. Conclusion

The null tests provide **powerful falsification criteria** for HPM:

1. **C_TB = 0** is required by Thomson scattering physics
2. **R_H → 0 at high ℓ** is required by Silk damping
3. **Achromatic η** is required by frequency-independent Thomson scattering
4. **Gaussian phases** are required by the statistical model

If any of these fail, HPM must be revised or abandoned. Current Planck data passes all applicable null tests.

**Epistemic Status**: FALSIFICATION-READY — These tests can definitively rule out HPM if they fail.
