# P12 — precise parity and spin-preserving spectral obstruction
Date 2026-10-26. Theorem scope: mathematical zero-mode Narain lattice; not BRST physical string states.

Let d>=1, G real symmetric positive definite, B real antisymmetric. For m,n in Z^d define
E_{G,B}(m,n)=(m+Bn)^T G^{-1}(m+Bn)+n^T G n,
s(m,n)=m^T n,
N_{G,B}(e,k)=#{(m,n) in Z^(2d): E=e, s=k}.
Every finite e has finitely many charges, since G is positive definite and the energy form is positive definite.

THEOREM 1 (parity bijection). The map P(m,n)=(m,-n) gives
E_{G,-B}(P(m,n))=E_{G,B}(m,n), s(P(m,n))=-s(m,n).
Therefore N_{G,-B}(e,k)=N_{G,B}(e,-k) for every e,k. In particular the unrefined energy counting functions are identical at all energies. Proof: -B times -n equals Bn, and n^TGn is invariant.

THEOREM 2 (spin-preserving equivalence obstruction). Suppose an integral bijection of charge lattices T:Z^(2d)->Z^(2d) obeys E_{G,-B}(Tq)=E_{G,B}(q) and s(Tq)=s(q) for all q. Then N_{G,-B}(e,k)=N_{G,B}(e,k) for every e,k. Contrapositively any rigorously certified nonzero difference N_{G,B}(e,k)-N_{G,-B}(e,k) rules out ALL such spin-preserving integral bijections, including those arising from an O(d,d;Z) transformation that preserves the specified E and spin observables. Proof: bijection transports finite charge fibers.

THEOREM 3 (explicit geometric GL test). For U in GL(d,Z), if U^T G U=G and U^T B U=-B, then T(m,n)=(U^{-T}m,Un) maps the +B background to -B with identical E and spin. Proof: B_- Un=-BUn=-U^{-T}Bn using U^TBU=-B; so m'+B_-n'=U^{-T}(m+Bn), and (U^{-T}x)^TG^{-1}(U^{-T}x)=x^TG^{-1}x from U^T G U=G; n'^TGn'=n^TGn. Spin is m'^T n'=m^Tn. Therefore a nonzero signed coefficient excludes any such U, not just signed permutations.

APPLICATION: P02 T2 first difference at E=3313/1325: +2 for s=-1, -2 for s=+1 (difference +B minus -B). P07 T3 first E=1164367/582071, T4 first E=9437981/4718325: +2 at s=+1, -2 at s=-1. Provided exact completeness checks are sound, each gives an obstruction to ANY energy- and spin-preserving charge bijection, stronger than the restricted signed-permutation search. This is a consequence of the observable's definition, not proof of physically distinct unoriented CFTs.

IMPORTANT SCOPE: Worldsheet orientation reversal changes conformal spin sign, and may identify B and -B in a parity-enlarged category. A nonzero spin-refined coefficient does not establish inequivalence if parity is allowed. Nor does it establish a new physics observable after modular integration, level matching, GSO/BRST projection or ghost contributions. O(d,d;Z) dualities preserve the underlying left/right conformal weights in the usual convention, hence preserve E and s when those are exactly the observables under study. This statement requires fixed normalization and orientation, not a classification of all CFT equivalences.

NOVELTY GATE: REVISE. Theorems 1-3 are elementary algebraic consequences and cannot be advertised as breakthrough. Their application strengthens the logical interpretation of existing finite certificates but does not solve the missing independent reproduction or all-parameter stability problems.

ADVERSARIAL CONTROL: If equivalence is permitted to reverse spin, the parity map P exists universally; thus the naive claim 'B and -B are inequivalent under all symmetries' is false.

NEXT: Complete P11 workflow logs and independent reproductions; then P13 exact integral indecomposability or counterexample.
