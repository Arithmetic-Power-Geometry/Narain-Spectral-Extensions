"""P60 independent six-vertex coarse-signature vs LC orbit audit using NetworkX atlas."""
import collections,itertools,json,time
import networkx as nx
start=time.monotonic()
graphs=[g for g in nx.graph_atlas_g() if len(g)==6]
assert len(graphs)==156
# Independent exact enumeration of graph-code vectors from NX neighbor sets.
def signature(g):
    neighbors=[set(g.neighbors(i)) for i in range(6)]
    terms=collections.Counter()
    for selected in itertools.product((0,1),repeat=6):
        counts=[0,0,0]
        for i in range(6):
            x=selected[i]
            z=sum(selected[j] for j in neighbors[i])%2
            counts[0 if (x,z)==(0,0) else 2 if (x,z)==(1,1) else 1]+=1
        terms[tuple(counts)]+=1
    assert sum(terms.values())==64
    return tuple(sorted(terms.items()))
# LC equivalence on unlabeled atlas using independent graph-isomorphism comparisons.
def lc(g,v):
    h=g.copy()
    for a,b in itertools.combinations(list(g.neighbors(v)),2):
        if h.has_edge(a,b):h.remove_edge(a,b)
        else:h.add_edge(a,b)
    return h
# canonical adjacency key under 720 vertex permutations, independent of NX isomorphism matching.
perms=list(itertools.permutations(range(6)))
def canonical(g):
    e=set(tuple(sorted(x)) for x in g.edges())
    return min(tuple(int(tuple(sorted((p[i],p[j]))) in e) for i,j in itertools.combinations(range(6),2)) for p in perms)
# More direct mapping via networkx isomorphism; assert atlas pairwise nonisomorphic.
lookup={canonical(g):i for i,g in enumerate(graphs)}
assert len(lookup)==156
parent=list(range(156))
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]];i=parent[i]
    return i
def union(a,b):
    a,b=root(a),root(b)
    if a!=b:parent[b]=a
for i,g in enumerate(graphs):
    for v in range(6):
        j=lookup[canonical(lc(g,v))]
        union(i,j)
classes=collections.defaultdict(list)
for i in range(156):classes[root(i)].append(i)
sig_classes=collections.defaultdict(set)
for i,g in enumerate(graphs):sig_classes[signature(g)].add(root(i))
cross={s:c for s,c in sig_classes.items() if len(c)>1}
print(json.dumps({'atlas_unlabeled_graphs':156,'LC_classes':len(classes),'distinct_coarse_signatures':len(sig_classes),'cross_class_signatures':len(cross),'class_unlabeled_sizes':sorted(map(len,classes.values())),'elapsed_seconds':round(time.monotonic()-start,3)},sort_keys=True))
assert len(classes)==26
assert len(sig_classes)==64
assert len(cross)==0
