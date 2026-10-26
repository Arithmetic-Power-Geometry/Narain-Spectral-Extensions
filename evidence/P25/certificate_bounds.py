from fractions import Fraction as F
import json
L=F(4,5);U=F(6,5);beta=F(1,6);H=F(21,10)
assert U*H<F(8,5)**2
assert H/L<F(5,3)**2
assert F(8,5)+beta*F(5,3)<2
assert H/L<3
print(json.dumps({'L':str(L),'U':str(U),'beta':str(beta),'H':str(H),'n_squared_upper':str(H/L),'m_norm_upper':str(F(8,5)+beta*F(5,3)),'all_charges_E_below_H_have_coordinates_in_minus1_0_1':True},indent=2))
