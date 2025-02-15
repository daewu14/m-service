import uvicorn

from routes.api import api
from pkg.logger.log import logger
import os


def run():

    app_host = os.environ.get('APP_HOST', '0.0.0.0')
    app_port = int(os.environ.get('APP_PORT', '5000'))

    app_debug = os.environ.get('APP_DEBUG', 'False') in ("1", "true", "yes", "on", "True", "TRUE")
    logger.info("Running on http://{}:{}".format(app_host, app_port), extra={"debug": app_debug})
    uvicorn.run(api, host=app_host, port=app_port)
