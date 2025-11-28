# core/registry.py
from typing import Callable, Dict, Tuple


class ModuleRegistry:
    """
    Registry بسيط يربط:
      (module_name, action_name) -> handler function
    """

    def __init__(self):
        self._handlers: Dict[Tuple[str, str], Callable] = {}

    def register(self, module: str, action: str, handler: Callable) -> None:
        key = (module, action)
        self._handlers[key] = handler

    def get_handler(self, module: str, action: str) -> Callable:
        key = (module, action)
        if key not in self._handlers:
            raise KeyError(f"No handler registered for {module}.{action}")
        return self._handlers[key]
