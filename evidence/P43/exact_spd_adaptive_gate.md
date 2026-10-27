# P43 exact-SPD and bounded adaptive evaluator — execution and gate

Date: 2026-10-27. Builds on byte-identical P42 source evidence/P42/certified_theta.py; new evidence/P43/adaptive.py was committed byte-identically to local executed file, Git blob ed8f31c2bfe80ab32e10719d8cc1aae2de8cc250.

## Exact precondition
For rational decimal Y=[[a,b],[b,d]] and rational lower bound l>0, check a-l>0 and (a-l)(d-l)-b^2>0 in Python fractions.Fraction. By Sylvester's criterion this proves Y-l I positive definite without floating-point boundary errors. Invalid matrices are rejected.

## Bounded adaptive logic
For k=0,...,max_k, evaluate the P42 analytic bound on the difference of two infinite Gaussian sums; only compute expensive interval theta when the tail bound <= epsilon. Return CERTIFIED_POSITIVE, CERTIFIED_NEGATIVE or INCONCLUSIVE based on the outward-rounded interval widened by the analytic tail; if no cutoff meets the analytic tail budget, return BUDGET_EXHAUSTED. Finite max_k gives guaranteed termination, including on equal inputs. The algorithm does NOT guarantee a sign certificate or total interval width <= epsilon.

## Actual local execution
Working directory /mnt/data/p43, Python mpmath 1.3.0. Exit 0; wall 10.24 s; peak RSS 99592 KB; stderr empty. SHA256 executed source 7a0a4e41b4bc2bcd9391b18f7cbb42e6b3b13b7e800de1fcadf5eccb58c0c7f9, stdout ee5aa7bb8ce690a5e7e62fa5c34f794c430b6f9a25fc14adb53bb6a2c4faad87, stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, resources d8355a7f3b29d2ea4545058dd4b9fbaa3654977d55c50e92e6a7f5f1519a7647. Raw files remain local; no claim of remote log upload.

Tests, Y=[[1.1,.23],[.23,1.3]], lambda=.949, interval dps=35:
- n=2, empty vs one edge, eps=1e-8, max_k=2: CERTIFIED_POSITIVE, k=2, tail <=4.543e-13, interval near +1.55808975775358.
- n=7, published P33 pair, eps=1e-12, max_k=3: CERTIFIED_NEGATIVE, k=3, tail <=8.149e-22, interval near -0.0022204981236453423567.
- n=1 identical empty graphs, eps=1e-8, max_k=2: INCONCLUSIVE, no false separation.
- n=7, eps=1e-50, max_k=1: BUDGET_EXHAUSTED, no false certificate.
- singular Y=[[1,1],[1,1]] with lambda=.1: REJECTED_EXACTLY.
- Y=[[1,.2],[.2,1]] with invalid lambda=1.1: REJECTED_EXACTLY.

## Soundness and complexity limits
The exact SPD test closes P42's identified near-boundary vulnerability. Conditional on correct interval-library outward rounding and P42's Gaussian tail inequality, each positive/negative status encloses the true sign of the *implemented* infinite Gaussian difference. The bounded loop terminates for finite max_k, but cannot guarantee any nonzero separation even when the exact difference is nonzero at an arbitrarily small scale. Naive work O(sum_{k<=max_k} 16(2k+1)^4 + n4^n) for evaluated cutoffs; this prototype evaluates theta only at first k meeting tail budget, so upper bound O(16(2K+1)^4+n4^n) at selected K plus O(max_k) tail checks, fixed precision.

Remaining gaps: epsilon controls only analytic tail, not total interval diameter; the input graph validity is not comprehensively validated before evaluation; mpmath.iv is a software dependency whose rounding guarantee needs independent verification; no independent generic evaluator, multi-instance performance comparison, pinned CI, or novel algorithmic theorem. The code only supports purely imaginary genus-two period matrices and graph-state code construction. Physical interpretation and novelty remain constrained by Dymarsky–Shapere 2021 and Henriksson–Kakkar–McPeak 2023.

## Gate
GO exact rational SPD validation, bounded adaptive cutoff, explicit failure statuses, six successful controls, byte-identical committed executed source.
REVISE full epsilon enclosure including rounding, input validation, independent implementation, CI, performance baselines, physical map audit.
NO-GO novel inverse-spectral theorem, new genus-two distinction, original Q1 physics paper or manuscript.
Next P44: total interval-width epsilon contract and independent edge-case/property tests, then prior-art comparison. No manuscript.
