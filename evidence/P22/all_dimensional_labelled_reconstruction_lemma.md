# P22 preliminary all-dimensional theorem — labelled zero-mode reconstruction

Let d>=1, L=Z^(2d), and Q(G,B)=[[G^-1,G^-1 B],[-B G^-1,G-B G^-1 B]], with G positive definite symmetric and B skew. E(v)=v^T Q v for labelled integral charge vectors v=(m,n).

**Proposition.** The 2d diagonal observations E(e_i), together with E(e_i+e_j) for 1<=i<j<=2d, determine Q exactly, hence determine G and B uniquely. There are (2d)(2d+1)/2=d(2d+1) observations. Indeed Q_ii=E(e_i), and Q_ij=[E(e_i+e_j)-E(e_i)-E(e_j)]/2. The top-left d-by-d block A of Q equals G^-1, so G=A^-1. The upper-right block C equals G^-1 B, so B=G C. This works for all d and over any field of characteristic not 2 where G is invertible. Each operation is exact rational arithmetic for rational input.

**Important limitations:** This is elementary polarization, NOT a new inverse-spectral theorem, because the charges are labelled. It does not solve reconstruction from an unlabelled theta series or prove a finite cutoff for spectral data. It does not identify O(d,d,Z) orbits from spectral multiplicities. It should be used as a positive control and a lower-bound target for attempts to remove labels.

**Research challenge:** Prove a nontrivial effective unlabeled reconstruction theorem under explicit height restrictions, or produce an exact minimal-dimension counterexample; distinguish equality of full spin-refined spectra from O(d,d,Z) equivalence. Do not conflate labelled polarization with breakthrough novelty.
