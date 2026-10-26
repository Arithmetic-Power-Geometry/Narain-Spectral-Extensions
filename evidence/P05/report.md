# P05 exact product inheritance — executed 2026-10-26
## Strict gate: REVISE for novelty, PASS for mathematical product lemma and tests
Let Theta_A, Theta_B be locally finite spin-refined series graded by nonnegative energy E and integral conformal spin s. Let S be a common spectator series with a unique E=0 spin=0 vacuum of multiplicity 1, all other states E>0, and nonnegative multiplicities. Suppose Delta=Theta_A-Theta_B vanishes below E=T and has nonzero Laurent coefficient C_T(z). Then (Theta_A-Theta_B)Theta_S has no terms below T and coefficient C_T(z) at T. Proof: convolution; only the spectator vacuum contributes at energy T. This is elementary algebra and not novel independently.

## Reproducible exact tests
Run python3 evidence/P05/check.py (standard library). The test enumerates all zero modes with E<=3 for the P02 two-torus base, then direct-product unit-radius spectator circles. Every spectator integer m,n at E<=3 lies in [-1,1]. For d=3,4,6 the spectator-state totals are 9,65,577; combined per-background E<=3 totals are 127,391,1703. All have leading coefficient 2 z^-1 - 2 z at 3313/1325.

## Failed test and repair (preserved)
Initial test failed the leading-coefficient assertion because Python collections.Counter subtraction truncates negative coefficients. The initial invalid line was delta=p-q; the corrected implementation is delta={key:p[key]-q[key] for key in p.keys()|q.keys()}. This was a test-harness bug, NOT a mathematical counterexample. Corrected rerun PASS. See failure_log.md.

## Adversarial and scope
An unrestricted claim for distinct spectator factors is false: (A tensor B) and (B tensor A) have identical refined spectra by commutativity, even when A and B differ. A signed formal spectator with zero vacuum coefficient annihilates the leading term, but is not a physical nonnegative spectator with unique vacuum. These illustrate why the common physical spectator hypothesis is essential.
A block product does not demonstrate an intrinsically coupled T6 construction. Spectral distinction rules out an orientation-preserving duality that preserves both left/right weights for the given pair, but this run does not exhaustively classify O(d,d;Z) equivalence, and orientation-reversing/parity maps require separate treatment. A six-torus is not a general Calabi-Yau manifold.

## Prior-art collision
Existing Narain partition-function literature uses lattice theta factorization and tensor products; Maloney & Witten (JHEP 10 (2020) 187) and Datta et al. (JHEP 05 (2022) 090) were already verified and registered in P01. Newly inspected: Yahagi, 'Narain CFTs and error-correcting codes on finite fields', JHEP 08 (2022) 058, doi:10.1007/JHEP08(2022)058 (publisher verified); Ando, Kawabata, Nishioka, 'Gauging Z_N symmetries of Narain CFTs', JHEP 02 (2026) 058, doi:10.1007/JHEP02(2026)058 (publisher verified). These further emphasize that lattice construction, gap and projection questions are active prior art. Neither proves the proposed genuinely coupled first-discrepancy theorem; novelty of that future result is not established.
## P06
Seek nonblock-coupled rational G and antisymmetric B in dimensions 3,4,6. Derive rigorous complete energy-box bounds, compute exact first spin-refined differences, attempt duality obstruction and perturbation certificates, and test for reductions to block products. Record failed cases and actual outputs append-only.
