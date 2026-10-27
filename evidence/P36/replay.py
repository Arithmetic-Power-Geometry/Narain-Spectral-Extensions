import itertools, collections, json
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
lookup={(a,b):i for i,cl in enumerate(classes) for a,b in cl}
factor=[(0,0),(0,1),(1,0),(1,1),(0,2),(2,0),(2,2),(1,2),(2,1),(2,2)]
def words(E):
 a=[0]*7
 for i,j in E:a[i]^=1<<j;a[j]^=1<<i
 for x in range(128):
  z=0
  for i in range(7):
   if x>>i&1:z^=a[i]
  yield tuple((x>>i&1)+2*(z>>i&1) for i in range(7))
def enumerator(E):
 w=list(words(E));c=collections.Counter();f=collections.Counter()
 for u,v in itertools.product(w,repeat=2):
  ex=[0]*10;exf=[0]*6
  for x,y in zip(u,v):
   j=lookup[(x,y)];ex[j]+=1;exf[factor[j][0]]+=1;exf[3+factor[j][1]]+=1
  c[tuple(ex)]+=1;f[tuple(exf)]+=1
 return c,f
p,fp=enumerator(A);q,fq=enumerator(B)
assert sum(p.values())==sum(q.values())==16384
assert p!=q and fp==fq
print(json.dumps({'genus_two_refined_equal':p==q,'different_monomials':sum(p[k]!=q[k] for k in p.keys()|q.keys()),'separating_factorization_equal':fp==fq,'separating_monomials':len(fp),'pair_count_each':sum(p.values()),'physical_theta_nonzero_certified':False},sort_keys=True))
