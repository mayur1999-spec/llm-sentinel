"""Policy-based adaptive model router."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class RouteDecision:
    route: str
    reason: str


def route_request(
    risk_level: str,
    estimated_quality: float,
    primary_model: str = "primary",
    fallback_model: str = "fallback",
) -> RouteDecision:
    """Route high-risk traffic to a fallback.

    This is a deterministic policy, not a learned router yet.
    """
    if risk_level == "CRITICAL" or estimated_quality < 0.80:
        return RouteDecision(
            route=fallback_model,
            reason="High reliability risk; fallback policy activated.",
        )

    return RouteDecision(
        route=primary_model,
        reason="Reliability within current policy limits.",
    )
