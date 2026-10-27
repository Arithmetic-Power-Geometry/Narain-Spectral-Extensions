import itertools,json,collections,hashlib
A=[(0,1),(0,3),(1,2)]
B=[(0,2),(0,3),(1,2),(1,3)]
n=4

def mask(edges):return sum(1<<(i*n+j) for i,j in edges for _ in [0])+sum(1<<(j*n+i) for i,j in edges)
def edges(m):return [(i,j) for i in range(n) for j in range(i+1,n) if (m>>(i*n+j))&1]
def permute(m,p):return mask([(p[i],p[j]) for i,j in edges(m)])
def canon(m):return min(permute(m,p) for p in itertools.permutations(range(n)))
def lc(m,v):
 e=set(edges(m));nbr=[u for u in range(n) if (m>>(v*n+u))&1]
 for i,j in itertools.combinations(nbr,2):
  k=tuple(sorted((i,j)))
  if k in e:e.remove(k)
  else:e.add(k)
 return mask(e)
ma,mb=mask(A),mask(B)
iso=canon(ma)==canon(mb)
q=collections.deque([ma]);seen={ma};path={ma:None};found=None
while q:
 m=q.popleft()
 if canon(m)==canon(mb):found=m;break
 for v in range(n):
  nxt=lc(m,v)
  if nxt not in seen:seen.add(nxt);path[nxt]=(m,v);q.append(nxt)
steps=[]
if found is not None:
 cur=found
 while path[cur] is not None:
  prev,v=path[cur];steps.append({'vertex':v,'from':edges(prev),'to':edges(cur)});cur=prev
 steps.reverse()
perm=next((list(p) for p in itertools.permutations(range(n)) if permute(found,p)==mb),None) if found is not None else None
assert perm is not None if found is not None else True
print(json.dumps({'A':A,'B':B,'isomorphic':iso,'LC_equivalent_up_to_permutation':found is not None,'visited_labeled_graphs':len(seen),'LC_steps':steps,'final_permutation':perm,'final_edges':edges(found) if found is not None else None},sort_keys=True))
