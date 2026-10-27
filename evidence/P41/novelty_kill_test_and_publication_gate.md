# P41 — hostile novelty and publication gate (2026-10-27)

## Scope and checked artifacts
Read back evidence/P40/source_formula_audit_gate.md, reference/references.bib and reference/verification_register.tsv from GitHub. Counted 21 BibTeX records and 21 verification-register rows. No new bibliography entry is added without full verification.

## Primary prior art, verified against public publisher pages
1. Dymarsky and Shapere, *Quantum stabilizer codes, lattices, and CFTs*, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160 (already stored). Their code-CFT construction and nondual isospectral examples predate P33.
2. Henriksson, Kakkar and McPeak, *Classical codes and chiral CFTs at higher genus*, JHEP 05 (2022) 159, DOI 10.1007/JHEP05(2022)159, publisher https://link.springer.com/article/10.1007/JHEP05%282022%29159 (newly checked for P41, not yet entered in bibliography/register).
3. Henriksson, Kakkar and McPeak, *Narain CFTs and quantum codes at higher genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, publisher https://link.springer.com/article/10.1007/JHEP04%282023%29011 (already stored). Their abstract explicitly says they prove the higher-genus theta-polynomial structure and show examples of genus-one isospectral CFTs distinguished at genus two.
4. Ando, Kawabata and Nishioka, *Quantum subsystem codes, CFTs and their Z2-gaugings*, JHEP 11 (2024) 125, DOI 10.1007/JHEP11(2024)125, publisher https://link.springer.com/article/10.1007/JHEP11%282024%29125 (newly checked, not yet entered).

## Novelty kill tests
A. Novel nondual Narain pair: FAIL. P33 is an exact reproduction of the published seven-vertex construction.
B. New genus-two distinction: FAIL. Published 2023 paper explicitly demonstrates the phenomenon.
C. General theta-polynomial algorithm: FAIL as stated. Polynomial construction and genus-two modular constraints were already derived in 2022–2023.
D. General rigorous numerical certificate algorithm: UNRESOLVED. P38–P40 show a successful example-specific certified interval evaluation and independent numerical replay, not a proved generic algorithm with a rigorous domain of admissibility, worst-case complexity, error budget, benchmark suite, and comparisons to existing certified Siegel-theta algorithms. An example-specific Gaussian union bound is standard analysis and does not establish novel theorem-level mathematics.
E. General inverse-spectral theorem: FAIL. No proof of a novel uniqueness or nonuniqueness theorem beyond published cases.
F. Reproducibility/methods paper: CONDITIONAL. May be worth writing only after independent full artifact replay, explicit theorem-level guarantees, meaningful multi-instance benchmarks, and transparent comparison with prior work.

## Proposed P42 experiment gate, not a manuscript
Specify input as an admissible graph code (or explicitly parameterized Construction-A lattice), a positive definite rational genus-two imaginary period matrix, and target error epsilon. Derive a universal tail bound with clearly verified coordinate normalization and a certified outward-rounded evaluation. Prove termination, enclosure correctness and a conservative computational cost bound. Test a suite of inequivalent graph-code pairs including positive and zero-difference controls, multiple matrices, near-separating and ill-conditioned matrices, plus independent replay. Compare runtime and precision against a naive interval direct-lattice baseline. Do not infer novelty from successful examples; search published algorithms for certified Siegel theta evaluations before any claim.

## Integrity audit and outstanding blockers
P39 reports outward-rounded arithmetic and a rigorous tail bound for its implemented Gaussian sum; P40 independently reproduced a floating-point result and checked relevant source formulas. However, full byte-identical P39 remote execution, independently certified theta-map normalization, global physical interpretation, and P27–P29 pinned CI remain unresolved. Do not label these as complete.
Do not infer publication acceptance or journal quartile from number of references.

## Strict decision
GO: independently reproduced published construction and useful certified numerical case study.
REVISE: general theorem and multi-instance independent benchmark, artifact provenance, CI and stronger prior-art kill tests.
NO-GO: new Narain isospectral pair, new higher-genus physical discovery, new inverse-spectral theorem, Q1 original theoretical-physics manuscript.
No manuscript prepared. Recommend P42 general certified algorithm only as a falsifiable research hypothesis.
