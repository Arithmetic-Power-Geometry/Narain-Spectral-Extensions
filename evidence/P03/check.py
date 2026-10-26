#!/usr/bin/env python3
"""Independent P03 exact arithmetic tests; standard library only."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
G=((F(2),F(1,3)),(F(1,3),F(3)))
det=G[0][0]*G[1][1]-G[0][1]**2
A=((G[1][1]/det,-G[0][1]/det),(-G[0][1]/det,G[0][0]/det))
def energy(v,b):
 m1,m2,n1,n2=v;x=m1+b*n2;y=m2-b*n1
 return A[0][0]*x*x+2*A[0][1]*x*y+A[1][1]*y*y+G[0][0]*n1*n1+2*G[0][1]*n1*n2+G[1][1]*n2*n2
def parts(k,d=2):
 a=[1]+[0]*k
 for n in range(1,k+1):
  for _ in range(d):
   for j in range(n,k+1):a[j]+=a[j-n]
 return a
Q=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
b=F(1,5);T=F(3313,1325)
counts={s:Counter((energy(v,s*b),v[0]*v[2]+v[1]*v[3]) for v in Q if energy(v,s*b)<=3) for s in (1,-1)}
D={key:counts[1][key]-counts[-1][key] for key in counts[1].keys()|counts[-1].keys()}
assert all(v==0 for (e,sp),v in D.items() if e<T)
assert D[(T,-1)]==2 and D[(T,1)]==-2
p=parts(8)
assert p[:4]==[1,2,5,10]
for total in range(9):
 dressed=Counter()
 for (e,sp),v in D.items():
  if not v:continue
  for n in range(total+1):
   m=total-n
   dressed[(e+2*(n+m),sp+n-m)]+=v*p[n]*p[m]
 if total==0:assert dressed[(T,-1)]==2 and dressed[(T,1)]==-2
 if total>0:assert not any(e==T and v for (e,sp),v in dressed.items())
projected_T=sum(v for (e,sp),v in D.items() if e==T and sp==0)
assert projected_T==0
proj_T2=Counter()
for (e,sp),v in D.items():
 if e!=T:continue
 for n,m in [(1,0),(0,1)]:
  if sp+n-m==0:proj_T2['total']+=v*p[n]*p[m]
assert proj_T2['total']==0
fake={(F(1),-1):2,(F(1),1):-2}
assert sum(v for (e,s),v in fake.items() if s==0)==0
assert all(sum(v for (ee,sp),v in D.items() if ee==e)==0 for e in {k[0] for k in D})
res={'status':'PASS_FORMAL_WITH_PROJECTION_COUNTEREXAMPLES','source_states_each':sum(counts[1].values()),'threshold':str(T),'zero_mode_leading':{'spin_-1':2,'spin_+1':-2},'oscillator_d2_levels_0_to_8':p,'checked_total_oscillator_levels':list(range(9)),'zero_spin_projected_at_T':projected_T,'zero_spin_projected_at_T_plus_2':proj_T2['total'],'unrefined_difference_vanishes_through_E3':True,'physical_string_projection_tested':False}
print(json.dumps(res,indent=2))
