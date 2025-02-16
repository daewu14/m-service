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
                        "id": "1",
                        "uuid": "dsesd-qwerd-d3ead-3fea5-6hgfs",
                        "email": "daewu@mail.com",
                        "created_at": "2025-02-16 22:11:02",
                        "updated_at": "2025-02-16 22:11:21"
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

    if user is None or len(user) == 0:
        return response(status=http_status.NOT_FOUND, message="User Not Found")

    logger.info("user-detail", extra={"user-detail": user[0]})
    data_map = {}
    for usr in user[0]:
        if usr != "password":
            data_map[usr] = f"{user[0][usr]}"

    return response(
        status=http_status.OK,
        message="User Found",
        data=data_map
    )
