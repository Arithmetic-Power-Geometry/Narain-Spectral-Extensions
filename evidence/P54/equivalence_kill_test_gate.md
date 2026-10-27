# P54 exact graph-equivalence kill test (2026-10-27)

## Scope
The P53 four-vertex formal genus-two polynomial witness was tested for simple graph isomorphism and local-complementation (LC) equivalence up to vertex permutation. This is a graph-state/local-Clifford equivalence test, not a full Narain CFT isomorphism proof.

## Executed exact witness
A edges (0,1),(0,3),(1,2); B edges (0,2),(0,3),(1,2),(1,3).
Exact canonical graph-isomorphism check: FALSE.
Breadth-first LC orbit search found a witness after visiting 10 labeled graphs:
LC at vertex 0: edges (0,1),(0,3),(1,2),(1,3).
LC at vertex 1: edges (0,1),(0,2),(1,2),(1,3),(2,3).
LC at vertex 0: edges (0,1),(0,2),(1,3),(2,3).
Apply vertex permutation [0,2,3,1] (old vertex -> new vertex): result exactly B.
LC equivalence up to permutation: TRUE. All adjacency transformations are exact integer bitmask operations; no numerical approximations.

## Execution and verification
Executed /mnt/data/p54/equivalence.py, exit 0, wall 1.00 s, peak RSS 95632 KB. Source SHA256 a09a3b080b8f69222622ad6c87b0d8c9dec151bcb2456d4aba263fe0ecb5059b; stdout SHA256 3cf4f024cdb1d95218ca3d4ffd24d08c6a5b05d399385c2f28077c2328c8421c; stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources SHA256 73eeda726bac8bcf3cd88d3bcbf023490a88478601d7dbbd9035a69542c66c8c. Local and GitHub source Git blob bc6466a62bc037220272024aa9a0a110b8363374, independently read back and byte-identical. Raw stdout and resources remain local, not committed.

## Interpretation and stopping gate
The P53 n4 candidate is NOT a pair of inequivalent graph-state local-Clifford classes. Its formal genus-two coefficient difference therefore cannot serve as evidence of a new inequivalent physical Narain pair. LC equivalence does not by itself prove equality of the fixed-basis genus-two theta evaluation; physical equivalence requires checking the exact code-CFT map and allowed transformations. The P53 interval at one period matrix was INCONCLUSIVE, so no contradiction follows.

GO: exact negative novelty test, explicit reproducible transformation witness, source readback.
NO-GO: claim of a new inequivalent n4 construction, a new physical spectral distinction, or Q1 original paper.
Next action only if a genuinely new question is specified: quotient small-graph candidate search by LC/permutation equivalence and verify the precise physical invariant. Avoid repeated phases without a surviving novelty hypothesis.
