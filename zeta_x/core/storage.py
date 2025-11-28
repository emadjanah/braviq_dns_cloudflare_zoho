# core/storage.py
import json
from pathlib import Path
from typing import Any, Dict


class ZetaStorage:
    """
    تخزين بسيط على ملف JSON – للبدء فقط.
    لاحقاً يمكن استبداله بـ DB حقيقية.
    """

    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write({"records": []})

    def _read(self) -> Dict[str, Any]:
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: Dict[str, Any]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def append_record(self, record: Dict[str, Any]) -> None:
        data = self._read()
        data.setdefault("records", []).append(record)
        self._write(data)

    def all_records(self):
        return self._read().get("records", [])
