import sympy as S
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,time,platform,hashlib
start=time.monotonic()
def build(d):
 G=S.eye(d);B=S.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=S.Rational(1,10+i)
  B[i,i+1]=S.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 return G,B
out={'python':platform.python_version(),'sympy':S.__version__}
for d in (3,4):
 G,B=build(d);A=G.inv()*B;f=S.factor(A.charpoly().as_expr());v=B.nullspace()[0] if d==3 else None
 out['T'+str(d)]={'charpoly':str(f),'factor_degrees':[int(S.degree(p)) for p,k in S.factor_list(f)[1]],'kernel':list(map(str,v)) if v is not None else None}
G,B=build(6);GI=G.inv();D=S.ilcm(*[z.q for z in GI]);Q=S.ilcm(*[z.q for z in B]);R=S.ilcm(*[z.q for z in G]);den=int(D*Q*Q*R)
Ai=[[int(GI[i,j]*D) for j in range(6)] for i in range(6)];Bi=[[int(B[i,j]*Q) for j in range(6)] for i in range(6)];Gr=[[int(G[i,j]*R) for j in range(6)] for i in range(6)]
ns=[n for n in product((-1,0,1),repeat=6) if sum(x*x for x in n)<=3]
ms=[m for m in product((-2,-1,0,1,2),repeat=6) if sum(x*x for x in m)<=5]
count=Counter()
for n in ns:
 w=sum(n[i]*Gr[i][j]*n[j] for i in range(6) for j in range(6))
 if 2*w>5*R:continue
 bn=[sum(Bi[i][j]*n[j] for j in range(6)) for i in range(6)]
 for m in ms:
  v=[Q*m[i]+bn[i] for i in range(6)]
  en=sum(v[i]*Ai[i][j]*v[j] for i in range(6) for j in range(6))*R+w*int(D)*Q*Q
  if 2*en<=5*den:count[(en,sum(m[i]*n[i] for i in range(6)))]+=1
first=min((en for (en,s) in count if count[en,s]!=count[en,-s]),default=None)
out['T6']={'n_candidates':len(ns),'m_candidates':len(ms),'states':sum(count.values()),'first':str(F(first,den)),'coeff':{str(s):count[first,s]-count[first,-s] for s in (-1,1)},'denominator':den}
out['elapsed_seconds']=round(time.monotonic()-start,3)
print(json.dumps(out,indent=2))
