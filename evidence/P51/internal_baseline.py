"""P51 internal baseline: direct word-pair evaluation vs exact monomial aggregation."""
import sys, time, json, importlib.util, importlib.metadata
from collections import Counter
sys.path.insert(0,'/mnt/data/p42')
from certified_theta import graph_words, theta_sites, evaluate, iv

def aggregate(n,edges):
    w=list(graph_words(n,edges)); out=Counter()
    for u in w:
        for v in w:
            c=[0]*16
            for a,b in zip(u,v): c[a*4+b]+=1
            out[tuple(c)]+=1
    return out

def poly_eval(poly,vals):
    out=iv.mpf(0)
    for powers,count in poly.items():
        term=iv.mpf(count)
        for i,k in enumerate(powers):
            if k:term*=vals[i]**k
        out+=term
    return out

A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
iv.dps=30
print(json.dumps({'environment':{'python':sys.version.split()[0],'mpmath':importlib.metadata.version('mpmath'),'flint_python':importlib.util.find_spec('flint') is not None},'scope':'internal baseline only; no FLINT benchmark'}),flush=True)
for name,n,edges in [('n2_empty',2,[]),('n4_oneedge',4,[(0,1)]),('n7_A',7,A),('n7_B',7,B)]:
    t=time.perf_counter();p=aggregate(n,edges);agg=time.perf_counter()-t
    vals=theta_sites(1,['1.1','.23','1.3'])
    t=time.perf_counter();direct=evaluate(n,edges,vals);td=time.perf_counter()-t
    t=time.perf_counter();pol=poly_eval(p,vals);tp=time.perf_counter()-t
    overlaps=not(direct.b<pol.a or pol.b<direct.a)
    print(json.dumps({'case':name,'n':n,'word_pairs':4**n,'unique_monomials':len(p),'aggregation_s':round(agg,6),'direct_s':round(td,6),'polynomial_s':round(tp,6),'overlap':overlaps,'direct_interval':str(direct),'polynomial_interval':str(pol)}),flush=True)
    assert overlaps
