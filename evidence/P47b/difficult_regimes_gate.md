# P47b individually bounded difficult-regime audit — 2026-10-27

## Execution
Executed /mnt/data/p47b/run.py in two separate processes, each with 28-second timeout and /usr/bin/time resource collection. Both exited 0 before timeout. GitHub source evidence/P47b/run.py independently fetched: Git blob 12ea2edf043877154c815a78f5e638c459bf05dc, equal to local git hash-object; local source SHA256 e622ec4053311c9dd279eeb7e2c7efeed271e4d4f76295fc6947476bd29aaf50. Driver uses local P44 and P46 implementations from P47; those dependencies are not embedded in this driver.

## Case 1: ill-conditioned SPD matrix
n=2, empty graph vs one-edge graph; Y=[[1,.95],[.95,1]], strict rational eigenvalue lower bound .04; Kmax=1; epsilon=1e-8.
P44: BUDGET_EXHAUSTED, elapsed .0011 s (no sign certificate).
P46: K=1 truncated difference [52.3318458952024016640084254018597715155859,52.3318458952024016640084254018597715156701]; analytic tail upper 3701021965.97111937283864602662731097845486; infinite enclosure [-3701021913.63927347763624436261888557659509,3701022018.30296526804104769063573638031464]; INCONCLUSIVE. No contradictory signs; not a successful certification. Wall 3.24 s, RSS 99352 KB, exit 0.
stdout SHA256 a19bc288180c1421cdc1a88db2f32babd0f766c909d37c31039c47832356c67e; resources SHA256 8b7b728d7ef308a9a925b9647f0dac8609d03a334f2312aea867e322136d0780.

## Case 2: near-separating genus-two period
n=7, published P33 graph pair; Y=[[1.1,.01],[.01,1.3]], strict lower bound 1.08; Kmax=0; epsilon=1e-5.
P44: BUDGET_EXHAUSTED, elapsed .0026 s.
P46: K=0 truncated difference [0.00000893553302061824787362189952468816299,0.00000893553302061824787362189952468849092]; analytic tail upper 1562353876.48466225340745749283120555484587; infinite enclosure [-1562353876.48465331787443687458333193294635,1562353876.48467118894047811107907917674540]; INCONCLUSIVE. The positive truncated difference is NOT evidence of a positive infinite difference. Wall 5.95 s, RSS 99596 KB, exit 0.
stdout SHA256 a224227bdb5dead7659af4f7a74444503557c6293afa32cb19a9469b53696be7; resources SHA256 7b08536114d5cfbb810b5eb2a59cdb024f81b0ab2665b150bec0e371cb1fd2ba.

Both stderr files empty, SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Raw logs are local, not yet uploaded to GitHub. No 28-second timeout occurred in these two cases; the earlier P47 whole-batch timeout remains a separate failed completion gate.

## Interpretation
The difficult regimes demonstrate honest failure semantics and severe conservative-tail inflation; they do not demonstrate a new certified distinction, improved efficiency, or robust performance in ill-conditioned settings. A higher cutoff, stronger lattice-tail bounds, or preconditioning is necessary. P46's interval backend is conditionally rigorous under decimal.exp's documented rounding and implementation assumptions, not formally verified.

GO: independently executed bounded difficult-regime tests; explicit inconclusive/budget-exhausted outcomes; byte-identical GitHub driver readback.
REVISE: near-separating K>=2 and ill-conditioned K>=2 under per-case resource budgets, sharper certified bounds, benchmark against established theta evaluators, remote logs and CI.
NO-GO: claims of new positive/negative signs in these regimes, general efficient algorithm, or original Q1 physics paper.
Next P48: derive a sharper bound using an exact rational spectral lower bound closer to the actual eigenvalue, and compare cost against an independent baseline without changing the novelty gate.
