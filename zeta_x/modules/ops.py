# modules/ops.py
from datetime import datetime
from typing import Any, Dict

from core.logger import get_logger

log = get_logger(__name__)


def register(registry, storage, config: Dict[str, Any]) -> None:
    registry.register("ops", "plan_visit", lambda **kw: plan_visit(storage, **kw))


def plan_visit(storage, country: str, city: str, purpose: str) -> Dict[str, Any]:
    """
    تخطيط بسيط لزيارة ميدانية – يمكن توسيعه لعمليات كاملة.
    """
    plan = {
        "module": "ops",
        "action": "plan_visit",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "country": country,
        "city": city,
        "purpose": purpose,
        "steps": [
            "Collect diplomatic & business contacts",
            "Prepare company profile & offer set",
            "Schedule meetings with key players",
            "Define risk & fallback scenarios",
        ],
    }
    storage.append_record(plan)
    log.info(f"[OPS] visit plan created for {city}, {country}")
    return plan
