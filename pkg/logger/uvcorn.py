import os

from pkg.logger.formater import CustomJsonFormatter

uvcorn_logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",  # Use custom JSON formatter
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": os.getenv("LOG_LEVEL", "ERROR"),
        },
    },
    "formatters": {
        "json": {
            "()": CustomJsonFormatter,  # Reference custom JSON formatter
        },
    },
}
