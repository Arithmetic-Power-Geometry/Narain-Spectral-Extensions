# P05 negative test and correction
Initial exact run raised AssertionError at the claimed leading coefficient for T3.
Cause: collections.Counter subtraction discards zero and negative values, invalid for signed multiplicity differences.
Original erroneous expression: delta=p-q
Corrected expression: delta={key:p[key]-q[key] for key in p.keys()|q.keys()}
After correction: PASS for T3/T4/T6. This is an implementation failure, not a failure of the theorem.
Adversarial factor swap: A⊗B vs B⊗A has identical graded spectrum, showing common-spectator assumption cannot be dropped.
Formal signed spectator with zero vacuum term annihilates the leading coefficient; not a physical positive-degeneracy example.
