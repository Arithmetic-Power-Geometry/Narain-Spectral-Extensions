import sys,json,time
sys.path.insert(0,'/mnt/data/p47')
from total_error import certify
from verified_decimal import run
A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
cases={'near':(7,A,B,['1.1','.01','1.3'],'1.08',0,'1e-5'),'ill':(2,[],[(0,1)],['1','.95','1'],'.04',1,'1e-8')}
name=sys.argv[1];n,a,b,y,l,k,eps=cases[name];start=time.monotonic()
p=certify(n,a,b,y,l,eps,k,(30,));print(json.dumps({'case':name,'backend':'P44','result':p,'elapsed':time.monotonic()-start}),flush=True)
q=run(n,a,b,y,l,k);print(json.dumps({'case':name,'backend':'P46','result':q,'elapsed':time.monotonic()-start}),flush=True)
