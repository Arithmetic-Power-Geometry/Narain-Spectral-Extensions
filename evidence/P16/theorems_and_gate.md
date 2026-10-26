# P16 — finite inverse-spectral distinguishability, independent check, novelty gate
Date 2026-10-26. Scope: Narain zero-mode mathematical spectrum, not full physical string theory.

## Definitions and elementary theorem
Let E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n, s(m,n)=m^T n, and N(E,s) the finite number of integral charges realizing the given energy and spin. Define an oriented spectral equivalence as an integral bijection preserving both E and s.

**Theorem A (one-coordinate obstruction).** Such an equivalence forces equality of N(E,s) for every (E,s). Thus one certified unequal multiplicity is sufficient to rule out oriented spectral equivalence. Proof: an integral bijection preserving the observables bijects their finite fibers. A single unequal coordinate is minimal in the number of measured coordinates needed to disprove equality; this is NOT a universal minimum-energy measurement theorem.

**Theorem B (energy-only converse fails).** For (G,+B) and (G,-B), the parity map (m,n)->(m,-n) preserves E and reverses s, so their entire energy-only multiplicities coincide. The exact spin-resolved P02/P07/P15 witnesses distinguish the two oriented spectra, conditional on completeness certificates. Therefore full unrefined energy equality does not imply an oriented energy-and-spin-preserving equivalence. Parity DOES relate them if orientation reversal is permitted; no absolute physical inequivalence follows.

**False converse and unproved claim.** Equality of finitely many energy-spin coordinates does not *by itself* establish equivalence, but no general necessary-and-sufficient finite-data theorem was proved. An attempted universal finite-indistinguishability argument by taking one torus radius large fails because momentum energies shrink. This is a recorded failed proof, not a counterexample.

## Independent T6 certificate
P16 independently recomputes P15 with a common integer denominator and one-sign (+B) enumeration, obtaining -B by the exact parity identity. Unlike P15's per-charge Fraction arithmetic and explicit two-sign loops, the second checker uses SymPy's exact inverse only once and integer operations inside the loop. Executed Python 3.13.5, SymPy 1.14.0, exit code 0. Candidates n=233, m=797, states +B=289; first E=3573739389131/1786726163119, coefficients +2 at s=1 and -2 at s=-1. Runtime 0.405 sec. Full source, stdout, empty stderr and hashes are saved.

## Literature novelty kill test
Dymarsky and Shapere, *Solutions of Modular Bootstrap Constraints from Quantum Codes*, Physical Review Letters 126 (2021) 161602, DOI 10.1103/PhysRevLett.126.161602, explicitly provide physically distinct isospectral theories. Dymarsky and Shapere, *Quantum stabilizer codes, lattices, and CFTs*, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160, discuss isospectral Narain code CFTs. Henriksson, Kakkar and McPeak, *Narain CFTs and Quantum Codes at Higher Genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, distinguish some genus-one isospectral theories using genus-two partition functions. These prior works defeat broad claims of discovering Narain isospectrality or the inadequacy of energy-only data. The parity argument is elementary and not a new general inverse-rigidity theorem. See publisher URLs https://doi.org/10.1103/PhysRevLett.126.161602 , https://doi.org/10.1007/JHEP03(2021)160 , https://doi.org/10.1007/JHEP04(2023)011 .

## Strict verdict
PASS: independent exact P15 T6 reproduction and elementary fiber-counting obstruction. REVISE: general inverse spectral rigidity and novelty. NO-GO: universal finite necessary-and-sufficient oriented equivalence criterion, full O(d,d;Z) classification, or physical string inequivalence. Next P17: theorem-by-theorem novelty kill-test and independent reproducibility review, while resolving unfinished P11 original-checker runs. Do not draft a paper yet.
