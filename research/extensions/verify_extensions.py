"""Exact bounded experiments for Narain oscillator and metric extensions."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
from pathlib import Path

G=((F(2),F(1,3)),(F(1,3),F(3)))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mul(A,v):return tuple(dot(row,v) for row in A)
def inverse(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
 return ((A[1][1]/d,-A[0][1]/d),(-A[1][0]/d,A[0][0]/d))
def energy(m,n,b,A=G):
 x=(m[0]+b*n[1],m[1]-b*n[0])
 return dot(x,mul(inverse(A),x))+dot(n,mul(A,n))
def charge_set():
 for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
  yield v[:2],v[2:]
def spin(m,n):return dot(m,n)
def zero_modes(b):
 c=Counter()
 for m,n in charge_set():
  e=energy(m,n,b)
  if e<=3:c[e,spin(m,n)]+=1
 return c
def partition_coeffs(N,dim=2):
 v=[0]*(N+1);v[0]=1
 for n in range(1,N+1):
  for _ in range(dim):
   for j in range(n,N+1):v[j]+=v[j-n]
 return v
def dressed(z,p):
 c=Counter()
 for (e,s),n in z.items():
  for i,a in enumerate(p):
   for j,b in enumerate(p):c[e+2*(i+j),s+i-j]+=n*a*b
 return c
def stability_checks():
 Hs=[((F(0),F(0)),(F(0),F(0))),
     ((F(1,10000),F(0)),(F(0),-F(1,10000))),
     ((F(0),F(1,10000)),(F(1,10000),F(0)))]
 for b in (F(1,10),F(1,5),F(2,5)):
  for H in Hs:
   A=tuple(tuple(G[i][j]+H[i][j] for j in range(2)) for i in range(2))
   for sg in (1,-1):
    w=((-1,0),(sg,0))
    t=energy(*w,sg*b,A)
    oppos=(tuple(-x for x in w[0]),tuple(-x for x in w[1]))
    for m,n in charge_set():
     if spin(m,n) and (m,n)!=w and (m,n)!=oppos:
      assert energy(m,n,sg*b,A)>t,(b,H,sg,m,n)
 return {'rational_b_values':['1/10','1/5','2/5'],'symmetric_perturbations':len(Hs),'background_signs':2,'status':'PASS (finite rational points only)'}
def main():
 plus=zero_modes(F(1,5));minus=zero_modes(F(-1,5))
 t=F(3313,1325)
 assert sum(plus.values())==sum(minus.values())==39
 assert all(plus[k]==minus[k] for k in set(plus)|set(minus) if k[0]<t)
 assert (plus[t,-1],minus[t,-1],plus[t,1],minus[t,1])==(2,0,0,2)
 p=partition_coeffs(3)
 assert p==[1,2,5,10]
 a=dressed(plus,p);b=dressed(minus,p)
 assert all(a[k]==b[k] for k in set(a)|set(b) if k[0]<t)
 assert a[t,-1]-b[t,-1]==2 and a[t,1]-b[t,1]==-2
 for m,n in charge_set():
  if all(abs(z)<=1 for z in m+n):
   assert energy(m,n,F(1,5))==energy(tuple(-x for x in m),n,F(-1,5))
 result={'status':'PASS','scope':'finite exact tests: zero modes up to energy 3; oscillator levels 0..3 per chirality',
 'zero_mode_charge_box':729,'zero_mode_states_per_sign_below_3':39,
 'oscillator_degeneracies':p,'threshold':str(t),
 'dressed_first_difference':{'energy':str(t),'spin_minus_one_difference':2,'spin_plus_one_difference':-2},
 'higher_dimension':{'dimension':6,'block_diagonal_metric':True,'B_field_blocks':['+1/5 J','0 J','0 J'],'status':'constructive product family; not a general T6 or Calabi-Yau classification'},
 'stability_spot_checks':stability_checks(),
 'caveat':'Formal unprojected oscillator state-counting series. Not a physical-string partition function or cosmological stability proof.'}
 Path(__file__).with_name('extension_results.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
