#!/usr/bin/env python3
# P07 independent exact checker. Standard library.
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import json
def inverse(a):
 n=len(a);x=[list(a[i])+[Q(i==j) for j in range(n)] for i in range(n)]
 for k in range(n):
  t=next(i for i in range(k,n) if x[i][k]);x[k],x[t]=x[t],x[k]
  z=x[k][k];x[k]=[v/z for v in x[k]]
  for i in range(n):
   if i!=k:
    z=x[i][k];x[i]=[v-z*w for v,w in zip(x[i],x[k])]
 return [r[n:] for r in x]
def quadratic(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),Q(0))
def run(d,h):
 g=[[Q(i==j) for j in range(d)] for i in range(d)]
 b=[[Q(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  g[i][i+1]=g[i+1][i]=Q(1,10+i)
  b[i][i+1]=Q(1,13+i);b[i+1][i]=-b[i][i+1]
 r=max(sum(abs(g[i][j]) for j in range(d) if j!=i) for i in range(d))
 l=1-r;u=1+r;beta=max(sum(abs(b[i][j]) for j in range(d)) for i in range(d))
 assert u<4*l
 nb=int(h/l);mb=next(k for k in range(1,40) if Q(k)>h*u+beta*beta*h/l+4*beta*h)
 nv=[v for v in product(range(-int(nb**0.5)-1,int(nb**0.5)+2),repeat=d) if sum(t*t for t in v)<=nb]
 mv=[v for v in product(range(-int(mb**0.5)-1,int(mb**0.5)+2),repeat=d) if sum(t*t for t in v)<=mb]
 gi=inverse(g);cs={1:Counter(),-1:Counter()}
 for n in nv:
  w=quadratic(n,g)
  if w>h:continue
  bn=[sum(b[i][j]*n[j] for j in range(d)) for i in range(d)]
  for m in mv:
   sp=sum(m[i]*n[i] for i in range(d))
   for s in (1,-1):
    v=[m[i]+s*bn[i] for i in range(d)]
    e=quadratic(v,gi)+w
    if e<=h:cs[s][(e,sp)]+=1
 delta={k:cs[1][k]-cs[-1][k] for k in cs[1].keys()|cs[-1].keys()}
 first=min((e for (e,sp),v in delta.items() if v),default=None)
 assert all(cs[1][e,sp]==cs[-1][e,-sp] for e,sp in cs[1])
 return dict(d=d,H=str(h),n_candidates=len(nv),m_candidates=len(mv),states_each=sum(cs[1].values()),first=str(first) if first is not None else None,first_coeff={str(sp):v for (e,sp),v in delta.items() if e==first and v})
if __name__=='__main__':
 print(json.dumps([run(3,Q(3)),run(4,Q(5,2)),run(6,Q(2))],indent=2))
