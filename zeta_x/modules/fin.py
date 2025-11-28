# modules/fin.py
from datetime import datetime
from typing import Any, Dict

from core.logger import get_logger

log = get_logger(__name__)


def register(registry, storage, config: Dict[str, Any]) -> None:
    registry.register("fin", "simple_margin", lambda **kw: simple_margin(storage, **kw))


def simple_margin(storage, exw_cost: float, freight: float, misc: float, sale_price: float) -> Dict[str, Any]:
    total_cost = exw_cost + freight + misc
    margin = sale_price - total_cost
    margin_pct = (margin / sale_price) * 100 if sale_price else 0

    result = {
        "module": "fin",
        "action": "simple_margin",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "exw_cost": exw_cost,
        "freight": freight,
        "misc": misc,
        "sale_price": sale_price,
        "total_cost": total_cost,
        "margin": margin,
        "margin_pct": round(margin_pct, 2),
    }
    storage.append_record(result)
    log.info(f"[FIN] margin calculation: {margin} ({margin_pct:.2f}%)")
    return result
