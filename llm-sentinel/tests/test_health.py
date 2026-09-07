from sentinel.evaluation.metrics import reliability_score
from sentinel.monitoring.health import classify_risk


def test_reliability_is_bounded():
    score = reliability_score(0.9, 0.9, 0.1, 1000)
    assert 0 <= score <= 1


def test_low_reliability_is_critical():
    assert classify_risk(0.70, True) == "CRITICAL"
