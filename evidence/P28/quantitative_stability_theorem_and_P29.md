# P28: dimension-uniform simultaneous-entry perturbation certificate

**Mathematical GO (proof candidate independently algebra-checked); novelty NO-GO; pinned CI unresolved.**

For every integer d>=2, take the P27 rational chain G0,B0 and J=[[0,I],[I,0]]. For arbitrary real symmetric ΔG and skew-symmetric ΔB, with **every independent entry** bounded by r(d)=1/[10000 d(d+8)] in absolute value, put G=G0+ΔG, B=B0+ΔB. Then G remains SPD and the integral Narain charge lattice with Q(G,B) admits no nontrivial simultaneous J/Q-orthogonal direct summand, even after arbitrary full O(d,d;Z) duality.

**Proof with explicit constants.** Let t=d r=1/[10000(d+8)]<=1/100000. By row sums ||ΔG||2,||ΔB||2<=t; G0 eigenvalues in (4/5,6/5), ||B0||2<1/6. Thus G eigenvalues >4/5-t, and ||B||2<1/6+t. For A=G^-1 and A0=G0^-1, ||A||<1/(4/5-t)<1.251, ||A0||<1.25, ||A-A0||<=||A||||ΔG||||A0||<1.564t<1.57t. Hence ||AB-A0B0||<1.57t/6+1.251t<1.513t<1.52t. The lower-right block satisfies
||G-BA B-(G0-B0 A0 B0)|| <=t+2(1.251)(1/6+t)t+(1/6)^2(1.57)t <1.47t.
Summing the norms of the four blocks bounds ||Q(G,B)-Q(G0,B0)||2< (1.57+1.52+1.52+1.47)t < 10t.

For any v=(m,n), E0(v) >= (4/5)(||m+B0n||²+||n||²) >=(2/5)||v||², since ||B0||<1/6 and ||m||²+||n||²<=2(||m+B0n||²+||n||²). Thus |E(v)-E0(v)|<10t||v||² <=25t E0(v). P27 proved global λ0=min_{v!=0} E0(v)>=1. Therefore the perturbed global minimum λ>=1-25t, hence 2λ>=2-50t.

P27 witness set W={p_i=(e_i,0),w_i=(0,e_i),c_i=(0,e_i-e_(i+1))} has 3d-1 vectors and spans the full lattice with connected nonzero J-pairing graph. For p_i,w_i the P27 bounds yield E0<2-1/(d+8). For c_i, P27 gives E0(c_i)<2-2/(i+10)+5/(i+12)^2 <2-1/(i+10)<=2-1/(d+8). (Check 5(i+10)<(i+12)^2 for all i>=0.) All W satisfy ||v||²<=2. Hence E(v)<2-1/(d+8)+20t. Since 70t=70/[10000(d+8)]<1/(d+8), E(v)<2-50t<=2λ. Thus every witness lies in the short-vector set of the perturbed metric; connectedness and spanning depend only on J and the fixed integer charges, so the P25 graph obstruction proves indecomposability. All d>=2, all simultaneous independent entry perturbations, including dense perturbations. Full O(d,d;Z) covariance follows by conjugating any hypothetical integral projector. QED.

**Important limitation:** This is an explicit *sufficient* open neighborhood, not a sharp radius or a general rational Narain decomposition algorithm. Uniform in dimension means a stated positive r(d), not a constant radius independent of d. The proof is a direct quantitative continuity extension of the P25/P27 short-vector lemma; independent publication novelty remains unestablished.

**Independent exact adversarial tests:** dense symmetric all-ones ΔG and dense upper-triangular skew ΔB with every independent entry at +r, dimensions d=2,3,4,6,10,16. Exact SymPy checker exit=0, empty stderr, WALL=2.97 s, RSS=128396 KB. SHA256: check.py 50387ba08bc29b9d69cfb91c96f9e6375d97f868c4282bed5064281face59843; stdout 16dd5c91307cafb906cb181d66d7280a9fc674358d0a97222dd4befe2a8deba6; stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Tests do not substitute for the universal operator-norm proof. Hidden decomposable controls were tested in P26; no fresh independent hidden-product test was run here.

**CI:** P27 matrix evidence/P27/ci_run/matrix.json absent at initial read; previous P25/P26 matrices also absent. GitHub Actions workflow creation alone is not execution. No pinned run can be declared passed without actual logs and matrix.

**Novelty:** Eichler–Kneser connected-vector lattice decomposition is close methodological prior art. Nikulin (1980), DOI 10.1070/IM1980v014n01ABEH001060, is verified and already in bibliography; no new fully verified unique references were identified for append. Mathematical GO; reproducibility REVISE; novelty NO-GO; manuscript NO-GO.

**P29:** (1) Independently verify every operator-norm constant, especially perturbation radius and strict inequalities, with a distinct proof/checker; (2) recover P27/P28 pinned CI runs and actual outputs, inspect GitHub Actions job logs and source hashes; (3) adversarially test all-negative, random rational, dense perturbations, near-singular G, and duality-hidden products; (4) seek a dimension-independent radius or a significantly stronger arithmetic invariant rather than routine continuity; (5) hostile Eichler–Kneser, Nikulin, Narain and moduli-space novelty audit; (6) preserve all failures append-only, commit and readback, strict GO/REVISE/NO-GO. Do not draft a manuscript absent independently verified originality.
