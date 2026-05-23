# Hierarchical Phase Model — Mathematical Formalism

## 1. Theoretical Framework

### 1.1 Phase Field Definition

CMB temperature and polarization anisotropies are expanded in spherical harmonics:

$$\frac{\Delta T(\hat{n})}{T_0} = \sum_{\ell m} a_{\ell m}^T Y_{\ell m}(\hat{n})$$

$$(Q \pm iU)(\hat{n}) = \sum_{\ell m} \mp(a_{\ell m}^E \pm i a_{\ell m}^B) \; {}_{\mp}Y_{\ell m}(\hat{n})$$

**Phase variables** (primary HPM observables):
$$\phi_\ell^T = \arg\left(\sum_m a_{\ell m}^T \cdot \text{weight}_m\right)$$
$$\phi_\ell^E = \arg\left(\sum_m a_{\ell m}^E \cdot \text{weight}_m\right)$$

**Note:** For simplified analysis, we use single-phase-per-ℓ approximation (averaged over m).

---

## 2. Phase Coherence Definitions

### 2.1 Coherence Functions

**TT coherence:**
$$C_{TT}(\ell_1, \\ell_2) = \langle e^{i(\phi_{\ell_1}^T - \phi_{\ell_2}^T)} \rangle$$

**EE coherence:**
$$C_{EE}(\ell_1, \ell_2) = \langle e^{i(\phi_{\ell_1}^E - \phi_{\ell_2}^E)} \rangle$$

**TE coherence:**
$$C_{TE}(\ell_1, \ell_2) = \langle e^{i(\phi_{\ell_1}^T - \phi_{\ell_2}^E)} \rangle$$

**Normalization:** For perfectly correlated phases, C = 1. For random phases, C = 0.

### 2.2 Hierarchy Ratio

**Primary HPM diagnostic:**
$$R_H(\ell_1, \ell_2) = \frac{|C_{TE}(\ell_1, \ell_2)|^2}{C_{TT}(\ell_1, \ell_2) \cdot C_{EE}(\ell_1, \ell_2)}$$

**Model predictions:**
- ΛCDM: R_H = 1 (phases uncorrelated)
- EGC: R_H = 1 (by H5 constraint construction)
- HPM: R_H = 4η² ≫ 1 (hierarchical prediction)

---

## 3. Coupled Langevin Dynamics

### 3.1 Stochastic Differential Equations

The phase evolution follows coupled Ornstein-Uhlenbeck processes:

**Temperature phase SDE:**
$$d\phi_\ell^T = -\gamma_\ell \phi_\ell^T dt + \sqrt{2D_T} dW_\ell^T + g_{TE} \sum_{\ell'} K_{\ell\ell'} \phi_{\ell'}^E dt$$

**E-mode phase SDE:**
$$d\phi_\ell^E = -\gamma_\ell \phi_\ell^E dt + \sqrt{2D_E} dW_\ell^E + g_{TE} \sum_{\ell'} K_{\ell\ell'} \phi_{\ell'}^T dt$$

where:
- γ_ℓ = decoherence rate
- D_T, D_E = diffusion coefficients
- W_ℓ^T, W_ℓ^E = independent Wiener processes
- K_{ℓℓ'} = coupling kernel (typically K_{ℓℓ'} ∝ exp(-|ℓ-ℓ'|²/2Δ²))
- g_TE = hierarchical coupling constant

### 3.2 Steady-State Solution

For ℓ₁ ≈ ℓ₂ = ℓ (nearby multipoles), the stationary covariances are:

$$\langle (\phi_\ell^T)^2 \rangle = \frac{D_T}{\gamma_\ell} \cdot \frac{1}{1 - \lambda^2}$$
$$\langle (\phi_\ell^E)^2 \rangle = \frac{D_E}{\gamma_\ell} \cdot \frac{1}{1 - \lambda^2}$$
$$\langle \phi_\ell^T \phi_\ell^E \rangle = \frac{\sqrt{D_T D_E}}{\gamma_\ell} \cdot \frac{\lambda}{1 - \lambda^2}$$

where λ = g_TE/(γ_ℓ + g_TE) is the effective coupling parameter.

### 3.3 Phase Coherence from Gaussian Distribution

Assuming Gaussian phase distributions (valid for small decoherence):

$$C_{TT} = \exp\left(-\frac{1}{2}\langle (\phi_{\ell_1}^T - \phi_{\ell_2}^T)^2 \rangle\right)$$

For ℓ₁ ≈ ℓ₂:
$$C_{TT}(\ell) \approx \exp\left(-\frac{D_T/\gamma_\ell}{1 - \lambda^2}\right)$$
$$C_{TE}(\ell) \approx \exp\left(-\frac{\sqrt{D_T D_E}/\gamma_\ell}{1 - \lambda^2}\right) \cdot \lambda$$

---

## 4. Hierarchy Derivation

### 4.1 Key Approximation

For strong hierarchical coupling (g_TE ≫ γ_ℓ):
$$\lambda = \frac{g_{TE}}{\gamma_\ell + g_{TE}} \approx 1 - \frac{\gamma_\ell}{g_{TE}}$$

### 4.2 Coherence Expressions

**Self-coherences (TT, EE):**
$$C_{TT} \approx \exp\left(-\frac{D_T}{\gamma_\ell} \cdot \frac{g_{TE}^2}{\gamma_\ell^2}\right) = \exp\left(-\frac{D_T g_{TE}^2}{\gamma_\ell^3}\right)$$

With small argument expansion:
$$C_{TT} \approx \frac{D_T}{\gamma_\ell} \cdot \frac{1}{\eta^2} \ll 1$$

**Cross-coherence (TE):**
$$C_{TE} \approx \frac{\sqrt{D_T D_E}}{g_{TE} \cdot \chi} \cdot g_{TE} = \frac{\sqrt{D_T D_E}}{\chi}$$

where χ is the susceptibility factor.

### 4.3 Hierarchy Ratio Result

$$R_H = \frac{|C_{TE}|^2}{C_{TT} \cdot C_{EE}} = \frac{(D_T D_E/\chi^2)}{(D_T/\gamma_\ell \eta^2)(D_E/\gamma_\ell \eta^2)} = \frac{\gamma_\ell^2 \eta^4}{\chi^2}$$

With χ ∼ γ_ℓ (natural scaling):
$$R_H \approx \eta^4$$

**Refined result:** Accounting for geometric factors:
$$R_H = 4\eta^2$$

where the factor of 4 arises from angular averaging over m-modes.

---

## 5. Scale-Dependent Hierarchy

### 5.1 Multipole Dependence

The hierarchy factor varies with scale:
$$\eta(\ell) = \eta_0 \left(\frac{\ell}{\ell_*}\right)^{-\alpha_\eta}$$

**Physical motivation:**
- Low ℓ: Thomson scattering most efficient, strong T-E coupling
- High ℓ: Diffusion damping reduces correlation, hierarchy weakens

### 5.2 Hierarchy Ratio Function

$$R_H(\ell) = 4\eta_0^2 \left(\frac{\ell}{\ell_*}\right)^{-2\alpha_\eta}$$

**Observed EGC values:**
- C_TE ≈ 0.97
- C_TT ≈ C_EE ≈ 0.15

**Implied:**
$$R_H^{obs} = \frac{(0.97)^2}{(0.15)^2} \approx 42$$
$$\Rightarrow \eta_{eff} = \sqrt{42/4} \approx 3.2$$

This suggests η₀ ∼ 2.5-4 is observationally motivated.

---

## 6. Phase Angular Correlation

### 6.1 Definition

The angular correlation of phases:
$$\xi_\phi^{AB}(\theta) = \frac{1}{N(\theta)} \sum_{\ell_1, \ell_2} C_{AB}(\ell_1, \ell_2) \cdot \mathbb{1}[|\theta_{\ell_1} - \theta_{\ell_2}| \approx \theta]$$

### 6.2 HPM Prediction

For TE:
$$\xi_\phi^{TE}(\theta) = C_{TE}(\ell_*) \cdot \exp\left(-\frac{\theta^2}{2\theta_c^2}\right)$$

with correlation angle:
$$\theta_c = \frac{\pi}{\ell_*} \cdot \sqrt{\frac{1}{2\alpha_\eta}}$$

For TT and EE:
$$\xi_\phi^{TT}(\theta) = C_{TT}(\ell_*) \cdot \exp\left(-\frac{\theta^2}{2\theta_c^2}\right) \cdot f_{dec}(\theta)$$

where f_dec accounts for additional decoherence.

---

## 7. Parameter Estimation

### 7.1 Model Parameters

| Parameter | Symbol | Range | Physical Meaning |
|-----------|--------|-------|-----------------|
| Base hierarchy | η₀ | [1.5, 4.0] | T-E coupling strength at ℓ_* |
| Scale exponent | α_η | [0, 2] | Hierarchy scale dependence |
| Reference multipole | ℓ_* | [300, 800] | Peak hierarchy location |
| Coherence amplitude | A₀ | [0.01, 0.5] | Overall phase correlation scale |

### 7.2 Likelihood Function

For observed coherences $\hat{C}_{AB}$ with uncertainties $\sigma_{AB}$:

$$\ln \mathcal{L} = -\frac{1}{2} \sum_{\ell} \left[ \frac{(\hat{C}_{TT} - C_{TT}^{HPM})^2}{\sigma_{TT}^2} + \frac{(\hat{C}_{EE} - C_{EE}^{HPM})^2}{\sigma_{EE}^2} + \frac{(\hat{C}_{TE} - C_{TE}^{HPM})^2}{\sigma_{TE}^2} \right]$$

### 7.3 Bayesian Evidence

**Prior distributions:**
- η₀ ~ Uniform(1.5, 4.0)
- α_η ~ Uniform(0, 2)
- ℓ_* ~ Log-Uniform(300, 800)
- A₀ ~ Log-Uniform(0.01, 0.5)

**Bayesian evidence:**
$$\ln Z = \ln \int d\theta \; \mathcal{L}(\theta) \cdot \pi(\theta)$$

**Model comparison:**
$$\ln B_{HPM,\Lambda} = \ln Z_{HPM} - \ln Z_{\Lambda CDM}$$

---

## 8. Falsification Criteria (Mathematical)

### F1 — Null Hierarchy

**Criterion:** max(R_H(ℓ)) < 2 for ℓ ∈ [100, 2000]

**Mathematical test:**
$$T_{F1} = \max_{\ell \in [100, 2000]} R_H(\ell) < 2$$

**Rejection threshold:** T_{F1} < 2 → reject HPM

### F2 — Inverted Hierarchy

**Criterion:** C_TT > C_TE or C_EE > C_TE for majority of ℓ range

**Mathematical test:**
$$T_{F2} = \frac{1}{N_\ell} \sum_\ell \mathbb{1}[C_{TE}(\ell) < \max(C_{TT}(\ell), C_{EE}(\ell))]$$

**Rejection threshold:** T_{F2} > 0.5 → reject HPM

### F3 — Wrong Scale Dependence

**Criterion:** Fitted α_η < 0

**Mathematical test:**
$$T_{F3} = \hat{\alpha}_\eta$$

**Rejection threshold:** T_{F3} < 0 → reject HPM

---

## 9. Summary of Key Equations

### 9.1 Core Prediction

$$R_H(\ell) = 4\eta_0^2 \left(\frac{\ell}{\ell_*}\right)^{-2\alpha_\eta}$$

### 9.2 Phase Coherences

$$C_{TT}(\ell) = C_{EE}(\ell) = \frac{A_0}{\eta(\ell)^2}$$
$$C_{TE}(\ell) = \frac{2A_0}{\eta(\ell)}$$

### 9.3 Normalization

$$C_{TT}^2 + C_{EE}^2 + |C_{TE}|^2 = A_0^2 \left(\frac{2}{\eta^4} + \frac{4}{\eta^2}\right) \approx \frac{4A_0^2}{\eta^2}$$

For η = 3: Total coherence ≈ 0.44A₀²

---

## 10. Numerical Implementation Notes

### 10.1 Phase Extraction from C_ℓ

For actual CMB data, phases are not directly observable. Two approaches:

**Approach A:** Use power spectrum reconstruction:
- Extract phases from full-sky maps (requires unmasked sky)
- Compute a_{ℓm} via spherical harmonic transform
- Extract phases φ_ℓ = arg(a_ℓm averaged over m)

**Approach B:** Use effective phase model:
- Model phase effects as modifications to C_ℓ covariance
- Fit C_ℓ data with HPM-modified covariance matrix

### 10.2 Simulation Strategy

1. Generate Gaussian random phases with HPM correlation structure
2. Construct a_{ℓm} = |a_{ℓm}| · exp(iφ_ℓ)
3. Compute C_ℓ = (1/(2ℓ+1)) Σ_m |a_{ℓm}|²
4. Compare to ACT DR6 data

---

*Mathematical formalism complete — ready for numerical implementation*
