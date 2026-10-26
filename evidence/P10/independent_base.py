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
Q=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
t=F(3313,1325);b=F(1,5);c={s:Counter((e(v,s*b),v[0]*v[2]+v[1]*v[3]) for v in Q if e(v,s*b)<=3) for s in (1,-1)}
d={k:c[1][k]-c[-1][k] for k in c[1].keys()|c[-1].keys()}
assert len(Q)==729 and sum(c[1].values())==sum(c[-1].values())==39
assert min(k[0] for k,v in d.items() if v)==t
assert d[t,-1]==2 and d[t,1]==-2
print(json.dumps({'charge_box':len(Q),'states_each':sum(c[1].values()),'first':str(t),'first_coeff':{'-1':d[t,-1],'+1':d[t,1]},'status':'PASS'},indent=2))
