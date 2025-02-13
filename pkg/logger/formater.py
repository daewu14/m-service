import logging

from json_log_formatter import JSONFormatter
from datetime import datetime
from flask import request

class CustomJsonFormatter(JSONFormatter):
    def json_record(self, message, extra, record):
        extra['message'] = message
        extra['level'] = record.levelname
        extra['timestamp'] = record.created
        extra['datetime'] = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        return extra

class CustomFlaskFormatter(JSONFormatter):
    def json_record(self, message, extra, record):
        extra.update({
            "message": message,
            "level": record.levelname,
            "timestamp": record.created,
            "datetime": datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S"),
            "ip": request.remote_addr if request else None,
            "method": request.method if request else None,
            "path": request.path if request else None,
            "protocol": request.environ.get("SERVER_PROTOCOL") if request else None,
            "status": record.status_code if hasattr(record, "status_code") else None,
        })
        return extra