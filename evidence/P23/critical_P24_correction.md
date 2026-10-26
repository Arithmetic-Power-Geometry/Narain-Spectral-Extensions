# P23 critical correction to proposed P24 shortcut

**Reject the irreducible-characteristic-polynomial shortcut in independent_audit_and_gate.md.** For every genuine Narain generalized metric Q satisfying QJQ=J (equivalently JQJ=Q^-1), the matrix S=JQ is an involution: S²=I. Its characteristic polynomial is (t-1)^d(t+1)^d and can NEVER be irreducible for d>=1. The original proposal to test irreducibility of charpoly(JQ) for T3/T4 is vacuous and must not be implemented or reported as a breakthrough.

The rational projectors (I±S)/2 always commute with S and are rational when Q is rational. Their images are J-definite (the left/right-moving eigenspaces), not hyperbolic of signature (k,k), so they do NOT produce Narain product splittings. This is a decisive adversarial counterexample to confusing rational idempotents with integral hyperbolic projectors.

Correct P24 direction: find **integral, J-selfadjoint, Q-selfadjoint idempotents with hyperbolic image**, using the two eigenspace decomposition S=±1 and arithmetic gluing/integrality constraints. Characterize rational block projectors on both definite eigenspaces and require J-isometric hyperbolic pairing and primitive unimodular integrality on the original lattice. Test exact duality-hidden product controls and T3/T4; do not infer full indecomposability from mere absence of a special bounded projector or from spectral irreducibility of JQ. A stronger obstruction may arise from the integral gluing of positive/negative rational eigensublattices, not from the minimal polynomial of S.

This correction is append-only; retain the failed proposed shortcut in the original audit as a recorded negative hypothesis.
