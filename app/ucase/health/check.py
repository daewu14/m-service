import app.ucase.health as case
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
                    "message": "Server Healthy"
                }
            },
        }
    }
}


# Check server health
async def check():
    return response(
        status=http_status.OK,
        message="Server Healthy"
    )
