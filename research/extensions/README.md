# Narain theory extensions — reproducible initial experiments

The two uploaded manuscripts address zero-mode spectral reconstruction and the exact first spin-sensitive separation for a rational two-torus. These research extensions do not replace or modify those certificates.

## Oscillator contributions

In the bosonic two-torus CFT, the formal chiral oscillator descendant factor is `P(q)=prod_{n>=1}(1-q^n)^(-2)`. The exact degeneracies for levels 0,1,2,3 are `[1,2,5,10]`. In the uploaded manuscripts' conventions, dressing at oscillator levels `N_L,N_R` adds `2(N_L+N_R)` to the energy and `N_L-N_R` to integral spin. The factor is background-independent.

The exact bounded computation establishes that dressing through levels 0..3 preserves the first energy-spin difference at `3313/1325`, with multiplicity differences 2 and -2 for spins -1 and +1. Its all-orders formal extension follows from the zero-mode first-separation theorem and the nonnegative oscillator grading; a complete string-worldsheet calculation requires further physical consistency conditions (including oscillator zero-point conventions, level matching, ghosts/projections as applicable).

## Higher dimensions

A constructive `T^6` family is `G6=diag(G0,G0,G0)` and `B6=diag(bJ,0,0)`. Its formal zero-mode theta function is `Theta(G0,b) * Theta(G0,0)^2`. A nonzero refined difference survives multiplication by the spectator factor with constant coefficient one; the first discrepancy remains at the seed threshold since spectators have nonnegative energy and a unique vacuum at zero. This is not a classification of all `O(6,6;Z)` or an extension to generic Calabi–Yau threefolds.

## Metric stability versus cosmology

The uploaded second paper proves static metric-perturbation stability on `b in [1/10,2/5]` for `max_ij |H_ij| <= 1e-4`. This package adds a finite set of exact rational spot checks at three field values and three symmetric perturbations. Such checks do not replace its continuum proof and do not say anything about Big Bang stability.

## Reproduce

```sh
python3 research/extensions/verify_extensions.py
```

The program writes `extension_results.json` next to itself, uses only the Python standard library and performs exact rational comparisons. Preserve earlier `research/sig` and `tests` certificates unchanged.

## Research gates

1. Independently rerun the original zero-mode and first-threshold exact certificates.
2. Derive the full oscillator factor in a precisely specified physical CFT, fix spin/energy/zero-point conventions and verify standard partition-function identities.
3. Generalize exact enumeration from `T^2` to genuinely coupled `T^3`, `T^4`, and `T^6`, with analytic charge bounds, comparison against existing literature and adversarial counterexample searches.
4. Treat compactification on Calabi–Yau manifolds separately: a torus product construction is not a general Calabi–Yau result.
5. Before any cosmological claim, specify a dynamical moduli action, potential, field equations, stability observable and physically justified initial conditions.
6. Preserve positive and negative test evidence append-only; verify bibliographic metadata before creating or appending academic references.

**Research status:** initial exact computational extensions PASS; all-orders physical CFT, generic higher-dimensional classification and dynamical cosmology remain OPEN.
