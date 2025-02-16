import app.ucase.user as user_case
from pkg.logger.log import logger
from pkg.http import response, http_status
import json

response_docs = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "status": "OK",
                    "message": "User Found",
                    "data": {
                        "id": 1,
                        "uuid": "23456823745634875",
                        "name": "Daewu Bintara",
                        "email": "daewu.bintara1996@gmail.com"
                    }
                }
            }
        },
    },
    404: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "status": "NOT_FOUND",
                    "message": "User Not Found"
                }
            }
        },
    },
}


async def user_by_id(user_id: int):
    user = await user_case.user_repository.find_by_id(user_id)
    logger.info("user-detail", extra={"user-detail": user[0]})
    if user is None or len(user) == 0:
        return response(status=http_status.NOT_FOUND, message="User Not Found")

    # user = json.loads(f"{user[0]}")
    return response(
        status=http_status.OK,
        message="User Found",
    )
