import itertools,collections,json
n=7
base=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6)]
L=base+[(0,5),(1,3),(1,5)];R=base+[(5,6)]
def idx(i,j):
 if i>j:i,j=j,i
 return j*(j-1)//2+i
def encode(E):return sum(1<<idx(i,j) for i,j in E)
def adj(M):
 a=[0]*n
 for j in range(n):
  for i in range(j):
   if M>>idx(i,j)&1:a[i]|=1<<j;a[j]|=1<<i
 return a
def lc(M,v):
 a=adj(M);neigh=[i for i in range(n) if a[v]>>i&1]
 for i,j in itertools.combinations(neigh,2):M^=1<<idx(i,j)
 return M
def canon(M):
 a=adj(M);best=(1<<21)
 for p in itertools.permutations(range(n)):
  k=0
  for j in range(n):
   for i in range(j):
    if a[p[i]]>>p[j]&1:k|=1<<idx(i,j)
  if k<best:best=k
 return best
def orbit(E):
 st=canon(encode(E));seen={st};queue=collections.deque([st]);steps=0
 while queue:
  m=queue.popleft();a=adj(m)
  for j in range(n):
   for i in range(j):
    if a[i]>>j&1:
     t=canon(lc(lc(lc(m,i),j),i));steps+=1
     if t not in seen:seen.add(t);queue.append(t)
 return seen,steps
A,ea=orbit(L);B,eb=orbit(R)
assert not(A&B)
print(json.dumps({'left_ELC_class_size':len(A),'right_ELC_class_size':len(B),'left_edges_checked':ea,'right_edges_checked':eb,'intersection_size':len(A&B),'non_T_equivalent_within_graph_code_ELC':True,'class_sizes_match_published_unordered':sorted([len(A),len(B)])==[9,10]},sort_keys=True))
