#!/usr/bin/env python3
"""P09: independent logical counterexample; not a string dynamics solver."""
from fractions import Fraction as F
import json
def potential(phi,m2):return F(1,2)*m2*phi*phi
models=[]
for m2 in (F(1),F(-1),F(0)):
 assert potential(F(0),m2)==0
 models.append(dict(m2=str(m2),V0="0",Vprime0="0",Vsecond0=str(m2),behavior="stable" if m2>0 else "unstable" if m2<0 else "inconclusive"))
assert len({x["behavior"] for x in models})==3
requirements=["specified critical string model","effective action and frame","moduli kinetic metric","derived potential or sources","dilaton and gravity equations","constraints and initial data","alpha-prime and loop-control domain","observables"]
print(json.dumps(dict(gate="NO-GO_DYNAMICS",toy_countermodels=models,missing_requirements=requirements,claim="Static Narain spectra do not determine a cosmological evolution law"),indent=2))
