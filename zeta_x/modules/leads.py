# modules/leads.py
from datetime import datetime
from typing import Any, Dict, List

from core.logger import get_logger

log = get_logger(__name__)


def register(registry, storage, config: Dict[str, Any]) -> None:
    registry.register("leads", "add_lead", lambda **kw: add_lead(storage, **kw))
    registry.register("leads", "list_leads", lambda **kw: list_leads(storage, **kw))


def add_lead(storage, name: str, country: str, channel: str, notes: str = "") -> Dict[str, Any]:
    lead = {
        "module": "leads",
        "action": "add_lead",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "name": name,
        "country": country,
        "channel": channel,
        "notes": notes,
    }
    storage.append_record(lead)
    log.info(f"[LEADS] added lead: {name} ({country}) via {channel}")
    return lead


def list_leads(storage, country: str | None = None) -> List[Dict[str, Any]]:
    records = [r for r in storage.all_records() if r.get("module") == "leads"]
    if country:
        records = [r for r in records if r.get("country") == country]
    return records
