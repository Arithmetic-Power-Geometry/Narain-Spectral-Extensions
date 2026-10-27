import itertools,collections,json,time

def graph(n,m):
 pairs=list(itertools.combinations(range(n),2));return [p for k,p in enumerate(pairs) if m>>k&1]
def adjacency(n,m):
 a=[0]*n
 for i,j in graph(n,m):a[i]|=1<<j;a[j]|=1<<i
 return a
def mask_from_adj(n,a):
 m=0;k=0
 for i in range(n):
  for j in range(i+1,n):
   if a[i]>>j&1:m|=1<<k
   k+=1
 return m
def lc(n,m,v):
 a=adjacency(n,m);ns=[i for i in range(n) if a[v]>>i&1]
 for i,j in itertools.combinations(ns,2):a[i]^=1<<j;a[j]^=1<<i
 return mask_from_adj(n,a)
def perm(n,m,p):
 a=[0]*n
 for i,j in graph(n,m):a[p[i]]|=1<<p[j];a[p[j]]|=1<<p[i]
 return mask_from_adj(n,a)
def iso_orbit(n,m,perms):return {perm(n,m,p) for p in perms}
def genus1(n,m):
 a=adjacency(n,m);cnt=collections.Counter()
 for x in range(1<<n):
  z=0
  for i in range(n):
   if x>>i&1:z^=a[i]
  c=[0,0,0]
  for i in range(n):
   s=((x>>i)&1)+2*((z>>i)&1)
   c[0 if s==0 else 2 if s==3 else 1]+=1
  cnt[tuple(c)]+=1
 return tuple(sorted(cnt.items()))
def classify(n):
 N=1<<(n*(n-1)//2);perms=list(itertools.permutations(range(n)))
 labels=[-1]*N;classes=[];start=time.monotonic()
 for seed in range(N):
  if labels[seed]!=-1:continue
  visited=set(iso_orbit(n,seed,perms));front=list(visited)
  for m in front:
   for v in range(n):
    for mm in iso_orbit(n,lc(n,m,v),perms):
     if mm not in visited:visited.add(mm);front.append(mm)
  idx=len(classes)
  for m in visited:
   assert labels[m]==-1
   labels[m]=idx
  classes.append({'representative':seed,'size':len(visited),'genus1':genus1(n,seed)})
 assert all(x>=0 for x in labels)
 groups=collections.defaultdict(list)
 for i,c in enumerate(classes):groups[c['genus1']].append(i)
 candidates=[ids for ids in groups.values() if len(ids)>1]
 print(json.dumps({'n':n,'graphs':N,'LC_permutation_classes':len(classes),'sizes':sorted([c['size'] for c in classes]),'cross_class_same_genus1_groups':len(candidates),'cross_class_candidate_pairs':sum(len(x)*(len(x)-1)//2 for x in candidates),'witnesses':[{'class_ids':x,'representatives':[graph(n,classes[i]['representative']) for i in x]} for x in candidates][:8],'seconds':round(time.monotonic()-start,4)}),flush=True)
 return classes,candidates
for n in [2,3,4,5]:classify(n)
