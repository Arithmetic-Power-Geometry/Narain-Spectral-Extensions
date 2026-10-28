# P30 exact spectral search — independent runnable checker
import sympy as s
from itertools import product
from collections import Counter
def qmat(b):
 g=s.Rational(1,10);G=s.Matrix([[1,g],[g,1]]);B=s.Matrix([[0,b],[-b,0]]);A=G.inv()
 return A.row_join(A*B).col_join((-B*A).row_join(G-B*A*B))
def spectrum(Q,R):
 c=Counter()
 for v in product(range(-R,R+1),repeat=4):
  z=s.Matrix(v);c[((z.T*Q*z)[0],v[0]*v[2]+v[1]*v[3])]+=1
 return c
J=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
T=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
Q=qmat(s.Rational(1,13));Qminus=qmat(s.Rational(-1,13));Qother=qmat(s.Rational(1,17))
assert T.T*J*T==J and T.T*Q*T==Qminus
for R in (2,3):
 a=spectrum(Q,R);b=spectrum(Qminus,R);c=spectrum(Qother,R)
 assert a==b and a!=c
 diff=sorted((k for k in a.keys()|c.keys() if a[k]!=c[k]))
 print('R',R,'charges',(2*R+1)**4,'duality_equal',a==b,'other_equal',a==c,'first_lexicographic_difference',diff[0])
