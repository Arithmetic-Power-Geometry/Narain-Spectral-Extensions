"""P48 exact rational spectral-bound optimization; analytic-only baseline benchmark."""
from fractions import Fraction as F
import json,sys,time
sys.path.insert(0,'/mnt/data/p47')
import mpmath as mp
from certified_theta import tail_bound

def admissible(Y,l):
 a,b,d=map(F,Y);l=F(l)
 return l>0 and a-l>0 and (a-l)*(d-l)>b*b

def optimized_lower(Y,bits=40):
 a,b,d=map(F,Y)
 if a<=0 or a*d<=b*b:raise ValueError('not SPD')
 lo=F(0);hi=min(a,d)
 for _ in range(bits):
  mid=(lo+hi)/2
  if admissible(Y,mid):lo=mid
  else:hi=mid
 return lo

def upper(iv):return float(iv.b)

def case(name,n,Y,baseline,eps):
 t=time.monotonic();best=optimized_lower(Y)
 mp.iv.dps=35
 rows=[]
 for K in range(5):
  old=upper(tail_bound(n,K,baseline));new=upper(tail_bound(n,K,str(best.numerator)+'/'+str(best.denominator)))
  rows.append({'K':K,'old_tail':old,'new_tail':new,'improvement_factor':old/new if new else None})
 # first cutoff with 2*tail <= epsilon
 def cutoff(field):return next((r['K'] for r in rows if 2*r[field]<=float(F(eps))),None)
 return {'name':name,'n':n,'Y':Y,'old_lower':baseline,'optimized_lower':str(best),'old_cutoff':cutoff('old_tail'),'optimized_cutoff':cutoff('new_tail'),'rows':rows,'seconds':time.monotonic()-t}

if __name__=='__main__':
 for args in [('published',7,['1.1','.23','1.3'],'.949','1e-12'),('near_separating',7,['1.1','.01','1.3'],'1.08','1e-5'),('ill_conditioned',2,['1','.95','1'],'.04','1e-8'),('diagonal',2,['1.1','0','1.3'],'.5','1e-8')]:
  print(json.dumps(case(*args),sort_keys=True),flush=True)
 for bad in [['1','1','1'],['0','0','1'],['1','2','1']]:
  try:optimized_lower(bad);raise AssertionError('accepted non-SPD')
  except ValueError:print(json.dumps({'invalid_Y':bad,'status':'REJECTED'}),flush=True)
