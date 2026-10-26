#!/usr/bin/env python3
"""P10 fresh, independent exact-rational reimplementation of P07/P08 windows."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
def inverse(a):
 d=len(a);x=[list(a[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  t=next(i for i in range(k,d) if x[i][k]);x[k],x[t]=x[t],x[k];v=x[k][k];x[k]=[z/v for z in x[k]]
  for i in range(d):
   if i!=k:
    v=x[i][k];x[i]=[z-v*w for z,w in zip(x[i],x[k])]
 return [r[d:] for r in x]
def q(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F(0))
def run(d,h,eps=F(0)):
 g=[[F(i==j) for j in range(d)] for i in range(d)];b=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  g[i][i+1]=g[i+1][i]=F(1,10+i);b[i][i+1]=F(1,13+i);b[i+1][i]=-b[i][i+1]
 g[0][0]+=eps
 r=max(sum(abs(g[i][j]) for j in range(d) if j!=i) for i in range(d));l=min(g[i][i] for i in range(d))-r;u=max(g[i][i] for i in range(d))+r
 beta=max(sum(abs(b[i][j]) for j in range(d)) for i in range(d));nb=int(h/l);mb=next(k for k in range(1,50) if F(k)>h*u+beta*beta*h/l+4*beta*h)
 nr=int(nb**.5)+1;mr=int(mb**.5)+1
 ns=[v for v in product(range(-nr,nr+1),repeat=d) if sum(t*t for t in v)<=nb]
 ms=[v for v in product(range(-mr,mr+1),repeat=d) if sum(t*t for t in v)<=mb]
 gi=inverse(g);c={1:Counter(),-1:Counter()}
 for n in ns:
  w=q(n,g)
  if w>h:continue
  bn=[sum(b[i][j]*n[j] for j in range(d)) for i in range(d)]
  for m in ms:
   sp=sum(x*y for x,y in zip(m,n))
   for sign in (1,-1):
    v=[m[i]+sign*bn[i] for i in range(d)];e=q(v,gi)+w
    if e<=h:c[sign][e,sp]+=1
 delta={k:c[1][k]-c[-1][k] for k in c[1].keys()|c[-1].keys()}
 first=min((e for (e,s),v in delta.items() if v),default=None)
 levels=sorted({e for e,s in c[1]})
 lower=max((e for e in levels if first is not None and e<first),default=None)
 upper=min((e for e in levels if first is not None and e>first),default=None)
 return {'d':d,'H':str(h),'epsilon':str(eps),'n_candidates':len(ns),'m_candidates':len(ms),'states_each':sum(c[1].values()),'first':str(first) if first is not None else None,'first_coeff':{str(s):v for (e,s),v in delta.items() if e==first and v},'gap_below':str(first-lower) if lower is not None else None,'gap_above':str(upper-first) if upper is not None else None,'L':str(l),'U':str(u),'beta':str(beta)}
if __name__=='__main__':
 print(json.dumps([run(3,F(3)),run(4,F(5,2)),run(3,F(3),F(1,10000)),run(4,F(5,2),F(1,10000)),run(6,F(2))],indent=2))
