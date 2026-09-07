"""Combined drift detection."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from .ks import ks_statistic
from .psi import psi


@dataclass(frozen=True)
class DriftResult:
    psi_score: float
    ks_statistic: float
    drift_detected: bool
    severity: str


def detect_drift(
    baseline: np.ndarray,
    current: np.ndarray,
    psi_threshold: float = 0.20,
    ks_threshold: float = 0.15,
) -> DriftResult:
    """Combine two interpretable drift signals.

    Severity is deliberately simple in v0.1. It can later be replaced by
    calibrated/streaming detection logic.
    """
    psi_score = psi(baseline, current)
    ks_score = ks_statistic(baseline, current)

    if psi_score >= 0.25 or ks_score >= 0.25:
        severity = "CRITICAL"
    elif psi_score >= psi_threshold or ks_score >= ks_threshold:
        severity = "WARNING"
    else:
        severity = "STABLE"

    return DriftResult(
        psi_score=psi_score,
        ks_statistic=ks_score,
        drift_detected=severity != "STABLE",
        severity=severity,
    )
