#!/usr/bin/env python3
"""P08 exact pointwise spectral tests, with rigorous uniform finite-charge bounds."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
def inverse(a):
 d=len(a);x=[list(a[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  t=next(i for i in range(k,d) if x[i][k]);x[k],x[t]=x[t],x[k];z=x[k][k];x[k]=[v/z for v in x[k]]
  for i in range(d):
   if i!=k:
    z=x[i][k];x[i]=[v-z*w for v,w in zip(x[i],x[k])]
 return [r[d:] for r in x]
def quad(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F(0))
def run(d,h,eps=F(0)):
 g=[[F(i==j) for j in range(d)] for i in range(d)]
 b=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  g[i][i+1]=g[i+1][i]=F(1,10+i)
  b[i][i+1]=F(1,13+i);b[i+1][i]=-b[i][i+1]
 g[0][0]+=eps
 r=max(sum(abs(g[i][j]) for j in range(d) if i!=j) for i in range(d))
 l=min(g[i][i] for i in range(d))-r;u=max(g[i][i] for i in range(d))+r
 beta=max(sum(abs(b[i][j]) for j in range(d)) for i in range(d))
 assert l>0 and u<4*l
 nb=int(h/l);mb=next(k for k in range(1,40) if F(k)>h*u+beta*beta*h/l+4*beta*h)
 nr=int(nb**0.5)+1;mr=int(mb**0.5)+1
 nv=[v for v in product(range(-nr,nr+1),repeat=d) if sum(t*t for t in v)<=nb]
 mv=[v for v in product(range(-mr,mr+1),repeat=d) if sum(t*t for t in v)<=mb]
 gi=inverse(g);c={1:Counter(),-1:Counter()}
 for n in nv:
  w=quad(n,g)
  if w>h:continue
  bn=[sum(b[i][j]*n[j] for j in range(d)) for i in range(d)]
  for m in mv:
   sp=sum(m[i]*n[i] for i in range(d))
   for sign in (1,-1):
    x=[m[i]+sign*bn[i] for i in range(d)]
    e=quad(x,gi)+w
    if e<=h:c[sign][e,sp]+=1
 delta={k:c[1][k]-c[-1][k] for k in c[1].keys()|c[-1].keys()}
 t=min((e for (e,s),v in delta.items() if v),default=None)
 levels=sorted({e for (e,s) in c[1]})
 below=max((e for e in levels if t is not None and e<t),default=None)
 above=min((e for e in levels if t is not None and e>t),default=None)
 assert all(c[1][e,s]==c[-1][e,-s] for e,s in c[1])
 return dict(d=d,H=str(h),epsilon=str(eps),L=str(l),U=str(u),beta=str(beta),nb=nb,mb=mb,n_count=len(nv),m_count=len(mv),states_each=sum(c[1].values()),first=str(t) if t is not None else None,first_coeff={str(s):v for (e,s),v in delta.items() if e==t and v},gap_below=str(t-below) if below is not None else None,gap_above=str(above-t) if above is not None else None)
if __name__=="__main__":
 print(json.dumps([run(3,F(3)),run(4,F(5,2)),run(3,F(3),F(1,10000)),run(4,F(5,2),F(1,10000)),run(6,F(2))],indent=2))
