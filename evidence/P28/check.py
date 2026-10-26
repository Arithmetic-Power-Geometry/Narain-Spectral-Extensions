import sympy as s,json,time
start=time.perf_counter();out=[]
for d in [2,3,4,6,10,16]:
 G=s.eye(d);B=s.zeros(d)
 for i in range(d-1):
  G[i,i+1]=G[i+1,i]=s.Rational(1,10+i)
  B[i,i+1]=s.Rational(1,13+i);B[i+1,i]=-B[i,i+1]
 r=s.Rational(1,10000*d*(d+8))
 D=s.ones(d);C=s.zeros(d)
 for i in range(d):
  for j in range(d):
   if i<j:C[i,j]=1;C[j,i]=-1
 Gp=G+r*D;Bp=B+r*C;A=Gp.inv()
 maxp=max(A[i,i] for i in range(d))
 maxw=max(1+(Bp[:,i].T*A*Bp[:,i])[0] for i in range(d))
 maxc=max(2-2*Gp[i,i+1]+((Bp[:,i]-Bp[:,i+1]).T*A*(Bp[:,i]-Bp[:,i+1]))[0] for i in range(d-1))
 assert max(maxp,maxw,maxc)<2-50*d*r
 out.append({'d':d,'r':str(r),'max_witness_below_lower_bound':True,'gap_to_2lambda_lower_bound':str(2-50*d*r-max(maxp,maxw,maxc))})
print(json.dumps({'tests':out,'runtime_seconds':round(time.perf_counter()-start,3)},indent=2))
