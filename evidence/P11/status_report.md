# P11 execution-status audit
Date: 2026-10-26. Strict gate: REVISE / NOT VERIFIED.

The original P01-P09 checker source files were inspected through GitHub. A GitHub Actions workflow was committed at .github/workflows/p11-reproduction.yml, configured to run every checker unchanged, save stdout/stderr, hashes, exit status, runtimes and JSON comparisons, and upload an artifact.

IMPORTANT: No completed GitHub Actions run or downloaded logs were obtained in this session. The isolated local container cannot resolve github.com and cannot clone this private repository. Therefore **none of the nine verbatim checker reruns is claimed to have completed during P11**. Workflow installation is not proof of workflow execution. No stdout or exit code is invented.

The P10 correction of the verification register was independently read back: 12 records, 6 columns each, 12 matching BibTeX keys and all VERIFIED source URLs. This verifies structure and recorded status, not fresh publisher-level DOI checking.

P02 polynomial classification and Paper I's interval certificate remain pending a clean-room rerun and independent source examination. No new mathematical theorem or duality claim is made here. All historical evidence preserved.

Next: inspect GitHub Actions -> P11 reproducibility; obtain completed run artifact. If actions unavailable, execute the exact commands from a complete repository checkout in a trusted runner. Compare each JSON field and retain errors. Then run the P12 parity/duality theorem programme.

P12 prompt: Formalize the orientation-preserving Narain equivalence and parity maps, prove precisely when conformal spin is invariant, and use exact first nonzero (E,s) coefficient to derive a duality obstruction with explicit assumptions. Test adverse symmetries and integral automorphisms. Save all code, proofs, failures and references append-only in evidence/P12, commit only to this repository and return GO/REVISE/NO-GO. Do not assert a physical inequivalence beyond the defined category.
