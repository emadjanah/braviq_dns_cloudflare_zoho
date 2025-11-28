# modules/recon.py
from datetime import datetime
from typing import Any, Dict

from core.logger import get_logger

log = get_logger(__name__)


def register(registry, storage, config: Dict[str, Any]) -> None:
    registry.register("recon", "scan_market", lambda **kw: scan_market(storage, config, **kw))
    registry.register("recon", "summary", lambda **kw: recon_summary(storage, **kw))


def scan_market(storage, config, country: str, sector: str = "pasta") -> Dict[str, Any]:
    """
    نموذج بسيط: لاحقاً يُربط بمصادر حقيقية (OSINT / APIs / DB).
    الآن يعطي تقريراً تجريبياً لكن منظم.
    """
    log.info(f"[RECON] scanning market: country={country}, sector={sector}")

    result = {
        "module": "recon",
        "action": "scan_market",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "country": country,
        "sector": sector,
        "findings": {
            "demand_trend": "unknown (placeholder)",
            "main_importers": [],
            "risk_level": "medium",
            "notes": "This is a placeholder result. Connect real data sources here."
        }
    }

    storage.append_record(result)
    return result


def recon_summary(storage, limit: int = 5) -> Dict[str, Any]:
    records = [r for r in storage.all_records() if r.get("module") == "recon"]
    return {
        "count": len(records),
        "last_records": records[-limit:]
    }
