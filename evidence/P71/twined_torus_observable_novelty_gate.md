# P71 — single-observable physical-normalization and novelty kill test
Date: 2026-10-28. Research gate only; no manuscript or P72.

## Candidate (exactly one)
Z_{0,1}(tau,tau-bar;G,B,u) = |eta(tau)|^(-2d) sum_{m,n in Z^d} (-1)^(m.u) q^((E+2m.n)/4) qbar^((E-2m.n)/4), with E=(m+Bn)^T G^-1(m+Bn)+n^T G n and primitive u=e_1. This is the torus trace with insertion of the order-two target-space translation symmetry g|m,n>=(-1)^(m.u)|m,n>. Symmetry marking u is part of the data; differences between differently marked but otherwise identical CFTs are not unmarked inequivalence certificates.

## Normalization and modular completion
For a=0,1 and b=0,1 define Z_{a,b} with winding n in Z^d+a u/2 and insertion (-1)^(b m.u), using same oscillator factor |eta|^(-2d) and quadratic E and spin m.n for fractional winding. The shift is along an isotropic winding direction and the order-two translation is nonanomalous in this lattice realization. With consistent phase conventions, modular T sends (a,b) to (a,a+b) mod 2 because exp(2pi i m.n)=(-1)^(a m.u), and modular S exchanges spatial and temporal holonomies (a,b)->(b,a). The oscillator factor cancels the modular weight of the theta lattice sum; these are covariance relations for the four sectors, NOT invariance of the individual Z_01. A complete normalization proof for all S sectors requires Poisson summation with the precise G,B convention; it is not independently executed here. Consequently modular consistency is provisional, not independently certified. A single twined trace is not by itself a modular invariant partition function. Orbifold Z_orb=(Z00+Z01+Z10+Z11)/2 only after the complete sector consistency and nonanomaly checks.

## Exact internal checks
At tau=i t (t>0), q=qbar=e^(-2pi t), so each charge contributes (-1)^(m.u) exp(-pi t E); this fixes the Boltzmann normalization. The vacuum (m,n)=(0,0) has insertion +1. At a=0, h=m.n is integral, hence the twining trace is T invariant. At a=1, h=m.n0 + (m.u)/2, giving T sector permutation b->b+a. Under (B,n)->(-B,-n), E fixed and spin changes sign while (-1)^(m.u) is unchanged; parity-related spectral asymmetries cannot certify inequivalent unoriented theories.

## Prior art / novelty kill
Kawabata, Nishioka, Okuda, Narain CFTs from quantum codes and their Z2 gauging, JHEP 05 (2024) 133, DOI 10.1007/JHEP05(2024)133, https://doi.org/10.1007/JHEP05%282024%29133 .
Gauging Z_N symmetries of Narain CFTs, JHEP 02 (2026) 058, DOI 10.1007/JHEP02(2026)058, https://link.springer.com/article/10.1007/JHEP02%282026%29058 .
Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, https://doi.org/10.1007/JHEP04%282023%29011 .
Ensemble averages of Z2 orbifold classes of Narain CFTs, JHEP 05 (2024) 240, DOI 10.1007/JHEP05(2024)240, https://link.springer.com/article/10.1007/JHEP05%282024%29240 .
The symmetry-twined torus observable, shift sectors, and gauging are established prior art. No pair of inequivalent theories with matching unrefined genus-one and genus-two observables and different marked twining traces has been identified. Distinct symmetry markings are an important false-positive risk. No novel physical theorem established.

## Strict gate
Observable physical definition: GO (standard). Oscillator normalization: GO (standard). Modular T sector covariance: GO (algebraic). Modular S sector covariance: REVISE (not independently reproduced). Beyond-known-genus-two discrimination: NO-GO (no candidate pair). Novelty: NO-GO for observable alone. Q1 manuscript: NO-GO. Stop before P72. P61/P63/P69 failures remain preserved.
