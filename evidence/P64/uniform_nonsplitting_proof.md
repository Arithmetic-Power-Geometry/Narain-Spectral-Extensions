# P64 — exact dimension-uniform non-splitting proof (2026-10-28)

Independent follow-up to P63. P63 STOP on theta-performance remains unchanged. No manuscript produced.

For d>=2 let Gii=1, G_{i,i+1}=1/(10+i), B_{i,i+1}=1/(13+i), B antisymmetric, zero-based i. E(m,n)=(m+Bn)^T G^{-1}(m+Bn)+n^T G n; J=[[0,I],[I,0]].

**Minimum lower bound.** A=G-I has operator norm <=1/5, so 4/5 I <=G<=6/5 I. If ||n||²>=2, E>=8/5; if n=0 and ||m||²>=2, E>=5/3; if n=0,m=+-e_i, E=(G^-1)ii>=1; if n=+-e_i, E>=1. Thus global minimum lambda>=1. The pure momentum basis energies <=5/4<2 and pure winding basis energies <=1+(5/4)*2/13²<2, hence all lie in S={v:0<E(v)<2lambda}.

**Mixed connectors.** For 0<=i<=d-2 take z_i=(m,n)=(-e_i,e_{i+1}). Then v=m+Bn=-(1-b_i)e_i-b_{i+1}e_{i+2}, with absent boundary term omitted. Here b_i=1/(13+i). A changes coordinate parity and ||A||<=1/5, so v^T G^-1 v=||v||²+sum_{k>=1}||A^k v||²<=||v||²+||Av||²/(1-1/25). Every edge incident on support {i,i+2} has weight <=1/(i+9); restricted bipartite adjacency has row and column sums <=2/(i+9), so ||Av||<=2||v||/(i+9). Therefore v^T G^-1 v <= F(i)=[(1-1/(i+13))²+1/(i+14)²][1+25/(6(i+9)²)]. Exact simplification:

1-F(i)=(12i^5+671i^4+14708i^3+157069i²+809974i+1589441)/(6(i+9)²(i+13)²(i+14)²)>0 for every i>=0.

Hence E(z_i)<2<=2lambda uniformly in d.

**Indecomposability.** Set p_i=(e_i,0), w_i=(0,e_i). All p_i,w_i,z_i belong to S. Their J pairings satisfy J(p_i,w_i)=1, J(z_i,w_i)=-1, J(z_i,p_{i+1})=1. These vertices span and their nonzero-pairing graph is connected. If Z^{2d}=L1 direct-sum L2 were simultaneously Q- and J-orthogonal, each vector of S must lie in a single summand (otherwise its Q-energy >=2lambda); J-nonorthogonality forces adjacent vectors into the same summand. The connected spanning set forces the other summand zero. Thus no nontrivial simultaneous integral J/Q-orthogonal decomposition exists for any d>=2; in particular no balanced-signature integral toroidal factorization.

**Verification and limitations.** Exact SymPy polynomial check found numerator coefficients [12,671,14708,157069,809974,1589441], all positive; independent exact rational finite d=2..12 neighboring mixed energies <2. Kneser's orthogonality-graph method and Hemkemeier–Vallentin (1998), https://eccc.weizmann.ac.il/report/1998/052/, precede the general method. Narain O(d,d;Z) framework is standard; see Hosono–Lian–Oguiso–Yau https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11159-Shing-Tung_Yau_335.pdf . Specific-family novelty is NOT established; this does not prove new general theory, a new CFT pair, or higher-genus physical discrimination. P61/P63 failures remain archived. Strict gate: mathematical GO for the explicit family theorem, novelty REVISE, Q1 readiness NO-GO. Do not begin manuscript or Prompt 4.
