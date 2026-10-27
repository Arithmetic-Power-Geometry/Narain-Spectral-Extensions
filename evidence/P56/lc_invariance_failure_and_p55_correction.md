# P56 — falsification of the coarse genus-one enumerator LC-invariance assumption

Date 2026-10-27. This is a correction to the interpretation of P55, preserved append-only.

## Exact test and counterexample
For every labeled simple graph on n=2,3,4,5 vertices and each vertex v, calculate the coarse genus-one graph-code enumerator E_G in three classes {0},{1,2},{3} using exact integer arithmetic, apply local complementation LC_v, and test whether E_G=E_LC_v(G).

Smallest observed counterexample: n=3, path edges {(0,1),(0,2)}, local complement at vertex 0 -> triangle {(0,1),(0,2),(1,2)}. Path signature {(0,1,2):3,(0,3,0):1,(1,2,0):3,(3,0,0):1}. Triangle signature {(0,3,0):4,(1,0,2):3,(3,0,0):1}. The two signatures are NOT equal, although graphs are LC equivalent.

## Exhaustive results (directed graph,vertex operations)
n=2: 2 graphs, 4 LC checks, 0 failures.
n=3: 8 graphs, 24 LC checks, 6 failures.
n=4: 64 graphs, 256 LC checks, 104 failures.
n=5: 1024 graphs, 5120 LC checks, 2620 failures.
All checks completed; no early exit or truncation.

## Corrected interpretation of P55
P55's exact LC/permutation class counts (2,3,6,11 for n2..5) remain supported. P55's observation that the CHOSEN class representatives have distinct coarse genus-one signatures remains a descriptive fact about those representatives only. It is NOT a valid equivalence-class invariant and cannot support the claim that all graphs in different classes have distinct signatures. A cross-class collision search must compute signatures of every member, and distinguish class overlap from collisions. P55's representative-only novelty gate is withdrawn. The P53 n4 formal candidate remains LC equivalent by the P54 exact witness; that result is not affected.

## Execution provenance
Executed /mnt/data/p56/full_audit.py, exit 0, wall 1.99 s, RSS 95504 KB, stderr empty. Source SHA256 075dd180f97a93544c4387fd32a1dbfa537cd0313361258edb662ab834fc4f0a; stdout SHA256 8fb7e40492882b06fa72f5559534e9f9f8413f1f76233c4935a9e4493e021f85; stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources SHA256 c6771d7335fbe71aedbbe8e7286307591a61117ef4bc37b8b6ce08ffb04baa8a. Source Git blob fbc3fb9b6ac39c7c57b5255c020c699647d28798, independently verified byte-identical to evidence/P56/exhaustive_lc_invariance_failure.py. Raw logs remain local.

## Publication and next step
GO: precise negative result, exhaustive n<=5 check, transparent correction and preservation of failed assumption.
NO-GO: coarse genus-one enumerator as an LC-invariant classification, previous representative-only cross-class uniqueness inference, novel Narain theorem, Q1 paper.
Next bounded step P57: construct full graph-to-LC-orbit mapping for n<=5; compute signature-to-class membership for ALL graphs; report exact cross-class collisions. Independently audit the physical meaning of the coarse enumerator before further physical claims. No paper.
