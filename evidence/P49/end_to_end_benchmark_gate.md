# P49 — End-to-end certified spectral-bound optimization benchmark (2026-10-27)

## Executed and verified source
Local /mnt/data/p49/benchmark.py; GitHub evidence/P49/benchmark.py, verified remote/local Git blob 0b739291811f5963de864af43ff8b1f27e5b64c0 (byte-identical). Dependencies are unchanged P44 total_error.py and certified_theta.py, copied locally; this is an end-to-end benchmark of P44's total interval-width evaluator, not just analytic tails.

Execution exit 0, wall 24.18 seconds, peak RSS 99724 KB, stderr empty. SHA256 benchmark source 38f865d3fc434bb5526829a6c0df25109fa20e13b1edf2e24b9f64db24e85756; stdout a3fb375854aaeed01d7781ac98566a4e9028c3bd2a0da45fc76d038ae373ee67; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 488aa1560ae22a3fe685f90b0350a4488605bad6072f01fb9d1210c6990752e4. Raw stdout/resources remain local.

## Exact optimization
Use Fraction to verify SPD and binary search 40 steps for a strict rational eigenvalue lower bound, checked via Sylvester's criterion. Pass that rational to the existing P44 total-width evaluator, which uses interval arithmetic for all certificate comparisons. No float conversions in the acceptance logic.

## Six measured runs
1. diagonal n2 Y=(1.1,0,1.3), epsilon=1e-8: old lower .5, K3, 4.895247 s, positive, total width <=2.1463547626143671e-12. Optimized lower 2418925581105/2199023255552, K2, 1.244606 s, positive, total width <=1.4969899281597854e-15. Runtime speedup 3.93x, **one case only**.
2. near-separating n7 published pair Y=(1.1,.01,1.3), epsilon=1e-5: old lower 1.08, K2, 2.177663 s, negative, width <=6.486358935192379e-9. Optimized lower 12089144022989/10995116277760, K2, 2.184256 s, negative, width <=2.419015617482399e-9. The earlier P47b K0 attempt was INCONCLUSIVE; this is a new numerical certification at K2, **not a new Narain construction**.
3. published n7 Y=(1.1,.23,1.3), epsilon=1e-12: old lower .949, K3, 6.044608 s, negative, width <=1.6296431401088474e-21. Optimized lower 10436578399731/10995116277760, K3, 6.302670 s, negative, width <=1.6002924414758336e-21. Optimized run slightly slower, no speedup.

The n7 near-separating result is a strictly negative enclosure of the implemented infinite Gaussian difference, conditional on the correctness of the theta formula, mpmath.iv rounding and analytic tail bound. It does not establish a novel physics theorem. The zero-separating limit remains a distinct control.

## Critical baseline and novelty assessment
The comparison is against P44 with a manually loose eigenvalue lower bound, **not** against state-of-the-art certified Siegel theta evaluators. The 3.93x improvement is entirely explained by a smaller lattice cutoff, and is not evidence of superior asymptotic complexity or novelty. The six runs are single executions without repeated timing statistics; CPU variation may influence timings. No new prior-art search or independent external benchmark was completed in P49.

## Publication gate
GO: exact bound integrated into complete certificate; six successful runs; near-separating K2 certified; byte-identical source readback.
REVISE: independently repeat runtimes, benchmark credible existing theta algorithms, preserve remote raw logs and CI, examine other difficult matrices and physical normalization.
NO-GO: original certified-theta algorithm theorem, novel Narain spectral distinction, Q1 original physics manuscript.
Next P50: hostile prior-art novelty audit and independent baseline, plus manuscript GO/NO-GO gate. Do not write manuscript unless original contribution survives.
