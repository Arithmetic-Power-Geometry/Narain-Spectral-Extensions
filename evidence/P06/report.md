# P06 — coupled rational Narain audit (2026-10-26)
## Decision: REVISE / NO-GO for breakthrough
Three rational connected-chain backgrounds d=3,4,6: G_ii=1, G_i,i+1=1/(10+i) (zero-based i), B_i,i+1=1/(13+i), B_i+1,i=-B_i,i+1; all other offdiagonals zero. Each G is strictly diagonally dominant, symmetric positive definite. These are coordinate-coupled, but no proof of GL(d,Z) indecomposability or O(d,d;Z) inequivalence is claimed.
E_B(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n, s=m·n.
For each d, Gershgorin eigenvalues lie in [L,U], where L=1-max row offdiagonal absolute sum >=4/5 and U<=6/5. The infinity norm of B is <=1/5. E<=2 implies ||n||²<=2/L<=5/2, so integer norm²<=2. Also ||m||<=sqrt(2U)+||B||_2 sqrt(2/L). Since ||B||_2<=sqrt(||B||_1||B||_infty)<=1/5, this is <2; hence integer ||m||²<=3. The code conservatively enumerates norm²<=4, ensuring completeness. All computations exact Fraction; no float rounding.
Executed output: d3: 19 n vectors, 33 m vectors, 29 states per sign; d4: 33 n, 89 m, 41 states; d6: 73 n, 485 m, 65 states. No spin-refined B-sign difference at or below E=2 in any case. The universal bijection (m,n)->(m,-n) proves unrefined energy equality and spin reversal for all energies, but NOT spin-refined equality at higher energies.
## Negative findings and failed novelty hypotheses
1. Nonzero offdiagonal entries do not prove irreducibility under integer basis change. Status: OPEN.
2. A genuine first difference at E<=2 was NOT found. Status: negative exact result, retained.
3. No full O(d,d;Z) search, obstruction or classification was executed. Status: OPEN.
4. Static parameter stability was not certified. Status: OPEN.
5. No result here supports Calabi-Yau or cosmological claims.
## Literature
Groot Nibbelink and Vaudrevange, 'T-duality orbifolds of heterotic Narain compactifications', JHEP 04 (2017) 030, DOI 10.1007/JHEP04(2017)030, publisher https://link.springer.com/article/10.1007/JHEP04(2017)030. Primary publisher metadata verified 2026-10-26. It establishes existing generalized metric and T-duality machinery; constructing a non-diagonal rational G,B is not inherently novel.
## P07 next
Study necessary/sufficient conditions for B-sign spin-refined equivalence, including orientation-reversing integral automorphisms, exact rational search for a coupled witness beyond E=2, a rigorous complete charge bound, and O(d,d;Z) obstructions. Do not claim new theorem until stronger prior-art kill tests and independent verification.
