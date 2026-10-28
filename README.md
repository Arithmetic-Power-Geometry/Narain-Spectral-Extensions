# Narain spectral and graph-code verification

Reproducibility code for the numerical and finite combinatorial calculations in:

Akhtar, M. A. K. (2026). *Exact Certificates and Falsification Controls for Narain Spectra, Graph Codes, and Integral Lattice Splitting* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23732752

## Requirements

Python 3; networkx, sympy, mpmath for the respective independent graph, exact-symbolic, and interval calculations. Other scripts use the Python standard library.

## Reproduction

- `python code/verify_n6.py`: exhaustive 32,768 labelled six-vertex graph classification (26 classes, 64 signatures, zero cross-class signature overlap).
- `python code/independent_n6.py`: independent atlas check on 156 nonisomorphic graphs.
- `python code/graph_small.py`: exact small-graph classification.
- `python code/lc_noninvariance.py`: local-complementation counterexamples.
- `python code/graph_code_enumerator.py`, `python code/two_copy_enumerator.py`, `python code/genus_two_refinement.py`, `python code/separating_specialization.py`: code-enumerator and refinement calculations.
- `python code/certified_gaussian.py`: interval enclosure of the implemented Gaussian sum; not a proof of fully normalized physical CFT inequivalence.
- `python code/verify_parameter_box.py`: exact checks for the stated non-splitting parameter bounds.
- `python code/spectral_control.py`: rational spectral calculation.

These programs support specified computations; not every result in the paper has an independently reproducible implementation here. The reported graph signatures are not local-complementation invariants. The seven-vertex comparison reproduces a previously published pair.

## License

Apache License 2.0. Copyright © 2026 Mohammad Amir Khusru Akhtar. See LICENSE.

## Citation

Akhtar, M. A. K. (2026). Exact Certificates and Falsification Controls for Narain Spectra, Graph Codes, and Integral Lattice Splitting (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23732752
