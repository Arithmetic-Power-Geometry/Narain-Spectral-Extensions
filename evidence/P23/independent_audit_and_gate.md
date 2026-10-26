# P23 — Adversarial proof, novelty and execution audit (2026-10-26)

## Independent local execution
Independent source evidence/P23/independent.py uses SymPy 1.14.0 generalized-metric block construction and exact rational arithmetic, rather than P22's Fraction-based direct energy evaluation. Executed locally on Python 3.13.5, exit code 0, stderr empty, 5.61 seconds wall, peak RSS 128596 KB. Source SHA256 c19f1a869e2a78ce98c17b862f96636164b1b4ff0d3ed2b01694f39d41500b7d. Stdout SHA256 f4bbae79bfe6765c1694c17f70843f9219d5d1b48596efc6752e2230125204bf. Verified all generalized metric entries have denominators dividing q det A; tested finite-charge bounds and positive-definiteness for non-diagonal A with A_ii=3, A_i,i+1=1 and skew C_i,i+1=1, q=3,h=6, d=1..4. Exactly 9+81+729+6561=7380 charge vectors; 472 have E<=3. Full output in independent_stdout.json. Sample checks do not substitute for all-dimensional proof.

## Original source pinned replay
Workflow .github/workflows/p23-audit.yml created with checkout, pinned SymPy 1.14.0, original evidence/P22/check.py and independent P23 checker executed unchanged. It records checkout source SHA256, stdout/stderr, elapsed time, exit code, and semantic JSON equality after removing only runtime fields, then uploads artifacts and commits raw evidence/P23/ci_run. **A workflow definition is not execution. Until ci_run/matrix.json is present and read back, P22 original clean-room replay is pending.** The local independent source was run, and local evidence was committed.

## Independent proof audit
- P22 Proposition 1: PASS. Generalized metric Q has all entries in (1/(q det A)) Z via adjugate. Hadamard or Leibniz yields det A<=d!h^d; any two distinct energies with denominators <=Dmax differ by >=1/Dmax². Elementary rational linear algebra.
- P22 Proposition 2: PASS with hypotheses. G=A/q SPD; T=dh bounds lambda_max(A) and ||C||_2, det A>=1 implies lambda_min(A)>=T^-(d-1). Energy positivity yields ||n||²<=H/L and ||m||²<=2HU+2 beta²H/L. This is a finite-window *enumeration* bound, not a finite distinguishing cutoff. Elementary norm bounds.
- P22 Proposition 3: PASS as a nonconstructive finiteness statement, but it does not provide a computable spectral equivalence decision or an effective first-difference cutoff. Its publication novelty is nil.
- P22 labelled reconstruction lemma: PASS by polarization; known elementary fact. It is not an unlabelled inverse-theta theorem.
- P21 local robustness: no new P23 independent all-box replay. It does not establish global rigidity.
- P20 integral projector: no terminating decision method or full T3/T4 O(d,d,Z) indecomposability proved.

## Primary-source novelty kill matrix
1. Schiemann (1997), Mathematische Annalen 308, 507-517, DOI 10.1007/s002080050086: proves ternary positive definite forms determined by theta series. Not a Narain spin-refined theorem, but kills dimension-free generalizations of arbitrary lattice theta nonrigidity.
2. Conway and Sloane (1992), International Mathematics Research Notices 1992(4), 93-96, DOI 10.1155/S1073792892000102: 4D isospectral positive lattice examples. They are NOT automatically Narain CFT counterexamples.
3. LMFDB reviewed Sturm-bound knowledge page https://www.lmfdb.org/knowledge/show/cmf.sturm_bound gives finite Fourier coefficient determination for forms in a fixed modular-form space M_k(N,chi). It does not automatically apply to arbitrary spin-refined nonholomorphic Narain theta series, and requires common weight/level/character.
4. Magma Handbook https://docs.magma-maths.org/LatticesQuadraticForms/Lattices/theta_modfrm.html explains integral lattice theta as modular forms, and finite coefficient determination in a specified finite-dimensional space. Kills any claim that 'finite theta coefficients determine an integral lattice theta function' is novel without additional hypotheses.
5. Dymarsky and Shapere (2021), Physical Review Letters 126, 161602, DOI 10.1103/PhysRevLett.126.161602: explicit physically distinct isospectral code CFTs; broad Narain isospectrality is not new.
6. Henriksson, Kakkar and McPeak (2023), JHEP 04, 011, DOI 10.1007/JHEP04(2023)011: higher-genus partition functions distinguish examples with the same genus-one function; higher-genus distinction is not novel in general.
7. Narain 1986, Maharana–Schwarz 1993, Groot Nibbelink–Vaudrevange 2017 already cover foundational moduli, generalized metric and duality framework. No novelty in basic O(d,d,Z) formulas.

## Bibliography
The six directly relevant journal references above were already in reference/references.bib and the append-only verification register. Publisher sources for Conway–Sloane, Dymarsky–Shapere and Henriksson et al. were rechecked in P23. No duplicate or unverified new BibTeX entry appended. LMFDB/Magma are technical documentation/knowledge resources, not new peer-reviewed journal entries; URLs and precise applicability are preserved here. Publisher metadata for the remaining historical references was not comprehensively reverified this phase.

## Failed conjectures and scope
- No effective finite unlabelled spectral distinguishing cutoff was proved. P22's rational grid gap does not solve the equivalence problem.
- False: equality of theta functions always determines underlying quadratic lattice. Conway–Sloane 4D counterexamples.
- False: all-dimensional lattice theta series always fail to determine the lattice. Schiemann's ternary theorem.
- False: genus-one isospectrality proves physical equivalence. Dymarsky–Shapere provide counterexamples.
- False: same genus-one partition function must imply same genus-two partition function. Henriksson–Kakkar–McPeak counterexamples.
- False: an ordinary Sturm bound directly applies to arbitrary nonholomorphic spin-refined Narain spectra without establishing a suitable modular form space.
- No all-dimensional full O(d,d,Z) classification or physical inequivalence proved.

## Strict P23 gate
**PASS** for independent exact non-diagonal finite tests and mathematical correctness of P22's elementary bounds.
**REVISE** for complete pinned CI original replay (pending artifact), comprehensive full-text theorem novelty audit and general unlabelled inverse rigidity.
**NO-GO** for Q1 breakthrough/novelty of P22 bounds; no manuscript authorized.

## Next: P24 priority
Attack full-duality integral projector obstruction with rational centralizer. Since P^T J=JP and P^T Q=QP, P commutes J^-1 Q = JQ. A rational matrix JQ with irreducible characteristic polynomial over Q admits no nontrivial rational commuting idempotent: its commutant is a field, so P=0 or I. This is a valid *sufficient* certificate for full O(d,d,Z) indecomposability, not necessary; test whether it applies to the coupled T3/T4. If characteristic polynomial reducible, investigate the full rational commutant and rational idempotents before attempting integrality; nonexistence of a rational projector proves nonexistence of integral ones, but existence of a rational projector does NOT prove integral decomposition. Derive exact proofs, test duality-hidden decomposable controls, preserve failed cases, and compare prior art on rational irreducibility/centralizers. Do not infer indecomposability from bounded search.
