import json

import app.ucase.user as user_case
from app.presentation.response_user_detail import ResponseUserDetail
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

# Get user by id
async def detail(user_id: int):
    try:
        user = await user_case.user_repository.find_by_id(user_id)

        if user is None:
            return response(status=http_status.NOT_FOUND, message="User Not Found")

        logger.info("user-detail", extra={"user-detail": f"{user.id}"})

        return response(
            status=http_status.OK,
            message="User Found",
            data=json.loads(ResponseUserDetail.from_orm(user).json())
        )
    except Exception as e:
        logger.error("user-detail", extra={"error": str(e)})
        return response(status=http_status.INTERNAL_SERVER_ERROR, message="Internal Server Error")
