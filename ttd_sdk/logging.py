import logging
from typing import Optional, Literal

# Define log levels as constants
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def _get_level(level: LogLevel | int | None) -> int:
    if isinstance(level, str):
        return getattr(logging, level.upper())
    return level or INFO

def configure_sdk_logging(
    level: LogLevel | int | None = INFO,
    log_file: Optional[str] = None,
    format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
) -> None:
    """Configure logging for the entire SDK"""
    logger = logging.getLogger("ttd_sdk")
    logger.handlers = []
    logger.setLevel(_get_level(level))
    logger.propagate = True
    
    formatter = logging.Formatter(format)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    if log_file:
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for the given name"""
    return logging.getLogger(f"ttd_sdk.{name.split('.')[-1]}")