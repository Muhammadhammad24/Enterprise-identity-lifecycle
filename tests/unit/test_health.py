import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from utils import health

def test_health_ok():
    assert health.health() == {"status": "ok"}
