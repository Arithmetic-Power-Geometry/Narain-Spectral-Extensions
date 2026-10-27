import networkx as nx, itertools, json, time
start=time.monotonic()
atlas=[g for g in nx.graph_atlas_g() if len(g)==6]
assert len(atlas)==156
seen=set(); classes=[]
for i,g in enumerate(atlas):
 if i in seen:continue
 q=[i]; seen.add(i);orbit=[]
 for j in q:
  orbit.append(j)
  h=atlas[j]
  for v in h.nodes:
   k=h.copy()
   nb=list(k.neighbors(v))
   for a,b in itertools.combinations(nb,2):
    if k.has_edge(a,b):k.remove_edge(a,b)
    else:k.add_edge(a,b)
   hits=[z for z,x in enumerate(atlas) if nx.is_isomorphic(k,x)]
   assert len(hits)==1
   z=hits[0]
   if z not in seen:seen.add(z);q.append(z)
 classes.append(orbit)
assert len(seen)==156
print(json.dumps({'atlas_unlabeled_graphs':156,'LC_classes':len(classes),'class_unlabeled_sizes':sorted(map(len,classes)),'elapsed_s':round(time.monotonic()-start,3)}))
