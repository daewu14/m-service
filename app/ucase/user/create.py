import json

import app.model.user
import pkg.helper.hash
from app.presentation.response_user_created import ResponseUserCreated
from pkg.logger.log import logger
from pkg.http import response, http_status
from app.request.request_create_user import RequestCreateUser
import app.ucase.user as user_case

# For swagger documentation
response_docs = {
    201: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "status": "CREATED",
                    "message": "Created",
                    "data": {
                        "user": {
                            "id": 23,
                            "uuid": "38591d14-66a3-469d-8d04-db334f291a30",
                            "name": "Daewu",
                            "email": "daewu1@mail.com",
                            "created_at": "2025-03-08T15:53:12"
                        }
                    }
                }
            },
        },
        422: {
            "description": "Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "missing",
                                "loc": [
                                    "body",
                                    "name"
                                ],
                                "msg": "Field required",
                                "input": {
                                    "email": "daewu1@mail.com",
                                    "password": "123123"
                                }
                            }
                        ]
                    }
                }
            },
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "status": "BAD_REQUEST",
                        "message": "Email already exists"
                    }
                }
            },
        },
    }
}


# Create new user
async def create(user: RequestCreateUser):
    try:
        logger.info("user-create", extra={"user": user.dict()})

        if user.email is None:
            user.email = ""

        # check email if not empty
        if user.email != "":
            check_email = await user_case.user_repository.find_by_email(user.email)
            if check_email is not None:
                return response(
                    status=http_status.BAD_REQUEST,
                    message="Email already exists"
                )

        generate_uuid = await user_case.user_repository.generate_uuid()

        user_model = app.model.user.User(
            name=user.name,
            email=user.email,
            password=pkg.helper.hash.sha256(user.password),
            uuid=generate_uuid
        )
        result = await user_case.user_repository.create(user_model)
        logger.info("user-created", extra={"user": f"{result}"})
        return response(
            status=http_status.CREATED,
            message="Success create new user",
            data={
                "user": json.loads(ResponseUserCreated.from_orm(result).json())
            }
        )
    except Exception as e:
        logger.error("user-create", extra={"error": str(e)})
        return response(
            status=http_status.INTERNAL_SERVER_ERROR,
            message=str(e)
        )
