import sympy as S,itertools,json,time
start=time.perf_counter();results=[]
for d in (3,4,6):
 G=S.eye(d);B=S.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=S.Rational(1,10+i)
  B[i,i+1]=S.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 A=G.inv();Q=A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B))
 denom=S.ilcm(*[x.q for x in Q]);M=[[int(denom*Q[i,j]) for j in range(2*d)] for i in range(2*d)]
 vlist=[];mn=10**100;examined=0
 for v in itertools.product((-1,0,1),repeat=2*d):
  if not any(v):continue
  z=sum(v[i]*M[i][j]*v[j] for i in range(2*d) for j in range(2*d) if v[i] and v[j]);examined+=1
  vlist.append((z,v));mn=min(mn,z)
 short=[v for z,v in vlist if z<2*mn];n=len(short)
 seen={0};stack=[0]
 while stack:
  v=short[stack.pop()]
  for j,w in enumerate(short):
   if j not in seen and sum(v[k]*w[d+k]+v[d+k]*w[k] for k in range(d)):
    seen.add(j);stack.append(j)
 rank=S.polys.matrices.DomainMatrix.from_Matrix(S.Matrix(short)).rank() if d<=4 else S.Matrix(short).rank()
 results.append(dict(d=d,minimum=str(S.Rational(mn,denom)),two_minimum=str(S.Rational(2*mn,denom)),nshort=n,connected=len(seen)==n,span_rank=rank,charges=examined,denominator=int(denom),elapsed=round(time.perf_counter()-start,3)))
 print(json.dumps(results[-1]),flush=True)
print('TOTAL',round(time.perf_counter()-start,3))
