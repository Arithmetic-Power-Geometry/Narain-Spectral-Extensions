# P27 — Hostile novelty and reproducibility gate (append-only)

## Theorem
See all_dimension_theorem_and_P28.md for the complete proof valid for all d>=2. Explicit witness set has size 3d-1 and proves absence of any simultaneous integral J/Q orthogonal product splitting under full O(d,d;Z). This is a true mathematical extension of P26 d=3,4,6; it is not an independently verified new theorem in the published literature.

## Local exact execution
Python 3.13.5, SymPy 1.14.0, /usr/bin/time. Exit 0; wall 2.31 seconds; RSS 128788 KB; empty stderr. Exact rational inverse and all 3d-1 witness energies <2 for d=2,3,4,5,6,8,10,12,16,20,30. Local source SHA256 a76b67bd262abb368505de314d95fc95d8c5d616a5870e41219998b67d7fbe6a; stdout SHA256 87a903bc797c8f828643d48a421ca1bfcd8ae319988c2859591940ae7c681b1f; stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Exact locally executed source restored including unused import. Output, resource and hashes saved append-only. GitHub readback verified for proof, source, stdout and provenance.

## Reproducibility outstanding
P25/P26 CI matrix files were NOT FOUND on GitHub when queried. P27 workflow .github/workflows/p27-verify.yml committed; CI matrix evidence/P27/ci_run/matrix.json not yet independently retrieved. Do NOT report CI success without that artifact. Historical P23 semantic comparison failure preserved.

## Literature kill test
- Eichler–Kneser theorem on indecomposable positive definite lattices and connected short/indecomposable vector classes, independently visible in https://www.geotop-bielefeld.de/node/830 and https://www.math.rwth-aachen.de/~Markus.Kirschmer/papers/herm.pdf . This is a close and powerful novelty obstacle for any claim that graph connectivity alone is new.
- Nikulin (1980), Integral symmetric bilinear forms and some of their applications, Mathematics of the USSR-Izvestiya 14(1), 103-167, DOI 10.1070/IM1980v014n01ABEH001060, primary bibliographic source https://www.mathnet.ru/eng/im1677 . Already in reference/references.bib.
- Hosono, Lian, Oguiso and Yau rational Narain lattice/gluing prior art requires closer comparison; no claims of new discriminant-gluing formalism.
- The explicit all-dimensional rational chain example and 3d-1 short witness proof are new *within this project*, but a mathematically elementary construction from classical methods. No peer-reviewed novelty priority established.

No new BibTeX records were appended because no newly identified primary paper had its full bibliographic metadata independently verified beyond the references already recorded. Existing 18 bibliography/register entries remain append-only.

## Failed conjectures / scope restrictions
1. P25/P26 CI cannot be claimed recovered: missing output files.
2. Full arbitrary rational Narain decomposition algorithm not proved; the certificate is sufficient, not necessary.
3. No uniform perturbation radius established.
4. No physical CFT irreducibility theorem beyond integral zero-mode J/Q orthogonal factorization.
5. No proof that Eichler–Kneser or related work does not subsume the graph idea.
6. Arbitrary dimension means each d>=2 in the stated rational chain family, NOT every rational G/B background.

## Gate
GO mathematical correctness of explicit all-dimensional chain obstruction.
REVISE reproducibility (pinned CI still pending).
NO-GO novelty/Q1 manuscript pending independent originality audit and stronger contribution.
