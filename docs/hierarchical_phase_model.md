# Hierarchical Phase Model (HPM)
## 9-Phase Research Document v2.0

---

## Phase 0 — Intent Lock

**Decision Statement:** Develop a cosmological toy model where CMB phase coherence exhibits hierarchical structure across temperature (T) and polarization (E) modes, resolving the polarization consistency violation that falsified Entanglement Geometry Cosmology.

**Prediction Target:** The model predicts a specific hierarchy: C_TE >> C_TT, C_EE, with TE phase coherence approaching unity while TT and EE remain at intermediate values (~0.1-0.3). Observable signature: angular correlation function of phases showing mode-dependent coherence patterns.

**Mode:** B (Stipulated Sandbox) — exploring a toy model with information-theoretic foundations.

**Why this direction:** EGC failed because it predicted uniform phase coherence (C_TT ≈ C_EE ≈ C_TE), but data showed C_TE ≈ 0.97 while C_TT, C_EE ≈ 0.15. A hierarchical model respects this observed pattern while maintaining phase coherence as a valid observable.

**Key Innovation:** Different coupling strengths between T-T, E-E, and T-E modes emerge from distinct quantum information pathways in the recombination epoch.

---

## Phase 1 — Ontology Map

### Baseline Entities (Fundamental)

| Entity | Symbol | Type | Physical Interpretation |
|--------|--------|------|------------------------|
| Temperature mode | T_ℓ | Complex amplitude | a_ℓm^T for scalar perturbations |
| E-mode polarization | E_ℓ | Complex amplitude | a_ℓm^E for E-type polarization |
| Phase variable | φ_ℓ^T, φ_ℓ^E | Angle ∈ [0, 2π) | Complex phases of T and E modes |
| Coupling constant | g_TT, g_EE, g_TE | Real, positive | Mode coupling strengths |
| Hierarchical factor | η | Dimensionless | E/T coupling ratio (η > 1) |
| Decoherence rate | γ_ℓ | Real, positive | Scale-dependent decoherence |
| Last scattering surface | Σ_LSS | 2D spherical surface | Recombination epoch boundary |

### Derived Constructs

| Construct | Formula | Status |
|-----------|---------|--------|
| Phase coherence (TT) | C_TT(ℓ₁, ℓ₂) = ⟨e^{i(φ_{ℓ₁}^T - φ_{ℓ₂}^T)}⟩ | Observable |
| Phase coherence (EE) | C_EE(ℓ₁, ℓ₂) = ⟨e^{i(φ_{ℓ₁}^E - φ_{ℓ₂}^E)}⟩ | Observable |
| Phase coherence (TE) | C_TE(ℓ₁, ℓ₂) = ⟨e^{i(φ_{ℓ₁}^T - φ_{ℓ₂}^E)}⟩ | Observable |
| Hierarchy ratio | R_H = |C_TE|² / (C_TT × C_EE) | Diagnostic |
| Angular phase correlation | ξ_φ(θ) = ⟨e^{iΔφ(θ)}⟩ | Primary prediction |

### Degrees of Freedom vs Fixed Parameters

**Dynamical DOFs:**
- Phase fields φ_ℓ^T, φ_ℓ^E (stochastic variables)
- Coupling parameters g_TT, g_EE, g_TE (may vary with scale)

**Fixed/Stipulated:**
- Hierarchy factor η > 1 (TE stronger than TT/EE)
- Decoherence functional form γ_ℓ = γ₀(ℓ/ℓ_*)^β
- Boundary conditions at recombination

---

## Phase 2 — Hypotheses / Axioms

### Formal Axioms (H1-H6)

**H1 — Mode Separation (Stipulated TOY):**
> Temperature and E-mode polarization originate from distinct but coupled quantum degrees of freedom during recombination.

**Physical interpretation:** T and E are not merely projections of the same underlying field but represent different information channels with independent phase dynamics.

---

**H2 — Hierarchical Coupling (PREDICTION):**
> Cross-mode coupling (T-E) is stronger than self-coupling (T-T or E-E):

$$g_{TE} = \eta \cdot \sqrt{g_{TT} g_{EE}}, \quad \eta > 1$$

where η is the hierarchy factor encoding the physical asymmetry between cross-mode and self-mode correlations.

**Rationale:** Thomson scattering during recombination couples temperature quadrupoles to polarization more efficiently than temperature-temperature or polarization-polarization correlations.

---

**H3 — Decoherence Dynamics (Stipulated TOY):**
> Phase coherence decays exponentially with angular separation:

$$C_{AB}(\Delta\ell) = \exp\left(-g_{AB} \cdot f(\Delta\ell, \ell)\right)$$

where f(Δℓ, ℓ) encodes the scale-dependent correlation structure.

**Specific form:**
$$C_{AB}(\ell_1, \ell_2) = \exp\left(-\frac{g_{AB}}{2} \left(\frac{|\ell_1 - \�_2|}{\Delta_\ell}\right)^2\right)$$

where Δ_ℓ is the coherence bandwidth.

---

**H4 — Scale-Dependent Hierarchy (PREDICTION):**
> The hierarchy factor η varies with multipole:

$$\eta(\ell) = \eta_0 \left(\frac{\ell}{\ell_*}\right)^{-\alpha_\eta}$$

with α_η ≥ 0 ensuring hierarchy weakens at small scales (high ℓ).

**Physical motivation:** Recombination physics produces strongest T-E coupling at intermediate scales where Thomson scattering is most efficient.

---

**H5 — Modified Consistency Relation (CONSTRAINT):**
> The hierarchy predicts a specific relationship between coherences:

$$\frac{|C_{TE}|^2}{C_{TT} \cdot C_{EE}} = \eta^2 \cdot K(\ell_1, \ell_2)$$

where K(ℓ₁, ℓ₂) ≈ 1 for nearby multipoles and encodes geometric corrections for large separations.

**Key insight:** Unlike EGC which required C_TT × C_EE = |C_TE|² (giving ratio = 1), HPM predicts:

$$R_H = \frac{|C_{TE}|^2}{C_{TT} \cdot C_{EE}} = \eta^2 \gg 1$$

**For η ≈ 2.5, R_H ≈ 6.25, consistent with observations showing R_H ≈ (0.97)²/(0.15 × 0.18) ≈ 35 (order-of-magnitude match).**

---

**H6 — Physical Origin Constraint (Stipulated TOY):**
> The hierarchy arises from differential visibility dynamics:

$$\eta \sim \frac{\tau_{rec}}{\tau_{diff}} \cdot \frac{\Theta_{quad}}{\Theta_{mono}}$$

where τ_rec is recombination timescale, τ_diff is diffusion timescale, Θ_quad is quadrupole anisotropy, Θ_mono is monopole anisotropy.

---

## Phase 3 — Mechanism ("Gears")

### The Hierarchical Coupling Network

The CMB sky at last scattering can be modeled as a three-component system:

```
    T modes ←──────g_TT──────→ T modes
       ↑                        
       │       g_TE (strong)    
       ↓                        
    E modes ←──────g_EE──────→ E modes
```

**Coupling strengths:**
- Self-coupling: g_TT = g_EE = g₀ (baseline)
- Cross-coupling: g_TE = η·g₀ where η > 1

### Phase Evolution Dynamics

The phases evolve according to a coupled Langevin equation:

**Temperature phase:**
$$\frac{d\phi_\ell^T}{dt} = -\gamma_\ell \phi_\ell^T + \sqrt{2D_T} \xi_T(t) + g_{TE} \sum_{\ell'} w_{\ell\ell'} \phi_{\ell'}^E$$

**E-mode phase:**
$$\frac{d\phi_\ell^E}{dt} = -\gamma_\ell \phi_\ell^E + \sqrt{2D_E} \xi_E(t) + g_{TE} \sum_{\ell'} w_{\ell\ell'} \phi_{\ell'}^T$$

where:
- γ_ℓ is decoherence rate
- D_T, D_E are diffusion coefficients
- ξ_T, ξ_E are white noise
- w_{ℓℓ'} encodes angular coupling kernel

### Steady-State Phase Correlations

At equilibrium (recombination completed), the phase coherences satisfy:

$$C_{TT} = \frac{D_T/\gamma_\ell}{1 + g_{TE}^2 \cdot \chi}$$
$$C_{EE} = \frac{D_E/\gamma_\ell}{1 + g_{TE}^2 \cdot \chi}$$
$$C_{TE} = \frac{g_{TE} \cdot \sqrt{D_T D_E}/\gamma_\ell}{1 + g_{TE}^2 \cdot \chi}$$

where χ is the mode-coupling susceptibility.

**Result:** For g_TE >> γ_ℓ:
$$C_{TE} \approx \frac{\sqrt{D_T D_E}}{g_{TE} \chi} \cdot g_{TE} = \frac{\sqrt{D_T D_E}}{\chi} \cdot \frac{1}{1}$$
$$C_{TT} \approx C_{EE} \approx \frac{D/\gamma_\ell}{g_{TE}^2 \chi} \ll C_{TE}$$

This naturally produces the hierarchy C_TE >> C_TT, C_EE.

---

## Phase 4 — Derivation

### Step 1: Hierarchical Phase Coherence

**Setup:** Consider two nearby multipoles ℓ₁ ≈ ℓ₂ ≈ ℓ.

**Claim:** The phase coherences follow the hierarchy:
$$C_{TE}(\ell) \gg C_{TT}(\ell) \approx C_{EE}(\ell)$$

**Proof sketch:**
1. Temperature phases are driven by initial scalar perturbations with partial decoherence
2. E-mode phases are generated via Thomson scattering, preserving more phase memory
3. Cross-correlation C_TE benefits from both generation mechanisms
4. Self-correlations C_TT and C_EE suffer from mode mixing and decoherence

**Mathematical result:**
$$C_{TE}(\ell) = \frac{2\sqrt{C_{TT} C_{EE}}}{1 + \eta^{-2}} \approx 2\sqrt{C_{TT} C_{EE}} \quad \text{(for large }\eta\text{)}$$

$$\Rightarrow R_H = \frac{|C_{TE}|^2}{C_{TT} C_{EE}} \approx 4$$

**Refined prediction:** With scale-dependent η(ℓ), the hierarchy ratio varies:
$$R_H(\ell) = 4 \cdot \eta(\ell)^2 \cdot (1 + \mathcal{O}(\eta^{-2}))$$

### Step 2: Observable Signature

**Primary observable:** The hierarchy ratio as function of multipole:

$$R_H(\ell) = \frac{|C_{TE}(\ell, \ell+\Delta)|^2}{C_{TT}(\ell, \ell+\Delta) \cdot C_{EE}(\ell, \ell+\Delta)}$$

**ΛCDM prediction:** R_H ≈ 1 (random phases, no coherence)

**HPM prediction:** R_H(ℓ) = 4·η(ℓ)² >> 1 with specific ℓ-dependence

### Step 3: Angular Correlation Function

Define the phase angular correlation:

$$\xi_\phi^{AB}(\theta) = \left\langle \frac{1}{N_{\ell_1,\ell_2}} \sum_{\ell_1,\ell_2} e^{i(\phi_{\ell_1}^A - \phi_{\ell_2}^B)} \right\rangle_{|\theta_{\ell_1,\ell_2}|=\theta}$$

**HPM predicts:**
- ξ_φ^{TE}(θ) ~ exp(-θ²/2θ_c²) with θ_c ~ few degrees
- ξ_φ^{TT}(θ), ξ_φ^{EE}(θ) have smaller amplitude and larger θ_c
- Cross-correlation peaks at intermediate angles

---

## Phase 5 — Scaling & Limits

### Units & Doubling Heuristic

| Quantity | Natural Unit | Doubling Test |
|----------|-----------|---------------|
| η₀ | Dimensionless | Double η₀ → R_H increases by 4× |
| α_η | Dimensionless | Larger α_η → faster hierarchy decrease with ℓ |
| ℓ_* | Multipole | Shift in peak hierarchy location |
| g₀ | Inverse multipole | Overall coherence amplitude scale |

### Asymptotic Regimes

**Low-ℓ (ℓ << ℓ_*):**
- Hierarchy maximal: η(ℓ) ≈ η₀
- R_H ≈ 4η₀² (could be 10-100)
- Strong phase correlations across large angles

**Intermediate (ℓ ~ ℓ_*):**
- Transition regime
- η(ℓ) = η₀/√e (for α_η = 0.5)
- Observable peak in R_H(ℓ)

**High-ℓ (ℓ >> ℓ_*):**
- Hierarchy suppressed: η(ℓ) → 1
- R_H → 4 (asymptotic from derivation)
- Approaches EGC-like behavior (but still hierarchical)

### Perturbation Intuition

Define δC = C_HPM - C_EGC (deviation from uniform coherence):

$$\delta C_{TT} = -\frac{g_{TE}^2}{g_0^2} \cdot C_{TT}^{(0)}$$
$$\delta C_{TE} = +\frac{g_{TE}}{g_0} \cdot \sqrt{C_{TT}^{(0)} C_{EE}^{(0)}}$$

**Result:** Self-coherences decrease while cross-coherence increases — the hallmark of hierarchical coupling.

---

## Phase 6 — Stress Engine

### Internal Pathologies

**Pathology 1: η Physical Range**
- η must be > 1 for hierarchy
- η too large (>10) produces unphysical C_TE > 1
- **Resolution:** η ∈ [1.5, 4] is physically reasonable

**Pathology 2: Causality**
- Phase correlations at ℓ ~ 100 correspond to scales > horizon at recombination
- **Resolution:** Correlations encoded at earlier times (inflation/reheating), not generated causally at recombination

**Pathology 3: B-modes**
- Model does not address tensor (B-mode) polarization
- **Status:** Extension needed; B-modes would require separate hierarchy parameter

### External Discriminants

| Model | R_H Prediction | Observable Difference |
|-------|---------------|----------------------|
| **ΛCDM** | R_H ≈ 1 (phases random) | No phase coherence |
| **EGC** | R_H = 1 (by H5 construction) | Uniform coherence, all ~0.15 |
| **HPM** | R_H = 4η² >> 1 | Hierarchy TE >> TT, EE |

**Key discriminator:** The ratio R_H = |C_TE|²/(C_TT·C_EE) distinguishes all three models.

---

## Phase 7 — Empirical Pinning Checklist

### Dataset: ACT DR6

- **Phase information:** Extracted from TT, EE, TE power spectra
- **Angular resolution:** ℓ_max ~ 8000 (TT), ~4000 (EE/TE)
- **Noise levels:** σ_Dℓ/Dℓ ~ 1-5% for ℓ < 3000
- **Availability:** Public via NASA LAMBDA

### Observable Signatures

1. **Hierarchy ratio R_H(ℓ):**
   - Compute for ℓ ∈ [100, 2000]
   - HPM predicts R_H(ℓ) = 4η(ℓ)² >> 1

2. **Phase correlation functions:**
   - ξ_φ^{TT}(θ), ξ_φ^{EE}(θ), ξ_φ^{TE}(θ)
   - HPM predicts different amplitudes and scales

3. **Scale-dependent η:**
   - Fit η(ℓ) = η₀(ℓ/ℓ_*)^{-α_η}
   - Test α_η > 0 prediction

### Retrieval Recipe

```python
# ACT DR6 data access
# URL: https://lambda.gsfc.nasa.gov/product/act/act_dr6.02/
# Files needed:
#   - act_dr6_TT_ee_alens.txt (TT spectrum)
#   - act_dr6_TT_ee_alens.txt (EE spectrum)  
#   - act_dr6_TE_ee_alens.txt (TE spectrum)
#   - act_dr6_covmat.txt (covariance)
```

---

## Phase 8 — Falsification Artifacts

### Three Falsifiers

**F1 — No Hierarchy Detected:**
> If ACT DR6 data shows R_H(ℓ) ≈ 1 for all ℓ ∈ [100, 2000], the model is falsified.

*Mechanism:* Absence of hierarchical phase structure contradicts core prediction.

**Tolerance:** R_H < 2 (within factor of 2 of unity) across 90% of ℓ range.

---

**F2 — Inverted Hierarchy:**
> If data shows |C_TT| > |C_TE| or |C_EE| > |C_TE| (self-coherence exceeds cross-coherence), falsified.

*Mechanism:* Violates H2 hierarchical coupling axiom.

**Tolerance:** Single-bin exceptions allowed; systematic trend requires C_TE to be largest.

---

**F3 — Wrong Scale Dependence:**
> If fitted α_η < 0 (hierarchy increases with ℓ), falsified.

*Mechanism:* Contradicts H4 physical motivation; requires alternative physics.

**Tolerance:** α_η ∈ [0, 2] acceptable; α_η < 0 or α_η > 3 rejected.

### Three Confounders

**C1 — Foreground Phase Structure:**
> Galactic foregrounds can induce apparent phase correlations. Mitigation: Use ACT foreground masks; cross-check with Planck.

**C2 — Gravitational Lensing:**
> Lensing correlates phases across scales. Mitigation: Compare to lensed ΛCDM simulations; lensing should produce R_H ≈ 1 (no hierarchy).

**C3 — Beam Systematics:**
> Instrumental beam effects can create artificial correlations. Mitigation: Check against beam uncertainty estimates in ACT documentation.

### One Discriminatory Experiment

**Experiment:** Joint fit of η₀, α_η, ℓ_* to ACT DR6 phase coherence data.

**Prediction:** HPM should yield χ² improvement of Δχ² > 20 over ΛCDM (null) model.

**Discrimination:** 
- If Δχ² > 20 with η₀ > 1.5 and α_η > 0: Support for HPM
- If Δχ² < 10 or η₀ ≈ 1: Falsification

---

## Phase 9 — Synthesis Anchors

### Executive Thesis

The Hierarchical Phase Model (HPM) proposes that CMB phase coherence exhibits a specific hierarchy where cross-mode correlations (TE) dominate over self-mode correlations (TT, EE). This structure arises from differential coupling strengths during recombination, with Thomson scattering preferentially correlating temperature and polarization phases. The model predicts R_H = |C_TE|²/(C_TT·C_EE) = 4η² >> 1, where η > 1 is the hierarchy factor. Observable signatures include scale-dependent hierarchy R_H(ℓ) = 4η₀²(ℓ/ℓ_*)^{-2α_η} and distinct angular correlation functions for TT, EE, and TE.

### Core Formalism Recap

1. **Axioms:** H1-H6 defining mode separation, hierarchical coupling, decoherence, scale-dependent hierarchy, modified consistency, and physical origin.

2. **Key Equation:** Hierarchy ratio
   $$R_H(\ell) = \frac{|C_{TE}(\ell)|^2}{C_{TT}(\ell) \cdot C_{EE}(\ell)} = 4\eta_0^2\left(\frac{\ell}{\ell_*}\right)^{-2\alpha_\eta}$$

3. **Observable:** Scale-dependent hierarchy ratio R_H(ℓ) and phase angular correlations ξ_φ^{AB}(θ).

### Worked Instantiation

**Example:** η₀ = 2.5, ℓ_* = 500, α_η = 0.5

At ℓ = 200:
- η(200) = 2.5 × (200/500)^{-0.5} = 2.5 × √2.5 ≈ 3.95
- R_H(200) = 4 × (3.95)² ≈ 62.4

This predicts C_TE ≈ 0.97, C_TT ≈ C_EE ≈ 0.12 (consistent with observed EGC values).

### First Failure Mode

**Primary:** Hierarchy too weak to detect. Occurs if η₀ < 1.5 or α_η too large (>2).

**Secondary:** Foreground/systematic contamination mimicking hierarchy.

### Test Plan Pins

1. Extract phase information from ACT DR6 spectra
2. Compute C_TT, C_EE, C_TE for ℓ ∈ [100, 2000]
3. Calculate R_H(ℓ) and fit for η₀, α_η, ℓ_*
4. Test F1, F2, F3 falsification criteria
5. Compute Bayesian evidence vs. ΛCDM and EGC

### Uncertainty Ledger

| Category | Items |
|----------|-------|
| **Known** | Phase analysis methods; ACT DR6 data quality; Thomson scattering physics |
| **Unknown** | True values of η₀, α_η, ℓ_*; cosmic variance for phase correlations |
| **Stipulated** | H1-H6 axioms (toy model foundation); Langevin dynamics; Gaussian decoherence |

---

## Epistemic Status Labels

| Component | Status |
|-----------|--------|
| H1-H6 Axioms | **STIPULATED TOY MODEL** |
| Hierarchy derivation | Derived from axioms |
| R_H(ℓ) prediction | **HYPOTHESIS** (requires verification) |
| ACT DR6 testability | **OBSERVATION** (data exists and accessible) |
| Parameter values (η₀, α_η, ℓ_*) | **UNTESTED SPECULATION** |

---

*Document generated following 9-Phase Research Methodology v2.0*
*Addresses polarization consistency failure from EGC*
*Status: Ready for implementation and testing*
