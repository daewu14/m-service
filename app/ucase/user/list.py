import app.ucase.user as case
from pkg.logger.log import logger
from pkg.http import response, http_status, request

# For swagger documentation
response_docs = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "status": "OK",
                    "message": "Loaded"
                }
            },
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "status": "BAD_REQUEST",
                        "message": "Not Found"
                    }
                }
            },
        },
    }
}


# List of user with pagination
async def list(page: int):
    return response(
        status=http_status.OK,
        message="User Found",
        data={
            "page": page,
        }
    )
