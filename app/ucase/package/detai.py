import app.ucase.package as case
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


# For get detail package
async def detai():
    # example of getting user_id value from request
    # user_id = request.get("user_id")
    return response(
        status=http_status.OK,
        message="User Found"
    )
