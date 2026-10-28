from collections import Counter
from itertools import product
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
def words(edges):
 adj=[0]*7
 for i,j in edges:adj[i]^=1<<j;adj[j]^=1<<i
 out=[]
 for x in range(128):
  z=0
  for i in range(7):
   if x>>i&1:z^=adj[i]
  out.append(tuple((x>>i&1)+2*(z>>i&1) for i in range(7)))
 return out
def poly(w):
 c=Counter()
 for u,v in product(w,repeat=2):
  h=[0]*16
  for x,y in zip(u,v):h[x+4*y]+=1
  c[tuple(h)]+=1
 return c
P=poly(words(A));Q=poly(words(B))
assert sum(P.values())==sum(Q.values())==16384
assert P!=Q
print('pairs_per_graph',16384)
print('left_monomials',len(P),'right_monomials',len(Q))
print('differing_monomials',sum(P[k]!=Q[k] for k in P.keys()|Q.keys()))
