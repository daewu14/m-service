import logging

from json_log_formatter import JSONFormatter
from datetime import datetime
class CustomJsonFormatter(JSONFormatter):
    def json_record(self, message, extra, record):
        extra['message'] = message
        extra['level'] = record.levelname
        extra['timestamp'] = record.created
        extra['datetime'] = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        return extra