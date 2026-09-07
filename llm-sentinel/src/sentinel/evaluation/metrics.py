"""Reliability metrics."""

from __future__ import annotations
import numpy as np


def bounded(value: float) -> float:
    return float(np.clip(value, 0.0, 1.0))


def reliability_score(
    quality: float,
    tool_success: float,
    error_rate: float,
    latency_ms: float,
    latency_target_ms: float = 2000.0,
) -> float:
    """Transparent baseline reliability score in [0, 1]."""
    quality = bounded(quality)
    tool_success = bounded(tool_success)
    error_rate = bounded(error_rate)

    latency_score = bounded(1.0 - latency_ms / max(latency_target_ms, 1.0))

    return float(
        0.55 * quality
        + 0.20 * tool_success
        + 0.15 * (1.0 - error_rate)
        + 0.10 * latency_score
    )
