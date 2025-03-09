import json

import app.ucase.user as case
import pkg.helper.paginate
from app.presentation.response_user_detail import ResponseUserDetail
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
                    "message": "Users found",
                    "data": [
                        {
                            "id": 6,
                            "uuid": "efff816d-d16c-4c84-ad68-42a64ca5320f",
                            "name": "Daewu Gus BP",
                            "email": "daewu6@mail.com",
                            "created_at": "2025-03-09T14:38:44",
                            "updated_at": "2025-03-09T14:38:44"
                        },
                        {
                            "id": 5,
                            "uuid": "d1ebc2f2-d44e-45eb-8e02-17e890a993a5",
                            "name": "Daewu Gus BP",
                            "email": "daewu5@mail.com",
                            "created_at": "2025-03-09T14:38:34",
                            "updated_at": "2025-03-09T14:38:34"
                        },
                        {
                            "id": 4,
                            "uuid": "44f4ef6e-bc3f-48a2-b32b-6ff8044987ce",
                            "name": "Daewu Gus BP",
                            "email": "daewu4@mail.com",
                            "created_at": "2025-03-09T14:35:03",
                            "updated_at": "2025-03-09T14:35:03"
                        },
                        {
                            "id": 3,
                            "uuid": "87de0259-cc45-448b-aa74-bb4556248dd9",
                            "name": "Daewu Gus BP",
                            "email": "daewu3@mail.com",
                            "created_at": "2025-03-09T14:34:47",
                            "updated_at": "2025-03-09T14:34:47"
                        },
                        {
                            "id": 2,
                            "uuid": "8a644dd6-1478-4b9f-ae0a-658e41f1be0d",
                            "name": "Daewu Gus BP",
                            "email": "daewu2@mail.com",
                            "created_at": "2025-03-09T12:40:58",
                            "updated_at": "2025-03-09T12:40:58"
                        }
                    ],
                    "meta": {
                        "next_page": 5,
                        "pref_page": None,
                        "total_data": 5
                    }
                }
            },
        }
    },
    404: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "status": "NOT_FOUND",
                    "message": "Users not found on this page(10)",
                    "meta": {
                        "next_page": None,
                        "pref_page": 5,
                        "total_data": 0
                    }
                }
            }
        },
    },
    500: {
        "description": "Internal Server Error",
        "content": {
            "application/json": {
                "example": {
                    "status": "INTERNAL_SERVER_ERROR",
                    "message": "Internal Server Error"
                }
            }
        },
    }
}


# List of user with pagination
async def list(page: int):
    try:
        paginate = pkg.helper.paginate.new_paginate(limit=5, offset=page)
        result = await case.user_repository.get_with_paginate(paginate)
        logger.info("user-list", extra={"result": f"{result}"})

        # Loop user detail data from list of result
        results = [
            json.loads(ResponseUserDetail.model_validate(user).json())
            for user in result
        ]

        if len(results) == 0:
            return response(
                status=http_status.NOT_FOUND,
                message=f"Users not found on this page({page})",
                meta=paginate.get_meta(results)
            )

        return response(
            status=http_status.OK,
            message="Users found",
            data=results,
            meta=paginate.get_meta(results)
        )
    except Exception as e:
        logger.error("error-user-list", extra={"error": str(e)})
        return response(
            status=http_status.INTERNAL_SERVER_ERROR,
            message=str(e)
        )
