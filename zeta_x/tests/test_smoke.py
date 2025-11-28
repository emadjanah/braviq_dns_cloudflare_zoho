# tests/test_smoke.py
from zeta_engine import ZetaEngine
from main import load_config


def test_engine_boot():
    config = load_config()
    engine = ZetaEngine(config)
    assert engine is not None
