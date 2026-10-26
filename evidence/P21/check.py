from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import isqrt
import json,time,platform,hashlib
start=time.monotonic()
def invert(A):
 n=len(A);a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  pivot=next(i for i in range(k,n) if a[i][k]);a[k],a[pivot]=a[pivot],a[k]
  q=a[k][k];a[k]=[x/q for x in a[k]]
  for i in range(n):
   if i!=k:
    q=a[i][k];a[i]=[x-q*y for x,y in zip(a[i],a[k])]
 return [row[n:] for row in a]
def quad(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F(0))
def matvec(A,v):return [sum((A[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(v))]
def vectors(d,cap):
 lim=isqrt(cap)
 return [v for v in product(range(-lim,lim+1),repeat=d) if sum(x*x for x in v)<=cap]
def work(d,H):
 G=[[F(i==j) for j in range(d)] for i in range(d)]
 B=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):
  G[i][i+1]=G[i+1][i]=F(1,10+i)
  B[i][i+1]=F(1,13+i);B[i+1][i]=-B[i][i+1]
 GI=invert(G)
 # r=1e-12, all entries of symmetric G and antisymmetric B varied independently
 r=F(1,10**12); L0=F(89,110);U0=F(131,110);beta0=F(27,182)
 L=L0-d*r;U=U0+d*r;beta=beta0+d*r
 assert L>F(1,2) and beta<1 and d*r<1 and U<4*L
 ncap=H//L
 # strict bound m² < HU+ beta² H/L + 4 beta H
 M=H*U+beta*beta*H/L+4*beta*H
 mcap=(M.numerator-1)//M.denominator
 ns=vectors(d,int(ncap));ms=vectors(d,int(mcap))
 byspin=defaultdict(list);allstates=0
 for n in ns:
  w=quad(n,G)
  if w>H+F(1,100):continue
  bn=matvec(B,n)
  for m in ms:
   spin=sum(m[i]*n[i] for i in range(d))
   if not spin:continue
   x=[m[i]+bn[i] for i in range(d)]
   e=quad(x,GI)+w
   # Retain energies near window only, for witness selection, but compute exact witness-to-all opposite candidate separation below.
   byspin[spin].append((e,m,n))
   if e<=H:allstates+=1
 pos=defaultdict(list)
 for s,arr in byspin.items():
  if s>0:
   for e,m,n in arr:
    if e<=H:pos[(e,s)].append((m,n))
 # choose earliest E with spin+ multiplicity not matched by spin- (P07/P15)
 chosen=None
 for e,s in sorted(pos):
  opposite=[(m,n) for en,m,n in byspin[-s] if en==e]
  if len(pos[(e,s)])!=len(opposite):
   chosen=(e,s,pos[(e,s)],opposite);break
 assert chosen is not None
 e,s,witnesses,opp_at=chosen
 # gap to all opposite-spin candidates, regardless of whether their central energies lie in H
 diffs=[(abs(en-e),en,m,n) for en,m,n in byspin[-s] if en!=e]
 gap,near,mnear,nnear=min(diffs)
 assert not opp_at and gap>0
 # uniform Lipschitz <=160*d*r for each candidate; separation if 2*160*d*r < gap
 drift=160*d*r
 assert 2*drift<gap and drift<H-e
 # derive all-coordinate perturbation certificate: eigen bound and operator norm <=d*r, n²<=3,m²<=6,
 # beta<=1, L>=1/2, x<=sqrt(6)+sqrt(3)<5.
 # |delta E| <= 4 dr + 100 dr + 40 dr + 8(dr)^2 <=152 dr <160 dr
 # all-energy n,m candidate uniform bound from above
 result={'d':d,'H':str(H),'r':str(r),'L_box':str(L),'U_box':str(U),'beta_box':str(beta),'ncap':int(ncap),'mcap':int(mcap),'n_candidates':len(ns),'m_candidates':len(ms),'positive_spin_states_in_window':allstates,'witness_energy':str(e),'spin':s,'witness_charges':[{'m':list(m),'n':list(n)} for m,n in witnesses], 'opposite_same_energy_count':len(opp_at),'nearest_opposite_energy':str(near),'nearest_opposite_charge':{'m':list(mnear),'n':list(nnear)},'opposite_gap':str(gap),'H_margin':str(H-e),'uniform_energy_drift_bound':str(drift),'twice_drift_less_than_gap':2*drift<gap,'drift_less_than_H_margin':drift<H-e,'opposite_spin_candidate_count':len(byspin[-s]),'central_witness_multiplicity':len(witnesses),'forced_pair_check':all((tuple(-x for x in m),tuple(-x for x in n)) in witnesses for m,n in witnesses)}
 return result
out={'python':platform.python_version(),'cases':[]}
for d,H in [(3,F(3)),(4,F(5,2)),(6,F(5,2))]:
 a=work(d,H);out['cases'].append(a);print('case',d,'gap',a['opposite_gap'],'margin',a['H_margin'],flush=True)
out['runtime_seconds']=round(time.monotonic()-start,3)
print(json.dumps(out,indent=2))
