# P04 — Narain CFT physical consistency and projection audit
Date: 2026-10-26. Gate: REVISE.

## Defined observable
In the manuscript's normalization E=pL²+pR² and s=m·n=(pL²-pR²)/2, the toroidal CFT weights are hL=(E+2s)/4 and hR=(E-2s)/4. For d=2 compact bosons, Z=Theta(G,B;tau)/|eta(tau)|^4, with q=exp(2pi i tau), qbar=exp(-2pi i conjugate(tau)), and eta(q)=q^(1/24) product(1-q^k). This is a full compact-boson CFT torus partition function, not a critical string amplitude. The eta denominator contributes the common vacuum shift -d/24 per chirality and all oscillators.

## Modular consistency
T: hL-hR=m·n+N_L-N_R is integer, so torus Z is invariant under tau->tau+1. S: the even unimodular Narain lattice yields the standard Siegel-Narain theta modular covariance that cancels eta's modular weight. This is a literature-backed structural theorem, NOT a fresh independent Poisson-resummation proof or numerical S test. B-sign reversal does not violate modular invariance: each background individually has a modular-invariant torus partition function.

## Rigorous B-sign parity identity
Define charge map (m,n)->(m,-n). E_{-B}(m,-n)=E_B(m,n), while s(m,-n)=-s(m,n). Oscillator left/right interchange preserves degeneracy. Thus Z_{-B}(tau1,tau2)=Z_B(-tau1,tau2), and both agree at tau1=0. Their generic complex-tau partition functions need not agree. The exact leading zero-mode signed difference is -4i sin(2pi tau1) exp(-pi tau2 T), T=3313/1325, with the common eta factor multiplying it in the full compact-boson CFT.

## Projection counterexamples
Spin-zero *primary* projection annihilates the first T coefficient, which has only s=+-1. At one oscillator unit, signed contributions from first threshold to total spin zero cancel. Neither operation alone constitutes a complete string-theory physical-state selection. A physical BRST/GSO/mass-shell analysis requires choice of string model, noncompact sectors, intercepts and possible projections. The source manuscripts do not specify such a construction.

## Distinctions that must not be collapsed
Worldsheet conformal spin hL-hR is the difference of Virasoro weights. It is not target-space angular momentum. Fermionic spin structures classify worldsheet fermion boundary conditions, absent from this purely bosonic Narain calculation. Physical closed-string level matching concerns total left/right contributions, but it is only one of multiple constraints.

## Primary literature and verified bibliographic reuse
Datta, Duary, Kraus, Maity and Maloney, 'Adding flavor to the Narain ensemble,' JHEP 05 (2022) 090, DOI 10.1007/JHEP05(2022)090, publisher https://link.springer.com/article/10.1007/JHEP05(2022)090. Already in reference/references.bib (P01), no duplicate entry added.
Maloney and Witten, 'Averaging over Narain moduli space,' JHEP 10 (2020) 187, DOI 10.1007/JHEP10(2020)187, publisher https://link.springer.com/article/10.1007/JHEP10(2020)187. Already verified and recorded in P01.
Independent contextual corroboration: Narain CFT torus formula and modular properties in primary scholarly literature; no new incomplete bibliography entries added.

## Execution and limitations
Python exact fractions, 729 charges, 39 states each E<=3, first coefficient (+2 at spin -1,-2 at spin +1), B-sign bijection, unrefined cancellation, spin-zero primary and one-descendant cancellation checked. Actual stdout preserved in results.json. No independent numerical S-transform check, no full BRST/GSO cohomology, no string amplitude, no new theorem beyond the already established Narain formalism.

## Verdict
PASS: defined toroidal-CFT identity and exact negative controls.
REVISE: physically projected observables; string model not specified.
NO-GO: claiming the B-sign example proves physical inequivalence of critical strings, string theory itself, or a new modular-invariant construction.

## P05 next
Prove an arbitrary-dimensional product inheritance theorem with careful hypotheses, show where cancellations arise, test exact spectator factors and duality distinctions, then identify whether coupled (nonproduct) higher-dimensional families are necessary for genuine novelty. Preserve code, outputs, negative findings and verified bibliography append-only in evidence/P05; commit only here.
