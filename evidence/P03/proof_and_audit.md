# P03 — all-orders oscillator factor and projection caveats
Date: 2026-10-26
Gate: REVISE for physical/publication novelty; PASS for formal common-factor theorem.

## Definitions and conventions
For a toroidal CFT with d compact free bosons let q=exp(2pi i tau), qbar=exp(-2pi i bartau), with Narain zero-mode weights hL=pL^2/2, hR=pR^2/2 and integer primary spin s=hL-hR=m.n. In the manuscripts' convention E=2(hL+hR). Define formal zero-mode series Theta_±=sum_{m,n} X^E Z^s, where exponents E are real and locally finite below any finite cutoff. Let Delta0=Theta_+-Theta_-.
For oscillator levels (r,t) in nonnegative integers, A_d(q,qbar)=prod_{k>=1}(1-q^k)^(-d)(1-qbar^k)^(-d). Oscillator dressing sends (E,s) to (E+2(r+t),s+r-t), multiplicity a_d(r)a_d(t), where a_d(k) is coefficient of prod_{j>=1}(1-q^j)^(-d). The Dedekind eta vacuum factors q^(-d/24) qbar^(-d/24) are common shifts; keep them explicit for modular/physical interpretations.

## Theorem (common-factor first-difference preservation)
Suppose Delta0 has no terms at E<T and nonzero coefficient Laurent polynomial C_T(Z) at E=T. Suppose a common dressing A has only nonnegative E-shifts and its zero-shift term equals 1. Then A Delta0 has no terms below T and its coefficient at T is exactly C_T(Z). Proof: convolution at E<T is empty because both input series have no negative oscillator energy; at E=T only the zero-shift oscillator term can contribute, and it is 1. This is an elementary filtered formal-series lemma, NOT a novel string-theory result.

## Exact example
At b=1/5 the source pair has T=3313/1325 and C_T(Z)=2 Z^(-1)-2 Z^(+1). The d=2 oscillator coefficients for a single chirality at levels 0..8 are [1,2,5,10,20,36,65,110,185]. A separate exact rational Python run checked levels 0..8 and found the first coefficient unchanged.

## Projections and negative controls
P0 (spin-zero projection) kills C_T, because it contains only Z^(-1) and Z^(+1). Thus a projected leading threshold is NOT necessarily T. After one oscillator level, contributions at E=T+2 and spin zero cancel in the signed difference: (+2 from s=-1, r=1,t=0) + (-2 from s=+1,r=0,t=1)=0. This does not establish that *every* physical level-matched observable agrees: higher zero-mode energies may contribute, and physical string constraints are sector-dependent.
For the chosen B-sign pair the unrefined spectrum is exactly equal by n->-n with B sign flip (energy reflection), so setting Z=1 annihilates Delta0 globally, not just below E=3. Spin-refined data are necessary for this witness.
A spin-zero selection on full descendants is only a mathematical toy projection; it is NOT by itself a complete closed-string physical-state projection. Level matching and on-shell conditions depend on string theory and sectors, intercepts and ghosts. The physical interpretation remains OPEN for P04.

## Literature collision
Datta, Duary, Kraus, Maity and Maloney (JHEP 05 (2022) 090, doi:10.1007/JHEP05(2022)090), sections 2 and equations 2.3-2.4, explicitly give L0=pL^2/2+N, L0bar=pR^2/2+Nbar and Z=theta/|eta|^(2d). This independently establishes the oscillator factor as standard, and rules out claiming its introduction as novel. Publisher metadata and original article verified 2026-10-26.
Additional source: arXiv:2102.12509 (preprint of the same already-registered paper); not added as a duplicate bibliographic entry.

## Reproducibility
Run python3 evidence/P03/check.py (Python 3 standard library). Exact fractions throughout. Results captured in results.json. The GitHub copy was checked against recorded output fields; a local source-equivalent script was executed. Tests do not certify a physical string amplitude.

## Gate and next
Formal theorem PASS. Publication-level novelty and physical projection REVISE. P04: specify bosonic versus heterotic/superstring sectors, modular properties, zero-point energies, ghosts and GSO/level-matching; calculate whether a physically meaningful refined observable retains or loses the witness, without confusing zero-mode spin with worldsheet fermionic spin structure. Preserve positive and negative results.
