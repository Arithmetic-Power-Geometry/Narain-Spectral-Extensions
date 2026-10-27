# P46 — corrected independent Decimal interval audit (2026-10-27)

## Scope and honest status
A second implementation based on Python stdlib decimal and fractions (no mpmath import) repairs the P45 interval-order failure. The local executable is /mnt/data/p46/verified_decimal.py. This report is committed to GitHub; the executable and raw logs remain local, **not committed**, so remote source readback is NOT claimed.

## Correction
P45 incorrectly assumed that Decimal.exp obeys context-directed rounding. Python decimal documents exp() as correctly rounded using ROUND_HALF_EVEN instead. P46 evaluates Decimal.exp at 70 decimal digits and expands each nonpositive-argument result by 1e-65 absolute, which exceeds one ulp at that precision. Exact rational Machin-type alternating arctangent bounds enclose pi, converted by directed decimal division. Other elementary operations use ROUND_FLOOR/ROUND_CEILING; all interval additions, multiplications, differences and final intervals assert lower <= upper. This is an independently implemented enclosure **conditional on the Python decimal documentation and correct arithmetic implementation**; not a machine-checked proof.

## Real local run
Python 3, exit 0, wall 12.45 s, max RSS 96240 KB; stderr empty.
SHA256 source 49200250eed3460e5f2a3d337f0794af3e965a0564fac5fff343534e36ee3439.
Git blob local source 53c31268077748cbceee42e8c53e89b06214410b.
SHA256 stdout 7b5159b89a60737f03d387d3f2924b840bf945e4376ea596248013671a5e3bdd.
SHA256 stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
SHA256 resources 608c7b39fdd211f99232ff332677c64f70846adfb2ea825ad8eddef380eb40aa.

## Three executed cases at Y=[[1.1,.23],[.23,1.3]], lambda=.949
1. Identical n=1, K=2: truncated [-4.31e-39,+4.31e-39], infinite [-1.27880629002533847350381590171937600920976e-14,+1.27880629002533847350381590171937600920976e-14]; INCONCLUSIVE.
2. Unequal n=2, K=2: truncated [1.55808975775358094486356061735682016429706,1.55808975775358094486356061735682016431977], infinite [1.55808975775312670999708366089666877131296,1.55808975775403517973003757381697155730387]; POSITIVE.
3. Published P33 n=7, K=3: truncated [-0.00222049812364534235672839766311023352146,-0.00222049812364534235672839766311023282936], infinite [-0.00222049812364534235754321288184800713315248,-0.00222049812364534235591358244437245921766752]; NEGATIVE.

The independently calculated analytic tail for case 3 is 8.14815218737773611692478963002704826023477e-22. All three final enclosures have ordered endpoints and agree in sign with P44.

## Remaining correctness and novelty gaps
- This implementation still relies on correct decimal.exp rounding and a fixed absolute padding; it does not formally verify the runtime implementation of exp.
- This is independent source and arithmetic backend, but shares the same mathematical Gaussian expression and tail inequality as P44; a separate derivation and independent physics map audit remain necessary.
- No large randomized test suite, ill-conditioned cases, baseline benchmark against state-of-art Siegel theta software, pinned remote CI, or full remote source/log upload.
- No novel Narain pair, inverse-spectral theorem, or demonstrated original certified-theta algorithm. Prior published seven-vertex example remains prior art.

GO: independent repaired ordered enclosures and three passing controls, including nonzero seven-vertex certificate.
REVISE: upload full source and raw logs, verify remote source readback, property tests and rigorous prior-art comparison.
NO-GO: original Q1 physics manuscript.
Next P47: multiple graphs and period matrices with independent cross-backend testing, including near-separating and ill-conditioned matrices, and explicit failure statuses.
