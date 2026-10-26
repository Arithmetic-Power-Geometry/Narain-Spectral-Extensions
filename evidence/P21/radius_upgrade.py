from fractions import Fraction as F
import json,time,platform
st=time.monotonic()
r=F(1,10**7);L0=F(89,110);U0=F(131,110);beta0=F(27,182)
case=[(3,F(3),F(15336,98369999),F(581846,582071)),(4,F(5,2),F(5324,20446075),F(4715663,9436650)),(6,F(5,2),F(115293091512,301956721567111),F(1786152037333,3573452326238))]
rows=[]
for d,H,gap,margin in case:
 L=L0-d*r;U=U0+d*r;beta=beta0+d*r
 mlimit=H*U+beta*beta*H/L+4*beta*H
 ncap=H//L;mcap=(mlimit.numerator-1)//mlimit.denominator
 drift=160*d*r
 assert L>F(1,2) and U<4*L and beta<1 and ncap==3 and mcap==({3:5,4:4,6:4}[d])
 assert 2*drift<gap and drift<margin
 rows.append({'d':d,'radius':str(r),'ncap':int(ncap),'mcap':int(mcap),'L':str(L),'U':str(U),'beta':str(beta),'gap':str(gap),'twice_drift':str(2*drift),'margin':str(margin),'all_checks':True})
print(json.dumps({'radius':str(r),'cases':rows,'runtime_seconds':round(time.monotonic()-st,6),'python':platform.python_version()},indent=2))
