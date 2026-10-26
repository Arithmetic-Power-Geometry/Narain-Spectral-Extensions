#!/usr/bin/env python3
"""P14 exact-rational central and independent B-direction tests. Stdlib only."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json,platform
def inv(a):
 d=len(a);x=[list(a[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  z=x[k][k];x[k]=[t/z for t in x[k]]
  for i in range(d):
   if i!=k:
    z=x[i][k];x[i]=[t-z*w for t,w in zip(x[i],x[k])]
 return [r[d:] for r in x]
def dot(x,A,y):return sum((x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(y))),F(0))
def build(d):
 g=[[F(i==j) for j in range(d)] for i in range(d)];b=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  g[i][i+1]=g[i+1][i]=F(1,10+i);b[i][i+1]=F(1,13+i);b[i+1][i]=-b[i][i+1]
 return g,b
def calc(g,b,h):
 d=len(g);r=max(sum(abs(g[i][j]) for j in range(d) if i!=j) for i in range(d));L=min(g[i][i] for i in range(d))-r;U=max(g[i][i] for i in range(d))+r;beta=max(sum(abs(b[i][j]) for j in range(d)) for i in range(d));assert L>0 and U<4*L
 nb=int(h/L);mb=next(k for k in range(1,100) if F(k)>h*U+beta*beta*h/L+4*beta*h)
 nr=int(nb**.5)+1;mr=int(mb**.5)+1
 ns=[v for v in product(range(-nr,nr+1),repeat=d) if sum(x*x for x in v)<=nb];ms=[v for v in product(range(-mr,mr+1),repeat=d) if sum(x*x for x in v)<=mb]
 gi=inv(g);c={1:defaultdict(list),-1:defaultdict(list)}
 for n in ns:
  w=dot(n,g,n)
  if w>h:continue
  bn=[sum(b[i][j]*n[j] for j in range(d)) for i in range(d)]
  for m in ms:
   s=sum(x*y for x,y in zip(m,n))
   for sign in (1,-1):
    v=[m[i]+sign*bn[i] for i in range(d)];e=dot(v,gi,v)+w
    if e<=h:c[sign][(e,s)].append((m,n))
 delta={k:len(c[1][k])-len(c[-1][k]) for k in c[1].keys()|c[-1].keys()}
 t=min((e for (e,s),v in delta.items() if v),default=None)
 return c,t,{'n_count':len(ns),'m_count':len(ms),'nb':nb,'mb':mb,'L':str(L),'U':str(U),'beta':str(beta),'states_each':sum(map(len,c[1].values()))}
def run(d):
 g,b=build(d);h=F(3) if d==3 else F(5,2);c,t,meta=calc(g,b,h)
 levels=sorted({e for e,s in c[1] if e<t});groups=[]
 for e in levels:
  asym={s:len(c[1][(e,s)])-len(c[1][(e,-s)]) for s in set(k for ee,k in c[1] if ee==e)}
  if any(asym.values()):groups.append({'E':str(e),'asym':{str(k):v for k,v in asym.items() if v}})
 for i,j in [(0,1),(0,2)]:
  if j>=d:continue
  bp=[row[:] for row in b];bp[i][j]+=F(1,10000);bp[j][i]-=F(1,10000)
  cp,tp,mp=calc(g,bp,h)
  if tp is not None and tp<t:
   witness={'direction':f'B[{i},{j}] += 1/10000','first':str(tp),'central_first':str(t),'spin_coeff':{str(s):len(cp[1][(tp,s)])-len(cp[-1][(tp,s)]) for ee,s in cp[1].keys()|cp[-1].keys() if ee==tp and len(cp[1][(tp,s)])!=len(cp[-1][(tp,s)])}}
   return {'dimension':d,'central':meta,'central_first':str(t),'lower_central_asymmetry':groups,'counterexample':witness}
 return {'dimension':d,'central':meta,'central_first':str(t),'lower_central_asymmetry':groups,'counterexample':None}
if __name__=='__main__':
 print(json.dumps({'cases':[run(3),run(4)],'python':platform.python_version()},indent=2))
