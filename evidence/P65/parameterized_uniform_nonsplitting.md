# P65 — Parameterized uniform non-splitting theorem (2026-10-28)

Let d>=2. Let G be symmetric tridiagonal with G_ii=1, G_(i,i+1)=a_i, |a_i|<=1/20, and let B be antisymmetric with B_(i,i+1)=b_i in [2/25,3/25]. For Q(m,n)=(m+Bn)^T G^{-1}(m+Bn)+n^T G n and J((m,n),(m',n'))=m.n'+n.m', there is no nontrivial simultaneous integral J/Q-orthogonal direct-sum decomposition of Z^(2d).

Proof: A=G-I has norm <=1/10. Thus G is positive definite. For any nonzero (m,n), Q>=1: if ||n||²>=2 then n^T G n>=9/5; if ||n||²=1 then n^T G n=1; if n=0 and ||m||²>=2 then m^T G^-1 m>=20/11; if n=0 and m=+-e_i then (G^-1)_ii>=1 by Schur complement. Hence lambda=min_{v!=0}Q(v)>=1.

All p_i=(e_i,0) have Q<=10/9<2; all w_i=(0,e_i) have Q<=1+2*(3/25)^2/(9/10)<2. For each i<d-1, z_i=(-e_i,e_(i+1)) has v=-e_i+B e_(i+1)=-(1-b_i)e_i-b_(i+1)e_(i+2), with absent boundary term omitted. Thus ||v||²<=(23/25)^2+(3/25)^2=538/625. Since v is supported on one parity and A flips parity, v^T G^-1 v=sum_{k>=0}v^T A^(2k)v <=||v||²/(1-1/100) <=2152/2475<1. Consequently Q(z_i)<2<=2lambda.

In any simultaneous integral Q/J-orthogonal decomposition, each nonzero vector of energy <2lambda belongs wholly to one summand. The J pairings J(p_i,w_i)=1, J(z_i,w_i)=-1 and J(z_i,p_(i+1))=1 connect all basis vectors. They span, forcing the other summand to be zero.

Counterexample outside parameter box: G=I, B=0 splits into d hyperbolic planes. The box is sufficient, not necessary or optimal. Exact rational independent verification: bound 2152/2475 and 20 deterministic parameter cases in dimensions 2..6, all connector energies <2. The method resembles Kneser's orthogonal decomposition argument; Hemkemeier and Vallentin, On the Decomposition of Lattices, ECCC TR98-052 (1998), https://eccc.weizmann.ac.il/report/1998/052/. Narain lattice framework: Hosono et al., c=2 Rational Toroidal Conformal Field Theories, https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11159-Shing-Tung_Yau_335.pdf. Recent related code lattice work: https://doi.org/10.1063/5.0293228. Specific novelty not established; no new physical genus-two observable or Q1 claim.

Gate: mathematical GO for sufficient theorem; optimality NO-GO; originality REVISE; Q1 physics NO-GO. P61/P63 STOP decisions remain unchanged. No manuscript or Prompt 4.
