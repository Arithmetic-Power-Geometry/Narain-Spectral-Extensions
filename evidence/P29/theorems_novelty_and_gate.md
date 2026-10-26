# P29 exact arithmetic decomposition and novelty kill-test — 2026-10-27

## Strict result
**GO (mathematical algorithm):** exact terminating decision and construction of the finest simultaneous integral J/Q orthogonal direct-sum decomposition, for any rational symmetric positive-definite Q and integral symmetric J on L=Z^N. This is an elementary generalization of existing Kneser-style lattice decomposition algorithms, NOT verified original research. **NO-GO** for breakthrough/Q1 paper. **REVISE** pinned GitHub Actions provenance and broader adversarial testing. No manuscript. Do NOT advance to P30 publication gate yet.

## Theorem (finite simultaneous-form decomposition)
Let Q be rational SPD, J integral symmetric. Define M=max_i Q(e_i). A nonzero v is Q-indecomposable if it cannot be written v=x+y with nonzero integer x,y and Q(x)<Q(v), Q(y)<Q(v). Let V be ALL nonzero integer v with Q(v)<=M. Let A subset V be those Q-indecomposable vectors. Construct graph on A with an edge v--w whenever v^T Qw !=0 OR v^T Jw !=0. Let A_1,...,A_k be connected components and L_i=span_Z A_i. Then L=direct_sum_i L_i, distinct L_i are orthogonal under BOTH Q and J, and these are the finest nonzero integral simultaneous orthogonal summands. Thus k=1 iff no nontrivial simultaneous integral J/Q orthogonal splitting exists. For Narain J and Q, any nontrivial component gives an integral idempotent P satisfying P²=P, P^T J=JP and P^T Q=QP; an actual *Narain product* additionally requires a proper balanced hyperbolic J-signature, so a simultaneous splitting alone must NOT automatically be called a Narain product. In fact each component of an even unimodular hyperbolic J lattice is even unimodular; if J|L_i is indefinite with signature (k_i,k_i), it gives a Narain product, while definite components require further physical interpretation.

**Proof.** Every basis vector e_i has Q(e_i)<=M. If it is Q-decomposable, write it as x+y with strictly smaller positive Q norms. Repeat for x and y. Since Q is SPD, there are finitely many integer vectors of Q-norm <=M, and strictly decreasing norms along every branch, so the process terminates in Q-indecomposable vectors, all with norm <=M. Hence A generates L over Z. Under ANY integral Q-orthogonal decomposition L=L_1 direct_sum L_2, a Q-indecomposable v must lie in one summand: otherwise the nonzero projections x,y are integral and Q(v)=Q(x)+Q(y), both smaller, contradiction. Therefore each Q-indecomposable v belongs to one summand. The same holds for simultaneous J/Q decompositions. Nonzero Q or J pairings force graph-adjacent vectors into the same summand. Conversely different connected components have pairwise Q=J=0 by graph construction. Since Q is SPD, the rational spans of different components are linearly independent, and because A generates L integrally, L=direct_sum L_i as Z modules. Every simultaneous orthogonal decomposition is a grouping of these L_i, proving fineness and termination.

**Effective finite bound.** Compute the rational inverse Q^-1 and let C=max_i sum_j |(Q^-1)_ij| (infinity operator norm). Then v^T Qv >=||v||²/C. Every v in V satisfies ||v||²<=MC. Set R=ceil(sqrt(MC)), or conservatively the smallest integer R>=1 with (R+1)²/C>M. Enumerate [-R,R]^N minus zero; evaluate Q(v)<=M exactly. To test Q-indecomposability of v in V, check each x in V with Q(x)<Q(v) and y=v-x in V with Q(y)<Q(v). Build graph by exact rational pairings. With T=(2R+1)^N, O(N² T²) rational arithmetic operations plus rational matrix inversion and graph operations is a conservative upper bound; intermediate rational bit complexity and enumeration output can be exponential in input size. This is a **terminating algorithm with a crude bound**, not a polynomial-time complexity result. For an arbitrary integral J, the resulting components may be J-degenerate; for Narain even unimodular J, their J restrictions are nondegenerate and unimodular, but balanced signature still needs checking.

## Independent exact executions
Local Python 3.13/SymPy 1.14:
- evidence/P29/algorithm.py: exact Fraction Q-pairings, SymPy rational inverse bound, union-find; 1D product, 2D product, 2D non-diagonal coupled rational G/B; exit 0; wall 1.77 s; peak RSS 128656 KB; stderr empty.
- evidence/P29/independent.py: independent SymPy matrix energy, direct decomposition test, BFS components; exit 0; wall 1.56 s; peak RSS 128524 KB; stderr empty.
Both agree: d1 product has one 4-vector component; d2 uncoupled product has two 4-vector components; d2 coupled G_01=1/10, B_01=1/13 has one 8-vector component. The exact coupled Q is non-diagonal rational. This is a small adversarial smoke test, not broad independent validation of complexity, full O(d,d;Z), or difficult d>=3 cases.
Hashes are in local_sha256.txt, raw stdout/stderr and resource records are in evidence/P29. GitHub readback of source, output and bibliography required.

## P28 independent audit
The P28 norm argument appears internally consistent: ||Delta G||,||Delta B||<=d r, ||G^-1||<=1/(4/5-t), ||G^-1-G0^-1||<=1.57t, ||Q-Q0||<10t; E0(v)>=(2/5)||v||², giving lambda>=(1-25t)lambda0. For the 3d-1 witnesses ||v||²<=2 and E0<=2-1/(d+8), the strict 70t<1/(d+8) suffices. **No fresh independently executed P28 checker was run during P29.** P27/P28 CI matrices remain absent at readback; do not claim pinned replay.

## Inverse-spectral kill-test
No new finite UNLABELLED energy-and-spin inverse-spectral rigidity theorem or rigorous nondual isospectral pair was established in P29. Enumerating rational bounded-height candidate Q and finite spectral windows is not a uniform identification theorem: distinct full spectra may agree arbitrarily far, and full-isospectral nonduality must be excluded separately. Labelled polarization reconstruction is elementary. This research branch is NO-GO for breakthrough at P29.

## Hostile prior-art novelty
Hemkemeier and Vallentin, 'On the decomposition of lattices', ECCC TR98-052 (1998), provides a lattice orthogonal-decomposition algorithm and related Kneser methods: https://eccc.weizmann.ac.il/eccc-reports/1998/TR98-052/index.html . Eichler–Kneser indecomposable-vector connectivity is explained in https://www.geotop-bielefeld.de/node/830 . Brandhorst and Veniani, 'Hensel lifting algorithms for quadratic forms', Mathematics of Computation 93 (2024) 1963–1991, DOI 10.1090/mcom/3909, gives discriminant orthogonal group algorithms. Mizoguchi and Oikawa, 'Unifying error-correcting code/Narain CFT correspondences via lattices over integers of cyclotomic fields', Physics Letters B 862 (2025) 139308, DOI 10.1016/j.physletb.2025.139308, is further Narain lattice construction prior art. All three new primary references were verified and appended to reference/references.bib and reference/verification_register.tsv. The simultaneous-two-form graph criterion follows directly from the classical method. This is NOT independently established new theorem-level novelty. A general rational Narain product decision procedure may be practically useful but cannot yet justify a Q1 novelty claim.

## Failed hypotheses and limitations (preserved)
1. Failed to recover P27/P28 GitHub CI matrices: both 404.
2. Failed to establish a new unlabelled finite inverse-spectral rigidity theorem or full-duality counterexample.
3. The decomposition algorithm is not demonstrated polynomial-time; the explicit complexity bound is exponential in dimension and arithmetic height.
4. Algorithm adapts classical indecomposable-vector decomposition; originality gate NO-GO.
5. Only small d1/d2 exact checks completed; no large non-diagonal d3/d4 adversarial run in this phase.
6. No new independent P28 execution, only algebraic re-audit.
7. No physical CFT factorization claim from J/Q splitting without the hyperbolic signature test.

## Publication gate
MATHEMATICAL: GO for exact terminating algorithm (classical extension), P28 proof algebraic re-audit REVISE pending independent replay.
REPRODUCIBILITY: REVISE, CI absent.
NOVELTY: NO-GO for claimed breakthrough, Q1 manuscript, and P30 submission programme.
RECOMMENDATION: **Do not execute P30 as a publication gate yet.** First discover a demonstrably new invariant, sharp complexity result, or rigorous nondual isospectral counterexample and independently verify against strongest prior art.
