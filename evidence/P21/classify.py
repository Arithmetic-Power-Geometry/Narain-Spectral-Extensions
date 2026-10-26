from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json,time,platform
st=time.monotonic()
def inv(A):
 d=len(A);Z=[list(A[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  p=next(i for i in range(k,d) if Z[i][k]);Z[k],Z[p]=Z[p],Z[k];v=Z[k][k];Z[k]=[x/v for x in Z[k]]
  for i in range(d):
   if i!=k:
    v=Z[i][k];Z[i]=[x-v*y for x,y in zip(Z[i],Z[k])]
 return [x[d:] for x in Z]
def quad(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),F(0))
def vec(d,k):return [v for v in product(range(-2,3),repeat=d) if sum(x*x for x in v)<=k]
def canon(m,n):
 a=tuple(m)+tuple(n);b=tuple(-x for x in a);return min(a,b)
out={'method':'complete_finite_window_energy_degeneracy_orbits','cases':[]}
for d,H,mc in [(3,F(3),5),(4,F(5,2),4),(6,F(5,2),4)]:
 G=[[F(i==j) for j in range(d)] for i in range(d)];B=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):G[i][i+1]=G[i+1][i]=F(1,10+i);B[i][i+1]=F(1,13+i);B[i+1][i]=-B[i][i+1]
 I=inv(G);energies=defaultdict(list)
 for n in vec(d,3):
  w=quad(n,G)
  if w>H:continue
  bn=[sum((B[i][j]*n[j] for j in range(d)),F(0)) for i in range(d)]
  for m in vec(d,mc):
   v=[m[i]+bn[i] for i in range(d)];e=quad(v,I)+w
   if e<=H:energies[e].append((m,n,sum(m[i]*n[i] for i in range(d))))
 groups=[];cross=[]
 for e,charges in energies.items():
  orbits={canon(m,n) for m,n,s in charges}
  if len(orbits)>1:
   groups.append({'E':str(e),'charge_count':len(charges),'distinct_pm_orbits':len(orbits),'spins':sorted({s for m,n,s in charges})})
   if len({s for m,n,s in charges})>1:cross.append(str(e))
 out['cases'].append({'d':d,'H':str(H),'states':sum(map(len,energies.values())),'energy_levels':len(energies),'accidental_energy_levels':len(groups),'accidental_examples':groups[:10],'cross_spin_accidental_levels':len(cross),'cross_spin_examples':cross[:10]})
out['runtime_seconds']=round(time.monotonic()-st,3);out['python']=platform.python_version();print(json.dumps(out,indent=2))
