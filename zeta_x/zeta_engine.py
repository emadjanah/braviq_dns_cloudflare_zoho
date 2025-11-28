# zeta_engine.py
import importlib
from typing import Any, Dict

from core.logger import get_logger
from core.storage import ZetaStorage
from core.registry import ModuleRegistry

log = get_logger(__name__)


class ZetaEngine:
    """
    المحرك المركزي لـ ZETA-X
    مسؤول عن:
      - تحميل الإعدادات
      - تهيئة التخزين
      - تسجيل وتشغيل الموديولات
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.storage = ZetaStorage(config["database"]["path"])
        self.registry = ModuleRegistry()
        self._load_modules()

    def _load_modules(self) -> None:
        enabled = self.config.get("modules", {}).get("enabled", [])
        for module_name in enabled:
            try:
                module_path = f"modules.{module_name}"
                mod = importlib.import_module(module_path)

                if not hasattr(mod, "register"):
                    log.warning(f"Module {module_name} has no register()")
                    continue

                mod.register(self.registry, self.storage, self.config)
                log.info(f"Loaded module: {module_name}")

            except Exception as e:
                log.exception(f"Failed to load module {module_name}: {e}")

    def run(self, module: str, action: str, **kwargs) -> Any:
        """
        تشغيل أمر داخل موديول واحد.
        مثال:
          engine.run("recon", "scan_market", country="Libya")
        """
        handler = self.registry.get_handler(module, action)
        log.info(f"Running {module}.{action} with kwargs={kwargs}")
        return handler(**kwargs)
