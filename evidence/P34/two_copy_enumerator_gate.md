# P34 — Exact two-copy complete enumerator control (2026-10-27)

## Scope and conclusion
For the published seven-vertex Dymarsky–Shapere isospectral graph pair, independently enumerate ordered pairs of graph-code stabilizer words. The raw 16-symbol complete enumerators differ, while the genus-one refined enumerators agree. This is a rigorous algebraic result, NOT yet a proof that physical genus-two partition functions differ: the genus-two higher-weight theta substitution may have a kernel. Henriksson, Kakkar and McPeak, JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011, prove the higher-genus code-CFT polynomial framework and discuss genus-two distinctions. The reference is already in the verified bibliography; no duplicate entry.

## Exact local experiment
Graph A edges: (0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5).
Graph B edges: (0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6).
For every x in F2^7, let z=A*x over F2. Encode each site as symbol s_i=x_i+2*z_i in {0,1,2,3}. For each ordered pair (u,v) of the 128 codewords, count the 16 site types s_i(u)+4*s_i(v), obtaining one 16-component exponent vector summing to seven. Compare integer multiplicities of all exponent vectors.

Results: genus-one equality true, 16 genus-one monomials; 16,384 ordered pairs per graph; genus-two raw complete enumerator equality false; A has 7,579 monomials, B has 5,246, with 9,448 different coefficients. Positive and negative total coefficient differences are both 10,827. A first positive witness exponent [0,0,0,0,0,0,0,1,0,0,0,2,0,1,2,1] has difference +2. A first negative witness [0,0,0,0,0,0,0,1,0,0,0,2,2,0,1,1] has difference -2. These are raw algebraic witnesses only, not physical theta-function witnesses.

## Actual executed local evidence
Python script /mnt/data/p34/genus2.py. Source SHA256 2fac9d30c7ff609bccb7a322be8a6f39f27b4c2b51afbd1e2316e4dcb738d436. stdout SHA256 9ccd8d2beb92c4195189b81ec8af42f4510c0acb0fa2a7d953538fe5cbf94c6d. stderr empty, SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. resource SHA256 e94c33c2af1d05fde508978966741a3898bd877f778c14496492f8fd48585f72. Exit 0, wall 1.06 seconds, max RSS 100500 KB. Internal enumerator computation 0.049163 seconds. Source and raw logs exist locally but are not yet committed byte-identically.

## Failed hypotheses and unresolved gates
1. The genus-one equality does not extend to equality of raw complete two-copy enumerators.
2. Raw polynomial inequality does not automatically imply physical genus-two partition-function inequality after higher-weight theta substitution.
3. P33 published code-level ELC inequivalence is not a fresh standalone proof of full Narain O(7,7;Z) inequivalence without the paper's equivalence framework.
4. Missing P27–P29 CI pinned matrices remain unresolved.
5. No new theorem or novelty has been established.

## Strict decision
GO: exact two-copy code enumerator inequivalence.
REVISE: exact physical genus-two theta substitution, byte-identical remote replay, pinned CI, independent second implementation.
NO-GO: new inverse-spectral theorem, new counterexample, novelty, breakthrough and manuscript.
P35 is appropriate only as a controlled genus-two theta specialization verification, not a publication phase.
