# P14 exact-rational perturbation audit
2026-10-26. Gate REVISE: no open-neighborhood theorem established.

## Actually executed
The exact rational Python checker was run locally under Python 3.13.5; results.json records its stdout. For T3 with H=3: 27 n candidates, 81 m candidates, 125 states, first difference 1164367/582071. For T4 with H=5/2: 65 n candidates, 137 m candidates, 129 states, first difference 9437981/4718325. No central energy level strictly below first discrepancy has a nonzero spin asymmetry. Tested independent B01 and B02 perturbations by +1/10000 and found no earlier difference. No random floating-point inference was used.

## Charge completeness
If L<=lambda_min(G), lambda_max(G)<=U and ||B||2<=beta, E<=H implies ||n||²<=H/L and ||m||<=sqrt(HU)+beta sqrt(H/L). With U<4L the bound ||m||² < H U + beta² H/L +4 beta H is conservative. The code enumerates all integral n and m within these bounds. For an all-entry box ||Delta G_ij||<=r, ||Delta B_ij||<=r, Gershgorin gives Lr >= L0-dr, Ur<=U0+dr, and beta_r<=beta0+dr; positivity holds for sufficiently small r. This is a finite-charge completeness recipe, NOT a certificate that central degeneracy classes remain equal throughout the box.

## Unresolved obstruction
The absence of central spin asymmetry below the threshold does not show equality as rational functions of the independent G and B entries. A central coincidence can split in an arbitrarily small perturbation, potentially creating an earlier first discrepancy. The two tested B directions cannot exclude this. Therefore no radius, no interval enclosure, and no open-neighborhood stability theorem is claimed.

## Negative evidence
No earlier discrepancy found in four tested B perturbations. No counterexample to stability found; equally, no proof of stability obtained. Full symbolic degeneracy-stratification and all-entry interval verification remain unperformed. P13 geometric GL(d,Z) indecomposability is not a substitute for the stability proof.

## Next P15
Execute the T6 coupled search beyond E=2 with independently derived finite-energy norm bounds and exact rational enumeration. Preserve performance/timeouts, null windows, first signed coefficient if found, code and actual outputs; do not extrapolate from a finite search or claim full O(d,d,Z) inequivalence.
