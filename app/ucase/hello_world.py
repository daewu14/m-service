from pkg.http import response, http_status

response_docs = {
    200: {
        "description": "Successful Response",
        "content": {
            "application/json": {
                "example": {
                    "status": "OK",
                    "message": "Hello World!"
                }
            }
        }
    }
}
def hello_world():
    return response(
        status=http_status.OK,
        message='Hello World!'
    )