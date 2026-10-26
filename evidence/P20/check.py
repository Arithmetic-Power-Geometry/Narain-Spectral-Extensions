import sympy as S,json,time,platform
st=time.monotonic()
def build(d):
 G=S.eye(d);B=S.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=S.Rational(1,10+i)
  B[i,i+1]=S.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 return G,B
def general(G,B):
 I=G.inv();return (S.BlockMatrix([[I,I*B],[-B*I,G-B*I*B]])).as_explicit()
def Jmat(d):return S.BlockMatrix([[S.zeros(d),S.eye(d)],[S.eye(d),S.zeros(d)]]).as_explicit()
def check_projector(P,J,Q):return {'idempotent':P*P==P,'J_self_adjoint':P.T*J==J*P,'Q_self_adjoint':P.T*Q==Q*P,'rank':P.rank(),'integral':all(z.q==1 for z in P)}
out={}
for d in (3,4):
 G,B=build(d);Q=general(G,B);J=Jmat(d)
 out['T'+str(d)]={'charpoly':str(S.factor((G.inv()*B).charpoly().as_expr())),'Q_positive':all(z>0 for z in G[:d,:d].diagonal()),'JQJ_eq_Qinv':J*Q*J==Q.inv()}
 if d==3:
  v=S.Matrix([13,0,14]);proj=v*(v.T*G)/(v.T*G*v)[0]
  out['T3']['projection_e1']=[str(z) for z in proj[:,0]]
d=3;G=S.diag(2,3,5);B=S.zeros(d);K=S.zeros(d);K[0,1]=1;K[1,0]=-1
T=S.BlockMatrix([[S.eye(d),-K],[S.zeros(d),S.eye(d)]]).as_explicit()
J=Jmat(d);Q=general(G,B);Q2=T.T*Q*T
Q_expected=general(G,-K)
P=S.diag(1,0,0,1,0,0);P2=T.inv()*P*T
out['B_shift_control']={'duality_preserves_J':T.T*J*T==J,'conjugate_Q':Q2==Q_expected,'projector_original':check_projector(P,J,Q),'projector_transformed':check_projector(P2,J,Q2),'P2':[[str(z) for z in row] for row in P2.tolist()],'Q2_cross_coupling':Q2!=Q,'Bprime':[[str(z) for z in row] for row in (-K).tolist()]}
out['elapsed_s']=round(time.monotonic()-st,3);out['python']=platform.python_version();out['sympy']=S.__version__
print(json.dumps(out,indent=2))
