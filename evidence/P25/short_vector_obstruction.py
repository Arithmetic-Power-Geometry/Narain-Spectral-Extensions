from fractions import Fraction as F
from itertools import product
import json,time
st=time.monotonic()
def inv(a):
 d=len(a);z=[list(a[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  p=next(i for i in range(k,d) if z[i][k]);z[k],z[p]=z[p],z[k];v=z[k][k];z[k]=[x/v for x in z[k]]
  for i in range(d):
   if i!=k:
    v=z[i][k];z[i]=[x-v*y for x,y in zip(z[i],z[k])]
 return [row[d:] for row in z]
def E(g,b,gi,m,n):
 d=len(g);x=[F(m[i])+sum((b[i][j]*n[j] for j in range(d)),F(0)) for i in range(d)]
 return sum((x[i]*gi[i][j]*x[j]+F(n[i])*g[i][j]*n[j] for i in range(d) for j in range(d)),F(0))
def rank(a):
 if not a:return 0
 a=[list(map(F,row)) for row in a];n=len(a[0]);k=0
 for j in range(n):
  p=next((i for i in range(k,len(a)) if a[i][j]),None)
  if p is None:continue
  a[k],a[p]=a[p],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
  for i in range(k+1,len(a)):
   v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k
out=[]
for d in (3,4):
 g=[[F(i==j) for j in range(d)] for i in range(d)];b=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):g[i][i+1]=g[i+1][i]=F(1,10+i);b[i][i+1]=F(1,13+i);b[i+1][i]=-b[i][i+1]
 gi=inv(g);vs=[]
 for m in product((-1,0,1),repeat=d):
  for n in product((-1,0,1),repeat=d):
   if any(m) or any(n):vs.append((E(g,b,gi,m,n),m+n))
 lam=min(x[0] for x in vs)
 low=[v for e,v in vs if e<2*lam]
 parent=list(range(len(low)))
 def root(i):
  while parent[i]!=i:
   parent[i]=parent[parent[i]];i=parent[i]
  return i
 for i in range(len(low)):
  for j in range(i):
   a=low[i];v=low[j]
   pairing=sum(a[k]*v[d+k]+a[d+k]*v[k] for k in range(d))
   if pairing:parent[root(i)]=root(j)
 components={}
 for i in range(len(low)):components.setdefault(root(i),[]).append(low[i])
 component_ranks=sorted((rank(x) for x in components.values()),reverse=True)
 out.append({'d':d,'box':'[-1,1]^(2d)','sample_minimum':str(lam),'vectors_below_twice_sample_minimum':len(low),'span_rank':rank(low),'ambient_rank':2*d,'J_graph_component_ranks':component_ranks,'global_minimum_certified':False})
print(json.dumps({'results':out,'runtime_seconds':round(time.monotonic()-st,4)},indent=2))
