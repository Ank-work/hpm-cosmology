# HPM repair summary after critiques (real-data-only)

## What we keep (successes)
1. **No dummy phases**: the repaired hierarchy statistics are computed from real ACT DR6 spectra only.
2. **Observable definition fixed**: hierarchy is built directly from the standard TE correlation coefficient magnitude, 
   \(\mathcal{R}^{TE}_\ell = |C^{TE}_\ell|/\sqrt{C^{TT}_\ell C^{EE}_\ell}\).
3. **Prediction-style sanity checks on held-out \(\ell\) bins** (train 593–2000, test 2000–8319) now refer to real data.

## What we can’t match (remaining gaps)
1. The earlier strong claims about large \(\eta_0\) / \(R_H\) do not survive a consistent TE-hierarchy mapping.
2. Simple monotonic parameterizations (power law, log-quadratic, cutoff) do not generalize well when the full bin-to-bin TE structure is present.
3. \(\chi^2\) remains large under naive uncertainty propagation for ratio-based hierarchy statistics, indicating a missing covariance/likelihood model.

## Best current repaired envelope (v4)
Two-branch power-law envelope for \(\eta(\ell)\) inferred from real ACT TE:
- \(\eta_0\approx 0.1807\)
- \(\ell_{\rm br}\approx 1223\)
- Predictive performance: RMSE(test) on \(\eta\) ≈ **0.196**.

## Net status
This is **partial success**: real-data-defined hierarchy statistic + real-data predictive envelope improves over the single-power-law fits, but full ‘decisive’ validation claims are no longer supported.
