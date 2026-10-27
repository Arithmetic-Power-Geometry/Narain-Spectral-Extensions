# P44 — total interval-width contract and adversarial validation (2026-10-27)

## Actual executed implementation and provenance
The executed source is evidence/P44/total_error.py; it imports evidence/P42/certified_theta.py (same code was copied to the local P44 run directory). GitHub readback of P44 source is Git blob aa586e27188512644541521c31c89cfe33918ae4, matching local git hash-object exactly: BYTE-IDENTICAL. Local source SHA256 465b7d1cc9aa47c0379a1440f51aa37be7acc379500a7bb2c777620be7c806da. Local stdout SHA256 5c737497486f29944ff155c6304c5b562c6ef785fdba3ce88a497b0280ac37ba; stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resource SHA256 6b812ab649467ec8c43a4d3a53ab9d6ec9068b5a1356d28fb55f8b243ed9f99f. Exit 0; wall 8.30 s; max RSS 99980 KB. Raw logs exist at /mnt/data/p44 and are NOT claimed remotely uploaded.

## Specification and soundness
Input graph code is n vertices, n in [1,12] for this implementation, simple undirected edges supplied as sorted pairs (i,j) with 0<=i<j<n, no duplicates; graph pairs share n. Y=[[a,b],[b,d]] and strict lambda lower bound are parsed as exact rational fractions. Exact Sylvester criterion requires lambda>0, a-lambda>0, (a-lambda)(d-lambda)-b^2>0. Epsilon is exact positive rational. K runs from 0 to max_k; precision is selected from an explicit finite list.

At each candidate K and precision, the evaluator obtains a positive analytic tail enclosure T for the difference of infinite Gaussian sums, then an outward-rounded interval [L,U] for the truncated difference. It constructs [L-T,U+T] and accepts only if its computed width upper bound is <= the lower bound of epsilon's interval representation. It reports CERTIFIED_NEGATIVE only if the widened upper bound is <0, CERTIFIED_POSITIVE only if its lower bound is >0; otherwise INCONCLUSIVE. If no candidate meets the total width contract, it returns BUDGET_EXHAUSTED. Finite loops guarantee termination. Conditional on the mpmath.iv enclosure semantics and the P42 Gaussian tail bound, the returned interval encloses the infinite Gaussian difference. This is a soundness statement for this restricted mathematical expression, not a new physics theorem.

## Eight local tests (all pass)
Y=[[1.1,.23],[.23,1.3]], lambda=.949.
1. n=2 empty graph vs one edge, epsilon=1e-8: CERTIFIED_POSITIVE, K=2, dps=30, final width <=9.08469732953913456768e-13.
2. n=7 published P33 pair, epsilon=1e-12: CERTIFIED_NEGATIVE, K=3, dps=30, final width <=1.62964314010884734049e-21.
3. n=1 identical empty graphs, epsilon=1e-8: INCONCLUSIVE, K=2, dps=30, width <=2.55761258005069741795e-14; no false inequality.
4. n=7 pair, epsilon=1e-50, max_k=1: BUDGET_EXHAUSTED; no false certificate.
5. Duplicate graph edge: REJECTED_EXACTLY.
6. Self-loop: REJECTED_EXACTLY.
7. Singular Y: REJECTED_EXACTLY.
8. Invalid lower eigenvalue bound: REJECTED_EXACTLY.

## Adversarial limitations and publication kill tests
- User-supplied rational decimals must be accepted as exact intended inputs; the implementation does not support arbitrary algebraic or complex period matrices.
- n<=12 is a software resource guard, not a mathematical limitation; worst-case work remains exponential O(n*4^n+(2K+1)^4) at fixed precision.
- A bounded list of precisions and max_k may return BUDGET_EXHAUSTED even if a narrower certificate is theoretically attainable.
- Identical graph inputs correctly yield INCONCLUSIVE; no inequality claim is made.
- The Gaussian tail bound and mpmath.iv rounding assumptions need external verification in a second independent implementation. No GitHub Actions pinned CI or independent generic baseline was run.
- Prior art: Dymarsky–Shapere JHEP 03 (2021) 160 and Henriksson–Kakkar–McPeak JHEP 04 (2023) 011. A generic interval enclosure for theta sums and exponential tails is standard numerical analysis; no novel theorem or algorithm has yet been established.
- Only the restricted code-CFT Gaussian theta numerator was certified, not a new full physical Narain equivalence result.

## Strict gate
GO: exact SPD and graph validation, total-width error contract, eight executed controls, source byte-identical GitHub readback.
REVISE: independent interval backend, randomized/adversarial property tests, comparison with established certified Siegel theta methods, full CI and raw log upload, broader physical theta conventions.
NO-GO: original general mathematical theorem, new isospectral construction, Q1 theoretical physics paper or manuscript.
Next P45: independent interval backend and controlled baseline benchmarking with a strict novelty kill test. Do not draft a paper.
