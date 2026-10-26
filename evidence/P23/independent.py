import sympy as s, itertools, json, time, hashlib, sys
from fractions import Fraction as F
start=time.perf_counter()
records=[]
for d in range(1,5):
 q=3;h=6
 A=s.eye(d)*3
 for i in range(d-1):
  A[i,i+1]=A[i+1,i]=1
 C=s.zeros(d)
 for i in range(d-1):
  C[i,i+1]=1;C[i+1,i]=-1
 assert all(z>0 for z in [A[:k,:k].det() for k in range(1,d+1)])
 G=A/q; B=C/q
 Q=(s.BlockMatrix([[G.inv(),G.inv()*B],[-B*G.inv(),G-B*G.inv()*B]])).as_explicit()
 D=q*int(A.det()); bound=q*s.factorial(d)*h**d
 assert all((D*x).q==1 for x in Q)
 assert D<=bound
 T=d*h
 # ||B||_2 <= max row/col norm <= T/q
 L=s.Rational(1,q*T**(d-1)); U=s.Rational(T,q);beta=s.Rational(T,q)
 assert (G-L*s.eye(d)).is_positive_semidefinite and (U*s.eye(d)-G).is_positive_semidefinite
 H=s.Rational(3)
 ncap=int(s.floor(H/L));mcap=int(s.floor(2*H*U+2*beta**2*H/L))
 checked=0; within=0
 # bounded 3^(2d) charge test, including difficult non-diagonal examples
 for charge in itertools.product((-1,0,1),repeat=2*d):
  v=s.Matrix(charge); e=(v.T*Q*v)[0];assert (D*e).q==1
  m=charge[:d];n=charge[d:];
  if e<=H:
   within+=1;assert sum(z*z for z in n)<=ncap and sum(z*z for z in m)<=mcap
  checked+=1
 records.append({'d':d,'q':q,'h':h,'det_A':int(A.det()),'denominator_D':D,'Dmax':int(bound),'charges':checked,'within_H':within,'ncap':ncap,'mcap':mcap,'pass':True})
print(json.dumps({'checker':'independent sympy generalized-metric block construction','python':sys.version.split()[0],'sympy':s.__version__,'cases':records,'elapsed_seconds':round(time.perf_counter()-start,5)},indent=2))
