from fastapi import Response
import json
import http

http_status = http.HTTPStatus


def response(status: http_status = http_status.OK,
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

    return Response(
        status_code=status,
        media_type="application/json",
        content=json.dumps(map),
    )
