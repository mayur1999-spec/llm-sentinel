import numpy as np
from sentinel.drift.psi import psi


def test_identical_distribution_has_near_zero_psi():
    x = np.linspace(0, 1, 1000)
    assert psi(x, x) < 1e-10


def test_shifted_distribution_has_positive_psi():
    rng = np.random.default_rng(1)
    baseline = rng.normal(0, 1, 1000)
    current = rng.normal(2, 1, 1000)
    assert psi(baseline, current) > 0.2
