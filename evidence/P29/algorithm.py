from fractions import Fraction as F
from itertools import product
import json,time,hashlib,sys
start=time.perf_counter()
def matmul(a,b):return sum(x*y for x,y in zip(a,b))
def dot(a,Q,b):return sum(a[i]*Q[i][j]*b[j] for i in range(len(a)) for j in range(len(b)))
def run(Q,J):
 N=len(Q); M=max(Q[i][i] for i in range(N)); D=max(sum(abs(x) for x in row) for row in Q)
 # conservative bound from rational matrix inverse: lambda_min >= 1/||Q^-1||infty
 import sympy as s
 A=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row] for row in Q]); ai=A.inv();lower=F(1,1)/max(sum(abs(F(int(x.p),int(x.q))) for x in ai.row(i)) for i in range(N))
 R=int((M/lower)**F(1,2)) if False else 1
 while lower*(R+1)**2<=M:R+=1
 V=[v for v in product(range(-R,R+1),repeat=N) if any(v) and dot(v,Q,v)<=M]
 energies={v:dot(v,Q,v) for v in V}; minimal=[]
 for v in sorted(V,key=lambda v:(energies[v],v)):
  e=energies[v]; ismin=True
  for x in V:
   if energies[x]>=e:continue
   y=tuple(a-b for a,b in zip(v,x))
   if y in energies and energies[y]<e:ismin=False;break
  if ismin:minimal.append(v)
 parent=list(range(len(minimal)))
 def root(i):
  while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
  return i
 for i in range(len(minimal)):
  for j in range(i):
   if dot(minimal[i],Q,minimal[j]) or dot(minimal[i],J,minimal[j]):parent[root(i)]=root(j)
 comps={}
 for i,v in enumerate(minimal):comps.setdefault(root(i),[]).append(v)
 return {'rank':N,'M':str(M),'lower_eigen_bound':str(lower),'coordinate_bound':R,'vectors_in_ball':len(V),'minimal_vectors':len(minimal),'component_sizes':sorted(map(len,comps.values())),'components':list(comps.values())}
def matrices(d,coupled):
 import sympy as s
 G=s.eye(d);B=s.zeros(d)
 if coupled:
  for i in range(d-1):G[i,i+1]=G[i+1,i]=s.Rational(1,10+i);B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 A=G.inv();q=A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B));j=s.zeros(d).row_join(s.eye(d)).col_join(s.eye(d).row_join(s.zeros(d)))
 return [[[F(int(q[i,k].p),int(q[i,k].q)) for k in range(2*d)] for i in range(2*d)],[[F(int(j[i,k])) for k in range(2*d)] for i in range(2*d)]]
results=[]
for d,c in [(1,False),(2,False),(2,True)]:
 Q,J=matrices(d,c);r=run(Q,J);r['d']=d;r['coupled']=c;results.append(r)
print(json.dumps({'results':results,'seconds':round(time.perf_counter()-start,5)},default=str,indent=2))
