# P19–P23 theorem-development blueprint — 2026-10-26

## P19 reproducibility gate (current)
Original P01-P09 sources are unchanged. P18 runner at evidence/P18/run_originals.py executes nine originals verbatim, records pinned checkout SHA, Python/platform, per-source SHA256, stdout/stderr and their SHA256, exit status, runtime and recursive JSON differences. P19 GitHub Actions workflow is configured to run on its own creation/push, upload the p19-original-checker-logs artifact and commit evidence/P19/ci_run back to THIS repository. **Until an actual CI commit or artifact is fetched, no run success is claimed.** Local P02 copied source executed with exit 0 and preserved stdout. Distinguish 'JSON schema mismatch' from mathematical assertion failure. Verify Paper I 68-row interval asset by obtaining its original data and checker; do not reconstruct missing rows.

Gate P19 GO: 9/9 actual verbatim logs + hashes and pinned SHA; every failure classified, corrected only in new source (never rewrite historical logs); P02 full polynomial certificate and Paper I interval independently verified; bibliographic register structurally consistent and externally corroborated. Otherwise REVISE.

## P20 — Full O(d,d,Z) decomposition
Let J=[0 I;I 0] on Z^(2d), Q(G,B) be the positive definite generalized metric. Define product decomposition as an integral primitive J-orthogonal direct sum into even unimodular hyperbolic charge sublattices, simultaneously Q-orthogonal; equivalently find a nontrivial integral idempotent P with P²=P, P^T J=J P, P^T Q=Q P, with J restricted to both summands unimodular of signatures (k,k) and (d-k,d-k). Necessity/sufficiency require proof and careful distinction of coordinate GL(d,Z) from full O(d,d,Z). The existence of real/rational projectors does NOT imply integral primitive splitting. Construct decomposable adversarial examples by O(d,d,Z) conjugating block backgrounds to dense coupled-looking G,B; these MUST classify decomposable. Search exact modular obstructions or finite bounded enumeration with explicit limits, then seek a terminating algorithm or prove undecidability/complexity as appropriate. Do not call bounded non-detection a global proof.

Gate P20 GO only for a fully proved and independently checked criterion or explicit O(d,d,Z) decomposition counterexample; otherwise REVISE.

## P21 — Robust spectral separation
Avoid demanding an unchanged first energy threshold. Define finite-window distinguishability: existence of some (E,s) with different spin-refined multiplicities below a fixed H. First prove/disprove an open all-entry perturbation box for T3/T4/T6 by enumerating a uniform finite charge superset using Gershgorin L(r),U(r),beta(r). Classify equalities as rational functions in independent symmetric G entries and skew B entries, separate forced identities from accidental collisions, and bound distinct energy branches with rational interval arithmetic. For any claimed radius, prove exact nonvanishing on the entire box; a finite set of tested directions is insufficient. Adversarial controls: accidental degeneracy splitting, eigenvalue-bound boundary, rational near-collisions, parity-conjugate branches.

Gate P21 GO: explicit positive rational radius with checkable interval certificate or exact counterexample disproving the proposed theorem. REVISE if only pointwise experiments.

## P22 — Finite inverse reconstruction
State a bounded arithmetic class (dimension d, denominator and height bounds for G,B, positivity window, fixed equivalence relation). Finite class modulo specified equivalence may yield a finite distinguishing cutoff by enumeration, but this is trivial unless constructive bounds/complexity are nontrivial. Seek effective spectral separation bound and reconstruction procedure, or counterexamples with equal finite data. Contrast orientation-preserving O(d,d,Z), orientation reversal, and energy-only vs spin-refined equivalence. Do not infer a full CFT classification from zero-mode data. Adversarial tests: code-CFT isospectral pairs, exact T-dual pairs, GL-split backgrounds hidden by dualities, B-sign parity, arbitrarily close rational metrics.

Gate P22 GO: independently proved nontrivial finite theorem with explicit effective bounds and a novelty kill-test against theta series and inverse spectral literature; otherwise REVISE/NO-GO.

## P23 — final referee/novelty gate
Independent checker reproduction on fresh checkout; exact rational certificates; independent symbolic proof checks; primary publisher/DOI metadata audit; source-claim matrix; no physical inequivalence without the necessary oriented CFT definition and duality analysis. Compare against Dymarsky–Shapere (2021), Henriksson–Kakkar–McPeak (2023), Narain (1986), and arithmetic quadratic-form/theta-series inverse spectral results. Ask a hostile reviewer to falsify every theorem. Journal fit only after an original general theorem or substantive new algorithm survives. No manuscript before essential gates PASS.

## Append-only discipline
Write evidence/P20..P23 with code, actual stdout/stderr, exact source SHA256, timings, failures, counterexamples, tests, bibliographic register updates and explicit negative results. Commit ONLY to Arithmetic-Power-Geometry/Narain-Spectral-Extensions. Never silently replace earlier evidence or write to String-Theory source repo.
