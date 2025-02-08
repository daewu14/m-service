import logging
from pkg.logger.formater import CustomJsonFormatter


# Create a custom logger
logger = logging.getLogger('flask_service_logger')

# Set the log level
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()

# Set the log level for handlers
console_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
json_format = CustomJsonFormatter()

console_handler.setFormatter(json_format)

# Add handlers to the logger
logger.addHandler(console_handler)
