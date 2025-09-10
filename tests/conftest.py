import sys
from pathlib import Path

# repo root = tests/ ka parent
ROOT = Path(__file__).resolve().parent.parent
# src ko Python path me daalo
sys.path.insert(0, str(ROOT / "src"))
