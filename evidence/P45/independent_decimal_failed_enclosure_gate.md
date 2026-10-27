# P45 — independent Decimal backend adversarial audit: FAILED enclosure

Date: 2026-10-27. No manuscript. This is a failed hypothesis and is preserved append-only.

## Independent test
A separate Python stdlib decimal + fractions evaluator was written at /mnt/data/p45/independent_decimal.py. It uses a different numerical backend from P42-P44 (mpmath.iv), builds the 16 four-index local Gaussian theta values by exact rational exponents and decimal transcendental evaluations, then evaluates full graph-code sums. It was intended as an independent outward-rounded baseline. Executed three cases at Y=[[1.1,.23],[.23,1.3]], lambda=.949:
- n=1 identical empty graph pair, K=2: status INCONCLUSIVE.
- n=2 empty vs one-edge, K=2: status POSITIVE.
- n=7 published pair, K=3: status NEGATIVE.

## CRITICAL FAIL: invalid enclosures
The computed *truncated* intervals do not have ordered endpoints:
- n=1 identical: [1.4247233264285E-28, -1.4247233264285E-28], lower > upper.
- n=2 unequal: [1.55808975775358094486356061795502003519065, 1.55808975775358094486356061727560776358183], lower > upper.
- n=7 published: [-0.00222049812364534235672839701428352069923, -0.00222049812364534235672839831617146853472], lower > upper.
The implementation's Decimal.exp use does not provide the required directed-rounding guarantee merely by setting context.rounding. Its finite sums are NOT valid outward-rounded intervals. Even if tail widening yields plausible intervals, that cannot retroactively validate the truncated enclosures. Therefore the purported independent certified backend FAILS. Sign agreement is only a numerical diagnostic, not a rigorous cross-check.

## Real local provenance
Source /mnt/data/p45/independent_decimal.py SHA256 ca3a35fe80637d5e1130aea1a75f915ba8f5939c3fee547fe48de5fbe9f34e16; Git blob 6aa3da7abb0424e4cdc479402bd933e45f34772a.
stdout /mnt/data/p45/stdout SHA256 d48e5dd1519c80e5c8e879eaa12b931f534643c1efa4427350ee2f4514f2d29c.
stderr empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
resources SHA256 f16b7d5d653f559ee9a47d16217a7d617bca1ddeee2d6900a5b9f7f651c3265d.
Exit 0; wall 8.87s; peak RSS 96264 KB. The process exit status 0 does NOT indicate a valid interval proof. Raw files exist locally; source/logs have not been committed byte-identically to GitHub.

## Research implications
The P44 mpmath.iv result is NOT disproved by this failure; it remains a separate backend with its own assumptions. But P45 provides no independent certified corroboration. Before proceeding, implement a genuinely rigorous second backend, e.g. exact-rational Taylor enclosures with mathematically proved remainder or a verified MPFR directed-rounding library, and add mandatory interval-invariant assertions (lower <= upper) at every operation. Re-run all controls and compare against P44 only after invariant tests pass.

GO: defect detection, negative-control stress test, append-only failure provenance.
REVISE: independent certified implementation, raw GitHub artifacts, full baseline comparisons, CI.
NO-GO: independent rigorous replication, novel algorithm theorem, original Q1 paper.
