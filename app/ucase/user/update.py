import app.ucase.user as case
import pkg.helper.hash
from app.request.request_update_user import RequestUpdateUser
from pkg.logger.log import logger
from pkg.http import response, http_status

# For swagger documentation
response_docs = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "status": "OK",
                    "message": "User updated",
                    "data": {
                        "uuid": "efff816d-d16c-4c84-ad68-42a64ca5320f",
                        "user": {
                            "email": "daewu.gbp@mail.com",
                            "name": "DaewuGBP",
                            "password": "12345678",
                            "updated_at": "2025-03-09T23:17:17.177321"
                        }
                    }
                }
            },
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
                                "body"
                            ],
                            "msg": "Field required",
                            "input": None
                        }
                    ]
                }
            }
        },
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "status": "NOT_FOUND",
                    "message": "User not found"
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
                    "message": "Field required"
                }
            }
        },
    },
}


# Update existing user
async def update(uuid: str, user: RequestUpdateUser):
    # check user
    check_user = await case.user_repository.find_by_uuid(uuid=uuid)
    if check_user is None:
        return response(
            status=http_status.NOT_FOUND,
            message="User not found"
        )

    if user.email is None and user.name is None and user.password is None:
        return response(
            status=http_status.BAD_REQUEST,
            message="Field required"
        )

    values = {}
    if user.email is not None and user.email != check_user.email:
        values['email'] = user.email
    if user.name is not None and user.name != check_user.name:
        values['name'] = user.name
    if user.password is not None and pkg.helper.hash.check_sha256(user.password, check_user.password) is False:
        values['password'] = pkg.helper.hash.sha256(user.password)

    if values == {}:
        return response(
            status=http_status.BAD_REQUEST,
            message="No data to update, all data is the same"
        )

    try:
        if 'email' in values and values['email'] is not None:
            check_email = await case.user_repository.find_by_email(user.email)
            if check_email is not None:
                return response(
                    status=http_status.BAD_REQUEST,
                    message="Email already used by another user"
                )

        result = await case.user_repository.update_values_by_id(user_id=check_user.id, values=values)
        logger.info("user-updated", extra={"user": f"{result}"})

        if 'password' in values and values['password'] is not None:
            values['password'] = user.password

        return response(
            status=http_status.OK,
            message="User updated",
            data={
                "uuid": uuid,
                "user": values
            }
        )
    except Exception as e:
        logger.error("user-update-error", extra={"error": str(e)})
        return response(
            status=http_status.INTERNAL_SERVER_ERROR,
            message="Internal server error"
        )
