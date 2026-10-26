# P13 — rigorous GL(d,Z) simultaneous indecomposability
Date: 2026-10-26. Exact calculations with SymPy 1.14.0 and Python 3.13. No full O(d,d,Z) classification.

## Definition
A geometric integral splitting is U in GL(d,Z) and 0<k<d for which U^T G U and U^T B U are both block diagonal with blocks of size k and d-k. G is symmetric positive definite and B antisymmetric. This is narrower than decomposability up to arbitrary Narain T-duality.

## General rational obstruction
Let A=G^-1 B. If a rational basis simultaneously splits G and B into blocks, then A becomes block diagonal in the same basis, so its characteristic polynomial factors over Q. Thus irreducibility over Q is sufficient for rational (hence integral) geometric indecomposability. Reducibility is NOT sufficient for a decomposition.

## T4 complete proof
The exact characteristic polynomial of A is
(351652043925*x^4 + 5547197084*x^2 + 9486400)/351652043925.
SymPy exact factor_list returns a single degree-four factor with multiplicity one, hence irreducible over Q. This rules out every nontrivial rational block decomposition and therefore every GL(4,Z) geometric splitting. A self-contained independent irreducibility certificate (e.g. a suitable modular prime or rational-factor exclusion) is desirable before publication; factor_list is the executed exact computer-algebra certificate.

## T3 complete proof
B has rank two and rational kernel generated primitively by v=(13,0,14)^T. Any simultaneous 1+2 G,B block splitting forces its one-dimensional block into ker(B), hence that rank-one summand is Zv. For an integral direct sum orthogonal with respect to G, the projection P_v(x)=v*(v^T G x)/(v^T G v) must map every integral x to an integral vector. Here v^T G v=365 and (v^T G)/(v^T G v)=(13/365,283/40150,14/365). Already P_v(e1)=v*(13/365) is not integral (first component 169/365). Contradiction. This excludes every GL(3,Z) geometric splitting, not just signed permutations.

## Adversarial controls and limitations
Signed-permutation search checked 48 T3 and 384 T4 matrices, finding no decomposition. These bounded subgroup searches are supportive, not the basis of the proofs. G=diag(2,3,5), B=0 is explicitly decomposable, showing that reducible characteristic polynomials can accompany decompositions.
The GL(d,Z) geometric result does NOT establish nonproduct structure under the larger O(d,d,Z) group, and cannot establish physically inequivalent oriented or unoriented string CFTs. No new bibliographic entries: existing Narain and T-duality sources remain relevant; no additional metadata verified during P13.

## Gate and next
PASS for the precisely defined GL(3,Z) and GL(4,Z) geometric indecomposability propositions; REVISE for full T-duality indecomposability and Q1-level novelty.
P14: study the rational-function degeneracy classes of all charges below the first P07 discrepancy, then either prove a nonzero all-entry perturbation box via rational interval bounds or produce an exact counterexample to stability. Record actual code, stdout, failures, source hashes, references and GitHub readback.
