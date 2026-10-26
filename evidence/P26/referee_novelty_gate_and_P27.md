# P26 hostile referee — 2026-10-27

## Strict conclusions
**GO mathematical subgate:** the short-vector obstruction is valid and now gives exhaustive exact certificates for the specified coupled T3, T4 AND T6 backgrounds under full O(d,d;Z), subject to pinned source replay.
**REVISE reproducibility:** P25 CI matrix evidence/P25/ci_run/matrix.json remains unavailable at readback. Local independent third checker exited 0; byte-identical committed-source GitHub replay not yet confirmed.
**NO-GO breakthrough/novelty:** Eichler–Kneser indecomposable positive definite lattice decomposition uses indecomposable vectors and connected nonzero-pairing graphs; this is strong preexisting methodological prior art. The P25 lemma adapts this standard idea to simultaneous J/Q orthogonality and short vectors, but new theorem-level novelty is NOT independently established. No manuscript.

## Line-by-line mathematical referee
Let J=[[0,I],[I,0]], Q=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]]. Q is symmetric positive definite and QJQ=J for symmetric SPD G and skew B. Charge spin is m·n, while J(v,v)=2m·n. The P25 theorem needs only integral J and SPD Q. Any integral idempotent P selfadjoint for J and Q yields L=im(P) direct_sum ker(P), orthogonal for both. Every v with 0<Q(v)<2lambda must lie in exactly one summand because a nonzero vector in either has Q-norm >=lambda. Edges of the nonzero-J-pairing graph force the same summand. If this graph is connected and the short vectors span L over Q, the other summand has rank 0. This is valid in all dimensions; no unproved integrality implication is needed.

For all chain d>=2 with G_ii=1, G_i,i+1=1/(10+i), B_i,i+1=1/(13+i), the maximum G off-diagonal absolute row sum <=1/10+1/11<1/5, B row sum <=1/13+1/14<1/6. Thus lambda_min(G)>4/5, lambda_max(G)<6/5, ||B||_2<1/6. For E<21/10, ||n||²<21/8<3 and ||m||<sqrt(63/25)+(1/6)sqrt(21/8)<8/5+5/18=169/90<2. Consequently each coordinate of m,n belongs to {-1,0,1}. This certifies exhaustive enumeration below H=21/10 in ALL d>=2, although enumeration size 3^(2d) grows exponentially. For the tested d, 2lambda<H, hence the enumerated minimum and short set are globally exact.

Third independently coded SymPy-to-integer generalized metric checker enumerated d3 728 nonzero charges, d4 6560, d6 531440. Exact minima:
d3 lambda=585096/582071, 40 short vectors, rank 6, J graph connected;
d4 lambda=4739621/4718325, 56 short vectors, rank 8, J graph connected;
d6 lambda=1792977755011/1786726163119, 76 short vectors, rank 12, J graph connected.
All 2lambda<21/10. d6 result is NEW to this programme. The P25 theorem therefore extends to d6 under full integral duality.

## Adversarial exact controls
Independent SymPy exact tests at d=3,4,6: integral B shift, GL(d,Z), factorized T-duality exchanging m0/n0, and their composition, each verified T^T J T=J, |det T|=1 and exact preservation of energy and J-pairing under charge change. For decomposable Q=I, explicit rank-two integral projector P=diag(E00,E00) passes P²=P, J-selfadjointness and Q-selfadjointness; its short-vector J-graph is disconnected. All local tests exited 0. This is a positive control for duality invariance and a negative control for falsely classifying decomposable lattices. It does NOT test every element of O(d,d,Z), but covariance is proved symbolically for arbitrary T.

## CI and provenance
P25 CI run matrix remains NOT_FOUND, so the requested pinned CI recovery is NOT complete. Third local checker: Python/SymPy exact, exit 0, stderr empty, wall 13.72s, peak RSS 268760 KB, actual stdout and hashes committed. Adversarial checker: exit 0, stderr empty, wall 1.76s, peak RSS 128524 KB. Source files are preserved, but byte-identical remote replay and source hash comparison remain a P27 gate. Do not label CI PASS.

## Prior-art kill test
Eichler–Kneser unique indecomposable orthogonal decomposition for positive definite integral lattices uses connected indecomposable vectors under nonzero bilinear pairings. See University of Bielefeld Geotop notes 'Definite forms and the Eichler-Kneser theorem' https://www.geotop-bielefeld.de/node/830 and the lecture notes 'Lecture Notes on Quadratic Forms and Lattices' Theorem 6.19 (Eichler, Kneser), https://www.math.uni-sb.de/~ag-schulze/rsp_lecturenotes_quadraticforms.pdf. This is close prior art for the connectivity strategy. The P25 short-vector threshold and simultaneous J/Q formulation is a direct elementary sufficient-condition adaptation; novelty currently NO-GO without a rigorous literature distinction. Nikulin 1980 discriminant forms and gluing (DOI 10.1070/IM1980v014n01ABEH001060) remain relevant. The 2023 Designs, Codes and Cryptography article 'The irreducible vectors of a lattice' https://link.springer.com/article/10.1007/s10623-022-01119-y discusses indecomposable/relevant vectors, further restricting novelty. Full publication metadata for this recent article was not verified in this phase, so no new BibTeX entry appended. These sources are recorded as verified web/academic evidence but not all independently publisher-verified full bibliographic entries.

## Failures and limits
- P25 pinned GitHub CI output not recovered: unresolved.
- No arbitrary-dimensional connectedness induction proved. All-dimensional completeness bound is NOT an all-dimensional indecomposability theorem.
- No terminating arbitrary-dimensional integral decomposition algorithm established.
- Short-vector graph criterion is sufficient, not necessary. Failure to connect cannot prove decomposability.
- No claim about all physical CFT factorization beyond charge-lattice integral Q/J splitting.
- No Q1-level novelty established; no manuscript.

## P27
1. Obtain actual P25/P26 GitHub Actions outputs at pinned SHA; record and verify source SHA, stdout/stderr, exit code, wall/RSS and semantic output equality; distinguish CI failure from absent artifact.
2. Attack an all-dimensional chain family: determine exact minima and J-graph connectivity via induction or a dimension-free finite witness set, not only d=3,4,6.
3. Search primary sources for Eichler–Kneser indecomposable vectors, orthogonal decomposition algorithms, Narain rational lattices and Nikulin discriminant gluing. Add BibTeX only after verifying full metadata.
4. Independently reimplement T6 with Sage/FLINT or another exact arithmetic engine; stress arbitrary O(d,d,Z) words and decomposable controls.
5. Seek a theorem genuinely beyond known connected-vector lattice criteria (effective complexity, arithmetic gluing, or a new nontrivial obstruction). Return strict novelty verdict and do not draft manuscript without a defensible original contribution.
