# P10 — independent publication-readiness audit
Date 2026-10-26. FINAL GATE: **NO-GO for a submission-ready Q1-level manuscript**; REVISE for a narrower research article after corrective work.

## Work actually performed
Fetched all nine committed checker source files and relevant result files from the new private GitHub repository. Independently implemented and **executed locally** two new exact-rational programmes: (i) P02 base threshold test (729 charges, 39 states each, threshold 3313/1325, coefficients +2 at s=-1 and -2 at s=+1), and (ii) five P07/P08 coupled cases including T3/T4 first thresholds, perturbations, all adjacent energy gaps and T6 E<=2 negative control. Full actual stdout committed alongside the independent scripts. These are not verbatim fresh executions of all nine original checkers: the unrerun stages are explicitly marked in audit_matrix.json. Do not claim otherwise.

## Material reproducibility defect discovered and corrected
reference/verification_register.tsv had a six-column header but its first five rows had seven fields (duplicate BibTeX key in third field), shifting URL, status and notes. The P01 DictReader lint would fail. Saved unmodified original in evidence/P10/verification_register_before_repair.tsv and corrected exactly the five malformed rows in the existing register. All 12 rows now have six fields. The five corrected rows were previously misreported as clean in earlier turns because only key counts, not column contents, had been checked. This audit explicitly corrects that assertion.

## Confirmed positive evidence
P02 central finite threshold and first coefficients independently reproduced. P07 T3 threshold 1164367/582071 and T4 threshold 9437981/4718325 independently reproduced, with +2 at spin +1 and -2 at spin -1. P08 pointwise G11 perturbation 1/10000 and exact adjacent gaps reproduced. T6 remains negative through E<=2. These are exact finite-charge certificates conditional on the proved norm completeness bounds.

## Proof audit
For E=(m+Bn)^T G^-1(m+Bn)+n^T G n, with Gershgorin L<=lambda(G)<=U and ||B||_2<=beta, E<=H implies ||n||²<=H/L and ||m||<=sqrt(HU)+beta sqrt(H/L). The P07/P08 m bound uses sqrt(U/L)<2 to replace cross term 2 beta H sqrt(U/L) by 4 beta H. This is valid for the stated rational families. No finite search establishes full GL(d,Z) or O(d,d;Z) nonduality. No proof of integral indecomposability or full all-entries stability box exists. Positive adjacent-level gaps are insufficient for a robust first-discrepancy theorem if lower-level degeneracies split.

## Novelty kill test and physical limitations
Narain compactification, lattice theta and flavored partition functions, modular properties, O(d,d;Z), tensor-product inheritance and parity relations are prior art. See the already-registered Narain 1986; Maloney and Witten 2020; Dymarsky and Shapere 2021; Datta et al. 2022; Groot Nibbelink and Vaudrevange 2017. A coupled-coordinate rational example alone does not establish indecomposability, a new physical string observable or a breakthrough. No critical-string BRST/GSO physical-state survival has been shown. P09 dynamics NO-GO stands.

## Essential gates before drafting
1. Verbatim clean-room rerun of every original P01-P09 checker against a full checkout; compare JSON semantically and preserve stdout/stderr and environment hashes.
2. Verify full P02 polynomial classification and Paper I interval certificate, not just the central finite threshold.
3. Prove a nontrivial new rigidity or stability theorem, including all lower-level pairings; or limit claims to verified finite counterexamples with a defensible prior-art distinction.
4. Analyze O(d,d;Z) and parity carefully; no unqualified inequivalence claim.
5. Independently adjudicate novelty with primary literature, and resolve any remaining metadata errors.
6. No physical dynamics, moduli stabilization or Big Bang assertions.

## Publication verdict
NO-GO for submission-ready Q1 manuscript today. Conditional REVISE for a mathematically scoped note; no manuscript drafted. New GitHub repository only; all original files outside the corrected verification register left untouched.
