# P32: published code-CFT reconstruction, first bounded control (2026-10-27)

## Literature baseline
Dymarsky and Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP03(2021)160, DOI 10.1007/JHEP03(2021)160, https://link.springer.com/article/10.1007/JHEP03(2021)160: real self-dual stabilizer codes, graph-code Narain CFTs, physically distinct isospectral examples among graphs n<=8. Henriksson, Kakkar and McPeak, Narain CFTs and quantum codes at higher genus, JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011: genus-one isospectral examples with different genus-two partition functions. Both already in verified bibliography, so no duplicate append.

## Exact bounded graph-code control
Enumerate all 2^(4 choose 2)=64 simple labelled graphs with n=4. Quotient by all 4!=24 vertex relabellings: exactly 11 unlabelled graphs. For each graph with binary adjacency A, enumerate the 2^4 stabilizer words (x,z=Ax mod 2), count each site's (x_i,z_i) in {(0,0),(1,0),(0,1),(1,1)}. Construct complete 4-variable Pauli-composition enumerator. No collision between distinct graph-isomorphism classes among 11 enumerators. This is a small-n negative control, NOT the full code-CFT genus-one partition polynomial, not a graph-local-Clifford equivalence test, and not a reconstruction of the published n>=7 nondual isospectral pair.

Independent local execution: /mnt/data/p32/graph_code.py, SHA256 4319294348841890858393ba0306327a4611637315c17f43c5b5a49d0a493b21; stdout SHA256 fc6fd9c98a7d925c35d1c5b1f4bfd33d8dad7273a6d31ae3c260f10c3bd5f0df; stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resource SHA256 9f93dbc5f2100f91660b3530c52cf0d787905205890ce7c36b6159dbad444e22; exit 0; wall 1.09s; peak RSS 95628 KB; stdout elapsed 0.002124s. Committed graph_code_enumerator.py is a clean equivalent checker, NOT byte-identical to the local executed source. Do not conflate SHA256.

## P27–P29 CI status
At P30 and P31, evidence/P27/ci_run/matrix.json, P28/ci_run/matrix.json, P29/ci_run/matrix.json were all absent. They have not been recovered during P32. No pinned CI success claim.

## Failed hypotheses and next test
1. n=4 complete Pauli enumerator did not collide across 11 graph isomorphism classes.
2. Graph isomorphism is strictly weaker than code equivalence under graph local complementation and vertex permutations; no physical inequivalence claim.
3. A collision in the complete Pauli enumerator would not by itself prove nondual Narain CFTs, and absence of collision does not preclude equal genus-one partition functions after theta specialization.
4. Need extract the actual published graph pair and its exact invariant, independently reproduce the paper's complete weight-enumerator/genus-one polynomial identity, certify graph-code inequivalence under the published duality group, then compare genus two.
5. Do not launch a manuscript or declare a breakthrough.

## Gate
GO: small-n exhaustive combinatorial control.
REVISE: actual published isospectral-pair reproduction, duality equivalence algorithm, CI provenance.
NO-GO: new theorem, new isospectral nondual example, publication novelty.
