# P25 — Full-duality indecomposability proof programme

## Objective
Prove or refute integral hyperbolic splitting for coupled T3/T4 under full O(d,d,Z), without relying on bounded projector enumeration. Produce a terminating decision algorithm for rational Narain generalized metrics if possible; otherwise exhibit a precise obstruction to decidability/termination and a rigorous narrower theorem.

## P25.1 independent pinned replay
Recover P23 CI run and artifact, rerun evidence/P24/projector_checker.py verbatim at pinned SHA in fresh Python 3.13/SymPy 1.14 environment. Preserve raw stdout/stderr, exit code, wall time, RSS, SHA256, environment, JSON comparisons and GitHub run ID in evidence/P25 append-only. If workflow listing unavailable, create a workflow that commits its raw logs and verify readback; never claim execution without artifacts.

## P25.2 rational centralizer and integral gluing
For S=JQ, S²=I. Describe End_Q(V_+)×End_Q(V_-) and characterize P commuting with S and J-selfadjoint. Parameterize rational J-orthogonal subspaces of balanced signature, then test integral gluing of L across V_+ and V_- via saturation, Smith normal form and discriminant forms. Seek a finite arithmetic obstruction sufficient for absence of integral hyperbolic projector; rigorously bound denominators/heights if claiming a terminating algorithm.

## P25.3 adversarial controls
Reconstruct all d=3 and d=4 chain G,B with exact rationals. Test hidden products under B-shifts, factorized T-duality, GL(d,Z), and random short O(d,d,Z) words. Verify both positive and negative cases with a second independently written checker. Never infer global nonexistence from a bounded search.

## P25.4 novelty kill tests
Compare projector arithmetic to primitive sublattice splitting, even unimodular indefinite lattices, Nikulin discriminant gluing, rational Narain lattice classifications, and integral matrix conjugacy algorithms. Verify full publisher metadata and append only new verified BibTeX entries. Explicitly distinguish an elementary reformulation from a novel effective theorem.

## Gate
GO only for a mathematically nontrivial independently proved algorithm/obstruction or a rigorous counterexample with established novelty. REVISE for exact partial checks without termination. NO-GO for claimed full T3/T4 indecomposability without proof. No manuscript.
