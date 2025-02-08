from pkg.logger.log import logger
from pkg.app.ucase import UCase

class HelloWorldCase(UCase):
    
    def serve(self):
        logger.info("Returning hello world message", extra={"data": {"trace": "hello_world.get_message"}})
        return self.response({"message": "hello world", "data": "oke"})