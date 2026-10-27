"""P44: certified total-width contract for graph-code Gaussian differences."""
import json
from fractions import Fraction
import mpmath as mp
from certified_theta import theta_sites, evaluate, tail_bound

def validate(n, A, B, Y, lower, epsilon, max_k, precisions):
    if type(n) is not int or n<1 or n>12: raise ValueError('n outside supported range')
    if len(Y)!=3: raise ValueError('Y needs 3 entries')
    a,b,d=map(Fraction,Y); t=Fraction(lower); eps=Fraction(epsilon)
    if t<=0 or a-t<=0 or (a-t)*(d-t)<=b*b: raise ValueError('invalid strict SPD bound')
    if eps<=0 or type(max_k) is not int or max_k<0: raise ValueError('invalid budget')
    if not precisions or any(type(p) is not int or p<20 for p in precisions): raise ValueError('invalid precisions')
    for edges in (A,B):
        if type(edges) not in (list,tuple): raise ValueError('edges must be a sequence')
        seen=set()
        for edge in edges:
            if type(edge) not in (list,tuple) or len(edge)!=2: raise ValueError('malformed edge')
            i,j=edge
            if type(i) is not int or type(j) is not int or not (0<=i<j<n) or (i,j) in seen:
                raise ValueError('invalid or duplicate edge')
            seen.add((i,j))
    return eps

def certify(n,A,B,Y,lower,epsilon='1e-8',max_k=3,precisions=(30,50)):
    eps=validate(n,A,B,Y,lower,epsilon,max_k,precisions)
    for k in range(max_k+1):
        for dps in precisions:
            mp.iv.dps=dps
            tail=tail_bound(n,k,lower)
            # Compare interval endpoints against exact rational epsilon via an interval.
            e=mp.iv.mpf(eps.numerator)/eps.denominator
            if tail.b*2>=e.a: continue
            vals=theta_sites(k,Y)
            delta=evaluate(n,A,vals)-evaluate(n,B,vals)
            lo=delta.a-tail.b;hi=delta.b+tail.b
            width=hi-lo
            if width.b<=e.a:
                status='CERTIFIED_NEGATIVE' if hi<0 else 'CERTIFIED_POSITIVE' if lo>0 else 'INCONCLUSIVE'
                return {'status':status,'K':k,'dps':dps,'interval':[str(lo),str(hi)],'total_width_upper':str(width.b),'epsilon':str(eps)}
    return {'status':'BUDGET_EXHAUSTED','max_k':max_k,'epsilon':str(eps)}

if __name__=='__main__':
    A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
    B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
    Y=['1.1','.23','1.3'];lower='.949'
    for name,n,a,b,eps,k in [('positive',2,[],[(0,1)],'1e-8',2),('negative',7,A,B,'1e-12',3),('equal',1,[],[],'1e-8',2),('exhausted',7,A,B,'1e-50',1)]:
        print(json.dumps({'case':name,**certify(n,a,b,Y,lower,eps,k)},sort_keys=True),flush=True)
    for name,n,a,b,y,l in [('duplicate',2,[(0,1),(0,1)],[],Y,lower),('selfloop',2,[(0,0)],[],Y,lower),('singular',1,[],[],['1','1','1'],'.1'),('badlower',1,[],[],Y,'2')]:
        try:certify(n,a,b,y,l);raise AssertionError('accepted '+name)
        except ValueError:print(json.dumps({'case':name,'status':'REJECTED_EXACTLY'}),flush=True)
