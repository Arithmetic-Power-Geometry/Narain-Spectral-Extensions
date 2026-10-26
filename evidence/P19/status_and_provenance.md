# P19 evidence and limitations — 2026-10-26

## Executed locally
Fetched the original evidence/P02/independent_checker.py from GitHub, copied it verbatim into local /mnt/data/p19_local/p02.py, and ran python in the container. Original fetched source length 3034 characters; local executed file 3034 bytes. Exit 0, 4.184 seconds, stderr empty. Source SHA256 48767666983c64a1e11efd7863fae0a79b7ebce627607e094648a101fcd10493; stdout SHA256 1cd74dbc6e97a6d162164008709895ea71e1c4d8559cc7ac214250da8be65bc7; stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Full source and stdout committed as P02_executed_source.py and P02_actual_stdout.json. Source is a verbatim copy, not a pinned git checkout; distinguish this from P11's requested original checkout audit.

Output: PASS; 729 charges, 576 nonzero-spin per sign; each sign 570 strict, 2 at_zero, 2 at_half, 2 identical; gap 6/265; first threshold 3313/1325; 39 states per sign. Its JSON content matches committed P02/results.json semantically. This does not verify Paper I's separate 68-row interval asset.

## Original P01-P09
Fetched and inspected the nine original source files from GitHub. Their GitHub blob IDs and source lengths were recorded in connector output; no original full checkout was obtained in this local environment (git remote fails DNS). Only P02 was executed locally. The new P19 workflow should execute all nine from its pinned checkout and commit actual logs. Workflow creation is NOT proof of completion. No fabricated P01/P03-P09 outputs.

## References
Fetched reference/references.bib and reference/verification_register.tsv: 13 BibTeX keys, 13 unique six-column TSV rows, key sets match, every row marked VERIFIED. This is a structural check only; no new external publisher DOI metadata was verified in P19. No reference metadata was changed.

## P18 artifact recovery
The available GitHub connector exposes run/job/artifact fetches by known run ID, but no general list-runs or dispatch operation. P18 run ID is not known. No P18 completed artifact was recovered. The newly installed P19 workflow is designed to persist run results to the repository to eliminate this discovery blocker, subject to GitHub Actions execution and permissions.

## Gate
REVISE — P02 local run PASS; original nine-run CI result unverified, Paper I interval unverified, external bibliography recheck incomplete. No manuscript authorized.
