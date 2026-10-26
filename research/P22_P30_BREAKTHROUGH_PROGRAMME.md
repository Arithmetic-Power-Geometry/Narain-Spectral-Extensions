# P22–P30 breakthrough-seeking research programme (2026-10-26)

## Nonnegotiable principles
We cannot guarantee a novel theorem, nor prove a false conjecture. Target all integer dimensions d>=1 via dimension-parametric proofs, then verify exact low-dimensional cases and adversarial controls. Distinguish: zero-mode energy-only theta data; spin-refined data; full oriented Narain O(d,d,Z) orbit; full CFT genus-one/genus-two observables. Never infer a stronger equivalence or physical inequivalence from a weaker observable. Do not draft a manuscript until the theorem and novelty gates pass.

## Novelty kill-tests from primary sources
Schiemann (1997) proved theta-series determination of positive ternary forms; any universal 'theta data never reconstructs' statement is false in that setting. Conway–Sloane (1992) constructed distinct four-dimensional lattices with the same theta series; any universal theta uniqueness is false. Dymarsky–Shapere (2021) already exhibit isospectral code CFTs; Henriksson–Kakkar–McPeak (2023) already distinguish some genus-one-isospectral theories at genus two. P21 local stability is an example-specific continuity argument and insufficient alone for a breakthrough. Verified primary bibliography is append-only in reference/references.bib and verification_register.tsv.

## P22 — Dimension-uniform inverse-spectral decision problem
1. Fix d, height h, common denominator q, spectral cutoff H, and arithmetic class A(d,q,h): symmetric positive-definite G and skew B with entries in (1/q)Z of numerator absolute value <=h; require an explicit positive lower eigenvalue bound.
2. Define separate equivalence targets: (a) equality of energy-only counts, (b) equality of (E,s) counts, (c) O(d,d,Z) equivalence, (d) parity-extended equivalence. State a finite canonical representative scheme, or admit that bounded input matrices may have representatives outside A.
3. Prove a uniform finite-charge enumeration bound from L,U,beta and a cutoff H, with integer arithmetic and explicit complexity; implement independent exact checkers.
4. Seek an EFFECTIVE distinguishing cutoff F(d,q,h) for pairs with genuinely unequal full spin-refined spectra, not a tautological maximum over unknown first differences. Derive via algebraic height bounds and rational energy denominator constraints if possible. Do not claim F for pairs with identical full spectra.
5. Try to reconstruct rational generalized metric from finitely many *labelled* energy observations; contrast the unlabelled inverse problem. Identify which observations are actually necessary and give sharp counterexamples.
6. Run negative controls: integer B shifts, factorized T duality, charge relabellings, B sign parity, code-CFT isospectral pairs, 4D theta-isospectral lattices. Preserve every failed conjecture.

Gate: GO only for a nontrivial proven effective theorem or exact counterexample to a credible prior conjecture; otherwise REVISE.

## P23 — Independent prior-art and theorem referee
Compare every candidate to Schiemann 1997, Conway–Sloane 1992, Narain and O(d,d) duality literature, Dymarsky–Shapere 2021, Henriksson–Kakkar–McPeak 2023, theta-series and modular forms inverse problems. Verify publisher metadata, check all references, reconstruct each proof independently, run code from pinned Git commit and preserve stdout/stderr, SHA256, runtime and memory. Return strict GO/REVISE/NO-GO.

## P24 — Stronger alternative: effective projector obstruction
For the integral projector criterion P^2=P, P^T J=JP, P^T Q=QP, seek a terminating decision algorithm for the existence of primitive hyperbolic summands for arbitrary rational Q and all d. Explore rational commutant, algebraic centralizer, integral lattice idempotents and local-global obstructions. Prove or refute that rational irreducibility of a suitable commutant implies integral indecomposability. Adversarially test T-duality-hidden products. A bounded search alone is never a proof.

## P25 — Stronger alternative: generic local identifiability
For all d, characterize the Jacobian rank of finitely many labelled energy-spin functions in the d^2-dimensional G/B parameter space modulo continuous or discrete symmetries. Prove a generic full-rank theorem with an explicit rational determinant witness, and separate local labelled rigidity from unlabelled global spectral rigidity. Kill-test against classical inverse quadratic-form results.

## P26 — Higher-genus distinction with exact arithmetic
Study whether selected higher-genus theta coefficients separate specific energy-spin-isospectral but nondual pairs. Existing higher-genus code-CFT distinctions are prior art, so require new effective bounds or a genuinely new family. Do not claim physical nonduality without a full O(d,d,Z) certificate.

## P27 — Certified complexity and scalable algorithms
Develop exact branch-and-bound with rigorously bounded charge search, rational intervals and independent certificates for arbitrary d. Compare against direct enumeration on fixed input families and worst-case adversarial cases. Seek provable complexity or parameterized bounds, not only speedups.

## P28 — Counterexample discovery
Systematically search smallest dimensions/heights for false converses, near-collisions and hidden dualities. Negative results can be publishable only when rigorous, nontrivial and not already known.

## P29 — Independent mathematical verification
Separate proof author, adversarial reviewer, and independently written checker; verify every theorem and proof dependency. Pin environment and commit, preserve failing tests append-only. Do not suppress negative outcomes.

## P30 — Publication decision
Only after independently verified original theorem, decisive primary-source novelty, full reproducibility and scope-consistent physics interpretation, select journal and draft. Otherwise retain NO-GO, with the best counterexample/algorithmic note as fallback.

## Immediate first executable task
Execute P22 in evidence/P22 using exact rational enumeration and a small explicitly bounded A(d,q,h) test bed (e.g. d=1,2,3 initially). Prove the dimension-uniform finite-charge bounds first, then attempt a NONTRIVIAL effective finite distinguishing cutoff and labelled local reconstruction. Preserve all actual code, outputs, failures, references and provenance. Commit to Narain-Spectral-Extensions only. Report GO/REVISE/NO-GO, then P23 or P24 based on results.
