# P51 — internal baseline and external comparator availability gate (2026-10-27)

## External comparator status
Checked Python environment: Python 3.13.5, mpmath 1.3.0, importlib.util.find_spec('flint') returned False. The python-flint package was NOT available. NO FLINT numerical benchmark was executed. Do not claim a comparison to FLINT, Sage, quasi-linear theta algorithms or a state-of-the-art certified method. The requested external baseline remains blocked/unperformed.

## Executed internal baseline
Source evidence/P51/internal_baseline.py, byte-identical to locally executed /mnt/data/p51/benchmark.py (Git blob 1197a6a12c21e58ce14aca96f0aa468d90026ff6; SHA256 446b1570d697c10891ecafec890ddf20d6025cda79d1aa653175706a3b294b0f). Imports P42 certified_theta.py, uses mpmath.iv 30 dps, K=1 and rational decimal Y=(1.1,.23,1.3). For each graph, constructs exact Counter of 16-symbol genus-two monomial signatures across all ordered codeword pairs, then evaluates grouped polynomial with interval arithmetic; compares to direct word-pair interval evaluation. All four intervals overlap; overlap is a consistency check, NOT equality proof of infinite theta functions, and K1 does not imply certified nonvanishing.

Results (single-run timing; seconds):
- n2 empty: 16 pairs, 10 monomials, aggregation .000047, direct .000191, polynomial .000204, overlap yes.
- n4 one edge: 256 pairs, 100 monomials, aggregation .000305, direct .004263, polynomial .003219, overlap yes.
- n7 published A: 16384 pairs, 7579 monomials, aggregation .168837, direct .451971, polynomial .469325, overlap yes. Including aggregation, grouping is SLOWER.
- n7 published B: 16384 pairs, 5246 monomials, aggregation .022626, direct .393905, polynomial .226206, overlap yes. Including aggregation, grouped total .248832 s vs .393905 s direct; only one case.

Execution: exit 0, wall 4.89s, peak RSS 102280 KB, stderr empty. SHA256 stdout 9e54b74377f55cf73d1523c690772f3fba60e71304a3d867b6ff94ebc667c492; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 533880d91f3b40ab7d34dcf3315ddead478473196d5e1e28bfe5c63e1e354af6. Local raw logs /mnt/data/p51/{stdout,stderr,resources} not remotely committed.

## Interpretation and research gate
Exact monomial grouping does not universally accelerate evaluation. Its one-time construction cost and variable unique-monomial counts matter; results do not show improved asymptotic complexity or novelty. No repeated timing distributions, higher precision scaling, multiple period matrices or independent external implementation benchmark. P50's hostile prior-art NO-GO remains.

GO: four measured internal cases, interval-overlap checks, executed source byte-identical to GitHub.
REVISE: install/pin an accessible certified theta implementation and match normalization and inputs, repeat timing across precision and graph size, add CI and remote raw logs, prove any genuine code-specific advantage.
NO-GO: claim that FLINT was benchmarked, that grouping is generally faster, that a new algorithmic theorem was proved, or that an original Q1 manuscript is ready.

Next decision: a bounded external-comparator feasibility gate. If a rigorous equivalent FLINT benchmark cannot be run and no nontrivial novel theorem survives, close the Q1-novelty claim and archive as a reproducibility study.
