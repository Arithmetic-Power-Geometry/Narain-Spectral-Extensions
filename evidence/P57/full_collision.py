"""P57: exact all-member coarse genus-one signature cross-LC-class audit, n=2..5."""
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
def audit(n):
    start=time.monotonic(); N=1<<(n*(n-1)//2)
    perms=list(itertools.permutations(range(n)))
    def orbit(m): return {perm(n,m,p) for p in perms}
    labels=[-1]*N; classes=[]
    for seed in range(N):
        if labels[seed]>=0:continue
        seen=orbit(seed); queue=list(seen)
        for m in queue:
            for v in range(n):
                for z in orbit(lc(n,m,v)):
                    if z not in seen: seen.add(z);queue.append(z)
        cid=len(classes)
        for m in seen:
            assert labels[m]==-1
            labels[m]=cid
        classes.append(sorted(seen))
    assert all(x>=0 for x in labels)
    assert sum(map(len,classes))==N
    signatures=collections.defaultdict(lambda:collections.defaultdict(list))
    for m in range(N): signatures[genus1(n,m)][labels[m]].append(m)
    cross={sig:group for sig,group in signatures.items() if len(group)>1}
    pairs=sum(sum(len(group[a])*len(group[b]) for a,b in itertools.combinations(group,2)) for group in cross.values())
    example=None
    if cross:
        sig,groups=next(iter(sorted(cross.items(),key=lambda z:str(z[0]))))
        a,b=sorted(groups)[:2]; m1,m2=groups[a][0],groups[b][0]
        example={'signature':[[list(k),v] for k,v in sig],'class_ids':[a,b], 'graph_masks':[m1,m2], 'edges':[graph(n,m1),graph(n,m2)],'class_sizes':[len(classes[a]),len(classes[b])],'members_sharing_signature':[len(groups[a]),len(groups[b])]}
        assert labels[m1]!=labels[m2]
        assert genus1(n,m1)==genus1(n,m2)
    result={'n':n,'labeled_graphs':N,'LC_classes':len(classes),'distinct_signatures':len(signatures),'signatures_shared_across_classes':len(cross),'cross_class_graph_pairs_same_signature':pairs,'example':example,'elapsed_s':round(time.monotonic()-start,4)}
    print(json.dumps(result,sort_keys=True),flush=True)
    return result
if __name__=='__main__':
    for n in range(2,6):audit(n)
