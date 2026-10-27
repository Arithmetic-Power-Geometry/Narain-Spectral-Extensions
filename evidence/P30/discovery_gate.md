# P30-DISCOVERY — 2026-10-27

## Strict gate
GO: exact rational T2 duality control and finite-box spectrum tests.
REVISE: pinned CI recovery, byte-identical GitHub replay, difficult higher-dimensional P29 algorithm tests.
NO-GO: new inverse-spectral theorem, new nondual full-isospectral pair, novelty, breakthrough and manuscript. Do NOT recommend P31 publication phase.

## CI
evidence/P27/ci_run/matrix.json, evidence/P28/ci_run/matrix.json, evidence/P29/ci_run/matrix.json each returned NOT_FOUND on GitHub readback. No job logs recovered. This is unavailable evidence, not proof of CI failure.

## Exact controls
Use G=[[1,1/10],[1/10,1]], B=[[0,b],[-b,0]], Q=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]], J=[[0,I],[I,0]]. Enumerate all (m,n) in [-R,R]^4, recording exact energy E and spin m.n.

At b=1/13 versus b=-1/13, R=2 (625 charges) spectra match. In fact P=[[0,1],[1,0]], T=diag(P,P) satisfies T^TJT=J and T^TQ(1/13)T=Q(-1/13), proving equality of FULL energy-and-spin spectra. This is T-DUAL, not a new counterexample.

At b=1/17, R=2 and R=3 boxes differ. Independently verified earliest numerical energy discrepancy: E=28711/28611, spin=0, counts 0 for b=1/13 and 4 for b=1/17. Since these are charge-box spectra, this alone does not certify a complete-energy-ball mismatch.

## P29 theorem audit
The P29 atom-graph argument is mathematically valid: all integer basis vectors decompose through strictly shorter Q-norms into finite indecomposable atoms; their connected components under nonzero Q OR J pairings span the finest simultaneous integral orthogonal summands. Rational SPD Q guarantees a finite bound R from inverse Q row norms. Runtime bound remains exponential. Narain product further requires a proper balanced J-signature subset. No independent higher-dimensional replay or algorithmic novelty demonstrated.

## Hostile novelty
Dymarsky–Shapere, Quantum stabilizer codes, lattices, and CFTs, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160, already construct physically inequivalent isospectral Narain CFTs (first code example n=7). Henriksson–Kakkar–McPeak, Narain CFTs and Quantum Codes at Higher Genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, distinguish genus-one isospectral cases at genus two. Conway–Sloane and Cervino–Hein provide Euclidean lattice isospectral precedents, not automatic spin-refined Narain examples. All are already in the verified repository bibliography; no duplicate entries appended.

## Failed hypotheses and limits
- b versus -b is an explicit T-dual control, not nondual.
- b=1/17 does not match the finite spectral window.
- Finite-box agreement does not prove theta-series equality.
- Existing published nondual isospectral Narain pairs eliminate a bare existence novelty claim.
- No inverse rigidity theorem or new nondual full-spectrum pair proved.
- No pinned P27–P29 CI logs or matrices recovered.
- Locally executed independent checkers are not byte-identical to the cleaner committed P30 control; do not conflate hashes.

## Exact local execution
Checker A: Python 3.13.5 SymPy 1.14.0; source SHA256 ff4fa844b544aa045de9b2c6bf791d5429412bcd2df5892067f92b07fa276291; stdout 44c3627d7c73bdfb0613933539bdaf7cef4b5114bacc2a3193060c436fef0517; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; wall 8.43s RSS 128912 KB exit 0.
Checker B: independent Fraction arithmetic; source SHA256 519a9a374279b7fd2c3f77c64f78394e67ddd2f4d4fc06358887c371a2321c16; stdout bac019f9eee8075d408410c7e55664143d42c027cd91cb2edce2b8c93f189016; stderr empty; wall 4.69s RSS 97420 KB exit 0.
Local raw outputs and sources are in /mnt/data/p30, but were NOT committed byte-identically. Committed evidence/P30/reproducible_spectral_control.py is a separate equivalent exact control. No manuscript.
