# P75 — Final algorithmic / physical-value kill test (2026-10-28)

## Question
Does the P74 graph grouping of Q-indecomposable components, connected by nonzero J-pairings, offer a new algorithmic advantage or previously unknown Narain CFT invariant?

## Literature verified
Hemkemeier and Vallentin, *On the decomposition of lattices*, ECCC TR98-052 (1998), https://eccc.weizmann.ac.il/report/1998/052/ (publisher repository, verified 2026-10-28). This work explicitly constructs indecomposable Q-orthogonal components using Kneser's graph and provides algorithmic comparisons against prior lattice baselines.
Hemkemeier and Vallentin, *Incremental Algorithms for Lattice Problems*, arXiv:math/0604320 (2006), https://arxiv.org/abs/math/0604320 (verified abstract 2026-10-28), gives incremental orthogonal decomposition algorithms.
Hosono, Lian, Oguiso and Yau, *c=2 Rational Toroidal Conformal Field Theories*, https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11159-Shing-Tung_Yau_335.pdf (verified full text, 2026-10-28), defines Narain partition functions and O(d,d;Z) moduli.

## Exact algorithmic observation
Given a computed Q-indecomposable decomposition L=⊕_i L_i with integral basis matrices U_i, construct graph edges iff U_i^T J U_j !=0. Its connected components give the finest simultaneous Q/J decomposition (P74). After Q decomposition, testing all cross blocks is bounded by O(N^2) scalar J-pairing evaluations over all basis vectors, plus O(N^2) graph processing for r<=N, ignoring bit complexity and dense matrix multiplication. This bound does NOT bound the cost of finding Q-components; it does not improve known asymptotic lattice-decomposition algorithms. No measured speedup or rigorous complexity advantage has been produced.

## False positives and physical limitations
A decomposition result is invariant under simultaneous integral congruence of J,Q and thus under O(d,d;Z) reparametrization, but it is already determined by the two forms. This alone gives no physically new observable or pair of inequivalent CFTs. Comparing a method with only the naive projector enumeration is insufficient: strong classical Kneser/Hemkemeier-Vallentin baselines are required. No benchmark against them was executed; performance advantage is unsupported. G=I,B=0 gives d hyperbolic factors; d=1 gives a single J-connected pair. Neither is novel. No classification beyond the exact grouping rule is supplied.

## Strict decisions
Correctness of grouping reduction: GO (conditional on accurate Kneser component computation).
Novel complexity theorem: NO-GO.
Measured advantage over best existing lattice methods: NO-GO (not measured).
New physical invariant: NO-GO.
Q1 physics and independent mathematical publication: NO-GO.
Recommended action: close the current non-splitting/algorithmic branch for publication. Preserve earlier P61/P63/P69/P73 failures. Reopen only with an externally benchmarked novel algorithm, an original necessary/sufficient moduli theorem, or a certified physical consequence surviving existing theory.
No manuscript or P76 initiated.
