# P01 — source, theorem and prior-art audit
Date: 2026-10-26
Verdict: REVISE — strong mathematical direction, no demonstrated breakthrough or publication-ready Part III novelty.
Method: textual review of the two supplied 13-page manuscripts, existing extension source/results and five verified primary-source bibliography records. This is not a full exhaustive literature review nor an independent proof verification.

## Source-to-claim map
Paper I, Sections 2–3: E=(m+Bn)^T G^{-1}(m+Bn)+n^T G n; spin=m^T n. Theorem 3.1 reconstructs fixed-basis G,B from five labelled evaluations. These are not five anonymous energy levels.
Paper I, Section 4: Theorems 4.1–4.2 reconstruct restricted rectangular families from unlabelled spectra; explicit cutoff 17/8 applies only under displayed parameter bounds.
Paper I, Section 5: Proposition 5.1 gives B-sign energy reflection and spin reversal. Theorem 5.2 proves a rational spin-inequivalent pair at energy 3373/1325. This is a witness, NOT the first difference.
Paper I, Section 6: Proposition 6.1 rational interval robustness radius 1/90; Theorem 6.2 generic spin asymmetry on an open dense full-Lebesgue-measure set in displayed coordinates, not a quotient measure.
Paper I, Section 7: Theorems 7.1–7.2 show no universal finite cutoff for all unrestricted backgrounds, including joint spin-refined data.
Paper II, Sections 2–5: D_ES is the least energy with unequal joint counts. Theorem 4.1 gives T(b)=(133-6b+18b^2)/53 for 0<b<1/2; exact rational polynomial certificate classifies 576 nonzero-spin charges PER sign in the 729-charge box. At b=1/5 first difference is 3313/1325.
Paper II, Section 6: zero-mode refined theta first nonzero coefficient -4i sin(2*pi*tau1) exp(-pi*tau2*T(b)), with a higher-energy remainder. It is not a full physical string partition function.
Paper II, Section 7: integer B-shifts and symmetry boundaries: D_ES=+infinity when dist(b,Z) is 0 or 1/2.
Paper II, Section 8: gap 6/265 on b in [1/10,2/5], and symmetric static metric perturbation <=1e-4; this is not a cosmological stability theorem.

## Important audit observations
1. The source manuscripts are logically compatible: 3373/1325 is a valid Paper I witness, 3313/1325 is the Paper II first threshold. Never describe the first as minimal.
2. Existing research/extensions/verify_extensions.py is a bounded exact-rational experiment (oscillator levels 0..3, rational spot checks). Its T6 claim is product-factorization reasoning, not coupled T6 enumeration.
3. Physical string theory is not established by these computations. Worldsheet toroidal CFT partition functions, string level matching, ghosts and other sector-dependent conditions must be treated distinctly.
4. Theorem 8.2 is static metric stability, not cosmological evolution.
5. Paper II's finite exact certificate is analytically motivated, but an independent implementation, raw output and adversarial test evidence remain necessary.
6. The papers' full numbered reference lists have NOT all been reverified in P01. Do not treat five checked references as exhaustive coverage.

## Verified prior-art collision tests
- Narain (1986) establishes modular-consistent toroidal lattice compactification as standard background. Thus generic T6 Narain construction is not new.
- Maloney & Witten (2020) already treat Narain partition functions/moduli averaging. A generic claim to introduce Narain partition functions fails novelty.
- Dymarsky & Shapere (2021, JHEP) connect Lorentzian lattices and Narain CFTs. A broad lattice/CFT construction is not new.
- Dymarsky & Shapere (2021, PRL) explicitly construct physically distinct isospectral code CFT examples. Broad 'isospectral but distinct CFTs' is not new.
- Datta et al. (2022) already develop flavored Narain partition functions. General charge-refined partition-function construction is not new.
None of these verified abstracts alone settles whether a new *exact first-discrepancy theorem for coupled higher-dimensional families* is known. That claim remains OPEN, requiring targeted mathematical literature review and proof.

## Candidate contributions and gates
A. Multiply a zero-mode refined theta difference by a common oscillator factor with constant term 1: likely elementary formal-series algebra; NO-GO as stand-alone breakthrough.
B. Block-product T6 inheritance: elementary factorization; NO-GO as stand-alone breakthrough.
C. Physically projected spin-resolved first-discrepancy theorem: REVISE, only after rigorous specification of physical state space and literature review.
D. Genuinely coupled higher-dimensional rational backgrounds with exact first-separation, nonduality, quantitative stability and independent certificates: CONDITIONAL GO for investigation, not a proven new theorem.
E. Calabi–Yau and Big Bang claims: NO-GO without separately defined geometry/dynamics and physical evidence.

## Unresolved and negative findings
- No claim that string theory has been proved.
- No evidence that a T6 product is a generic Calabi–Yau construction.
- No new theorem proved by P01.
- No exhaustive reference audit of the manuscripts completed.
- No independently executed exact charge enumeration in P01; prior results remain baseline only.
- GitHub PDF binary uploads remain outstanding; source hashes are recorded in evidence/P00.
- Do not promote any result to publication-ready until P02 and subsequent proof gates pass.

## Decision
REVISE. Proceed with P02 independently, then target P03 and P06, with a stronger P01b prior-art sweep before any novelty claim. Preserve the existing manuscripts as inputs; write only to Narain-Spectral-Extensions.
