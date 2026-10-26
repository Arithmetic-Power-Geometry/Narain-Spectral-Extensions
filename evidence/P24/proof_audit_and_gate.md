# P24 exact projector audit — 2026-10-26

## CI recovery
P23 GitHub Actions CI matrix evidence/P23/ci_run/matrix.json was queried by GitHub contents API; returned NOT_FOUND. The connector exposes fetch by run/job ID but no listing of all push-triggered runs, and no run ID was available. Therefore P23 clean-room replay remains **UNVERIFIED**. Do not equate workflow creation with execution.

## Exact local execution
Python 3.13.5, SymPy 1.14.0. The original locally executed prototype (not byte-identical to committed cleaned checker) exited 0; stderr empty; wall 1.90 seconds; peak RSS 129932 KB; internal runtime 0.07988 seconds. Results: for d=3 and 4, (JQ)^2=I and charpoly(JQ)=(t-1)^d(t+1)^d; both canonical rational eigenspace projectors (I±JQ)/2 are J- and Q-selfadjoint but nonintegral. Positive product control d=3: rank-2 integral projector survived B-shift and combined B-shift + GL(3,Z) change. A cleaned exact checker, evidence/P24/projector_checker.py, was committed; a pinned byte-identical CI replay of this committed version is still required. This distinction is important provenance.

## Correct necessary-and-sufficient criterion
Let L=Z^(2d), J=[[0,I],[I,0]], Q rational positive-definite satisfying QJQ=J. A nontrivial Narain product split of rank (k,k) exists iff there is an integer matrix P with:
1. P²=P, 0<rank(P)<2d, rank(P)=2k with 1<=k<d.
2. P^T J=J P (J-orthogonal projector).
3. P^T Q=Q P (energy orthogonal projector).
4. The restriction of J to P(L) has signature (k,k), and P(L) is even unimodular (equivalently the rank-2k summand has a J-Gram matrix with determinant ±1 and the correct signature/parity).
Since P is integral idempotent, L=P(L)⊕ker(P) as free abelian groups, and J-selfadjointness makes the summands J-orthogonal. As J on L is even unimodular, each summand is even unimodular. In particular its indefinite signature must be balanced, and classification gives U^k. Conversely any integral J-orthogonal Q-orthogonal product decomposition gives P. This is an equivalence/reformulation, not a novel terminating decision algorithm.

Note: The even-unimodular and signature conditions cannot be dropped; a rational positive/negative spectral projector is not a hyperbolic product projector. Rational idempotents without integral gluing do not establish an integral split.

## Exact full-duality covariance
For T in O(J,Z), Q'=T^T Q T and P'=T^-1 P T. Then P' is integer idempotent and P'^T J=J P', P'^T Q'=Q' P'. Thus the criterion is invariant under all integral T-dualities, not merely geometric GL(d,Z) transformations. The explicit positive control uses an integral B-shift T=[[I,-K],[0,I]] with K skew integral, and W=diag(U^-T,U) for U=I+E_01. Both satisfy T^T J T=J and W^T J W=J; the transformed rank-two P remains integral and passes all four identities. The local exact computation verified this.

## Negative results
- The canonical projectors (I±JQ)/2 always exist over Q for rational Q, but their images are J-positive/J-negative definite, not hyperbolic. Their nonintegrality in T3/T4 proves NOTHING about other integral hyperbolic projectors.
- Irreducibility of charpoly(JQ) is impossible: (JQ)^2=I, so charpoly=(t-1)^d(t+1)^d.
- No proof that the coupled T3/T4 backgrounds lack other integral hyperbolic projectors.
- No effective terminating arbitrary-d algorithm or new novelty claim.
- B-shift/GL positive controls prove that a correct search must detect hidden products, not that every hidden product has been found.
- Original P23 CI artifacts still missing, so that prerequisite is unresolved.

## Literature and novelty
Narain's lattice/moduli framework, Maharana–Schwarz O(d,d) duality, and Hosono–Lian–Oguiso–Yau rational Narain lattices and double cosets are direct prior art. Recent Narain code lattice gluing work also makes lattice-gluing originality a high bar. No bibliographic entry added without independently verifying full publisher metadata. The exact projector equivalence is a direct lattice splitting characterization, not established as novel.

## Strict gate
**GO** for correctness of exact projector characterization and adversarial positive controls.
**REVISE** for full T3/T4 indecomposability, an effective terminating decision algorithm, and a comprehensive novelty proof.
**NO-GO** for manuscript or breakthrough claims.
