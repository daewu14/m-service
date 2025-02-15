from fastapi import FastAPI
import app.ucase.user.detail

api = FastAPI()


@api.get("/api/v1/user/{user_id}", responses=app.ucase.user.detail.response_docs)
async def user(user_id: int):
    return await app.ucase.user.detail.user_by_id(
        user_id=user_id
    )
