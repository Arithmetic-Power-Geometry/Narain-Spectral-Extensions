from fractions import Fraction as F
from itertools import product
from collections import Counter
import json,time,platform,hashlib
D=6;H=F(5,2)
G=[[F(i==j) for j in range(D)] for i in range(D)];B=[[F(0) for j in range(D)] for i in range(D)]
for i in range(D-1):
 G[i][i+1]=G[i+1][i]=F(1,10+i);B[i][i+1]=F(1,13+i);B[i+1][i]=-B[i][i+1]
def inv(A):
 n=len(A);M=[list(A[i])+[F(i==j) for j in range(n)] for i in range(n)]
 for k in range(n):
  j=next(j for j in range(k,n) if M[j][k]);M[k],M[j]=M[j],M[k];t=M[k][k];M[k]=[v/t for v in M[k]]
  for j in range(n):
   if j!=k:
    t=M[j][k];M[j]=[v-t*w for v,w in zip(M[j],M[k])]
 return [r[n:] for r in M]
I=inv(G)
def quad(v,M):return sum((v[i]*M[i][j]*v[j] for i in range(D) for j in range(D)),F(0))
r=max(sum(abs(G[i][j]) for j in range(D) if j!=i) for i in range(D));L=1-r;U=1+r;beta=max(sum(abs(B[i][j]) for j in range(D)) for i in range(D))
nb=int(H/L);mb=next(k for k in range(1,30) if F(k)>H*U+beta*beta*H/L+4*beta*H)
ns=[v for v in product(range(-2,3),repeat=D) if sum(x*x for x in v)<=nb]
ms=[v for v in product(range(-3,4),repeat=D) if sum(x*x for x in v)<=mb]
t0=time.monotonic();a=Counter();b=Counter()
for n in ns:
 w=quad(n,G)
 if w>H:continue
 bn=[sum(B[i][j]*n[j] for j in range(D)) for i in range(D)]
 for m in ms:
  spin=sum(m[i]*n[i] for i in range(D))
  for sign,c in [(1,a),(-1,b)]:
   x=[m[i]+sign*bn[i] for i in range(D)];e=quad(x,I)+w
   if e<=H:c[(e,spin)]+=1
assert sum(a.values())==sum(b.values())
assert all(a[e,s]==b[e,-s] for e,s in a)
delta={k:a[k]-b[k] for k in a.keys()|b.keys()};first=min((e for (e,s),v in delta.items() if v),default=None)
result={'dimension':D,'H':str(H),'L':str(L),'U':str(U),'beta':str(beta),'n_norm_sq_max':nb,'m_norm_sq_max':mb,'n_candidates':len(ns),'m_candidates':len(ms),'states_each':sum(a.values()),'first':str(first) if first is not None else None,'first_coeff':{str(s):v for (e,s),v in delta.items() if e==first and v},'elapsed_seconds':round(time.monotonic()-t0,3),'python':platform.python_version(),'gate':'FINITE_WINDOW_ONLY'}
print(json.dumps(result,indent=2))
