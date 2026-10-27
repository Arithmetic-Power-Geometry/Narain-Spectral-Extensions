"""P56 independent exhaustive test: coarse graph-code genus-one enumerator under LC."""
import itertools,collections,json

def graph(n,m):
 pairs=list(itertools.combinations(range(n),2))
 return [p for k,p in enumerate(pairs) if m>>k&1]
def mask(n,edges):
 pairs=list(itertools.combinations(range(n),2));s=set(edges)
 return sum(1<<k for k,p in enumerate(pairs) if p in s)
def lc(n,m,v):
 e=set(graph(n,m));nb=[u for u in range(n) if u!=v and tuple(sorted((u,v))) in e]
 for a,b in itertools.combinations(nb,2):
  p=(a,b)
  if p in e:e.remove(p)
  else:e.add(p)
 return mask(n,e)
def sig(n,m):
 adj=[0]*n
 for a,b in graph(n,m):adj[a]^=1<<b;adj[b]^=1<<a
 out=collections.Counter()
 for x in range(1<<n):
  z=0
  for i in range(n):
   if x>>i&1:z^=adj[i]
  counts=[0,0,0]
  for i in range(n):
   k=((x>>i)&1)+2*((z>>i)&1)
   counts[0 if k==0 else 2 if k==3 else 1]+=1
  out[tuple(counts)]+=1
 return tuple(sorted(out.items()))
for n in range(2,6):
 total=1<<(n*(n-1)//2);fails=0;first=None
 for m in range(total):
  a=sig(n,m)
  for v in range(n):
   new=lc(n,m,v)
   if sig(n,new)!=a:
    fails+=1
    if first is None:first={'edges_before':graph(n,m),'vertex':v,'edges_after':graph(n,new),'signature_before':a,'signature_after':sig(n,new)}
 print(json.dumps({'n':n,'graphs':total,'LC_checks':total*n,'noninvariant_directed_checks':fails,'first_witness':first}),flush=True)
