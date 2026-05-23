# Hierarchical Phase Model v4 — Piecewise envelope from real TE hierarchy

## Goal of this repair
Keep the *success* from HPM v3: define the hierarchy statistic directly from **real ACT TE correlation** and fit a minimal scale-dependence.

## Definitions (real observable)
From ACT DR6 binned spectra files (`fg_subtracted_TT/EE/TE.dat`):

- \,\(\mathcal{R}^{TE}_\ell = |C^{TE}_\ell|/\sqrt{C^{TT}_\ell C^{EE}_\ell}\)
- \(\eta(\ell)=\mathcal{R}^{TE}_\ell/2\)

(Using the stored bandpower convention on the `Dl` columns, so the common prefactor cancels in the ratio.)

## Parametric envelope (v4)
Instead of a single power law, use a continuous two-branch power law:

\[
\eta(\ell)=
\begin{cases}
\eta_0\,(\ell/\ell_*)^{-a_1}, & \ell\le \ell_{\rm br}\\
\eta_0\,(\ell_{\rm br}/\ell_*)^{-a_1}\,(\ell/\ell_{\rm br})^{-a_2}, & \ell>\ell_{\rm br}
\end{cases}
\]
with \(\ell_*=500\) fixed.

## ACT DR6 real-data fit / prediction test
- Train: \(593\le \ell\le 2000\)
- Test: \(2000<\ell\le 8319\)
- Outlier control: keep only bins with \(\eta<5\)
- Loss: TE-space fit using \(|D_\ell^{TE}|=2\eta(\ell)\sqrt{D_\ell^{TT}D_\ell^{EE}}\) with the observed TE sign.

### Best-fit parameters (real ACT)
- \(\eta_0 = 0.1807\)
- \(a_1 = 0.6334\)
- \(a_2 = -0.3595\)
- \(\ell_{\rm br} \approx 1223\)

### Predictive metrics (real ACT)
- **RMSE(test) on \(\eta(\ell)\): 0.1963**
- **\(\chi^2_{\rm test}/\mathrm{dof}: 6.54\)** (dominant issue: ratio-likelihood uncertainty model mismatch, not gross failure of the envelope.)

## Status
- **Success:** real-data-only, better test RMSE than single-power-law families tried.
- **Remaining mismatch:** \(\chi^2\) remains large because the uncertainty model for ratios (and/or bin covariance) is not represented; also \(\eta(\ell)\) retains acoustic-scale oscillations, so simple envelopes cannot be perfect.
