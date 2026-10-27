# P62 — New-question feasibility gate (not a new discovery)

Date: 2026-10-27. This is a novelty-screening decision, NOT an experiment, benchmark, theorem, or physical validation.

## Prior-art verification
- Henriksson, Kakkar, McPeak, *Narain CFTs and quantum codes at higher genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, https://link.springer.com/article/10.1007/JHEP04%282023%29011 . Verified publisher abstract: higher-genus partition functions are polynomials of higher-weight theta functions; genus-two constraints and isospectral examples already known.
- *Quantum subsystem codes, CFTs and their Z2-gaugings*, JHEP 11 (2024) 125, DOI 10.1007/JHEP11(2024)125, https://link.springer.com/article/10.1007/JHEP11%282024%29125 . Verified publisher abstract: subsystem-code Narain CFTs, gauging, small weighted graph classifications.
- *Gauging Z_N symmetries of Narain CFTs*, JHEP 02 (2026) 058, DOI 10.1007/JHEP02(2026)058, https://link.springer.com/article/10.1007/JHEP02%282026%29058 . Verified publisher abstract: gauging and code enumerator partition functions.
- FLINT Riemann theta documentation https://flintlib.org/doc/acb_theta.html ; certified error bounds, Siegel reduction and quasi-linear algorithms. Python binding https://python-flint.readthedocs.io/en/latest/acb_mat.html . Verified documentation, no local FLINT benchmark executed.

## Decision and hypothesis
STOP the P53–P60 graph collision enumeration branch as a proposed novel physics paper. P61 remains in force.
A DIFFERENT, falsifiable potential research question is whether a code-CFT-specific complete observable evaluator can offer an independently reproducible and rigorous efficiency advantage over FLINT's certified general-purpose theta evaluation on a clearly specified class of higher-genus code-CFT observables. This is NOT asserted novel: first kill-test the literature and direct API comparability, then design benchmark. No code or physical experiment was executed for P62.

## Strict preconditions before writing software or a paper
1. Identify the complete physical observable, including normalization, moduli, partition-function polynomial, and appropriate equivalence relation; check against the 2023 JHEP construction.
2. Establish that both methods evaluate the SAME observable and certify enclosures with matched absolute/relative error requirements; compare complete pipeline runtime and peak memory, not theta kernels in isolation.
3. Use FLINT / python-flint if actually available and record exact version, API, backend, precision, machine, test matrices, warmups, repetitions, and failures. If FLINT is unavailable, label the comparison UNTESTED and do not claim speedups.
4. Prespecify separating, nonseparating, ill-conditioned and representative published cases, and independent consistency tests. Avoid cherry-picking.
5. Search targeted prior art for code-specific certified partition-function evaluators and reproducibility packages; a positive speed comparison alone is not proof of novelty.
6. Publish neither Q1 physics manuscript nor a theorem unless original mathematical or physical contribution is independently established. If the kill-test fails, STOP this new direction as well.

## Gate
GO: formulate and literature-check the new, testable question.
REVISE: source audit, exact observable specification, FLINT availability and matched baseline protocol.
NO-GO: present Q1 physics manuscript, claimed new theta algorithm, claimed speedup, claimed new Narain CFT distinction.
