import asyncio

from fastapi import FastAPI

import app.ucase.health.check
import app.ucase.user.detail

api = FastAPI()


@api.get("/", responses=app.ucase.health.check.response_docs)
def index():
    return asyncio.run(app.ucase.health.check.check())

@api.get("/health", responses=app.ucase.health.check.response_docs)
def index():
    return asyncio.run(app.ucase.health.check.check())

@api.get("/api/v1/user/{user_id}", responses=app.ucase.user.detail.response_docs)
async def user(user_id: int):
    return await app.ucase.user.detail.detail(
        user_id=user_id
    )
