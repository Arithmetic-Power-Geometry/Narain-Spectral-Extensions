from collections import Counter
from itertools import product
import json
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
def words(edges):
 a=[0]*7
 for i,j in edges:a[i]^=1<<j;a[j]^=1<<i
 out=[]
 for x in range(128):
  z=0
  for i in range(7):
   if x>>i&1:z^=a[i]
  out.append(tuple((x>>i&1)+2*(z>>i&1) for i in range(7)))
 return out
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
lookup={a+4*b:i for i,grp in enumerate(classes) for a,b in grp}
assert len(lookup)==16
def polynomial(edges):
 w=words(edges);c=Counter()
 for u,v in product(w,repeat=2):
  ex=[0]*10
  for a,b in zip(u,v):ex[lookup[a+4*b]]+=1
  c[tuple(ex)]+=1
 return c
p=polynomial(A);q=polynomial(B);dif={k:p[k]-q[k] for k in p.keys()|q.keys() if p[k]!=q[k]}
assert sum(p.values())==sum(q.values())==16384
print(json.dumps({'left_monomials':len(p),'right_monomials':len(q),'different_monomials':len(dif),'equal_refined_polynomials':p==q,'first_positive':next(((list(k),v) for k,v in sorted(dif.items()) if v>0),None),'first_negative':next(((list(k),v) for k,v in sorted(dif.items()) if v<0),None)},sort_keys=True))
