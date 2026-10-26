# P08 exact static perturbation audit — 2026-10-26
Gate: REVISE. Pointwise tests PASS; requested full interval stability certificate NOT achieved.

The exact-rational checker recomputes P07's connected-chain G,B families at d=3,4,6, and perturbs G[0,0] by +1/10000 for d3/d4. The central thresholds and exact adjacent distinct-level gaps are recorded in results.json. Both perturbations preserve a nonzero leading coefficient +2 at spin +1 and -2 at spin -1; the thresholds shift. These are exact rational, not floating point, findings.

## Rigorous uniform positivity and completeness
For arbitrary simultaneous entrywise symmetric perturbations |delta G_ij|<=r, Gershgorin gives lambda_min(G+delta G)>=89/110-d*r, and lambda_max<=131/110+d*r. For antisymmetric entrywise |delta B_ij|<=r, the operator norm is bounded by beta+(d-1)r, beta=27/182. In particular r<=1/1000 and d<=6 guarantee positivity since 89/110-6/1000>0. Define Lr=89/110-d*r, Ur=131/110+d*r, Br=27/182+(d-1)r. For any state E<=H, ||n||²<=H/Lr and ||m||<=sqrt(H Ur)+Br sqrt(H/Lr). Therefore finite uniform integer norm bounds are floor(H/Lr) for n and any integer bound strictly exceeding H Ur+Br² H/Lr+2 Br H sqrt(Ur/Lr) for m. The code uses the stronger rational upper bound sqrt(Ur/Lr)<2 for its tested central and perturbed points. This is a rigorous uniform charge-completeness recipe, NOT a complete interval energy-ordering certificate.

## Missing interval theorem
A positive adjacent-level gap at the central parameter does NOT by itself prove stability of the first *signed* spectral discrepancy under arbitrary perturbations. Coincident lower-energy levels could split differently across the two backgrounds, introducing an earlier discrepancy. To certify an open neighborhood one must group all lower-energy charges by a parameter-independent pairing or prove exact polynomial/rational-function identities throughout the neighborhood, and bound all remaining competitors using rational interval arithmetic. No such full grouping certificate has been completed here. Hence no nonzero multidimensional stability radius is claimed. In particular, pointwise perturbation +1/10000 is not proof for the whole box of that radius.

## T6
The exact E<=2 run remains negative: 65 states per sign. No search beyond E=2 completed in P08. The absence of a witness below the cutoff does not imply full spectral equivalence.

## Static versus dynamical
Positive definiteness and spectral order stability are static statements about the parameter-dependent quadratic form. They do not provide equations of motion, an effective potential, a time-dependent stability theorem, moduli stabilization or cosmological evidence.

## Literature verification
Existing publisher-verified Narain moduli and duality sources: Groot Nibbelink and Vaudrevange, JHEP 04 (2017) 030, DOI 10.1007/JHEP04(2017)030; Maloney and Witten, JHEP 10 (2020) 187, DOI 10.1007/JHEP10(2020)187. Both already registered, so no duplicate bibliography additions. New external source consulted: Mahmood and Reid-Edwards, 'Torus bundles, automorphisms and T-duality', JHEP 05 (2021) 003, DOI 10.1007/JHEP05(2021)003, publisher metadata verified.

## P09 strict conditional gate
P09 should not invent a cosmological or dynamical theory. Unless a well-motivated action, explicit potential, dynamical variables, evolution equations and relevant boundary conditions are supplied and justified, issue NO-GO for dynamics, document missing ingredients and restrict output to static Narain CFT mathematics. Do not draft unsupported Big Bang or stabilization claims.
