# P22 — Dimension-uniform exact bounds, adversarial controls, and strict novelty gate
Date 2026-10-26. **Status: partial theorem proved; inverse-spectral rigidity NOT proved.**

## Definitions
Fix integers d>=1,q>=1,h>=1. Let A be a symmetric positive-definite integral d-by-d matrix and C a skew-symmetric integral matrix, all entries bounded in absolute value by h. Set G=A/q, B=C/q. Charges m,n range over Z^d. Define E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n and spin s=m^T n.

## Proposition 1 (uniform rational denominator and spacing, all d)
Put D=q det A, which is a positive integer. Every E(m,n) lies in (1/D) Z. Furthermore D<=Dmax=q d! h^d. Therefore any distinct energy values arising from any TWO backgrounds in this bounded class differ by at least 1/Dmax².

**Proof.** Since A^-1=adj(A)/det A, the generalized metric is
Q=[[q adj(A)/det A, adj(A) C/det A],[-C adj(A)/det A, (A det A-C adj(A) C)/(q det A)]].
Every block has denominator dividing q det A. Thus D E is integral for integral charges. The Leibniz determinant formula gives |det A|<=d! h^d. Two rational energies with denominators D1,D2<=Dmax have nonzero difference with numerator at least one when expressed over D1 D2. QED.

**Limit:** This is a grid spacing for two ALREADY DISTINCT energies. It does not guarantee that unequal full spin-refined spectra first differ below any specified cutoff.

## Proposition 2 (uniform finite charge bounds, all d)
Let L>0 be any certified lower bound for lambda_min(G), U>=lambda_max(G), beta>=||B||2. For E(m,n)<=H, H>=0,
||n||²<=H/L,
||m||²<=2 H U+2 beta² H/L.
This follows from E>=L||n||² and ||m||<=||m+Bn||+beta||n||<=sqrt(UH)+beta sqrt(H/L), then (a+b)²<=2a²+2b². Thus a complete exact search uses n in integer ball of squared radius floor(H/L) and m in integer ball of squared radius floor(2HU+2 beta²H/L).

For the entire arithmetic class without a supplied L, let T=dh. Gershgorin/row norm gives lambda_max(A)<=T. Since det A>=1 and the product of the other d-1 positive eigenvalues is at most T^(d-1), lambda_min(A)>=T^(-(d-1)). Hence one can take L=1/(q T^(d-1)), U=T/q, beta=T/q. Uniform explicit caps:
||n||²<=H q T^(d-1),
||m||²<=2 H T/q+2 H T^(d+1)/q.
These bounds are intentionally loose but rigorous for ALL d,q,h and rational H>=0. They give a terminating algorithm for the finite-window spin-refined spectrum. They are not a universal finite distinguishing cutoff.

## Proposition 3 (finite arithmetic class, but no constructive spectral-rigidity claim)
For fixed d,q,h there are finitely many A,C. Hence the set of first distinguishing energies over pairs whose FULL spin-refined spectra differ is finite and has a maximum, if any such pairs exist. This purely existential statement does NOT supply an effective computable bound or a terminating test for full spectral equality. A program that simply increases H until a difference appears can run forever for genuinely isospectral pairs. Do not call this an effective reconstruction theorem.

## Exact local checks
check.py executed with Python 3.13.5, exit 0, internal runtime 0.3881 seconds, stderr empty. Tested G=I, q=3,h=4 and B01=1/3 for d>=2, all charges in {-1,0,1}^{2d}: d1 9, d2 81, d3 729. All energies had denominator dividing D=q det A, D<=q d! h^d. The finite-box parity relation E_{G,-B}(m,n)=E_{G,+B}(m,-n) with spin reversal passed. For these special low-dimensional controls, no spin asymmetry was detected in the finite box; this is NOT a general equality theorem. d1 factorized T-duality G=2/3 vs G'=3/2 with (m,n) swapped passed on 49 charges. Algebra proves the d1 duality for all charges, independent of test size.

## Negative and adversarial controls
- FALSE: energy-only spectrum uniquely reconstructs a positive quadratic lattice in all dimensions. Conway–Sloane (1992) already give four-dimensional isospectral lattices; these are prior-art controls, not automatically Narain counterexamples.
- FALSE: all dimensions have identical inverse-spectral behavior. Schiemann (1997) proved ternary theta rigidity for positive definite forms, unlike dimension four.
- FALSE: spin-refined equality implies literal equality of (G,B) matrices: d1 factorized T-duality gives distinct G and identical spin-refined spectra under charge exchange.
- FALSE: B-sign energy-only equality implies oriented spin-refined equality: parity reverses spin; P15/P21 supply examples where the spin-refined spectra differ.
- UNSOLVED: effective universal cutoff for unequal FULL spin-refined Narain spectra in the bounded arithmetic class. The denominator gap alone does not resolve it.
- UNSOLVED: inverse reconstruction from unlabelled multiplicities, O(d,d,Z) equivalence, or physically inequivalent CFT classification.
- The all-dimension labelled reconstruction in the previous P22 note is elementary polarization, not novelty.

## Literature matrix (publisher metadata independently checked)
Schiemann, *Mathematische Annalen* 308 (1997) 507–517, DOI 10.1007/s002080050086: rigidity of ternary positive-definite quadratic forms by theta series. Conway and Sloane, *International Mathematics Research Notices* 1992(4), 93–96, DOI 10.1155/S1073792892000102: four-dimensional same-theta examples. Both are already appended and verified in reference/references.bib and reference/verification_register.tsv; no duplicate entries added. The finite-coefficient modular-forms reconstruction method for integral lattices is established prior art; see Magma handbook on theta series as modular forms. These are distinct from the spin-refined Narain inverse problem. Primary-literature coverage is not yet comprehensive.

## Strict publication gate
**PASS**: elementary all-dimension denominator/spacing and complete finite-charge enumeration theorems, plus exact adversarial controls.
**REVISE**: original effective unlabelled spin-refined reconstruction theorem and strong Q1 novelty; neither has been established.
**NO-GO**: claiming a universal effective distinguishing cutoff, full O(d,d,Z) classification, or physical string inequivalence from the current work. No manuscript drafted.

## P23/P24 recommended
P23: perform a hostile novelty kill-test of the dimension-uniform bounds against classical geometry of numbers, modular theta Sturm bounds, and code-CFT literature; independently reproduce all local checkers at a pinned SHA. In parallel, P24 should attack the integral idempotent existence problem with rational centralizer, integral-lattice obstruction and duality-hidden decomposable adversarial examples. Prefer P24 as the stronger original theorem opportunity if P23 finds P22 bounds elementary. Preserve failures append-only; only claim breakthrough if an independently proved nontrivial result survives.
