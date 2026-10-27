# P48 exact rational eigenvalue-bound optimization — analytic baseline gate (2026-10-27)

## Executed artifact and provenance
evidence/P48/bound_benchmark.py was executed locally at /mnt/data/p48/bound_benchmark.py, and independently fetched after GitHub commit. Local and remote Git blob: 0eccf5d3c808174c5c6fc165eac531c8b32595f6, byte-identical.
SHA256 source 32a40714a4f48b247e7a6ad93637e999ea6222a856056604fbedd38950312845; stdout 3acd74d700b84caa479401916bcd84ea4a2d4d5070b9e640bb5808b14170c5c3; stderr empty e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 6827c1bbb9eef7084be0fe2c1b77dad74001119a408dfa4bdbeceb37ac313396. Exit 0, wall 1.38s, peak RSS 99468 KB. Raw logs local, not remotely uploaded.

## Method
For symmetric rational Y=[[a,b],[b,d]], exact Fraction arithmetic checks a>0 and ad>b². Binary bisection for 40 steps produces rational l with l>0, a-l>0, (a-l)(d-l)>b², hence Y-l I strictly positive definite. The same existing P42 analytic tail formula is evaluated with the old user-supplied l and the optimized rational l, for K=0,...,4, at 35 interval decimal digits. Cutoff is first K with 2*tail_upper <= user epsilon, and NONE when not attained by K4. The source converts interval tail endpoints to Python float for *benchmark display and threshold comparison only*. This is NOT a new certification path: for a rigorous certificate, compare outward-rounded interval endpoints against exact rational epsilon as P44 does.

## Results
Case | n | Y | old l | optimized l | first K old | first K optimized | old/new tail at K2
Published seven-vertex pair | 7 | (1.1,.23,1.3) | .949 | 10436578399731/10995116277760 | 3 | 3 | 1.01064312891
Near separating | 7 | (1.1,.01,1.3) | 1.08 | 12089144022989/10995116277760 | 2 | 2 | 2.68140432344
Ill conditioned | 2 | (1,.95,1) | .04 | 13743895347/274877906944 | NONE by K4 | NONE by K4 | 5.97143970054
Diagonal | 2 | (1.1,0,1.3) | .5 | 2418925581105/2199023255552 | 3 | 2 | ~2.20161216569e11

Ill-conditioned K4 tails: old 2.37278305137e7, optimized 1.73829895388e6, still too large. Three non-SPD matrices (singular, zero-leading-entry, indefinite) rejected exactly.

## Critical interpretation
The improvement comes from replacing a deliberately loose eigenvalue lower bound by a tight rational bound. This is standard spectral numerical analysis, not original research. It improves the analytic upper bound but does not by itself improve actual theta-evaluation runtime or provide new spectral distinctions. The original P47b ill-conditioned and near-separating tests were inconclusive at low K; this benchmark does not reverse those statuses. Float conversions are non-certifying and must be removed from any future theorem-level acceptance decision.

## Gate
GO: exact rational spectral optimization, four analytic benchmark regimes, three exact invalid-input rejections, byte-identical GitHub source.
REVISE: integrate into total-width P44 evaluator using fully interval/rational comparisons; execute actual full theta evaluations at changed cutoffs; independent baseline against published certified Siegel theta algorithms; CI, raw log preservation.
NO-GO: novel algorithm, improved asymptotic complexity, original inverse-spectral theorem, Q1 manuscript.
Next P49: full runtime and total-width evaluation with optimized bounds, then independent state-of-the-art literature and implementation comparison. No manuscript.
