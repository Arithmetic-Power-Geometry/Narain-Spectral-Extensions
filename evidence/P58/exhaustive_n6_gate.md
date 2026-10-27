# P58 six-vertex exhaustive collision gate — 2026-10-27

## Hypothesis
Do distinct LC/permutation equivalence classes of labeled simple six-vertex graph codes share the same coarse three-symbol genus-one enumerator?

## Exact executed result
Enumerated all 2^15=32768 labeled simple graphs on six vertices. Computed each graph's integer three-symbol enumerator. Classified graphs by union-find over local complementation at each of six vertices and the five adjacent vertex swaps, which generate arbitrary vertex permutations. Tested whether any enumerator signature occurs in two different union-find classes.

Output:
- 32768 graphs, 64 distinct signatures, 62 signature groups with multiple graphs (within class), largest signature group 3060.
- 26 LC/permutation classes.
- ZERO signature groups occurring in two different classes; ZERO cross-class graph pairs with matching signature.
- The union-find classification elapsed 6.296 seconds; complete internal computation 6.309 seconds.

## Execution provenance and caveats
Local executed source: /mnt/data/p58/search.py SHA256 87393d95dcdcec8c3e8aa7defc04b6116e244acc26bc4be5744262f2f13be44b; Git blob fb62578baaae30c71fa2c8b618dbffc6c2e5b86f.
stdout SHA256 f6742fd7c8325203885b3c4df8e124ddf32e9d2459e9a89e9476ae59e2194bbc; stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resource log SHA256 dd20f5f4880620d6117e31f0f9f0c761b9ead509fa50fe9b49b1112391346217.
Process exit 0, wall 7.55s, peak RSS 98712 KB, under 65-second timeout.
Committed evidence/P58/exhaustive_n6.py is a shorter equivalent algorithm (remote blob 9d8a83b004b48be2d04af4c5dd807f8a3a649115), NOT byte-identical to the executed local script. The committed source has not been independently replayed; this is an outstanding reproducibility requirement. Raw stdout and resource files remain local and are not committed.

## Interpretation
Combined with the corrected P57 all-member n2..5 audit, this gives finite exact computational evidence that in the simple graph-code family n=2..6, equal coarse genus-one signatures imply LC/permutation equivalence. P56 proved the converse fails: signatures are not invariant within an LC orbit. This result is limited to the tested graph-code family and does not prove Narain CFT physical equivalence or any general minimum counterexample size.

## Research gate
GO: full n6 exact finite enumeration and negative collision result.
REVISE: byte-identical replay of committed source; independent implementation and source checks; physical map; literature novelty audit for finite classification statement.
NO-GO: novel Narain pair, general theorem for all n, Q1 original physics manuscript.
Next action: replay committed P58 source and, only if a concrete novelty question survives, perform bounded n7 candidate filtering and equivalence checks.
