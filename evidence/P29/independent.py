import sympy as s,itertools,json,time
start=time.perf_counter()
records=[]
for d,coupled in [(1,False),(2,False),(2,True)]:
 G=s.eye(d);B=s.zeros(d)
 if coupled:
  for i in range(d-1):G[i,i+1]=G[i+1,i]=s.Rational(1,10+i);B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 A=G.inv();Q=A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B));J=s.zeros(d).row_join(s.eye(d)).col_join(s.eye(d).row_join(s.zeros(d)))
 M=max(Q[i,i] for i in range(2*d)); lower=1/max(sum(abs(A.inv()[i,j]) for j in range(2*d)) for i in range(2*d)) if False else 1/max(sum(abs(Q.inv()[i,j]) for j in range(2*d)) for i in range(2*d))
 R=0
 while lower*(R+1)**2<=M:R+=1
 V=[]
 for v in itertools.product(range(-R,R+1),repeat=2*d):
  if not any(v):continue
  z=s.Matrix(v);e=(z.T*Q*z)[0]
  if e<=M:V.append((tuple(v),e))
 vals={v:e for v,e in V};atoms=[]
 for v,e in V:
  if not any(xe<e and tuple(v[i]-x[i] for i in range(2*d)) in vals and vals[tuple(v[i]-x[i] for i in range(2*d))]<e for x,xe in V):atoms.append(v)
 seen=set();sizes=[]
 for v in atoms:
  if v in seen:continue
  stack=[v];seen.add(v);count=0
  while stack:
   x=stack.pop();count+=1
   for y in atoms:
    if y in seen:continue
    a=s.Matrix(x);b=s.Matrix(y)
    if (a.T*Q*b)[0] or (a.T*J*b)[0]:seen.add(y);stack.append(y)
  sizes.append(count)
 records.append({'d':d,'coupled':coupled,'M':str(M),'lower_eigen_bound':str(lower),'coordinate_bound':R,'vectors_in_ball':len(V),'minimal_vectors':len(atoms),'component_sizes':sorted(sizes)})
print(json.dumps({'records':records,'seconds':round(time.perf_counter()-start,5)},indent=2))
