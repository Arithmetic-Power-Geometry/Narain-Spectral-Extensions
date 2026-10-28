from fractions import Fraction as F
from sympy import eye, zeros
a=F(1,20); b0=F(2,25); b1=F(3,25)
assert ((1-b0)**2+b1*b1)/(1-4*a*a)==F(2152,2475)<1
for d in range(2,7):
 for seed in range(4):
  G=eye(d); B=zeros(d)
  for i in range(d-1):
   t=[-a,F(0),a,F(1,40)][(seed+i)%4]
   b=[b0,b1,F(1,10),F(9,100)][(seed+2*i)%4]
   G[i,i+1]=G[i+1,i]=t
   B[i,i+1]=b;B[i+1,i]=-b
  inv=G.inv()
  for i in range(d-1):
   m=zeros(d,1); n=zeros(d,1)
   m[i]=-1;n[i+1]=1
   v=m+B*n
   assert (v.T*inv*v+n.T*G*n)[0]<2
print("PASS: exact rational certificate and 20 parameter cases")
