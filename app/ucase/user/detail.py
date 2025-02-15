import app.ucase.user as user_case
from pkg.logger.log import logger
from pkg.http import response, http_status

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
    logger.info("user-detail", extra={"user-detail": user})
    if user is None:
        return response(status=http_status.NOT_FOUND, message="User Not Found")

    return response(
        status=http_status.OK,
        message="User Found",
        data={
            "id": user[0],
            "uuid": user[1],
            "name": user[2],
            "email": user[3],
        }
    )
