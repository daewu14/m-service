from pkg.logger.log import logger
from pkg.app.ucase import UCase


class HelloWorldCase(UCase):
    def serve(self):
        logger.info("Returning hello world message", extra={"data": {"trace": "hello_world.get_message"}})

        return self.response(
            status=self.http_status.OK,
            data={
                "id": "a4fca275-a317-4235-9502-a81a842aaf0d",
                "name": "Daewu Bintara",
                "email": "daewu@mail.com"
            },
        )
