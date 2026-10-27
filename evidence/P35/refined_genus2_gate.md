# P35 — Genus-two refined enumerator verification, 2026-10-27

## Primary source
Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011, https://inspirehep.net/files/a4114600f231e0b863f9b88bc7333031 ; equations (3.28), (3.32)–(3.46), especially 10-variable refinement (3.37)–(3.46). The paper states genus-two theta functions have relations; do not identify distinct refined polynomials with analytically distinct partition functions without proving nonvanishing modulo those relations. The paper's (3.46) text appears to duplicate ZZ already assigned in (3.43); its expanded equation (3.47) identifies the final class as XZ or ZX. Code uses XZ/ZX and flags this convention for independent source checking.

## Exact independent experiment
Graph edge lists are reproduced in evidence/P35/check.py. Every one of 128 stabilizer words from each graph is enumerated and all 128^2=16384 ordered pairs are mapped into the 10 classes: (I,I), (I,Y), (Y,I), (Y,Y), (I,X/Z), (X/Z,I), (X,X)/(Z,Z), (Y,X/Z), (X/Z,Y), (X,Z)/(Z,X). Code convention 0=I,1=X,2=Z,3=Y. This corresponds to the published refined genus-two polynomial.

Each graph produces 1251 distinct monomials; 756 coefficient differences. Lexicographically first positive difference is exponent [0,0,0,0,0,0,1,0,2,4] with +10; first negative is [0,0,0,0,0,0,1,0,4,2] with -2. Both coefficient sums equal 16384.

Local exact execution: exit=0, wall=0.97s, max RSS=96276 KB, stderr empty.
SHA256: check.py cf5a67c5582ef0e7014675a37e34323fb8fa979776599b395146e06694ed126b; stdout 313f63ebf2c09af6706b395a8c62b62b50dac08e00d679df51c2228d2782dd60; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 121fa0f4c923cc180fcd4fca8f41376bf079e354051b070ec29e375d4639f415. Raw source, stdout, stderr, resources and hashes committed separately. No GitHub Actions pinned execution claimed.

## Hostile gate
GO: exact genus-two 10-variable refined polynomial inequality; full 16384-pair enumeration and readback.
REVISE: nonvanishing under actual ten even theta constants, preferably by an exact nonzero Fourier coefficient or rigorous interval bound at a nondegenerate genus-two period matrix; independent second implementation; P27–P29 CI recovery.
NO-GO: claim of a newly discovered higher-genus distinction, novel theorem, publication manuscript. Published prior art already establishes higher-genus distinctions.
Failed hypotheses: P34's 16-variable raw polynomial difference was insufficient; P35 shows survival of the 16-to-10 refinement but still does not establish analytic theta nonvanishing. Apparent source typo in eq (3.46) must be resolved from eq (3.47) and independent convention checks.
Next phase should be physical theta-map verification, not another paper draft.
