import sympy as s,json,time,sys
from hashlib import sha256
start=time.perf_counter()
rows=[]
for d in [2,3,4,5,6,8,10,12,16,20,30]:
 G=s.eye(d);B=s.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=s.Rational(1,10+i)
  B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 A=G.inv()
 max_m=max(A[i,i] for i in range(d))
 max_n=max(1+(B[:,i].T*A*B[:,i])[0] for i in range(d))
 max_adj=max(((B[:,i]-B[:,i+1]).T*A*(B[:,i]-B[:,i+1]))[0]+2-2*G[i,i+1] for i in range(d-1))
 assert max(max_m,max_n,max_adj)<2
 rows.append(dict(d=d,m_max=str(max_m),n_max=str(max_n),adj_max=str(max_adj),witnesses=3*d-1,pass_=True))
print(json.dumps({'method':'SymPy exact inverse; all 3d-1 witness energies checked <2','results':rows,'runtime_seconds':round(time.perf_counter()-start,4)},indent=2))
