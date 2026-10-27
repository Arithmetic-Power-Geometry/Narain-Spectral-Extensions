"""P49: end-to-end P44 total-width certification with exact rational eigenvalue optimization."""
from fractions import Fraction as F
from time import perf_counter
import json
from total_error import certify

def optimized_lower(Y,bits=40):
    a,b,d=map(F,Y)
    if a<=0 or a*d<=b*b: raise ValueError('Y is not SPD')
    lo,hi=F(0),min(a,d)
    for _ in range(bits):
        mid=(lo+hi)/2
        if a-mid>0 and (a-mid)*(d-mid)>b*b:lo=mid
        else:hi=mid
    if lo<=0:raise ValueError('no positive rational bound')
    return str(lo.numerator)+'/'+str(lo.denominator)

def run(name,n,A,B,Y,old,epsilon,max_k):
    new=optimized_lower(Y)
    for kind,lower in [('baseline',old),('optimized',new)]:
        start=perf_counter()
        result=certify(n,A,B,Y,lower,epsilon,max_k,(30,))
        print(json.dumps({'case':name,'method':kind,'lambda':lower,'elapsed_s':round(perf_counter()-start,6),'result':result},sort_keys=True),flush=True)

if __name__=='__main__':
    A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
    B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
    run('diagonal_n2',2,[],[(0,1)],['1.1','0','1.3'],'.5','1e-8',3)
    run('near_separating_n7',7,A,B,['1.1','.01','1.3'],'1.08','1e-5',2)
    run('published_n7',7,A,B,['1.1','.23','1.3'],'.949','1e-12',3)
