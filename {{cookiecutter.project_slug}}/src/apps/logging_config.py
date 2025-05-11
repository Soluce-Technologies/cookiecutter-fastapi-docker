import logging
import os
from datetime import datetime
from logging.config import dictConfig

current_date = datetime.now()
log_dir = os.path.join(
    "logs",
    str(current_date.year),
    str(current_date.month).zfill(2),
    str(current_date.day).zfill(2),
)
os.makedirs(log_dir, exist_ok=True)

fastapi_log_file = os.path.join(log_dir, "fastapi.log")
celery_log_file = os.path.join(log_dir, "celery.log")


class EmojiLogFormatter(logging.Formatter):
    def format(self, record):
        # Add emoji based on log level or custom tags
        emoji_map = {
            "INFO": "ℹ️",
            "DEBUG": "🐛",
            "WARNING": "⚠️",
            "ERROR": "❌",
            "CRITICAL": "🔥",
            "PROCESSING": "🔄",
            "SUCCESS": "✅",
        }

        # Determine emoji based on the message content
        if "Processing" in str(record.msg):
            emoji = emoji_map.get("PROCESSING", "💬")
        elif "successfully" in str(record.msg) or "Success" in str(record.msg):
            emoji = emoji_map.get("SUCCESS", "💬")
        else:
            emoji = emoji_map.get(record.levelname, "💬")

        # Timestamp
        timestamp = datetime.utcnow().strftime("%b %d %Y %H:%M:%S GMT+0000")
        message = super().format(record)

        return f"[{timestamp}] {emoji} {message}"


# Define logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
        },
        "emoji": {
            "()": EmojiLogFormatter,  # Use custom formatter
            "format": "%(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "emoji",  # Use emoji formatter for console
        },
        "fastapi_file": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": fastapi_log_file,
        },
        "celery_file": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": celery_log_file,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "celery": {
            "handlers": ["console", "celery_file"],
            "level": "INFO",
            "propagate": False,
        },
        "fastapi": {
            "handlers": ["console", "fastapi_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


def setup_logging():
    dictConfig(LOGGING_CONFIG)
