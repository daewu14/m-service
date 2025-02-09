import logging
import os

from pkg.logger.formater import CustomJsonFormatter

_nameToLevel = {
    'CRITICAL': logging.CRITICAL,
    'FATAL': logging.FATAL,
    'ERROR': logging.ERROR,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET,
}


# Create a custom logger
logger = logging.getLogger('flask_service_logger')

# Setup log level
log_level_env = os.environ.get("LOG_LEVEL", "ERROR")
log_level = _nameToLevel.get(log_level_env)
if log_level is None:
    log_level = logging.ERROR

# Set the log level
logger.setLevel(log_level)

# Create handlers
console_handler = logging.StreamHandler()

# Set the log level for handlers
console_handler.setLevel(log_level)

# Create formatters and add them to handlers
json_format = CustomJsonFormatter()

console_handler.setFormatter(json_format)

# Add handlers to the logger
logger.addHandler(console_handler)
