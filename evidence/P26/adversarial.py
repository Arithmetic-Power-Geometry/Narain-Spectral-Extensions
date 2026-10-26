import sympy as s,json,time
st=time.perf_counter()
def jmat(d):return s.zeros(d).row_join(s.eye(d)).col_join(s.eye(d).row_join(s.zeros(d)))
def Q(G,B):
 A=G.inv();return A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B))
def form(d):
 G=s.eye(d);B=s.zeros(d)
 for i in range(d-1):G[i,i+1]=G[i+1,i]=s.Rational(1,10+i);B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 return Q(G,B)
def transforms(d):
 I=s.eye(d);Z=s.zeros(d);J=jmat(d)
 K=s.zeros(d);K[0,1]=1;K[1,0]=-1
 T=I.row_join(-K).col_join(Z.row_join(I))
 U=s.eye(d);U[0,1]=1
 W=U.inv().T.row_join(Z).col_join(Z.row_join(U))
 F=s.eye(2*d);i=0
 for a,b in ((i,i),(d+i,d+i)):F[a,b]=0
 F[i,d+i]=F[d+i,i]=1
 for x in (T,W,F,T*W*F):assert x.T*J*x==J and abs(x.det())==1
 return [('Bshift',T),('GL',W),('factorized',F),('composed',T*W*F)]
res=[]
for d in (3,4,6):
 J=jmat(d);q=form(d)
 for name,t in transforms(d):
  qt=t.T*q*t;assert qt==qt.T
  v=s.zeros(2*d,1);v[0]=1;v[d]=1;w=t.inv()*v
  assert (w.T*qt*w)[0]==(v.T*q*v)[0] and (w.T*J*w)[0]==(v.T*J*v)[0]
  res.append(dict(d=d,transformation=name,det=int(t.det()),energy_invariant=True,J_invariant=True))
for d in (3,4,6):
 J=jmat(d);Q0=s.eye(2*d);P=s.zeros(2*d)
 P[0,0]=P[d,d]=1
 assert P*P==P and P.T*J==J*P and P.T*Q0==Q0*P
 res.append(dict(d=d,transformation='decomposable_negative_control',integral_projector=True,short_graph_connected=False))
print(json.dumps({'tests':res,'seconds':round(time.perf_counter()-st,4)},indent=2))
