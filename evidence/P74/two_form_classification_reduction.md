# P74 — Exact classification reduction and novelty kill (2026-10-28)

## Result: exact simultaneous decomposition from positive-form components

Let L=Z^N, Q a positive-definite real symmetric form and J any symmetric bilinear form. Take the unique finest integral Q-orthogonal decomposition L=L_1 ⊕ ... ⊕ L_r into Q-indecomposable nonzero sublattices (the classical Kneser decomposition). Define a finite graph on {1,...,r}, with edge i--j iff J(L_i,L_j) is nonzero. The direct sums of L_i over graph connected components form the unique finest integral simultaneous Q/J-orthogonal decomposition. In particular L is simultaneously indecomposable iff the graph is connected.

Proof: Each simultaneous splitting is a Q-orthogonal integral splitting, hence (by uniqueness of Q-indecomposable components) is a grouping of the L_i. An edge cannot cross distinct J-orthogonal summands. Thus every connected graph component lies within one simultaneous summand. Conversely the sums over graph components are mutually Q-orthogonal by construction and mutually J-orthogonal because no cross edges exist. This is an exact finite reduction assuming one can compute the positive-form decomposition. It does not require J nondegenerate, though Narain J is unimodular.

This is equivalent to the integral idempotent criterion P^2=P, P^TQ=QP, P^TJ=JP, but provides a finite structural decision procedure when Kneser components are available. It is NOT a new necessary-and-sufficient closed-form parameter classification for arbitrary G,B and is NOT a new algorithm without independent complexity or baseline evidence.

## Counterexamples / negative cases
For G=I_d, B=0, the standard p_i and w_i are separate Q-indecomposable rank-one components, J edges p_i--w_i, so the graph has d components; the simultaneous decomposition is into d hyperbolic planes. For d=1 the graph has one component. For nontrivial Q-indecomposable lattice (r=1), graph is trivially connected; simultaneous indecomposability is immediate. These illustrate that P66 sufficient inequalities are not a necessary characterization.

## Strongest prior art
Hemkemeier, Vallentin, *On the decomposition of lattices*, ECCC TR98-052 (1998), https://eccc.weizmann.ac.il/report/1998/052/ : Kneser decomposition and algorithms. Their paper includes indecomposable-vector graph and decomposition procedure; the two-form grouping is an elementary corollary of uniqueness.
Hemkemeier, Vallentin, *Incremental Algorithms for Lattice Problems*, arXiv:math/0604320 (2006), https://arxiv.org/abs/math/0604320 : incremental orthogonal decomposition.
Hosono, Lian, Oguiso, Yau, *c=2 Rational Toroidal Conformal Field Theories*, arXiv:hep-th/0211230 (2003), https://archive.ymsc.tsinghua.edu.cn/pacm_download/58/489-017-0211230.pdf : Narain moduli and rational toroidal theory.

## Gate
Mathematical classification reduction GO. New mathematics NO-GO absent additional theorem beyond elementary grouping. Full parameter-space closed-form classification NOT ESTABLISHED. Q1 physics NO-GO. Manuscript NO-GO. Preserve P61/P63/P69/P73 negatives. Do not initiate P75 or write manuscript.
