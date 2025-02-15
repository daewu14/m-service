from fastapi import FastAPI, Response, status
import app.ucase.user.detail

api = FastAPI()


@api.get("/api/v1/user/{user_id}")
async def user(user_id: int):
    return await app.ucase.user.detail.user_by_id(
        user_id=user_id
    )
