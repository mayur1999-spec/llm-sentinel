"""Two-sample Kolmogorov-Smirnov drift statistic."""

from __future__ import annotations
import numpy as np


def ks_statistic(baseline: np.ndarray, current: np.ndarray) -> float:
    """Return the two-sample KS statistic without hiding the calculation."""
    baseline = np.sort(np.asarray(baseline, dtype=float))
    current = np.sort(np.asarray(current, dtype=float))

    if baseline.size == 0 or current.size == 0:
        raise ValueError("Both distributions must contain observations.")

    values = np.sort(np.concatenate([baseline, current]))
    baseline_cdf = np.searchsorted(baseline, values, side="right") / baseline.size
    current_cdf = np.searchsorted(current, values, side="right") / current.size

    return float(np.max(np.abs(baseline_cdf - current_cdf)))
