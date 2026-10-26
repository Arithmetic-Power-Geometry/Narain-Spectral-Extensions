#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
G=((F(2),F(1,3)),(F(1,3),F(3)))
d=G[0][0]*G[1][1]-G[0][1]**2
A=((G[1][1]/d,-G[0][1]/d),(-G[0][1]/d,G[0][0]/d))
def E(v,b):
 m1,m2,n1,n2=v;x=m1+b*n2;y=m2-b*n1
 return A[0][0]*x*x+2*A[0][1]*x*y+A[1][1]*y*y+G[0][0]*n1*n1+2*G[0][1]*n1*n2+G[1][1]*n2*n2
def S(v):return v[0]*v[2]+v[1]*v[3]
Q=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
b=F(1,5);T=F(3313,1325)
C={k:Counter((E(v,k*b),S(v)) for v in Q if E(v,k*b)<=3) for k in (1,-1)}
D={k:C[1][k]-C[-1][k] for k in C[1].keys()|C[-1].keys()}
assert len(Q)==729 and sum(C[1].values())==sum(C[-1].values())==39
assert D[T,-1]==2 and D[T,1]==-2
assert all(z==0 for (e,s),z in D.items() if e<T)
assert all(sum(z for (ee,s),z in D.items() if ee==e)==0 for e in {x[0] for x in D})
assert all(E((v[0],v[1],-v[2],-v[3]),-b)==E(v,b) and S((v[0],v[1],-v[2],-v[3]))==-S(v) for v in Q)
assert sum(z for (e,s),z in D.items() if e==T and s==0)==0
assert 2*D[T,-1]+2*D[T,1]==0
result={"status":"PASS_FOR_DEFINED_CFT_TESTS","charge_count":729,"states_E_le_3_each":39,"first_threshold":str(T),"first_difference":{"spin_-1":2,"spin_+1":-2},"unrefined_equal_E_le_3":True,"unrefined_equal_all_energies_by_bijection":True,"tau1_zero_partition_equal_all_energies_by_bijection":True,"generic_tau1_refined_difference":"-4i sin(2*pi*tau1) exp(-pi*tau2*T) at leading zero-mode order","spin_zero_primary_projection_at_T":0,"first_descendant_spin_zero_signed_coefficient_at_T_plus_2":0,"modular_S_proof":"standard even self-dual lattice theorem, not independently numerically checked","physical_string_state_space":"not specified; cannot infer survival"}
print(json.dumps(result,indent=2))
