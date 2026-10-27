# P55 exhaustive LC/permutation quotient and coarse genus-one collision gate

Date: 2026-10-27. Exact finite integer graph enumeration, not physical CFT equivalence proof.

## Executed method
Enumerate all labeled simple undirected graphs on n=2,3,4,5 vertices, 2^(n(n-1)/2) each. For each unassigned graph, form its full orbit under all n! vertex permutations and repeated local complementation at every vertex. Assign a class ID to each orbit member and assert no overlap. Compute the coarse three-variable genus-one enumerator on one representative of each orbit by exact binary graph-code arithmetic (classes {0},{1,2},{3}). Group representatives by their enumerator and count cross-class collision pairs.

## Results
n2: 2 labeled graphs; 2 LC/permutation classes, sizes [1,1], zero cross-class collisions.
n3: 8 graphs; 3 classes, sizes [1,3,4], zero cross-class collisions.
n4: 64 graphs; 6 classes, sizes [1,3,5,6,16,33], zero cross-class collisions.
n5: 1024 graphs; 11 classes, sizes [1,6,10,15,25,40,40,132,140,165,450], zero cross-class collisions.
The class sizes sum to all graphs at each n. In the enumerated scope, distinct LC/permutation classes do not have equal coarse genus-one enumerators. This does not establish a minimum n for all code-CFTs or a universal CFT isospectrality result.

## Execution provenance
Local /mnt/data/p55/search.py; GitHub evidence/P55/lc_quotient_exhaustive.py byte-identical, blob bc090379ba820f32ab0b0c884454a9764181de2a. SHA256 source 469f26a87ce31e7631b73e080ed37be528e22d4b3bdafe598ccd4850155f1a26; stdout 916752fa5ba85e4e7ab2547c789fc73163ea5dacdab3299d2deccad10b84d9da; stderr empty e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 4cc28a717fcaef85991ee15114f99e7cd7e99e616fa38b32282f381f7fd37758. Exit 0; wall 4.00s; RSS 95768 KB. Raw output/resources remain local, not remotely uploaded.

## Important caveat
The script computes genus-one enumerators only for one representative of each LC/permutation orbit. It does not separately assert that the coarse enumerator is invariant across *every* LC orbit member. That invariance is expected for the intended physical construction but must be checked directly before promoting the cross-class uniqueness observation to an unconditional exhaustive classification. Thus this is a candidate-class search result, not yet a formal proof that every pair of labeled graphs in different orbits is separated by the invariant.

## Gate
GO: all n<=5 labeled graph orbits enumerated exactly, no cross-class representative collisions, committed source independently read back.
REVISE: validate invariance of coarse enumerator under LC across all 1098 labeled graphs; extend to n6 only if a new hypothesis and resource budget justify it; verify graph-state-to-Narain equivalence scope.
NO-GO: novel Narain physics theorem, Q1 paper, minimum counterexample size, or any claim beyond tested graph-code family.
Next P56: test the orbit-invariance premise directly before increasing graph size.
