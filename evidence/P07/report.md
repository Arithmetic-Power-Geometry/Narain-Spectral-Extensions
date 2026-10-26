# P07 — coupled Narain rigidity audit
2026-10-26. Overall REVISE. Exact finite-window first-discrepancy certificates PASS.

Source family: G diagonal 1, G adjacent offdiagonal 1/(10+i); B adjacent upper entries 1/(13+i), lower entries negative; i starts at 0. This is the same P06 rational coupled family.

Completeness: if E=(m+Bn)^T G^-1(m+Bn)+n^T G n is at most H, Gershgorin yields L||n||²<=H, with L=89/110, U=131/110. Let beta=27/182 bound the B operator norm. Then ||m||<=sqrt(HU)+beta sqrt(H/L). Since U/L<4, ||m||²<HU+beta² H/L+4beta H. The checker enumerates all integer charges inside these conservative norm bounds.

Results from executed exact rational search:
T3, H=3: 125 states per sign; first difference 1164367/582071; coefficients spin +1: +2, spin -1: -2.
T4, H=5/2: 129 states per sign; first difference 9437981/4718325; coefficients spin +1: +2, spin -1: -2.
T6, H=2: 65 states per sign; no difference.
A separate signed-coordinate-permutation check for T3/T4 found no matrix simultaneously preserving G and reversing B. This is NOT a complete GL(d,Z) or O(d,d;Z) test.

B-sign parity: the integer bijection (m,n) to (m,-n) preserves E between +B and -B and flips conformal spin s=m.n. Thus unrefined spectra agree identically; the refined first coefficients obstruct any equivalence preserving both E and s. This is only a necessary spectral condition, not a full sufficient identifiability criterion. A parity reversal is not automatically a spin-preserving Narain duality.

Negative evidence: initial broad search timed out; bounded rerun completed. T6 remains unresolved above E=2. No general integer indecomposability, full duality orbit classification, necessary-and-sufficient theorem, or quantitative perturbation stability was proved.

Literature: Narain (1986), DOI 10.1016/0370-2693(86)90682-9; Groot Nibbelink and Vaudrevange (2017), DOI 10.1007/JHEP04(2017)030. Both already recorded in the verified reference register. No duplicate entry appended.

Gate: PASS exact finite windows, REVISE novelty and duality completeness. P08 should derive certified rational parameter neighborhoods, uniform charge bounds and spectral gap persistence, including counterexamples at boundaries; distinguish static spectral stability from dynamical stability.
