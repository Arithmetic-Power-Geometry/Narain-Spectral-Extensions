# P67 — Generic indecomposability and novelty gate (2026-10-28)

## Theorem
For d>=2, let M=Sym_d^+(R) x Skew_d(R). Define J=[[0,I],[I,0]], Q(G,B)=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]]. (Note the mixed-term sign follows E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n.) Then the subset of M admitting a nontrivial integral direct-sum splitting simultaneously orthogonal for J and Q is contained in a countable union of proper closed real-analytic zero loci. Consequently this subset is meagre and Lebesgue-null; the non-splitting locus contains a dense G_delta of full measure.

## Proof
An integral direct-sum splitting gives a nonzero nonidentity P in Mat_(2d)(Z) with P²=P and P^T J=J P and P^T Q(G,B)=Q(G,B)P. Conversely such an integral idempotent determines an integral splitting into im P and ker P, since x=Px+(I-P)x, with both sublattices J/Q orthogonal. There are countably many integral matrices P. For fixed nontrivial P, entries of F_P=P^T Q-Q P are real-analytic on connected open M (indeed rational in G,B with det G>0). The P65 explicit parameter-box theorem gives a point in M without any nontrivial compatible integral projector, hence F_P is not identically zero. Therefore the common zero set of its entries is contained in a proper real-analytic zero locus, closed, nowhere dense, and measure zero. Union over P is meagre and null. This establishes generic integral non-splitting. No claim about openness or algebraic classification of the complement.

## Counterexample and distinctions
G=I, B=0 is decomposable into d hyperbolic planes. More generally simultaneous block diagonal G and B give decomposable backgrounds. These are nongeneric examples. This does NOT prove physical interacting/indecomposable CFT in a stronger sense, nor characterize all T-duality equivalences, nor construct a novel higher-genus observable.

## Prior art
Hemkemeier and Vallentin, On the decomposition of lattices, ECCC TR98-052 (1998), https://eccc.weizmann.ac.il/report/1998/052/ — Kneser orthogonal decomposition method predates our connectivity criterion. Hosono, Lian, Oguiso and Yau, c=2 Rational Toroidal Conformal Field Theories, https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11159-Shing-Tung_Yau_335.pdf — Narain lattices and moduli. General countable analytic-zero-set genericity is standard. Specific literature completeness and originality remain unverified.

## Gate
Mathematical proof GO (conditional on the correctly stated energy convention); independent computational testing not required for analytic theorem; novelty REVISE; Q1 physics NO-GO. P61/P63 STOP conclusions preserved. No manuscript and no next research phase initiated.
