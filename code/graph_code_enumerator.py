import itertools,json,time
from collections import Counter
start=time.perf_counter()
def enumerator(n,edges):
 adj=[0]*n
 for i,j in edges:adj[i]^=1<<j;adj[j]^=1<<i
 out=Counter()
 for mask in range(1<<n):
  z=0
  for i in range(n):
   if mask>>i&1:z^=adj[i]
  counts=[0,0,0,0]
  for i in range(n):counts[((mask>>i)&1)+2*((z>>i)&1)]+=1
  out[tuple(counts)]+=1
 assert sum(out.values())==2**n
 return out
n=4;pairs=list(itertools.combinations(range(n),2));perms=list(itertools.permutations(range(n)))
def canon(E):
 return min(tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in E)) for p in perms)
reps={}
for bits in range(1<<len(pairs)):
 E=tuple(pairs[k] for k in range(len(pairs)) if bits>>k&1)
 key=canon(E);reps.setdefault(key,E)
by_enum={}
for E in sorted(reps):
 signature=tuple(sorted(enumerator(n,E).items()))
 by_enum.setdefault(signature,[]).append(E)
collisions=[v for v in by_enum.values() if len(v)>1]
print(json.dumps({'n':n,'labelled_graphs':64,'unlabelled_graphs':len(reps),'enumerator_collision_classes':len(collisions),'collisions':collisions,'elapsed_seconds':round(time.perf_counter()-start,6)},indent=2))
