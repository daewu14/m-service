from fastapi import FastAPI

import app.ucase.user.detail
import app.ucase.hello_world

api = FastAPI()


@api.get("/", responses=app.ucase.hello_world.response_docs)
def index():
    return app.ucase.hello_world.hello_world()


@api.get("/api/v1/user/{user_id}", responses=app.ucase.user.detail.response_docs)
async def user(user_id: int):
    return await app.ucase.user.detail.user_by_id(
        user_id=user_id
    )
