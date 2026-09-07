"""Simple evaluation event schema."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationEvent:
    request_id: str
    quality: float
    tool_success: float
    error_rate: float
    latency_ms: float
    input_tokens: int
    output_tokens: int
