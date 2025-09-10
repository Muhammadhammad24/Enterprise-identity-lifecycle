from utils import health

def test_health_ok():
    assert health.health() == {"status": "ok"}
