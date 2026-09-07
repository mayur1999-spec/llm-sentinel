import numpy as np
from sentinel.drift.ks import ks_statistic


def test_identical_distribution_has_zero_ks():
    x = np.linspace(0, 1, 100)
    assert ks_statistic(x, x) == 0.0


def test_shifted_distribution_has_positive_ks():
    baseline = np.linspace(0, 1, 1000)
    current = np.linspace(1, 2, 1000)
    assert ks_statistic(baseline, current) > 0.5
