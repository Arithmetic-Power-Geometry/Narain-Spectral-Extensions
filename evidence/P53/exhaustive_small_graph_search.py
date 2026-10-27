"""P53 exhaustive n<=4 simple labeled graph code enumerator collision search."""
import itertools,collections,json,sys
sys.path[:0]=['/mnt/data/p44','/mnt/data/p42']
from total_error import certify

def invariants(n,mask,pairs):
    edges=[e for k,e in enumerate(pairs) if mask>>k&1]
    adj=[0]*n
    for i,j in edges:adj[i]^=1<<j;adj[j]^=1<<i
    W=[]
    for x in range(1<<n):
        z=0
        for i in range(n):
            if x>>i&1:z^=adj[i]
        W.append(tuple((x>>i&1)+2*(z>>i&1) for i in range(n)))
    g=collections.Counter((w.count(0),w.count(1)+w.count(2),w.count(3)) for w in W)
    p=collections.Counter(tuple(sum(1 for a,b in zip(u,v) if 4*a+b==k) for k in range(16)) for u in W for v in W)
    return edges,g,p

for n in range(2,5):
    pairs=list(itertools.combinations(range(n),2));groups={};collisions=0;distinct=0;first=None
    for mask in range(1<<len(pairs)):
        edges,g,p=invariants(n,mask,pairs);key=tuple(sorted(g.items()))
        if key in groups:
            collisions+=1
            old_mask,old_edges,old_p=groups[key]
            if p!=old_p:
                distinct+=1
                if first is None:
                    first=(old_mask,mask,old_edges,edges,sum(p[k]!=old_p[k] for k in set(p)|set(old_p)))
        else:groups[key]=(mask,edges,p)
    print(json.dumps({'n':n,'labeled_graphs':1<<len(pairs),'coarse_genus1_collision_against_first':collisions,'different_formal_genus2_against_first':distinct,'first_witness':first}),flush=True)
    if n==4 and first:
        _,_,A,B,_=first
        result=certify(n,A,B,['1.1','.23','1.3'],'.949','1e-9',3,(30,))
        print(json.dumps({'case':'n4_formal_witness_physical_theta_test','Y':['1.1','.23','1.3'],'result':result}),flush=True)
