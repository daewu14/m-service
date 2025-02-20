from fastapi import Response, requests
import json
import http

http_status = http.HTTPStatus
request = requests.Request


def response(status: http_status = http_status.OK,
             message: str = "SUCCESS",
             data: dict = None,
             meta: dict | str = None,
             for_docs: bool = False):
    map = {
        "status": status.name,
        "message": message,
    }

    if data is not None:
        map["data"] = data

    if meta is not None:
        map["meta"] = meta

    if for_docs:
        return _docs(status=status, message=message, data=data, meta=meta)
    return Response(
        status_code=status,
        media_type="application/json",
        content=json.dumps(map),
    )


def _docs(status: http_status = http_status.OK,
          message: str = "SUCCESS",
          data: dict = None,
          meta: dict | str = None):
    map = {
        "status": status.name,
        "message": message,
    }

    if data is not None:
        map["data"] = data

    if meta is not None:
        map["meta"] = meta

    return {status: {
        "description": status.description,
        "content": {
            "application/json": {
                "example": map
            }
        },
    }}
