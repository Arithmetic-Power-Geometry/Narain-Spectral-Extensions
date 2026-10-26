import sympy as s,itertools,json,time
st=time.perf_counter();results=[]
for d in (3,4):
 G=s.eye(d);B=s.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=s.Rational(1,10+i)
  B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 A=G.inv();Q=A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B))
 vals=[]
 for v in itertools.product((-1,0,1),repeat=2*d):
  if not any(v):continue
  energy=sum(Q[i,j]*v[i]*v[j] for i in range(2*d) for j in range(2*d))
  vals.append((energy,v))
 lam=min(e for e,v in vals);assert 2*lam<s.Rational(21,10)
 short=[v for e,v in vals if e<2*lam]
 seen={0};stack=[0]
 while stack:
  i=stack.pop();v=short[i]
  for j,w in enumerate(short):
   if j in seen:continue
   pair=sum(v[k]*w[d+k]+v[d+k]*w[k] for k in range(d))
   if pair:seen.add(j);stack.append(j)
 R=s.Matrix(short).rank()
 assert len(seen)==len(short) and R==2*d
 results.append({'d':d,'minimum':str(lam),'twice_minimum':str(2*lam),'short_vectors':len(short),'J_connected_vertices':len(seen),'span_rank':R,'certified':True})
print(json.dumps({'method':'independent SymPy Q matrix + BFS J graph','cases':results,'runtime_seconds':round(time.perf_counter()-st,5)},indent=2))
