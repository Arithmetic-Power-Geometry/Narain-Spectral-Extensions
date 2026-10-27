# P52 — exact algebraic closure audit and comparator feasibility gate

Date: 2026-10-27. This is a finite integer-enumeration replay, not a FLINT benchmark or a novel theorem.

## Environment and comparator gate
Python 3.13.5; python-flint not installed (importlib.find_spec('flint') is None). A pip index probe failed with DNS resolution errors; an external FLINT installation or equivalent certified-theta comparison could not be completed in this environment. No claims of comparison to FLINT, Sage or state-of-the-art theta software.

## Preserved failed hypothesis
The first locally executed P52 audit assumed the *fully four-symbol* genus-one code enumerators of the published seven-vertex graph pair were identical. It exited 1 at assert ga==gb, wall 1.29s, RSS 99468 KB. This hypothesis is false: the published equality is for the coarser three-symbol specialization identifying X and Z, not the fully refined four-symbol enumerator. The original failed source SHA256 bd6b55c9526401fc7eb2328d4647c030844579fa01d567034fcc177a34ab2372; stderr SHA256 53753616f8c15a5187325029162f01d8be11a8b5d514614137f5fb3dc447c678; stdout empty SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources SHA256 114469e29f529124e6306fac43dddc6adfba64c6104d394bd6a858c435fbf8ae. The failed version was not uploaded; this record preserves its failure.

## Corrected exact algebraic replay
Committed evidence/P52/audit.py, locally executed byte-identical (Git blob eb40b41c24671c445b332d7439f2226230faf126). Independent finite integer codeword enumeration builds 16-symbol genus-two polynomial counters, projects each variable t_{a,b} to X_{class(a)}Y_{class(b)} where classes are identity {0}, X/Z {1,2}, Y {3}, and verifies the projected polynomial equals the exact outer product of the common three-variable genus-one enumerator with itself. Exact equality of projected genus-two polynomials follows by integer coefficient equality, with no numerical rounding.

Corrected output: graph A 7579 genus-two monomials, graph B 5246, union 10127, 9448 differing coefficients; common genus-one polynomial 16 monomials; separating polynomial 256 monomials; exact separating equality PASS and factorization PASS. This is consistent with prior P33/P36 results and is NOT a novel spectral distinction. Four-symbol genus-one equality is NOT claimed.

Corrected run exit 0; wall 1.45s; RSS 100620 KB; stderr empty. SHA256 source 69cde3302ed0385ac5b7f8e4ee8b81f106e9a1e7f0e9506577bb953c15363159; stdout 753bb39e5cc8b98739c0f5ed1ef5579b1d23073af7c5dd057884eadfd73a3030; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; resources 75bfecacfdf63efb60611caa70359bef5133bc832c4bfa24210af18b37f43cee. Raw logs are local, not remotely committed.

## Publication gate and stopping decision
GO: exact finite-code algebraic consistency, preserved failed hypothesis, byte-identical committed corrected source.
REVISE: externally benchmark a pinned certified theta implementation on equivalent mathematical inputs and normalization if available; resolve full physical theta map and derive a nontrivial novel code-specific result.
NO-GO: general four-symbol genus-one equality, completed FLINT comparison, novel theta algorithm, new Narain physical theorem, original Q1 manuscript.
STOP: further routine phases are not scientifically justified without a concrete new novelty hypothesis and executable independent external baseline. Archive P01–P52 as a reproducibility/negative-results research program rather than submit unsupported Q1 novelty claims.
