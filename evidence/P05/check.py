#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
G=((F(2),F(1,3)),(F(1,3),F(3)));det=G[0][0]*G[1][1]-G[0][1]**2
A=((G[1][1]/det,-G[0][1]/det),(-G[0][1]/det,G[0][0]/det))
def e(v,b):
 m1,m2,n1,n2=v;x=m1+b*n2;y=m2-b*n1
 return A[0][0]*x*x+2*A[0][1]*x*y+A[1][1]*y*y+G[0][0]*n1*n1+2*G[0][1]*n1*n2+G[1][1]*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
b=F(1,5);T=F(3313,1325)
base={sign:Counter((e(v,sign*b),spin(v)) for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)) if e(v,sign*b)<=3) for sign in (1,-1)}
def spectator(k):
 out=Counter()
 for vec in product(range(-1,2),repeat=2*k):
  m=vec[:k];n=vec[k:];ee=sum((x*x+y*y for x,y in zip(m,n)),0)
  if ee<=3:out[(F(ee),sum(x*y for x,y in zip(m,n)))]+=1
 return out
def conv(a,s,cap=F(3)):
 out=Counter()
 for (e1,t1),v1 in a.items():
  for (e2,t2),v2 in s.items():
   if e1+e2<=cap:out[(e1+e2,t1+t2)]+=v1*v2
 return out
res={}
for d in [3,4,6]:
 k=d-2;s=spectator(k);p=conv(base[1],s);q=conv(base[-1],s)
 delta={key:p[key]-q[key] for key in p.keys()|q.keys()}
 assert all(v==0 for (en,sp),v in delta.items() if en<T)
 assert delta[(T,-1)]==2 and delta[(T,1)]==-2
 assert sum(v for (en,sp),v in delta.items() if en==T)==0
 res[f'T{d}']={'spectator_states_E_le_3':sum(s.values()),'combined_states_E_le_3_each':sum(p.values()),'leading_spin_minus':delta[T,-1],'leading_spin_plus':delta[T,1]}
delta={key:base[1][key]-base[-1][key] for key in base[1].keys()|base[-1].keys()}
assert all(v*0==0 for v in delta.values())
assert conv(base[1],base[-1])==conv(base[-1],base[1])
result={'status':'PASS_PRODUCT_THEOREM_WITH_LIMITATIONS','threshold':str(T),'examples':res,'adversarial':{'swap_two_factors':'exact cancellation; X tensor Y vs Y tensor X','signed_zero_vacuum_factor':'formal counterexample only, not a physical spectator'},'scope':'product metrics/B fields only; no nonblock coupling or duality inequivalence certified'}
print(json.dumps(result,indent=2))
