#!/usr/bin/env python3
"""P02 independent exact rational threshold certificate. Python standard library only."""
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
def threshold(b):return (133-6*b+18*b*b)/53
def poly(v,sgn):
 z=energy(v,F(0))-threshold(F(0));p=energy(v,F(sgn))-threshold(F(1));q=energy(v,-F(sgn))-threshold(-F(1))
 return (z,(p-q)/2,(p+q)/2-z)
def val(p,b):return p[0]+p[1]*b+p[2]*b*b
def minimum(p,L,R):
 values=[(val(p,L),L),(val(p,R),R)]
 if p[2]>0:
  v=-p[1]/(2*p[2])
  if L<v<R:values.append((val(p,v),v))
 return min(values)
Q=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
nz=[v for v in Q if v[0]*v[2]+v[1]*v[3]]
assert len(Q)==729 and len(nz)==576
classification={}
for sign in (1,-1):
 counts=Counter();near=[];witness=[]
 for v in nz:
  p=poly(v,sign);lo,_=minimum(p,F(0),F(1,2))
  assert lo>=0,(sign,v,lo)
  if p==(0,0,0):kind="identical";witness.append(v)
  elif val(p,F(0))==0:kind="at_zero"
  elif val(p,F(1,2))==0:kind="at_half"
  elif lo>0:kind="strict"
  else:raise AssertionError(("unclassified",sign,v,p))
  counts[kind]+=1
  if kind!="identical":near.append(minimum(p,F(1,10),F(2,5))[0])
 assert counts==Counter({"strict":570,"at_zero":2,"at_half":2,"identical":2})
 assert min(near)==F(6,265)
 classification[str(sign)]={"counts":dict(counts),"witnesses":[list(x) for x in witness],"gap":str(min(near))}
b=F(1,5);t=threshold(b)
assert t==F(3313,1325)
levels={}
for sign in (1,-1):
 counts=Counter((energy(v,sign*b),v[0]*v[2]+v[1]*v[3]) for v in Q if energy(v,sign*b)<=3)
 assert sum(counts.values())==39
 levels[str(sign)]={"states":39,"spin_minus":counts[t,-1],"spin_plus":counts[t,1]}
assert (levels["1"]["spin_minus"],levels["1"]["spin_plus"],levels["-1"]["spin_minus"],levels["-1"]["spin_plus"])==(2,0,0,2)
for bb in [F(1,20),F(1,10),F(1,5),F(2,5),F(9,20)]:
 for sign in (1,-1):assert all(energy(v,sign*bb)>=threshold(bb) for v in nz)
for bb in [F(0),F(1,2),F(1)]:
 box=product(range(-8,9),range(-8,9),range(-2,3),range(-2,3))
 a=Counter((energy(v,bb),v[0]*v[2]+v[1]*v[3]) for v in box if energy(v,bb)<=3)
 box=product(range(-8,9),range(-8,9),range(-2,3),range(-2,3))
 c=Counter((energy(v,-bb),v[0]*v[2]+v[1]*v[3]) for v in box if energy(v,-bb)<=3)
 assert a==c,bb
assert any(energy(v,b)<F(3373,1325) for v in nz)
result={"status":"PASS","charge_box":len(Q),"nonzero_spin_per_sign":len(nz),"classification":classification,"first_threshold":str(t),"states":levels,"endpoint_tests":["0","1/2","1"],"interior_tests":["1/20","1/10","1/5","2/5","9/20"],"adversarial":"3373/1325 rejected as first threshold","limitations":["Paper I interval radius 1/90 not independently verified","not a full physical partition function"]}
print(json.dumps(result,indent=2))
