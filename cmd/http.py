from routes.api import app
import os


def run():
    app_host = os.environ.get('APP_HOST', '0.0.0.0')
    app_port = int(os.environ.get('APP_PORT', '5000'))
    app_debug = os.environ.get('APP_DEBUG', 'False') == 'True'
    app.run(host=app_host, port=app_port, debug=app_debug, load_dotenv=True)
