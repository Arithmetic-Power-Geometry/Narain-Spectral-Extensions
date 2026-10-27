from itertools import product
from math import exp, pi
from collections import Counter
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
Y=((1.1,.23),(.23,1.3))
def q(x):return Y[0][0]*x[0]**2+2*Y[0][1]*x[0]*x[1]+Y[1][1]*x[1]**2
def words(edges):
 a=[0]*7
 for i,j in edges:a[i]^=1<<j;a[j]^=1<<i
 for x in range(128):
  z=0
  for i in range(7):
   if x>>i&1:z^=a[i]
  yield tuple(((x>>i)&1,(z>>i)&1) for i in range(7))
def site(alpha,beta,K=2):
 val=0.
 for aa in product(range(-K,K+1),repeat=2):
  for bb in product(range(-K,K+1),repeat=2):
   l=tuple(aa[j]+bb[j]+(alpha[j]+beta[j])/2 for j in range(2))
   r=tuple(aa[j]-bb[j]+(alpha[j]-beta[j])/2 for j in range(2))
   val+=exp(-pi*(q(l)+q(r)))
 return val
local={k:site(k[:2],k[2:]) for k in product((0,1),repeat=4)}
def total(edges):
 w=list(words(edges));s=0.
 for u in w:
  for v in w:
   t=1.
   for i in range(7):
    al=(u[i][0],v[i][0]);be=(u[i][1],v[i][1]);t*=local[al+be]
   s+=t
 return s
print('A',format(total(A),'.17g'))
print('B',format(total(B),'.17g'))
print('difference',format(total(A)-total(B),'.17g'))
print('K',2,'local_values',len(local))
