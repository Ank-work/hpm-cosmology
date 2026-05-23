# Hierarchical Phase Model v3 (HPM v3) — Real-data TE hierarchy mapping

## What changed (repairs prompted by critique)
1. **No synthetic/“dummy” phase data**: all fits are done from **real** ACT DR6 binned spectra (`fg_subtracted_TT/EE/TE.dat`).
2. **Normalization is defined directly from the TE correlation coefficient** (real-data observable), removing the earlier inconsistent Thomson-normalization claim.
3. **Model parameters are fit to the derived hierarchy statistic** rather than to “phase coherence” amplitudes that were only self-consistent inside the toy generator.

## Definitions (real observable)
Let the binned spectra be the ACT DR6 bandpowers in the stored file convention.

Define the TE correlation coefficient magnitude:
\[
\mathcal{R}^{TE}_\ell \equiv \frac{|C^{TE}_\ell|}{\sqrt{C^{TT}_\ell C^{EE}_\ell}}
\]
Using the stored ACT spectra convention (Dl form with common prefactors), the conversion prefactor cancels in the ratio, so the same formula is used on the `Dl` columns.

Define the hierarchy statistic:
\[
R_H(\ell)=\frac{|C^{TE}_\ell|^2}{C^{TT}_\ell C^{EE}_\ell} = (\mathcal{R}^{TE}_\ell)^2
\]
Define the HPM hierarchy factor:
\[
\eta(\ell) \equiv \frac{\mathcal{R}^{TE}_\ell}{2} \quad\Rightarrow\quad R_H(\ell)=4\eta(\ell)^2
\]

## Parametric model (v3)
Use a minimal scale dependence:
\[
\eta(\ell)=\eta_0\,\left(\frac{\ell}{\ell_*}\right)^{-\alpha}
\]
In current repair runs, the quadratic log correction was found unnecessary for stability when fitting in a controlled (outlier-cut) regime.

## Real-data fit (ACT DR6)
Fit to the derived \(\eta(\ell)\) from real ACT DR6 binned spectra, with an outlier cut \(\eta<5\) to limit bins where the ratio becomes unstable.

**Best-fit (train: 593\le\ell\le2000, test: 2000<\ell\le8319):**
- \(\ell_* = 500\) (fixed)
- \(\eta_0 = 0.21023\)
- \(\alpha = 0.19537\)

**Prediction performance:**
- RMSE(\(\eta\)) on test ≈ **0.209**
- Training RMSE ≈ **0.095**

**Caveat (honest):**
Propagated \(\sigma_\eta\) yields large \(\chi^2/\mathrm{dof}\) in this simple pipeline; this is consistent with the likelihood error model for ratios needing a fuller covariance treatment.

## What v3 no longer claims
- It no longer claims an intrinsic “\(\eta_0=\sqrt{3}/4\approx0.433\)” normalization from Thomson geometry without explicitly matching the exact map/spectrum pipeline conventions.
- It no longer treats “\(C_{TE} \gg C_{TT}, C_{EE}\) in most bins” as a strict falsification criterion; real TE correlation magnitude is oscillatory and sign-alternating.

## Status
**HPM v3:** repaired phenomenological model, defined from real-data TE correlation coefficient and fit using real ACT spectra.

Next work (still needed):
- full covariance-aware uncertainty propagation for \(\eta(\ell)\)
- Planck/WMAP consistency using the same hierarchy mapping
- full phase extraction from maps with pipeline matched to the derived-spectra convention
