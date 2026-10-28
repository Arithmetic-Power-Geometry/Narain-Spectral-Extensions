"""P58: exact six-vertex graph-signature and LC/permutation union-find search."""
import itertools,collections,json,time
n=6
pairs=list(itertools.combinations(range(n),2));N=1<<len(pairs)
def adj(m):
 a=[0]*n
 for k,(i,j) in enumerate(pairs):
  if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
 return a
def sig(m):
 a=adj(m);out=collections.Counter()
 for x in range(1<<n):
  z=0
  for i in range(n):
   if x>>i&1:z^=a[i]
  c=[0,0,0]
  for i in range(n):
   s=((x>>i)&1)+2*((z>>i)&1)
   c[0 if s==0 else 2 if s==3 else 1]+=1
  out[tuple(c)]+=1
 return tuple(sorted(out.items()))
def lc(m,v):
 a=adj(m);ne=[i for i in range(n) if a[v]>>i&1];bits=m
 for i,j in itertools.combinations(ne,2):bits^=1<<pairs.index((i,j))
 return bits
def perm(m,p):
 aa=adj(m);b=[0]*n
 for i in range(n):
  for j in range(i+1,n):
   if aa[i]>>j&1:b[p[i]]|=1<<p[j];b[p[j]]|=1<<p[i]
 return sum(1<<k for k,(i,j) in enumerate(pairs) if (b[i]>>j&1) or (b[j]>>i&1))
start=time.monotonic();groups=collections.defaultdict(list)
for m in range(N):groups[sig(m)].append(m)
print(json.dumps({'phase':'signatures','graphs':N,'distinct_signatures':len(groups),'collision_signature_groups':sum(len(g)>1 for g in groups.values()),'largest_group':max(map(len,groups.values())),'elapsed':round(time.monotonic()-start,3)}),flush=True)
parent=list(range(N));rank=[0]*N
def root(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
def union(a,b):
 a=root(a);b=root(b)
 if a==b:return
 if rank[a]<rank[b]:a,b=b,a
 parent[b]=a
 if rank[a]==rank[b]:rank[a]+=1
swaps=[tuple((j if i==j-1 else j-1 if i==j else i) for i in range(n)) for j in range(1,n)]
for m in range(N):
 for v in range(n):union(m,lc(m,v))
 for p in swaps:union(m,perm(m,p))
print(json.dumps({'phase':'equivalence_union','elapsed':round(time.monotonic()-start,3)}),flush=True)
classes=collections.Counter(root(m) for m in range(N));cross=[];cross_pairs=0
for s,ms in groups.items():
 by=collections.defaultdict(list)
 for m in ms:by[root(m)].append(m)
 if len(by)>1:
  ids=sorted(by)
  cross_pairs+=sum(len(by[a])*len(by[b]) for a,b in itertools.combinations(ids,2))
  cross.append((s,by))
print(json.dumps({'phase':'final','n':n,'graphs':N,'classes':len(classes),'distinct_signatures':len(groups),'cross_class_signature_groups':len(cross),'cross_class_graph_pairs':cross_pairs,'elapsed':round(time.monotonic()-start,3)}),flush=True)
if cross:
 s,by=cross[0];ids=sorted(by);a,b=by[ids[0]][0],by[ids[1]][0]
 print(json.dumps({'phase':'first_witness','masks':[a,b],'edges':[[pairs[k] for k in range(len(pairs)) if m>>k&1] for m in [a,b]],'signature':[[list(k),v] for k,v in s],'class_sizes':[classes[ids[0]],classes[ids[1]]]}),flush=True)
