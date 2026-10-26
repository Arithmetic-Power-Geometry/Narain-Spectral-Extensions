from fractions import Fraction as F
import json,time,platform
st=time.monotonic();r=F(1,10**7)
def inv(A):
 d=len(A);Z=[list(A[i])+[F(i==j) for j in range(d)] for i in range(d)]
 for k in range(d):
  p=next(i for i in range(k,d) if Z[i][k]);Z[k],Z[p]=Z[p],Z[k];v=Z[k][k];Z[k]=[x/v for x in Z[k]]
  for i in range(d):
   if i!=k:
    v=Z[i][k];Z[i]=[x-v*y for x,y in zip(Z[i],Z[k])]
 return [z[d:] for z in Z]
def E(G,B,m,n):
 d=len(m);GI=inv(G);x=[F(m[i])+sum((B[i][j]*n[j] for j in range(d)),F(0)) for i in range(d)]
 return sum((x[i]*GI[i][j]*x[j]+F(n[i])*G[i][j]*n[j] for i in range(d) for j in range(d)),F(0))
out=[]
for d in (3,4,6):
 G=[[F(i==j) for j in range(d)] for i in range(d)];B=[[F(0) for j in range(d)] for i in range(d)]
 for i in range(d-1):G[i][i+1]=G[i+1][i]=F(1,10+i);B[i][i+1]=F(1,13+i);B[i+1][i]=-B[i][i+1]
 m=[0]*d;n=[0]*d;m[-1]=n[-1]=1
 mo=[0]*d;no=[0]*d;mo[0]=-1;no[0]=1
 cases=[]
 for name in ('central','all_entry_checkerboard','B_edge_plus','G_edge_minus','B_zero_outside_box'):
  g=[row[:] for row in G];b=[row[:] for row in B]
  if name=='all_entry_checkerboard':
   for i in range(d):
    for j in range(i,d):g[i][j]+=(-r if (i+j)%2 else r);g[j][i]=g[i][j]
    for j in range(i+1,d):b[i][j]+=(-r if (i+j)%2 else r);b[j][i]=-b[i][j]
  if name=='B_edge_plus':b[0][1]+=r;b[1][0]=-b[0][1]
  if name=='G_edge_minus':g[0][1]-=r;g[1][0]=g[0][1]
  if name=='B_zero_outside_box':b=[[F(0) for j in range(d)] for i in range(d)]
  ew=E(g,b,m,n);eo=E(g,b,mo,no)
  cases.append({'name':name,'witness_energy':str(ew),'nearest_central_opposite_charge_energy':str(eo),'difference':str(abs(ew-eo)),'separated':ew!=eo})
 out.append({'d':d,'cases':cases})
print(json.dumps({'cases':out,'runtime_seconds':round(time.monotonic()-st,3),'python':platform.python_version()},indent=2))
