from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import sympy as s, time, json, platform
start=time.monotonic(); d=6; H=F(5,2)
G=s.eye(d); B=s.zeros(d)
for i in range(d-1):
 G[i,i+1]=G[i+1,i]=s.Rational(1,10+i)
 B[i,i+1]=s.Rational(1,13+i); B[i+1,i]=-B[i,i+1]
GI=G.inv(); D=s.ilcm(*[x.q for x in GI]); A=[[int(GI[i,j]*D) for j in range(d)] for i in range(d)]
L=F(89,110); U=F(131,110); beta=F(27,182)
nb=int(H/L); mb=next(k for k in range(30) if F(k)>H*U+beta**2*H/L+4*beta*H)
ns=[v for v in product(range(-1,2),repeat=d) if sum(z*z for z in v)<=nb]
ms=[v for v in product(range(-2,3),repeat=d) if sum(z*z for z in v)<=mb]
Q=s.ilcm(*[x.q for x in B]); BI=[[int(B[i,j]*Q) for j in range(d)] for i in range(d)]
R=s.ilcm(*[x.q for x in G]); GG=[[int(G[i,j]*R) for j in range(d)] for i in range(d)]
energy_denom=int(D*Q*Q*R)
counts=defaultdict(lambda:[0,0]); states=0
for n in ns:
 wn=sum(n[i]*GG[i][j]*n[j] for i in range(d) for j in range(d))
 if F(wn,R)>H: continue
 bn=[sum(BI[i][j]*n[j] for j in range(d)) for i in range(d)]
 for m in ms:
  v=[m[i]*Q+bn[i] for i in range(d)]
  x=sum(v[i]*A[i][j]*v[j] for i in range(d) for j in range(d))*R + wn*int(D)*Q*Q
  if x*2<=5*energy_denom:
   spin=sum(m[i]*n[i] for i in range(d))
   counts[(x,spin)][0]+=1;states+=1
levels=sorted(set(x for x,spin in counts))
first=None; coeff={}
for x in levels:
 spins={z for energy,spin in counts if energy==x for z in (spin,-spin)}
 diffs={spin:counts[(x,spin)][0]-counts[(x,-spin)][0] for spin in spins}
 if any(diffs.values()):
  first=F(x,energy_denom);coeff={str(k):v for k,v in diffs.items() if v};break
out={'method':'integer_scaled_one_sign_spin_reflection','dimension':d,'H':str(H),'denominator':energy_denom,'candidate_n':len(ns),'candidate_m':len(ms),'states_plus':states,'first':str(first),'first_coeff':coeff,'elapsed_seconds':round(time.monotonic()-start,3),'python':platform.python_version(),'sympy':s.__version__,'norm_sq_n':nb,'norm_sq_m':mb}
print(json.dumps(out,indent=2))
