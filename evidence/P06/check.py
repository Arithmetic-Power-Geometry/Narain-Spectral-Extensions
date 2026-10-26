#!/usr/bin/env python3
"""P06: exact rational coupled Narain finite-window enumeration; Python stdlib."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
def inv(A):
 d=len(A); X=[list(A[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  p=next(i for i in range(k,d) if X[i][k]); X[k],X[p]=X[p],X[k]
  z=X[k][k]; X[k]=[v/z for v in X[k]]
  for i in range(d):
   if i!=k:
    z=X[i][k];X[i]=[v-z*w for v,w in zip(X[i],X[k])]
 return [r[d:] for r in X]
def dot(x,A,y):
 return sum((x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(y))),F(0))
def run(d):
 G=[[F(i==j) for j in range(d)] for i in range(d)]
 B=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  G[i][i+1]=G[i+1][i]=F(1,10+i)
  B[i][i+1]=F(1,13+i);B[i+1][i]=-B[i][i+1]
 R=max(sum(abs(G[i][j]) for j in range(d) if i!=j) for i in range(d))
 L=1-R;U=1+R;beta=max(sum(abs(B[i][j]) for j in range(d)) for i in range(d))
 assert L>=F(4,5) and U<=F(6,5) and beta<=F(1,5)
 # For E<=2, ||n||²<=2/L<=5/2 so integer ||n||²<=2.
 # ||m||<=sqrt(2U)+beta sqrt(2/L)<=sqrt(12/5)+sqrt(5/2)/5<2;
 # hence integer ||m||²<=3; enumerate conservatively through 4.
 nlist=[v for v in product((-1,0,1),repeat=d) if sum(x*x for x in v)<=2]
 mlist=[v for v in product(range(-2,3),repeat=d) if sum(x*x for x in v)<=4]
 I=inv(G);c={}
 for sign in (1,-1):
  out=Counter()
  for n in nlist:
   Bn=[sign*sum(B[i][j]*n[j] for j in range(d)) for i in range(d)]
   for m in mlist:
    x=[m[i]+Bn[i] for i in range(d)]
    E=dot(x,I,x)+dot(n,G,n)
    if E<=2:out[E,sum(m[i]*n[i] for i in range(d))]+=1
  c[sign]=out
 delta={k:c[1][k]-c[-1][k] for k in c[1].keys()|c[-1].keys()}
 first=min((e for (e,s),v in delta.items() if v),default=None)
 assert all(c[1][e,s]==c[-1][e,-s] for e,s in c[1])
 assert all(sum(v for (e,s),v in delta.items() if e==t)==0 for t in {x[0] for x in delta})
 return dict(dimension=d,G=[[str(v) for v in row] for row in G],B=[[str(v) for v in row] for row in B],lower_eigen_bound=str(L),upper_eigen_bound=str(U),B_infinity_bound=str(beta),n_vectors=len(nlist),m_vectors=len(mlist),states_each=sum(c[1].values()),first_discrepancy_E_le_2=str(first) if first is not None else None,first_difference={str(s):v for (e,s),v in delta.items() if e==first and v},unrefined_equal=True,complete_through_E="2")
res={"status":"PASS_FINITE_EXACT_ENUMERATION_NOT_GLOBAL_DUALITY_PROOF","cases":[run(d) for d in (3,4,6)],"limitation":"Only E<=2; integral indecomposability, O(d,d;Z) nonduality and perturbation interval not certified."}
print(json.dumps(res,indent=2))
