# -----------------------------
# FILE: app/utils/logger.py
# -----------------------------
import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
import sys
from typing import Optional


def configure_logging(
    level: Optional[str] = None, logfile: Optional[str] = None
) -> None:
    """Configure root logger using a simple but production-friendly setup.

    - Console handler (stream)
    - Optional rotating file handler
    - Level default comes from settings.LOG_LEVEL
    """
    from config.settings import settings  # local import to avoid circular imports

    log_level = (level or settings.LOG_LEVEL).upper()

    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    root = logging.getLogger()
    root.setLevel(getattr(logging, log_level, logging.INFO))

    # Clear existing handlers to avoid duplicate logs in interactive runs
    if root.handlers:
        for h in list(root.handlers):
            root.removeHandler(h)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(getattr(logging, log_level, logging.INFO))
    ch.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(ch)

    # Optional rotating file handler
    if logfile:
        fh = RotatingFileHandler(logfile, maxBytes=10 * 1024 * 1024, backupCount=5)
        fh.setLevel(getattr(logging, log_level, logging.INFO))
        fh.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
        root.addHandler(fh)


def get_logger(name: Optional[str] = None) -> Logger:
    """Return a configured logger for `name`.

    Call `configure_logging()` once on app startup (scripts or FastAPI startup event).
    """
    return logging.getLogger(name)
