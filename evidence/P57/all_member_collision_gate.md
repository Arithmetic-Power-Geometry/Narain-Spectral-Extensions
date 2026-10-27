# P57 all-member collision audit — corrected P55 inference

2026-10-27. Exhaustively enumerate every labeled simple graph at n=2,3,4,5; construct exact local-complementation/permutation orbits; calculate the three-class genus-one enumerator of EVERY labeled graph; map each signature to all orbit IDs and count signature collisions across different orbits.

Results (n, labeled graphs, LC/permutation classes, distinct signatures, cross-class collision pairs):
2: 2,2,2,0
3: 8,3,4,0
4: 64,6,9,0
5: 1024,11,21,0

All class sizes partition the complete graph set. There is no shared coarse genus-one signature across different LC/permutation orbits in this finite n<=5 family. The signatures are NOT LC-invariant within an orbit (P56); the correct statement is that their *sets* are disjoint across distinct orbits for n<=5. Do not extrapolate to n>=6, other code families, or physical CFT equivalence.

Execution: corrected standalone local /mnt/data/p57/full_collision.py, exit 0, wall 3.63 s, RSS 95884 KB. SHA256 local source 9c72f3197ca1445208c50052b37cff67b14e4ddf752c8362657af4d922b79ecc, stdout 03c59c4deeb73066878e8af87b66a62f8f9df198771370fa256fafda6627df30, stderr empty e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, resources 593d5109ff86e3f6c347f1f32b7ef430597958ac5435908fdd1c8aec4eefb0bc. The first local execution had import-time side effects from P55 and was superseded by this standalone execution; its outputs remain locally recorded.

GitHub evidence/P57/full_collision.py has been committed and independently read back, Git blob 9a182733da3fe5455b42c0ce35be027cd18578d7. NOTE: this source is a manually transcribed functionally equivalent version of the local executed script, not yet verified byte-identical to the executed source (local blob c6e56a6e4501cfe9bc51678abc71f194e6ed591a). Re-run the exact GitHub source in CI or locally before claiming source-identical reproducibility. Raw stdout and resources remain local.

GO: exhaustive all-member exact collision audit for n<=5; correct resolution of P55 representative-only weakness.
REVISE: byte-identical source replay, independent enumeration, pin dependencies, evaluate n6 only with a meaningful hypothesis and budget; establish physical equivalence scope.
NO-GO: any new Narain isospectral pair, general uniqueness theorem, or Q1 novelty paper.
