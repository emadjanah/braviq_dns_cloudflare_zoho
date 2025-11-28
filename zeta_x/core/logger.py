# core/logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from typing import Optional

_LOGGER: Optional[logging.Logger] = None


def get_logger(name: str = "zeta") -> logging.Logger:
    global _LOGGER
    if _LOGGER is not None:
        return _LOGGER

    logger = logging.getLogger("zeta")
    logger.setLevel(logging.INFO)

    # Stream handler (console)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(ch)

    # File handler
    log_path = Path("data/logs/zeta.log")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(fh)

    _LOGGER = logger
    return logger
