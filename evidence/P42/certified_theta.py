"""Generic interval enclosure for graph-code genus-two Gaussian sums, with conservative tails."""
import itertools, json, argparse, time
import mpmath as mp
iv=mp.iv

def graph_words(n, edges):
    adj=[0]*n
    for i,j in edges:
        assert 0<=i<j<n
        adj[i]^=1<<j;adj[j]^=1<<i
    for x in range(1<<n):
        z=0
        for i in range(n):
            if x>>i&1:z^=adj[i]
        yield tuple((x>>i&1)+2*(z>>i&1) for i in range(n))

def theta_sites(K, Y):
    y0,y01,y1=map(iv.mpf,Y)
    vals=[]
    for p,q in itertools.product(range(4),repeat=2):
        al=(p&1,q&1);be=(p>>1,q>>1);acc=iv.mpf(0)
        for a0,a1,b0,b1 in itertools.product(range(-K,K+1),repeat=4):
            l0=iv.mpf(a0+b0)+iv.mpf(al[0]+be[0])/2
            l1=iv.mpf(a1+b1)+iv.mpf(al[1]+be[1])/2
            r0=iv.mpf(a0-b0)+iv.mpf(al[0]-be[0])/2
            r1=iv.mpf(a1-b1)+iv.mpf(al[1]-be[1])/2
            e=y0*(l0*l0+r0*r0)+y1*(l1*l1+r1*r1)+2*y01*(l0*l1+r0*r1)
            acc+=iv.exp(-iv.pi*e)
        vals.append(acc)
    return vals

def evaluate(n,edges,vals):
    w=list(graph_words(n,edges));out=iv.mpf(0)
    for u in w:
        for v in w:
            t=iv.mpf(1)
            for a,b in zip(u,v):t*=vals[a*4+b]
            out+=t
    return out

def tail_bound(n,K,lam):
    c=2*iv.pi*iv.mpf(lam)
    S=1+2*iv.exp(-c/4)/(1-iv.exp(-c))
    T=2*iv.exp(-c*(K+iv.mpf('.5'))**2)/(1-iv.exp(-2*c*(K+iv.mpf('.5'))))
    return 2*(1<<(2*n))*n*4*T*S**3*(S**4)**(n-1)

def certify(n,A,B,Y,lam,K=2,dps=35):
    iv.dps=dps
    y0,y01,y1=map(mp.mpf,Y);lo=mp.mpf(lam)
    assert n>=1 and K>=0 and lo>0 and y0>lo and y1>lo
    # Sylvester test: Y-lambda*I positive definite; rational decimal inputs are exactly represented.
    assert (y0-lo)*(y1-lo)>y01*y01
    vals=theta_sites(K,Y);a=evaluate(n,A,vals);b=evaluate(n,B,vals);delta=a-b;tail=tail_bound(n,K,lam)
    if delta.b+tail.b<0:status='CERTIFIED_NEGATIVE'
    elif delta.a-tail.b>0:status='CERTIFIED_POSITIVE'
    else:status='INCONCLUSIVE'
    return dict(n=n,K=K,Y=Y,lambda_lower=lam,dps=dps,graph_a_edges=len(A),graph_b_edges=len(B),difference=str(delta),tail_upper=str(tail.b),status=status)

if __name__=='__main__':
    A=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(0,5),(1,3),(1,5)]
    B=[(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(2,4),(3,4),(4,5),(4,6),(5,6)]
    Y=['1.1','.23','1.3'];lam='.949';cases=[(1,[],[],2),(2,[],[(0,1)],2),(4,[],[(0,1)],2),(7,A,A,2),(7,A,B,3)]
    start=time.monotonic()
    for n,a,b,k in cases:
        print(json.dumps(certify(n,a,b,Y,lam,k),sort_keys=True),flush=True)
    print(json.dumps({'elapsed_internal_seconds':round(time.monotonic()-start,3),'cases':len(cases)}),flush=True)
