from cmd.abstract import AbstractCommand, argparse
import uvicorn
import os
from routes.api import api
from pkg.logger.log import logger
from pkg.logger.uvcorn import uvcorn_logging_config
from cmd import db_check

class HttpCommand(AbstractCommand):

    name = 'http'
    description = 'Runs http server'
    help = 'Runs http server'

    def run(self, parser: argparse.ArgumentParser):
        db_check.DBCheck().run(parser)

        app_name = os.environ.get('APP_NAME', 'App')
        app_host = os.environ.get('APP_HOST', '0.0.0.0')
        app_port = int(os.environ.get('APP_PORT', '5000'))

        app_debug = os.environ.get('APP_DEBUG', 'False') in ("1", "true", "yes", "on", "True", "TRUE")
        extra = {"debug": app_debug, "host": app_host, "port": app_port}
        if app_debug:
            extra["url"] = f"http://{app_host}:{app_port}"

        logger.info(f"{app_name} running", extra=extra)
        uvicorn.run(api, host=app_host, port=app_port, log_config=uvcorn_logging_config)
