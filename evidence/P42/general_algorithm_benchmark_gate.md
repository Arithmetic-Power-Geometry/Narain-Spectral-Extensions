# P42 — generalized certified genus-two Gaussian evaluator: first benchmark gate

Date: 2026-10-27. Scope: graph-state Construction-A code-CFT Gaussian expression at purely imaginary genus-two period matrix Omega=iY with rational decimal SPD Y, not general complex period matrices or arbitrary Narain backgrounds.

## Real execution and byte-identical source provenance
Executed local source /mnt/data/p42/certified_theta.py with mpmath 1.3.0; committed same bytes at evidence/P42/certified_theta.py. Local Git blob 106eca314d49bfd0f68fc3853ff2ba925c290eef; remote GitHub readback blob is IDENTICAL. SHA256 source e46f8a892a039afadae152a254396e21a5728747c9847450a06d40e1b924895e; stdout 18e2eda6deb88da9f92cae6fc922ca3f4b7476062fdc710aeb83a2656868605b; stderr empty e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources b8577ad3161ac0196b50150eb71209d2bcfa327f30f014a971f6223322502303. Wall 11.46s, max RSS 99604 KB, exit 0; internal elapsed 10.382s. Raw stdout/stderr/resources exist locally and are NOT yet remotely uploaded; hashes do not establish remote presence.

## Correctness statement for implemented Gaussian expression
For a graph on n vertices, generate 2^n words (x,Ax mod 2). For each ordered pair of words, multiply n local theta factors. Each local theta is a sum over four integers of exp(-pi*[L^T Y L+R^T Y R]), where L=a+alpha/2+b+beta/2, R=a+alpha/2-b-beta/2. At Y positive definite with lambda_min(Y)>lambda>0, use c=2*pi*lambda. Each omitted term is dominated by exp(-c sum_j (m_j+s_j)^2) for s_j in {0,1/2}. For S=1+2exp(-c/4)/(1-exp(-c)), T_K=2exp(-c(K+1/2)^2)/(1-exp(-2c(K+1/2))), the local truncation tail is <=4*T_K*S^3 and the full difference of two n-site graph sums is <=2*4^n*n*(4*T_K*S^3)*(S^4)^(n-1). Outward-rounded mpmath.iv arithmetic encloses finite evaluations and analytic bound. If upper(delta_interval)+upper(tail_interval)<0, the infinite difference is negative; similarly for positive. Otherwise report INCONCLUSIVE. A zero/equal input must never be incorrectly certified as unequal.

## Actual benchmark cases
All use Y=[[1.1,.23],[.23,1.3]], lambda=.949, 35 interval decimal digits:
- n=1, empty vs same, K=2: INCONCLUSIVE, interval straddles zero; tail <=1.279e-14.
- n=2, empty vs one edge, K=2: CERTIFIED_POSITIVE; delta approximately +1.5580897577535809449, tail <=4.543e-13.
- n=4, empty vs one edge, K=2: CERTIFIED_POSITIVE; delta approximately +4.7218753519128926778, tail <=2.866e-10.
- n=7, published 13-edge graph vs itself, K=2: INCONCLUSIVE; tail <=2.810e-6.
- n=7, published 13-edge vs 11-edge graph, K=3: CERTIFIED_NEGATIVE; delta enclosed in [-.00222049812364534235672839766455116582,-.00222049812364534235672839766445378899], tail <=8.149e-22.

## Algorithmic cost
Direct site precomputation is 16*(2K+1)^4 Gaussian summands. Each graph requires 4^n ordered codeword pairs and n interval multiplications, so the naive evaluation cost is O((2K+1)^4+ n*4^n) arithmetic operations at a fixed precision; arithmetic bit-complexity, precision selection and exponential input generation must be included for a full complexity theorem. Correctness is conditional on valid graph inputs and a verified strict positive-definite eigenvalue lower bound.

## Known gaps / hostile audit
1. The current source checks lambda_min(Y)>lambda using mp.mpf decimal arithmetic, not exact rational determinant comparison or interval arithmetic. It is reliable for the supplied inputs with a wide margin but is NOT a complete certified validation for near-boundary arbitrary inputs. Must repair before claiming a universal correctness theorem.
2. Does not implement adaptive epsilon-based stopping or all non-purely-imaginary Omega; it can return INCONCLUSIVE for equal inputs.
3. Five tests are smoke controls, not statistically meaningful multi-instance benchmarking; no performance comparison against established Siegel-theta libraries.
4. No independent generic implementation or pinned CI yet; earlier P27–P29 CI readback still unresolved.
5. Physical theta-map and normalization remain contingent on published conventions; no original physics discovery.
6. P33 seven-vertex example and genus-two distinction are published prior art; certified Gaussian summation bounds are standard and novelty is unproven.

## Strict gate
GO: working generalized interval prototype and five successful controls, byte-identical executed source on GitHub.
REVISE: exact SPD validation, adaptive error budgeting, independent generic replay, full raw execution uploads, multi-instance baselines, remote pinned CI and rigorous novelty search.
NO-GO: original general algorithm theorem, novel counterexample, original Q1 theoretical-physics manuscript.
Next P43 should fix exact SPD preconditions and add epsilon-based adaptive certification with explicit failure and termination semantics; do not draft a paper.
