# P53 small-graph discovery gate (2026-10-27)

## Hypothesis and exhaustive scope
Hypothesis: two simple graph codes of n<=4 can share the coarsened genus-one three-symbol enumerator yet have different formal 16-symbol genus-two polynomial coefficients. Enumerated ALL 2, 8, and 64 labeled simple graphs for n=2,3,4 respectively, by exact integer operations. Graphs are not quotiented by isomorphism or local Clifford equivalence; counts are not distinct physical classes. Each genus-one collision is counted against the first representative in the matching group, not all pairs.

Results: n2 0 collisions and 0 formal differences; n3 4 collisions and 0 formal differences; n4 55 collisions and 9 differences against the first representative. First n4 witness masks 13 and 30 with edges A={(0,1),(0,3),(1,2)}, B={(0,2),(0,3),(1,2),(1,3)}, 174 differing polynomial coefficients. This is a *formal enumerator difference*, not an established physical spectral distinction. Its novelty relative to published graph-code and theta identities has NOT been established.

## Physical theta kill test
At Y=[[1.1,.23],[.23,1.3]], lower bound .949, epsilon 1e-9, P44 returned INCONCLUSIVE at K2, dps30, interval approximately [-2.8655096672070425e-10, +2.8655096672070425e-10] and total width upper 5.731019334414085e-10. The interval contains zero. Thus it does NOT certify any physical separation. The center is numerically extremely close to zero, potentially due to theta identities or equivalent constructions; that possibility requires exact identity and equivalence checks, not inference. The P44 certificate is conditional on its implemented theta expression and analytic tail assumptions.

## Execution provenance
Executed /mnt/data/p53/search.py, GitHub byte-identical evidence/P53/exhaustive_small_graph_search.py. Git blob 5c99ab3b0deaa359f0d22f70a2702b0bf8bd8359; source SHA256 c234d06291fabb458fbcdc927928d4a46dacd6d13643106d83289f5f3d67b90d. stdout SHA256 4ac3cedf499d8315e62b7c97a74faf4c2001746260754cf042eaba7e0b58a5e7; stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resource file SHA256 253058ce98faefefeb751a2818a5b5a71c53a7eff49b0297bf25ffdcea13f5d5. Raw stdout/resources local only; script imports local P44/P42 dependencies and must be run with these available. This is a finite scope, not a global minimum-size proof.

## Decision
GO: falsifiable new search hypothesis, exhaustive exact n<=4 enumerations, transparent candidate and failed sign certification, byte-identical committed source.
REVISE: determine graph isomorphism/local Clifford equivalence, theta polynomial kernel identities, exact physical normalization; then independently verify any genuine surviving new distinction and published prior art.
NO-GO: new n4 physical counterexample, new Narain CFT theorem, Q1 publication claim.
Next research action only if justified: exact kernel/equivalence kill test on n4 witness. Stop if the formal difference lies in a known theta identity or physical equivalence.
