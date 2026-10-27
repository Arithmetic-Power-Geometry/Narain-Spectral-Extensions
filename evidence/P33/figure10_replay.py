from collections import Counter
import json
common=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6)]
left=common+[(0,5),(1,3),(1,5)]
right=common+[(5,6)]
expected={(7,0,0):1,(5,2,0):1,(4,2,1):5,(2,4,1):5,(5,0,2):1,(3,2,2):12,(1,4,2):9,(4,0,3):4,(2,2,3):22,(0,4,3):4,(3,0,4):5,(1,2,4):25,(2,0,5):11,(0,2,5):11,(1,0,6):10,(0,0,7):2}
def rep(edges):
 adj=[0]*7
 for i,j in edges:adj[i]^=1<<j;adj[j]^=1<<i
 out=Counter()
 for x in range(128):
  z=0
  for i in range(7):
   if x>>i&1:z^=adj[i]
  t=[0,0,0]
  for i in range(7):
   a=x>>i&1;b=z>>i&1
   t[0 if not(a or b) else 1 if a and b else 2]+=1
  out[tuple(t)]+=1
 return out
L=rep(left);R=rep(right)
assert L==R==expected
print(json.dumps({'n':7,'left_edges':left,'right_edges':right,'same_REP':L==R,'matches_published_equation_6_38':L==expected,'monomials':len(L),'codewords':sum(L.values())},sort_keys=True))
