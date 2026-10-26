# P25 — Exact full-duality indecomposability certificate for coupled T3 and T4
Date: 2026-10-26. This is a new rigorous result **within this research programme**. Independent external novelty has NOT been established. No manuscript.

## Theorem A (general short-vector obstruction; all dimensions)
Let L be an integral lattice of rank N with an integral nondegenerate bilinear form J and a positive-definite real quadratic form Q. Let lambda=min{Q(v):v in L, v!=0}. Form S={v in L:0<Q(v)<2lambda}. Make a graph with vertex set S and an edge between v,w whenever J(v,w)!=0. If S spans L tensor Q and this graph is connected, there is no nontrivial integral direct-sum decomposition L=L1 direct_sum L2 that is orthogonal for BOTH J and Q. In particular there is no nontrivial integral J-selfadjoint Q-selfadjoint projector.

Proof: For any v in S, decompose v=v1+v2 with vi in Li. Q-orthogonality gives Q(v)=Q(v1)+Q(v2). If both components are nonzero, Q(v)>=2lambda, contradiction. Thus each v belongs to exactly one summand. Nonzero J-pairing forces the endpoints to lie in the same summand, since J(L1,L2)=0. Connectivity places ALL S in one summand. Since S spans L over Q, the other summand has rank zero. Contradiction. The result holds for every N, and is invariant under integral J-isometries carrying Q by congruence. This is a sufficient obstruction, not a necessary condition, nor a general decision algorithm.

## Theorem B (full O(d,d;Z) indecomposability for explicit coupled T3 and T4)
For d=3 or 4, set G_ii=1, G_i,i+1=G_i+1,i=1/(10+i), B_i,i+1=1/(13+i), B_i+1,i=-1/(13+i), zero elsewhere (zero-based i). Let J=[[0,I],[I,0]], Q=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]], and E(m,n)=(m,n)^T Q(m,n). Then no nontrivial integral projector P with P²=P, P^T J=JP, P^T Q=QP exists. In particular these backgrounds are NOT T-dual to any nontrivial orthogonal product under full O(d,d;Z).

### Exact completeness proof
Gershgorin gives 4/5 I < G < 6/5 I for both d (maximum sum of off-diagonal magnitudes <=1/10+1/11<1/5). The induced operator norm ||B||_2 <= max absolute row sum <=1/13+1/14<1/6. Set H=21/10. If E(m,n)<H, then ||n||²<H/(4/5)=21/8<3. Also
||m|| <= ||m+Bn||+||B|| ||n|| < sqrt((6/5)(21/10)) + (1/6)sqrt(21/8) < 8/5+5/18=169/90<2.
The first strict radical inequality follows from (6/5)(21/10)=63/25<64/25, the second from 21/8<25/9. Because m,n are integral, ||n||²<3 and ||m||²<4 imply EVERY coordinate of m and n lies in {-1,0,1}. Thus the 3^(2d) finite charge box contains ALL vectors with E<H, with no unexamined charges outside the box.

### Exact enumeration and connectivity
Two independent programmes enumerate all charges in that box, compute exact energies, find the nonzero minimum lambda, enumerate S with E<2lambda, compute the rank of the short-vector matrix and the connected components of the J-pairing graph. For d=3, lambda=585096/582071, 2lambda=1170192/582071<21/10; |S|=40, rank span=6, graph connected (one component of 40). For d=4, lambda=4739621/4718325, 2lambda=9479242/4718325<21/10; |S|=56, rank span=8, graph connected (one component of 56). These exact rational calculations are reproduced by independent SymPy matrix Q/BFS and pure Fraction energy/union-find implementations. Since lambda<H and every E<H lies in the box, the enumerated lambda is the GLOBAL minimum. Since 2lambda<H, the enumerated S is COMPLETE. Apply Theorem A. QED.

### Duality scope
For T in O(J,Z), Q'=T^T Q T and P'=T^-1 P T preserve the integral projector equations. Therefore the nonexistence result is invariant under the full group O(d,d;Z), not just geometric GL(d,Z). The result concerns an integral charge-lattice product splitting of the zero-mode quadratic form, not every possible physical CFT factorization or orientation/parity classification.

## P23 and P24 reproduction status
Recovered P23 CI matrix: P22 original exit 0 and P23 independent exit 0, BUT both semantic_json_equal flags FALSE and the CI run lists both as failed. Thus P23 replay exists but is a FAIL, not a pass; investigate precise JSON differences in P26. Committed P24 checker rerun locally, exit 0, exact involution and B-shift/GL product controls pass. P25 workflow .github/workflows/p25-certificate.yml committed to replay all six scripts and preserve raw stdout/stderr; CI success requires independent readback of evidence/P25/ci_run/matrix.json.

## Evidence and limitations
Actual local exact scripts and outputs: short_vector_obstruction.py and short_stdout.json; independent_certificate.py and independent_stdout.json; certificate_bounds.py and bounds_stdout.json; P24_replay_stdout.json; empty stderr and per-process wall/RSS records. Source and stdout SHA256 in local_sha256.txt. Python 3.13.5, SymPy 1.14.0. All four local commands exited 0. The independent implementation uses matrix-based SymPy energies and BFS; the first uses Fraction inverse and union-find.

P25's all-dimensional theorem is a short-vector connectivity lemma. It may be a known lattice-indecomposability criterion or a close variant; **no novelty claim is made** until adversarial prior-art review. The exact T3/T4 application is a genuine new proof relative to P24, but its external publication novelty is not established. We have not proved a terminating arbitrary-dimensional decomposition decision procedure. T6 was not checked by this certificate. No manuscript.

## Strict gate
**GO (mathematical subgate)**: exact full O(d,d,Z) product-indecomposability of the two specified rational T3/T4 backgrounds, subject to byte-identical CI replay verification.
**REVISE (publication gate)**: independent novelty audit, P23 semantic JSON mismatch, further adversarial full-duality and generalized dimensions.
**NO-GO**: claiming a novel breakthrough or drafting manuscript before independent novelty and reproducibility gates pass.
