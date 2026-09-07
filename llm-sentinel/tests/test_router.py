from sentinel.routing.router import route_request


def test_high_risk_uses_fallback():
    result = route_request("CRITICAL", 0.70)
    assert result.route == "fallback"


def test_low_risk_uses_primary():
    result = route_request("LOW", 0.95)
    assert result.route == "primary"
