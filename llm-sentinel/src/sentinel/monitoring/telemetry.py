"""Telemetry data structures."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class TelemetryEvent:
    request_id: str
    timestamp: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    quality: float
    tool_success: float
    error_rate: float

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens
