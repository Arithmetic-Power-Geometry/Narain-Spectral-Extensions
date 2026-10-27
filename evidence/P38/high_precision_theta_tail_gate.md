# P38: high-precision nonseparating theta evaluation and analytic tail bound (2026-10-27)

Primary literature: Henriksson, Kakkar, McPeak, *Narain CFTs and quantum codes at higher genus*, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011; Dymarsky, Shapere, *Quantum stabilizer codes, lattices, and CFTs*, JHEP 03 (2021) 160, DOI 10.1007/JHEP03(2021)160. Both already verified in reference/references.bib and verification_register.tsv; no duplicate entries.

## Computation
Reused P37's two seven-vertex graph codeword lists, 128 codewords each, and 16384 ordered pairs per graph. At Omega=i[[1.1,.23],[.23,1.3]], evaluate each 2D local Gaussian theta by summing four integer variables a0,a1,b0,b1 in [-3,3]. Site shifts alpha/2,beta/2 are binary. The exponent is -pi[(a+alpha/2+b+beta/2)^T Y (a+alpha/2+b+beta/2)+(a+alpha/2-b-beta/2)^T Y (a+alpha/2-b-beta/2)]. Seven local factors multiply per codeword pair. mpmath decimal precision 65.

Computed:
lambda_min(Y)=0.94920127592031095023902582664616550831282960355781111807630371507
A=1.9619805059405370232356276839112625449667905662529703556451002103
B=1.9642010040641823655923560815757650702550786072321587350763219794
A-B=-0.0022204981236453423567283976645025252882880409791883794312217690867

## Analytic truncation tail
Y has smallest eigenvalue lambda=(2.4-sqrt((1.1-1.3)^2+4*.23^2))/2 >.9492. With c=2*pi*lambda and integer shift s in {0,1/2}, each local theta summand is bounded by exp[-c sum_{j=1}^4(n_j+s_j)^2]. Define S=1+2 exp(-c/4)/(1-exp(-c)), T_K=2 exp[-c(K+1/2)^2]/(1-exp[-2c(K+1/2)]). The infinite one-coordinate Gaussian sum is <=S and the part with |n|>K is <=T_K. The union bound gives local tail <=4 T_K S^3. Since every local full theta <=S^4, the two full 16384-term, seven-factor sums have combined absolute truncation error <=2*16384*7*(4 T_K S^3)*(S^4)^6 = 8.0013986934942853483655286493416640637056963862984770540446012016e-22 at K=3. This is a valid analytic truncation bound for the implemented theta sum, not a rounding-error bound.

## Local execution and provenance
Executed /mnt/data/p38/cert.py with Python mpmath 1.3.0, exit=0, wall=6.11 s, peak RSS=99216 KB, stderr empty.
SHA256 source fb0c1e633276f90df76a5e1afee24cff890bea1aeeaa3b3a5db4666871e1895f
stdout 9a39fa044c469f9a9294b1e926d510845dc3d029dd2ca54d4eaccfe461836b35
stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
resources 8605a2337b61687c1215d8e07c273ccdba3c0b919ac6af58db05d2fafd5e646a
Source and logs are local; NOT yet committed byte-identically. Hashes are not claimed to match any GitHub file.

## Strict limitations
65-digit mpmath evaluation is not an outward-rounded certified interval; the total rounding error is not bounded by the above analytic tail. The precise physical genus-two theta-map and normalization must be independently checked against the original source, rather than inferred from numerical agreement. The result is a high-confidence numerical reproduction with rigorous truncation bound, NOT yet a formally certified analytic or physical theorem. The higher-genus distinction is already published, so no novelty or manuscript claim.

GO: computed nonzero separation, rigorous analytic truncation bound for specified Gaussian expression.
REVISE: outward-rounded interval arithmetic, independent source-map verification, second implementation, pinned CI recovery.
NO-GO: new theorem, original Q1 physics manuscript, breakthrough.
