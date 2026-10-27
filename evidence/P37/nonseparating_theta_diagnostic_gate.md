# P37 — Nonseparating genus-two direct theta diagnostic (2026-10-27)

## Primary source
Henriksson, Kakkar and McPeak, Narain CFTs and quantum codes at higher genus, JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011, equations (3.14)-(3.15), (3.20), (3.28)-(3.32), (3.37)-(3.47). Verified publisher primary source https://inspirehep.net/files/a4114600f231e0b863f9b88bc7333031 . The source is already in reference/references.bib and verification_register.tsv; no duplicate.

## Local direct nonseparating analytic diagnostic
Period matrix Omega=i[[1.1,0.23],[0.23,1.3]], positive definite, off-diagonal nonzero. For every ordered pair of codewords of the P33 seven-vertex pair, compute a product over seven sites of truncated local theta series. Each local series sums integer a,b in [-K,K]^2 and evaluates exp(-pi * [(a+alpha/2+b+beta/2)^T Y (a+alpha/2+b+beta/2) + (a+alpha/2-b-beta/2)^T Y (a+alpha/2-b-beta/2)]). This directly implements the positive real Gaussian version of the published code-to-lattice theta map for purely imaginary Omega. No reliance on P35 formal polynomial differences.

K=2: A=1.9619805059406255, B=1.964201004064273, A-B=-0.002220498123647552.
K=3: identical at printed precision.
Local execution exit 0, wall 1.68 seconds, peak RSS 95624 KB, stderr empty.
Actual local source SHA256 0644956553e4ba0aefe1f39b68967263a2c8f33148ac51b565bf3c5f072bba36.
Actual stdout SHA256 0ee106d737f73d77372f4fae11a593651132bb01dd7707e8e0807fcddb34c434.
Actual stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
Actual resource SHA256 eb191c25ed72e20a81976b70f6e2051019f574ca061bb764d6c00d63a7fc5801.
Raw local source and logs: /mnt/data/p37/diagnostic.py, stdout, stderr, resources. They are NOT yet byte-identically uploaded to GitHub; do not attribute these hashes to any remote checker.

## Rigorous tail strategy (not yet a certificate)
Let lambda_min(Y)=(2.4-sqrt(0.2516))/2 > 0.949. For each of the four shifted integer summation coordinates, Gaussian exponent is bounded below by 2*pi*lambda_min(Y) times its squared magnitude. A union bound on coordinates outside [-K,K] yields a computable positive theta-tail upper bound based on exp(-2*pi*lambda_min*(K+1/2)^2), multiplied by an upper bound for the three unrestricted Gaussian sums. Propagate through sevenfold products and 16384 codeword pairs. This controls mathematical truncation, but the current IEEE double-precision evaluation lacks an independently certified rounding enclosure. Therefore no rigorous analytic nonzero certificate is claimed.

## Publication gate and failed hypotheses
GO: exact verified bibliography count 21 references / 21 verification-register entries; local nonseparating theta diagnostic nonzero; numerical K=2/K=3 convergence.
REVISE: certified interval arithmetic, explicit total tail bound and independent implementation; byte-identical remote execution; P27-P29 pinned CI.
NO-GO: new theorem, original nondual isospectral construction, Q1 original-research paper, breakthrough.
A reproducibility/verification paper is conceivable only with a clearly delimited new reproducibility contribution and full attribution to the 2021 and 2023 published results. No manuscript drafted.
