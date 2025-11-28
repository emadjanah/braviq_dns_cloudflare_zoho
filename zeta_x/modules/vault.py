# modules/vault.py
from datetime import datetime
from typing import Any, Dict

from core.logger import get_logger

log = get_logger(__name__)


def register(registry, storage, config: Dict[str, Any]) -> None:
    registry.register("vault", "store_note", lambda **kw: store_note(storage, **kw))


def store_note(storage, title: str, content: str, tag: str = "general") -> Dict[str, Any]:
    record = {
        "module": "vault",
        "action": "store_note",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "title": title,
        "content": content,
        "tag": tag,
    }
    storage.append_record(record)
    log.info(f"[VAULT] stored note: {title} [{tag}]")
    return record
