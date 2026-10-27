"""P52: independent exact-integer separating specialization audit and external baseline availability."""
import json, importlib.util, sys
from collections import Counter
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
def words(edges,n=7):
    adj=[0]*n
    for i,j in edges:adj[i]^=1<<j;adj[j]^=1<<i
    for x in range(1<<n):
        z=0
        for i in range(n):
            if x&(1<<i):z^=adj[i]
        yield tuple((x>>i&1)+2*(z>>i&1) for i in range(n))
def poly(edges):
    W=list(words(edges));p=Counter()
    for u in W:
        for v in W:
            counts=[0]*16
            for x,y in zip(u,v):counts[4*x+y]+=1
            p[tuple(counts)]+=1
    return p
def marginal(p):
    out=Counter()
    for ex,coeff in p.items():
        # Genus-two variables specialize to independent genus-one variables
        # t_{a,b} -> x_a*y_b, so only 4+4 marginal exponent counts survive.
        classes=((0,),(1,2),(3,))
        x=tuple(sum(ex[4*a+b] for a in cl for b in range(4)) for cl in classes)
        y=tuple(sum(ex[4*a+b] for a in range(4) for b in cl) for cl in classes)
        out[(x,y)]+=coeff
    return out
def genus1(edges):
    out=Counter()
    for w in words(edges):
        out[(w.count(0),w.count(1)+w.count(2),w.count(3))]+=1
    return out
p,q=poly(A),poly(B);ma,mb=marginal(p),marginal(q)
ga,gb=genus1(A),genus1(B)
assert ga==gb
assert ma==mb
expected=Counter({(x,y):cx*cy for x,cx in ga.items() for y,cy in ga.items()})
assert ma==expected
assert p!=q
print(json.dumps({'status':'PASS','graph_a_monomials':len(p),'graph_b_monomials':len(q),'genus2_union_monomials':len(set(p)|set(q)),'different_coefficients':sum(p[k]!=q[k] for k in set(p)|set(q)),'genus1_monomials':len(ga),'separating_monomials':len(ma),'separating_exact_equality':True,'factorization_exact':True,'flint_available':importlib.util.find_spec('flint') is not None,'python':sys.version.split()[0]},sort_keys=True))
