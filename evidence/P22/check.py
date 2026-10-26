from fractions import Fraction as F
from itertools import product
from math import factorial, isqrt
import json, hashlib, sys, time
st=time.monotonic()
def inverse(a):
 n=len(a);x=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for k in range(n):
  p=next(i for i in range(k,n) if x[i][k]);x[k],x[p]=x[p],x[k];z=x[k][k];x[k]=[v/z for v in x[k]]
  for i in range(n):
   if i!=k:
    z=x[i][k];x[i]=[v-z*w for v,w in zip(x[i],x[k])]
 return [row[n:] for row in x]
def determinant(a):
 n=len(a)
 if n==1:return a[0][0]
 return sum((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))
def energy(G,B,m,n):
 d=len(m);I=inverse(G);x=[F(m[i])+sum((B[i][j]*n[j] for j in range(d)),F(0)) for i in range(d)]
 return sum((x[i]*I[i][j]*x[j]+F(n[i])*G[i][j]*n[j] for i in range(d) for j in range(d)),F(0))
def spec(G,B,cap):
 d=len(G);r=range(-cap,cap+1);out={}
 for m in product(r,repeat=d):
  for n in product(r,repeat=d):
   e=energy(G,B,m,n);s=sum(x*y for x,y in zip(m,n));out[(e,s)]=out.get((e,s),0)+1
 return out
cases=[]
for d in (1,2,3):
 q=3;h=4;A=[[3 if i==j else 0 for j in range(d)] for i in range(d)];C=[[0]*d for _ in range(d)]
 if d>1:C[0][1]=1;C[1][0]=-1
 G=[[F(A[i][j],q) for j in range(d)] for i in range(d)];B=[[F(C[i][j],q) for j in range(d)] for i in range(d)]
 D=q*abs(determinant(A));assert D<=q*factorial(d)*h**d
 energies=[]
 for m in product((-1,0,1),repeat=d):
  for n in product((-1,0,1),repeat=d):
   e=energy(G,B,m,n);assert (D*e).denominator==1;energies.append(e)
 s=spec(G,B,1);sminus=spec(G,[[-x for x in row] for row in B],1)
 assert {(e,sp):c for (e,sp),c in sminus.items()}=={(e,-sp):c for (e,sp),c in s.items()}
 cases.append({'d':d,'q':q,'h':h,'D':D,'universal_Dmax':q*factorial(d)*h**d,'charges_tested':3**(2*d),'denominator_pass':True,'B_sign_spin_flip_pass':True,'different_spin_refined_within_box':s!=sminus})
# factorized T-duality in d=1: G=g vs G'=1/g, exchange m,n; spectra match for all charges.
g=F(2,3);dual=[]
for m,n in product(range(-3,4),repeat=2):
 e=F(m*m,1)/g+g*n*n;ed=F(n*n,1)/(1/g)+(1/g)*m*m
 assert e==ed
 dual.append((m,n))
print(json.dumps({'cases':cases,'factorized_T_duality_d1':{'G':str(g),'dual_G':str(1/g),'tested':len(dual),'pass':True},'runtime_s':round(time.monotonic()-st,4),'python':sys.version.split()[0]},indent=2))
