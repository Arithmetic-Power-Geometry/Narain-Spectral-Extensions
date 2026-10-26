import sympy as s,json,time
st=time.perf_counter()
def J(d):return s.zeros(d).row_join(s.eye(d)).col_join(s.eye(d).row_join(s.zeros(d)))
def Q(G,B):
 A=G.inv();return A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B))
def check(Q0,J0,P):
 return dict(idempotent=P*P==P,J_selfadjoint=P.T*J0==J0*P,Q_selfadjoint=P.T*Q0==Q0*P,integral=all(x.q==1 for x in P),rank=P.rank())
out=[]
for d in (3,4):
 G=s.eye(d);B=s.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=s.Rational(1,10+i)
  B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 j=J(d);q=Q(G,B);v=j*q;assert v*v==s.eye(2*d)
 p=(s.eye(2*d)+v)/2
 out.append({'d':d,'involution':True,'characteristic':str(s.factor(v.charpoly().as_expr())),'plus':check(q,j,p),'minus':check(q,j,s.eye(2*d)-p)})
d=3;j=J(d);q=Q(s.eye(d),s.zeros(d));p=s.zeros(2*d);p[0,0]=p[d,d]=1
k=s.zeros(d);k[0,1]=1;k[1,0]=-1
t=s.eye(2*d);t[:d,d:]=-k;assert t.T*j*t==j
qt=t.T*q*t;pt=t.inv()*p*t
assert all(check(qt,j,pt)[z] for z in ('idempotent','J_selfadjoint','Q_selfadjoint','integral'))
u=s.eye(d);u[0,1]=1
w=u.inv().T.row_join(s.zeros(d)).col_join(s.zeros(d).row_join(u))
assert w.T*j*w==j
q2=w.T*qt*w;p2=w.inv()*pt*w
assert all(check(q2,j,p2)[z] for z in ('idempotent','J_selfadjoint','Q_selfadjoint','integral'))
print(json.dumps({'coupled':out,'B_shift':check(qt,j,pt),'B_shift_GL':check(q2,j,p2),'runtime_seconds':round(time.perf_counter()-st,5)},indent=2))
