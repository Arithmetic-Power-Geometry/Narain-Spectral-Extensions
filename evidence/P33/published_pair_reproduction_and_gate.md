# P33: exact reproduction of published n=7 isospectral non-T-dual code CFTs

Source: Dymarsky and Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP03(2021)160, primary publisher PDF https://scoap3-prod-backend.s3.cern.ch/media/files/60795/10.1007/JHEP03(2021)160_a.pdf , Figure 10 and equation (6.38), PDF zero-index page 60; appendix D for ELC/code duality.

Two explicit 7-vertex graph adjacency edge sets are encoded in figure10_replay.py. For each graph, enumerate all 2^7 stabilizer words (x,A x) over F2 and compute the refined enumerator with variables x=identity, y=both X and Z (Y), z=exactly one of X or Z. Both graphs yield precisely the same 16 monomials and coefficients as the publisher's equation (6.38), total 128 words. This exact finite polynomial equality implies equality of the full genus-one code-CFT partition functions through the published theta substitution; no finite energy truncation is involved.

Independent complete edge-local-complementation (ELC) orbits modulo all 7! vertex permutations were computed in elc_full.py. Orbit sizes are 9 and 10 nonisomorphic graphs; 99 and 108 ELC moves were evaluated; orbit intersection is empty. This independently reproduces the paper's two distinct code-level T-equivalence classes. The sizes appear reversed relative to the figure-caption ordering because of graph labelling; unordered sizes agree [9,10]. The non-T-duality conclusion is within the published code-CFT/ELC equivalence framework, not a fresh general integral O(7,7;Z) matrix solver.

Both executed source scripts and raw stdout/stderr/resource files are committed under evidence/P33. SHA256 local:
figure10_replay.py f85ec1e97232733e6312d1de5ddab0c05086a757efd075eb4bb07abc8677e6dd
figure10.stdout aba9d7a9ce68e3f7e483f68f5fe7ec31af219caf3f047b9fdb0338c29
figure10.stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
figure10.resources e25f496942d8d7cfb4aa278fdf1c7752a7056b7d61cc418d20ca20341122dcf6
elc_full.py 4b7c6c5a52ee3a091f14a4539c7a872ba85130cadb6c2fce2eba9a765f126194
elc_full.stdout 14f1d00891bf9f6d6daa648a304bbca20713d73a8696c7ff28dfe4791bdd2b54
elc_full.stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
elc_full.resources a878451765f427020fcc892df6d402c7130730af4ce2dac2cebf2fbb70d36a6c

Measured executions: REP wall 0.98s, max RSS 95496 KB, exit 0; ELC wall 4.38s, max RSS 95500 KB, exit 0; stderr empty.

Failed hypotheses (append-only):
1. Initial graph transcription and y/z variable convention were incorrect; initial enumerator mismatched the published polynomial.
2. Early ELC run wrongly asserted the first representative had 10 rather than 9 nonisomorphic orbit members; it exited nonzero. Corrected independent full orbit computation yields 9 and 10 with disjoint classes.
3. A first constrained graph-edge search using the wrong y/z convention returned zero matches; corrected convention matched the source.
4. Published n=7 pair is not a new counterexample, and P33 does not establish new theorem-level novelty.
5. P27–P29 CI matrices remain unverified, and no new CI workflow success is claimed.
6. No genus-two distinction was independently computed here; that is the next reproduction gate.

Strict GO: independent exact full genus-one polynomial equality and exhaustive ELC inequivalence within code-CFT framework.
REVISE: remote pinned CI, separate independent implementation, genus-two replay.
NO-GO: novelty, new breakthrough, manuscript. Recommend P34 only as a reproducibility/novelty-kill research cycle, not publication.
