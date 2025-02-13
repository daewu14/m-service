from routes.api import app
from flask import request
from pkg.logger.log import logger
import sys
import time
import os


def run():
    # Disable Flask logs
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *args: None

    app_host = os.environ.get('APP_HOST', '0.0.0.0')
    app_port = int(os.environ.get('APP_PORT', '5000'))
    app_debug = os.environ.get('APP_DEBUG', 'False') in ("1", "true", "yes", "on")
    app.run(host=app_host, port=app_port, debug=app_debug, load_dotenv=True)


@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    if hasattr(request, "start_time"):
        if response.status_code != 308:
            response_time = time.time() - request.start_time
            response_time_ms = round(response_time * 1000, 2)
            extra = {
                "method": request.method,
                "status": response.status_code,
                "path": request.path,
                "response_time_ms": response_time_ms,
                "ip": request.remote_addr,
                "agent": request.user_agent
            }
            logger.info(f"{request.method}:{request.path}", extra=extra)
    return response
