"""Population Stability Index (PSI) implementation."""

from __future__ import annotations
import numpy as np


def psi(
    baseline: np.ndarray,
    current: np.ndarray,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Calculate PSI between two numeric distributions.

    PSI is a descriptive drift metric. It does not by itself prove that
    model quality has degraded.
    """
    baseline = np.asarray(baseline, dtype=float)
    current = np.asarray(current, dtype=float)

    if baseline.size == 0 or current.size == 0:
        raise ValueError("Both distributions must contain observations.")
    if bins < 2:
        raise ValueError("bins must be >= 2.")

    edges = np.histogram_bin_edges(baseline, bins=bins)
    if np.allclose(edges[0], edges[-1]):
        return 0.0

    baseline_counts, _ = np.histogram(baseline, bins=edges)
    current_counts, _ = np.histogram(current, bins=edges)

    baseline_pct = baseline_counts / baseline.size
    current_pct = current_counts / current.size

    baseline_pct = np.clip(baseline_pct, epsilon, None)
    current_pct = np.clip(current_pct, epsilon, None)

    return float(
        np.sum((current_pct - baseline_pct)
               * np.log(current_pct / baseline_pct))
    )
