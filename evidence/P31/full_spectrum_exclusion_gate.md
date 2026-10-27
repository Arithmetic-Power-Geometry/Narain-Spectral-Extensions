# P31 discovery gate: exact full-spectrum exclusion

For the Narain T2 family G=[[1,1/10],[1/10,1]], B=[[0,b],[-b,0]], define Q by the standard generalized metric. For b=1/13, multiplying every entry of Q by 167310 gives an integer. Therefore every integer charge has energy with reduced denominator dividing 167310.

For b=1/17, the winding charge (m,n)=(0,0,1,0) has spin zero and energy 28711/28611. This reduced denominator does not divide 167310 (their gcd is 99). Thus the b=1/17 complete spectrum contains an energy absent from the b=1/13 complete spectrum, independently of any charge cutoff.

A first checker run failed because it incorrectly used 16731, omitting the 1/10 term from G. The corrected local exact Fraction checker exited 0, empty stderr, wall 1.08 seconds, RSS 95628 KB. This is a complete-energy proof, not a finite-window inference.

The b=+1/13 and b=-1/13 backgrounds are still related by the exact coordinate-swap T-duality, so they do not provide a nondual isospectral pair.

Prior art: Dymarsky and Shapere (JHEP 03 (2021) 160) exhibit physically distinct isospectral Narain code CFTs; Henriksson, Kakkar and McPeak (JHEP 04 (2023) 011) study higher-genus distinctions. Both references are already in the verified bibliography. No new bibliographic entry needed.

GO: full-spectrum exclusion certificate. REVISE: pinned P27-P29 CI and byte-identical remote checker execution. NO-GO: novel isospectral counterexample, inverse theorem, manuscript or breakthrough. Do not recommend a publication phase.
