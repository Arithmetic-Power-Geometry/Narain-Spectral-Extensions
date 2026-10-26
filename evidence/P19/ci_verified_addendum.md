# P19 CI execution verified — append-only addendum (2026-10-26)

This file supersedes the **status assessment** in status_and_provenance.md, but preserves that earlier time-stamped record unchanged. After the P19 workflow was created, it actually executed and committed its logs to evidence/P19/ci_run.

## Provenance
Pinned Git checkout: 9670e2449d682900fd3218db208730d6bff53f7c.
Python: 3.13.16; Linux-6.17.0-1022-azure-x86_64.
Source SHA256, actual stdout SHA256, stderr SHA256, exit code, runtime and recursively computed JSON differences are in ci_run/matrix.json. Actual stdout/stderr and per-file artifact hashes are committed. 28 artifact files listed in ci_run/artifact_sha256.json. All nine original scripts exited 0. No historical P01-P09 file was rewritten.

| Phase | Exit | Seconds | JSON field differences | Classification |
|---|---:|---:|---:|---|
| P01 | 0 | 0.036 | 15 | Different purpose/schema: checker metadata lint vs research-status baseline |
| P02 | 0 | 1.730 | 0 | Exact JSON match; polynomial assertions PASS |
| P03 | 0 | 0.069 | 0 | Exact JSON match |
| P04 | 0 | 0.106 | 0 | Exact JSON match |
| P05 | 0 | 0.083 | 0 | Exact JSON match |
| P06 | 0 | 16.535 | 20 | Extra G/B/bounds/unrefined fields in checker and prose limitation representation; overlapping case values agree |
| P07 | 0 | 7.554 | 1 top-level type | stdout list vs baseline object containing results list plus added bounds and signed-permutation field; overlapping case values agree |
| P08 | 0 | 8.509 | 0 | Exact JSON match |
| P09 | 0 | 0.026 | 0 | Exact JSON match |

## Reconciliation details
P01 differences are all missing/extra top-level keys, not numerical discrepancies. P06 20 differences are 18 extra per-case diagnostic fields, one limitation field and one limitations-list field; overlapping case values agree: dimensions 3/4/6, n/m counts, states, null first discrepancy and cutoff. P07's stdout is a list of three case objects and baseline is {results:[three enriched case objects],gate:'REVISE'}; the overlapping keys d,H,n_candidates,m_candidates,states_each,first,first_coeff agree. None of these differences should be silently 'fixed' by modifying historical outputs.

## Remaining gates
- P11 nine-original execution: **PASS**. P02 polynomial checker run: **PASS** with exact JSON match.
- Paper I separate 68-row interval certificate: **UNVERIFIED**. No original 68-row asset and independent verifier were obtained; cannot claim a pass.
- Reference metadata: 13 BibTeX keys and 13 matching six-column TSV entries structurally consistent. Independent publisher/DOI re-verification **not performed** this phase.
- P13 GL(d,Z) proofs have prior algebraic cross-check; full O(d,d,Z) indecomposability remains unresolved.
- P14 open-neighborhood stability not proved; P15/P16 T6 first threshold independently reproduced in previous phases.
- Q1 novelty remains NO-GO pending P20-P23; no manuscript authorized.

**Strict P19: REVISE overall**, with the nine-script reproduction subgate upgraded to PASS. Next P20 (full duality decomposition) or P21 (robust separation) should only claim theorems after independent proof and adversarial tests.
