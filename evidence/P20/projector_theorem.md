# P20 — Exact integral-projector criterion and limits (2026-10-26)

## Setup
L=Z^(2d) with J=[[0,I],[I,0]] and positive definite rational generalized metric Q(G,B)=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]]. Then J is even unimodular of signature (d,d) and JQJ=Q^-1.

**Definition:** A Narain product splitting is a primitive integral J-orthogonal decomposition L=L1 ⊕ L2, with each Li even unimodular of signature (ki,ki), 0<k1<d, and Q(L1,L2)=0. It is invariant under O(J,Z) change of basis.

## Proposition (necessary and sufficient projector criterion)
Such a splitting exists if and only if an integer matrix P of size 2d satisfies:
(1) P²=P;
(2) P^T J=J P;
(3) P^T Q=Q P;
(4) the restriction of J to im(P) has signature (k,k) for some 0<k<d.

**Proof:** Given a splitting, define P as projection onto L1 along L2. The summands are integral, hence P integral and idempotent; J and Q orthogonality give (2),(3). Conversely integral idempotence yields L=im(P)⊕ker(P) as a direct sum of primitive integral lattices. From (2), J(im P,ker P)=0. Since J is unimodular and the direct sum is J-orthogonal, the determinant of each restriction is ±1, hence both are even unimodular. By (4), im(P) has signature (k,k), and the complementary signature is (d-k,d-k). From (3), Q(im P,ker P)=0. Thus this is a Narain product splitting. No bound on entries of P is supplied, and this equivalence is not a terminating algorithm.

**Important:** Merely P integral, idempotent, and selfadjoint is not sufficient without the signature condition. Also a rational projector does not prove integral splitting. For integral P, unimodularity of the two restrictions follows automatically from J unimodular and J orthogonality; it need not be separately assumed.

## Duality invariance
For T integral with T^T J T=J, define Q'=T^T Q T, P'=T^-1 P T. Then P' integral idempotent, and the J- and Q'-selfadjoint conditions are preserved by conjugation. This establishes invariance of existence of a valid projector under full O(d,d,Z).

## Executed exact controls
Python 3.13.5, SymPy 1.14.0; exit 0, 0.074 sec. For d=3,4, verified JQJ=Q^-1. For d=3, GL-geometric obstruction P_v(e1)=(169/365,0,182/365), nonintegral. For d=4, charpoly (351652043925*x^4+5547197084*x²+9486400)/351652043925 reproduces P13's irreducible quartic. Neither GL obstruction decides existence of a non-geometric O(d,d,Z) product projector.

Adversarial B-shift: G=diag(2,3,5), B=0, K01=1,K10=-1, T=[[I,-K],[0,I]]. Exact checks: T^T J T=J; T^T Q(G,0)T=Q(G,-K); P=diag(1,0,0,1,0,0) and P'=T^-1 P T both satisfy integer idempotence and J/Q selfadjointness, rank 2. P' projects to an even unimodular hyperbolic rank-two summand. This is a **genuinely nonzero off-diagonal B** with an integral product projector; do not mistake coupling for indecomposability. This particular integer B-shift is gauge-equivalent to B=0, so it is an adversarial *representation* control, not a new physically inequivalent example.

## Failure modes and unproved goals
- A bounded search for P with entries |Pij|<=M cannot prove nonexistence at unbounded height.
- The T3/T4 backgrounds have not been proved O(d,d,Z)-indecomposable; no exhaustive projector search, lattice arithmetic obstruction, or terminating decision algorithm was established.
- The criterion is an elementary reformulation of an orthogonal direct sum and may have limited novelty. Prior Narain duality literature already develops generalized metrics and O(d,d,Z); see source register and literature note.
- No new physical string inequivalence claim and no manuscript.

## Strict gate
**PASS** for the precisely formulated projector equivalence and explicit transformed-product control; **REVISE** for a computationally effective full-duality indecomposability theorem and publication novelty. P21: attempt robust finite-window spectral separation with rational perturbation boxes, forced/accidental degeneracy classification, exact interval certificates or counterexamples. Preserve every failed hypothesis and actual execution record.
