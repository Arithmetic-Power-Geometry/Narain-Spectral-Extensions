"""Exact-SPD precondition and bounded adaptive interval certification, P43."""
import json
from fractions import Fraction
import mpmath as mp
from certified_theta import theta_sites, evaluate, tail_bound

def exact_spd(Y, lower):
    if len(Y)!=3: raise ValueError('Y must have three entries')
    a,b,d=map(Fraction,Y); t=Fraction(lower)
    if t<=0 or a-t<=0 or (a-t)*(d-t)-b*b<=0:
        raise ValueError('not proved Y > lower*I > 0')
    return a,b,d,t

def adaptive(n,A,B,Y,lower,epsilon='1e-8',max_k=3,dps=35):
    exact_spd(Y,lower)
    if n<1 or max_k<0 or dps<20: raise ValueError('invalid dimensions or budget')
    eps=Fraction(epsilon)
    if eps<=0: raise ValueError('epsilon must be positive')
    mp.iv.dps=dps
    for k in range(max_k+1):
        tail=tail_bound(n,k,lower)
        if tail.b>mp.iv.mpf(str(eps.numerator))/eps.denominator: continue
        vals=theta_sites(k,Y)
        delta=evaluate(n,A,vals)-evaluate(n,B,vals)
        lo=delta.a-tail.b;hi=delta.b+tail.b
        if hi<0: status='CERTIFIED_NEGATIVE'
        elif lo>0:status='CERTIFIED_POSITIVE'
        else:status='INCONCLUSIVE'
        return dict(status=status,K=k,interval=[str(lo),str(hi)],tail_upper=str(tail.b),epsilon=str(eps),exact_spd=True)
    return dict(status='BUDGET_EXHAUSTED',max_k=max_k,epsilon=str(eps),exact_spd=True)

if __name__=='__main__':
    A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
    B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
    Y=['1.1','.23','1.3']; lower='.949'
    cases=[('positive',2,[],[(0,1)],'1e-8',2),('negative',7,A,B,'1e-12',3),('equal',1,[],[],'1e-8',2),('budget',7,A,B,'1e-50',1)]
    for name,n,a,b,eps,k in cases:
        print(json.dumps({'case':name,**adaptive(n,a,b,Y,lower,eps,k)},sort_keys=True),flush=True)
    for label,y,l in [('boundary',['1','1','1'],'.1'),('badlower',['1','.2','1'],'1.1')]:
        try:exact_spd(y,l);print('ERROR: invalid accepted',label)
        except ValueError:print(json.dumps({'case':label,'status':'REJECTED_EXACTLY'}),flush=True)
