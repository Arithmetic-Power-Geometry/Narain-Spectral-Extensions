# P27 — Dimension-uniform chain Narain indecomposability (2026-10-27)

## Result and precise scope
**Mathematical GO, novelty REVISE/NO-GO.** For EVERY integer d>=2, the rational chain background
G_ii=1, G_i,i+1=G_i+1,i=1/(10+i); B_i,i+1=1/(13+i), B_i+1,i=-1/(13+i) (zero-based indices), other entries zero,
has NO nontrivial integral direct-sum decomposition simultaneously orthogonal for J=[[0,I],[I,0]] and the Narain positive generalized metric Q. Consequently it has no nontrivial integral J- and Q-selfadjoint idempotent, even after any O(d,d;Z) duality. This is a charge-lattice splitting statement, NOT proof of arbitrary physical CFT irreducibility.

## Complete dimension-free proof
Let a_i=1/(10+i), b_i=1/(13+i). In every dimension d>=2, maximum off-diagonal row sums of G and B are <1/5 and <1/6 respectively. Thus 4/5 I < G < 6/5 I and ||B||_2<1/6, ||G^-1||_2<5/4.

Let lambda be the minimum nonzero energy E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. We prove lambda>=1:
- If ||n||²>=2, E> (4/5)*2>1.
- If ||n||²=1, n=±e_i and n^T G n=1, so E>=1.
- If n=0 and ||m||²>=2, E>(5/6)*2>1.
- If n=0 and ||m||²=1, m=±e_i and (G^-1)_ii>=1 by Schur complement (since G_ii=1), so E>=1.
Therefore lambda>=1.

Define 3d-1 positive-orientation witness vectors: p_i=(e_i,0), w_i=(0,e_i), and c_i=(0,e_i-e_(i+1)), i=0,...,d-2. Their negatives may also be included.

All witnesses have E<2<=2lambda:
1. E(p_i)=(G^-1)_ii<5/4<2.
2. E(w_i)=1+(B e_i)^T G^-1 (B e_i) <=1+(5/4)*2/13²<2 (each column B has at most two entries, each magnitude <=1/13).
3. For c_i, n=e_i-e_(i+1), n^T G n=2-2/(10+i). The vector Bn has at most four nonzero coordinates, each magnitude <=1/(12+i), including boundaries, hence ||Bn||²<=4/(12+i)². Thus E(c_i)<2-2/(10+i)+5/(12+i)²<2, because 5(10+i)<2(12+i)² for every integer i>=0 (difference is 2i²+43i+238>0).

The p_i,w_i are a full integral basis, so the short witnesses span Q^(2d). Under J, J(p_i,w_i)=1; J(p_i,c_i)=1 and J(p_(i+1),c_i)=-1. These edges connect the entire set of witnesses into one graph. The general short-vector obstruction from P25 applies: in any simultaneous integral J- and Q-orthogonal decomposition, each E<2lambda witness belongs to one summand; nonzero J-pairing forces connected witnesses into the same summand; since p_i,w_i span, the complementary summand is zero. This rules out ANY nontrivial integral orthogonal split.

If T in O(d,d;Z), Q'=T^TQT and P'=T^-1PT; the obstruction is invariant under full integral T-duality. QED.

**This proof is not an induction and does not depend on exhaustive 3^(2d) enumeration.** The explicit 3d-1 witnesses and inequalities apply for all d>=2.

## Independent exact tests
A local SymPy 1.14.0 checker evaluated every p_i,w_i,c_i with the exact rational inverse G^-1 for d=2,3,4,5,6,8,10,12,16,20,30; all E<2. Actual local stdout, stderr, resource and SHA256 are preserved in evidence/P27. Wall 2.31 s; peak RSS 128788 KB; exit 0; stderr empty. This supports but does not replace the symbolic proof.

## Novelty kill test
The proof is a short-vector connectivity sufficient condition. Eichler–Kneser orthogonal indecomposable lattice decomposition already uses connected indecomposable vectors; see https://www.geotop-bielefeld.de/node/830 and https://www.math.rwth-aachen.de/~Markus.Kirschmer/papers/herm.pdf. Nikulin 1980 (DOI 10.1070/IM1980v014n01ABEH001060) supplies classical discriminant-gluing theory. Our two-form J/Q certificate and explicit all-dimensional Narain family are not identical to those results, but novelty beyond this elementary adaptation is NOT established. **NO-GO for a breakthrough or Q1 manuscript** without an independent primary-source novelty proof and a nontrivial stronger result.

## CI recovery
P25 and P26 pinned CI matrices at evidence/P25/ci_run/matrix.json and evidence/P26/ci_run/matrix.json returned NOT_FOUND at the start of P27. Therefore CI recovery is not verified. A workflow definition is not an executed job. P27 local evidence is authentic but remote byte-identical replay remains pending. P23 semantic failure was previously diagnosed as environment Python version mismatch; preserve its failed status.

## P28
1. Execute pinned P27 workflow and verify GitHub raw logs, SHA256, source hashes, exit, timing and memory by readback; recover P25/P26 if accessible.
2. Independently attack every inequality above; generate counterexamples for nearby chain families and stress O(d,d;Z) duality and decomposable controls.
3. Establish whether the 3d-1 witness condition is known in indefinite plus positive double-form lattice literature; compare to Eichler–Kneser, Nikulin, Narain rational lattice decomposition and effective arithmetic algorithms.
4. Seek a stronger original theorem: e.g. a quantitative perturbation radius uniform in d, a certified family under sparse perturbations, or a finite complexity bound for integral J/Q decomposition. Test whether uniform perturbation survives as a function of d.
5. Preserve negative hypotheses, source-verified references and actual outputs append-only. Strict mathematical and novelty gates; NO manuscript without independent originality.
