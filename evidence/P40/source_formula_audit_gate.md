# P40 independent code-to-lattice formula audit (2026-10-27)

## Original source
Henriksson, Kakkar and McPeak, *Narain CFTs and quantum codes at higher genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, publisher PDF https://inspirehep.net/files/a4114600f231e0b863f9b88bc7333031. Equations (2.38)-(2.42), (3.13)-(3.15), (3.19)-(3.21), (3.28)-(3.32), (3.37)-(3.47) establish Construction A lattice vectors, left/right momenta, higher genus local Gaussian theta and the genus-two theta polynomial substitution. Eq (3.46) reads x[XZ]=x[ZZ], conflicting with (3.43); explicit (3.47) gives XZ/ZX and resolves the apparent typographical error. No correction to the published source is asserted.

## New independent implementation
Independent source evidence/P40/audit.py constructs 16 local theta values directly from (3.29), using a,b in [-2,2]^2, Y=[[1.1,.23],[.23,1.3]], and loops over all 128^2 codeword pairs for each seven-vertex graph. It does not use the P35 polynomial reduction or P39 interval implementation. The q_L and q_R shifts are (a+alpha/2+b+beta/2) and (a+alpha/2-b-beta/2), respectively, with exponent -pi(q_L^T Y q_L+q_R^T Y q_R) for Omega=iY. Both graph theta sums use the same universal genus-two oscillator denominator, so unequal lattice-theta numerators imply unequal normalized partition functions if the common denominator is finite and nonzero at this Omega. The source's normalization was checked at the level of the lattice theta numerator; full measure, sewing conventions, and global Riemann surface period-matrix validity were not separately checked.

## Real local run
stdout:
A 1.9619805059406259
B 1.9642010040642739
difference -0.0022204981236479959
K 2 local_values 16
stderr empty. Exit 0; wall 1.06 seconds; max RSS 95756 KB.
SHA256 of executed source 69edf627993c2ee68d23e149b8a55d52faa61f692caf7d947c661ddbd502ad3f
stdout 0c8a6c6a5b76610c920f8bd2ffc4a352a4122737d438b87d15719a5ad4b99908
stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
resources 584fd1cbc4abf8ad757507a7c00e293d210d25727d8fb13e3ad2b46625302f8e

## Strict gate
GO: independent direct source-based Gaussian implementation, agreement with P37 numerical results, published theta-map equation checked.
REVISE: verify source file byte identity via SHA after remote fetch; independent certified interval replay and theta-map normalization under alternative conventions; P27-P29 pinned CI recovery; novelty-kill literature review.
NO-GO: novel isospectral counterexample, new theorem, original Q1 theoretical physics manuscript. Published 2023 paper already establishes genus-two distinctions of genus-one isospectral code CFTs. Existing verified bibliography remains 21; no duplicate entries.
