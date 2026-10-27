# P50 — hostile prior-art novelty and publication gate (2026-10-27)

## Primary verified literature (web publisher / authoritative documentation)
1. Deconinck, B.; Heil, M.; Bobenko, A. I.; van Hoeij, M.; Schmies, M. (2004). Computing Riemann theta functions. Mathematics of Computation 73(247), 1417–1442. Publisher/PDF: https://page.math.tu-berlin.de/~bobenko/papers/2003_Bob_DHvHS.pdf . Arbitrary user-specified precision theta computation is established.
2. Labrande, H.; Thomé, E. (2016). Computing theta functions in quasi-linear time in genus 2 and above. LMS Journal of Computation and Mathematics 19, 163–177. DOI https://doi.org/10.1112/S1461157016000309 . Quasi-linear theta algorithms are established.
3. Kieffer, J. (2023). Certified Newton schemes for the evaluation of low-genus theta functions. Numerical Algorithms 93, 833–862. DOI https://doi.org/10.1007/s11075-022-01443-3 . Certified genus-1 and genus-2 theta methods established.
4. FLINT documentation: https://fredrikj.net/fdoc/html/acb_theta/index.html and https://fredrikj.net/fdoc/html/algorithms/special-functions/theta-quasi-linear.html . acb_theta handles general Riemann theta functions with characteristics, arbitrary genus, rigorous error bounds, symplectic reduction and quasi-linear methods. Software documentation; version and exact release not pinned.
5. High-dimensional Riemann theta computation (2023), DOI https://doi.org/10.1016/j.cnsns.2023.107266 , journal article with truncation bounds and hyperbolic-cross approaches; author metadata not independently verified here, so no invented author list.
6. Published code-CFT examples: Dymarsky and Shapere (2021), JHEP 03 160, DOI https://doi.org/10.1007/JHEP03(2021)160; Henriksson, Kakkar and McPeak (2023), JHEP 04 011, DOI https://doi.org/10.1007/JHEP04(2023)011. Published genus-one isospectral and higher-genus-distinguishable code constructions already exist.

## Comparison against P42–P49
P42–P44 establish an implementation for graph-code genus-two Gaussian expressions with exact rational SPD checks, interval rounding and Gaussian tails. P46 provides a second conditional arithmetic implementation; P45's failed enclosure remains in evidence. P47b shows severe inconclusive bounds in ill-conditioned/near-separating low-cutoff regimes. P48–P49 optimize a lower eigenvalue bound with rational bisection. P49 measured 3.93x improvement on one deliberately loose-bound baseline case, but no speedup on published seven-vertex cases; no comparison to FLINT, Sage or another established theta implementation was run. No novel complexity theorem, nontrivial general code-CFT acceleration, or new physical Narain distinction is established.

## Publication decision
GO: reproducibility/validation contribution can be documented as a research software note or educational reproduction, with proper attribution and a transparent negative novelty finding.
REVISE: before a methods submission, compare against a pinned FLINT version on equivalent theta values and precisions, derive any graph-code-specific reuse advantage, prove soundness with full physical normalization, independently benchmark and pin CI, preserve raw logs, and confirm a nontrivial surviving novelty claim.
NO-GO: claim that Gaussian tail certification, rational eigenvalue bisection, genus-two theta evaluation, or published seven-vertex separation are new. NO-GO for an original Q1 physics or numerical-methods manuscript at present.

## Next best decision
Do NOT draft the claimed novel Q1 paper. If pursuing novelty, design a strict P51 benchmark and theorem-discovery gate: code-specific polynomial reuse versus pinned FLINT/Sage certified theta baseline over many graph pairs and matrices; demand independently reproduced scaling or a new nontrivial theorem. If no original advantage survives, close the line as reproducibility research rather than extend phases indefinitely.

This is a literature/novelty audit, NOT an executed external-software benchmark. Existing P49 timings must not be presented as comparisons to the published methods.
