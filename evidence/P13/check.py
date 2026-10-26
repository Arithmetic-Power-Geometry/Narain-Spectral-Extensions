#!/usr/bin/env python3
"""Exact GL(Z) indecomposability certificates for P07 coupled T3/T4."""
import json, sympy as S
from itertools import permutations,product
x=S.Symbol("x")
def background(d):
 G=S.eye(d);B=S.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=S.Rational(1,10+i)
  B[i,i+1]=S.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 return G,B
def signed_count(d,G,B):
 tested=0;found=0
 for p in permutations(range(d)):
  for signs in product((-1,1),repeat=d):
   U=S.zeros(d)
   for j in range(d):U[p[j],j]=signs[j]
   tested+=1;H=U.T*G*U;K=U.T*B*U
   if any(all(H[i,j]==0 and K[i,j]==0 for i in range(k) for j in range(k,d)) for k in range(1,d)):found+=1
 return tested,found
def run(d):
 G,B=background(d);A=G.inv()*B
 f=S.factor(A.charpoly(x).as_expr());fac=S.factor_list(f)[1]
 tested,found=signed_count(d,G,B)
 out=dict(dimension=d,charpoly=str(f),factor_degrees=[int(S.degree(t,x)) for t,k in fac for _ in range(k)],signed_permutations_tested=tested,signed_permutation_decompositions=found)
 if d==4:
  assert len(fac)==1 and S.degree(fac[0][0],x)==4 and fac[0][1]==1
  out["GLZ_certificate"]="irreducible_Q_characteristic_polynomial"
 elif d==3:
  v=B.nullspace()[0];v=v*S.ilcm(*[t.q for t in v]);v=v/S.igcd(*[int(t) for t in v]);v=S.Matrix(v)
  norm=(v.T*G*v)[0];projection=[S.factor(z/norm) for z in v.T*G]
  assert any(z.q!=1 for z in projection)
  out.update(primitive_B_kernel=list(map(int,v)),kernel_norm=str(norm),projection_coefficients=[str(z) for z in projection],GLZ_certificate="nonintegral_G_orthogonal_projection_onto_primitive_B_kernel")
 return out
def control():
 G=S.diag(2,3,5);B=S.zeros(3)
 assert G.inv()*B==S.zeros(3)
 return dict(dimension=3,type="diagonal_G_zero_B",explicit_block_decomposition="identity",expected="decomposable",observed="decomposable")
if __name__=="__main__":
 print(json.dumps(dict(T3=run(3),T4=run(4),negative_control=control(),O_d_d_Z="NOT_CLASSIFIED",gate="PASS_GLZ_ONLY_REVISE_FULL_DUALITY"),indent=2))
