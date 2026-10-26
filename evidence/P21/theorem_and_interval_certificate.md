# P21 — Uniform all-entry spin-resolved spectral separation theorem
Date: 2026-10-26. Exact Narain zero-mode energy E_{G,B}(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n, spin s=m^T n. Applies separately to d=3,4,6 chain backgrounds from P07/P15. It does NOT establish full O(d,d,Z) nonduality or physical string inequivalence.

## Theorem (certified open neighborhood, stronger radius)
Let G0_ii=1, G0_i,i+1=G0_i+1,i=1/(10+i), B0_i,i+1=1/(13+i), B0_i+1,i=-1/(13+i) (zero-based i), other entries zero. Let symmetric Delta G and skew Delta B have each independent entry in [-1/10^7,+1/10^7]. Then G=G0+Delta G is positive definite. For each d in {3,4,6}, the spin-refined zero-mode spectra of (G,+B) and (G,-B) differ below H_d=3 for d=3, H_d=5/2 for d=4,6. More specifically the charges (m,n)=(e_d,e_d) and (-e_d,-e_d), with s=+1, have common energy E_w(G,B)<H_d and NO charge with spin -1 has exactly E_w(G,B). Their coefficient in N_{G,B}(E_w,+1)-N_{G,B}(E_w,-1) is therefore at least +2. Parity (m,n)->(m,-n) identifies the latter difference with the +B minus -B spin-refined difference. No constancy of E_w as a number is claimed.

## Uniform completeness and Lipschitz proof
Gershgorin at center: L0=89/110 <= lambda_min(G0), lambda_max(G0)<=U0=131/110; ||B0||2<=beta0=27/182. For any all-entry radius r, ||Delta G||2,||Delta B||2 <= d*r. Put L=L0-dr, U=U0+dr, beta=beta0+dr. The exact radius verifier establishes L>1/2, beta<1, U<4L at r=1/10^7 for d=3,4,6.

For E<=H: ||n||² <= H/L, and ||m|| <= sqrt(HU)+beta sqrt(H/L), whence ||m||² < HU+beta² H/L+4 beta H. Exact rational floor bounds give ||n||²<=3 for every d and ||m||²<=5 (d=3) or <=4 (d=4,6). Thus ALL possible negative-spin competitors below H are in the finite integer candidate sets enumerated by check.py.

For every candidate ||n||<2, ||m||<3, ||B0||<=1, x=m+B0n has ||x||<5. Resolvent identity bounds ||G^-1-G0^-1||<=dr/(L L0)<=4dr; ||G^-1||<=2. The kinetic difference is bounded by 25*4dr + 2*5*(2dr)*2 + (2dr)^2*2 <= (100+40+8)dr for dr<1. The winding term is <=4dr. Thus |E_{G,B}(m,n)-E_{G0,B0}(m,n)|<160dr. This is an explicit rational interval enclosure valid for EVERY candidate and EVERY allowed independent perturbation.

Exact enumeration gives central witness E0 and minimum positive distance gamma to ALL opposite-spin candidate energies (including energies above H, and with the harmless skip n^T G0 n>H+1/100). The skip cannot conceal a competitor entering E<=H: n^T G n >= n^T G0 n - ||Delta G|| ||n||² > H+1/100-3dr >H. The witness energy shifts by <160dr, every candidate opposite-spin energy by <160dr, and 320dr<gamma, while 160dr<H-E0. Consequently witness and every opposite-spin charge remain separated and witness remains below H. The sign-paired witness charges always have identical energies by quadratic evenness. This proves the theorem on the CLOSED box and hence its interior open neighborhood.

| d | H | central E0 | gamma nearest opposite spin | 320*d*r at r=1e-7 | ncap | mcap |
| 3 | 3 | 1164367/582071 | 15336/98369999 | 3/31250 | 3 | 5 |
| 4 | 5/2 | 9437981/4718325 | 5324/20446075 | 2/15625 | 3 | 4 |
| 6 | 5/2 | 3573739389131/1786726163119 | 115293091512/301956721567111 | 3/15625 | 3 | 4 |

All comparisons above were verified with Fraction, not floating point. See check.py, stdout.txt, radius_upgrade.py and radius_stdout.json. Radius 1e-7 is sufficient, not asserted maximal.

## Forced versus accidental identities
For d>=2, two fixed charges (m,n),(m',n') have IDENTICALLY equal energy as rational functions of every independent positive-definite symmetric G and skew B if and only if (m',n')=(m,n) or (-m,-n). Proof: at B=0, substitute G=tH with arbitrary SPD H and t>0. Comparing coefficients of t and t^-1 gives nn^T=n'n'^T and mm^T=m'm'^T, hence m'=epsilon*m and n'=eta*n with independent signs for nonzero vectors. If both are nonzero and epsilon*eta=-1, the linear-in-B coefficient would force m^T H^-1 B n identically zero for every SPD H and skew B. For independent m,n choose H=I and appropriate B; for proportional nonzero m,n choose H with H^-1 m not parallel n, then B. Contradiction. When either vector is zero the remaining independent sign is precisely overall sign. Thus the only forced degeneracy is charge negation. This is a basic algebraic lemma; no novelty is asserted.

Independent classify.py enumerated all central E<=H states and groups them by (m,n)~(-m,-n): 125 states/63 energies for T3, 129/65 for T4, 289/145 for T6. Zero energies contain >1 negation orbit in ALL three cases: no accidental central coincidences inside these windows. This does NOT claim no accidental coincidences at higher energies or for all parameter values.

## Adversarial controls and limitations
Exact perturbations of all entries in checkerboard signs, G01 minus r, and B01 plus r were evaluated, and the chosen central nearest opposite-spin pair remains separated. These pointwise tests are secondary; the all-entry interval proof is primary. B=0 lies far outside the tiny certified box and restores spin reversal via (m,n)->(-m,n), demonstrating that stability is LOCAL, not global. The adversarial script's 'separated' flag compares only two selected charges; at B=0 it does not measure full spin-resolved multiplicities. No perturbation beyond r=1e-7 is certified.

The proof does NOT show that the numerical first-discrepancy threshold is constant, that the first orbit remains the first, that spectra differ under unoriented parity equivalence, or that the physical CFTs are inequivalent. The theorem is example-specific and its novelty against the inverse-spectral and lattice literature is not yet established.

## Strict P21 gate
GO for the stated exact uniform local spectral separation theorem and its finite interval certificate. REVISE for a novel general theorem and Q1 manuscript gate. P22 should seek effective finite inverse reconstruction with explicit arithmetic-height bounds and adversarial isospectral controls, then P23 novelty kill-test. Do not draft a manuscript yet.
