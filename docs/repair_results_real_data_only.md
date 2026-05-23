# HPM repair results (real-data only): hierarchy mapping from TE

## Run context
- Data: ACT DR6 binned spectra, fg-subtracted combined TT/EE/TE files.
- No synthetic phases or dummy data.

## Derived observable
Using stored `Dl` columns:
- \(\mathcal{R}^{TE}_\ell = |Dl_{TE}|/\sqrt{Dl_{TT}\,Dl_{EE}}\)
- \(\eta(\ell)=\mathcal{R}^{TE}_\ell/2\)

## Train/test split
- Train: 593 \le \ell \le 2000
- Test: 2000 < \ell \le 8319

## Model fitted
\[
\eta(\ell)=\eta_0(\ell/\ell_*)^{-\alpha},\quad \ell_*=500\ (fixed)
\]

## Outlier control
- Kept only bins with \(\eta<5\) (ratio instability cut).

## Best-fit parameters (ACT DR6)
- \(\eta_0 = 0.21023\)
- \(\alpha = 0.19537\)

## Predictive metrics
- RMSE(\(\eta\)) train ≈ 0.095
- RMSE(\(\eta\)) test ≈ 0.209

## Honest interpretation
This repair keeps the model defined from real TE hierarchy, but it does **not** preserve the earlier large-\(\eta\) Thomson-normalization claim. It also does not rely on assuming \(C_{TE}\) dominates \(C_{TT}, C_{EE}\) in most bins, since real TE correlation magnitude is oscillatory.
