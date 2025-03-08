import asyncio

from fastapi import FastAPI

import app.ucase.health.check
import app.ucase.user.create
import app.ucase.user.detail
import app.ucase.user.list

api = FastAPI()


@api.get("/", responses=app.ucase.health.check.response_docs)
def index():
    return asyncio.run(app.ucase.health.check.check())


@api.get("/health", responses=app.ucase.health.check.response_docs)
def index():
    return asyncio.run(app.ucase.health.check.check())


@api.post("/api/v1/user", responses=app.ucase.user.create.response_docs)
async def create_user(user: app.ucase.user.create.RequestCreateUser):
    return await app.ucase.user.create.create(user=user)


@api.get("/api/v1/user/{user_id}", responses=app.ucase.user.detail.response_docs)
async def user(user_id: int):
    return (await app.ucase.user.detail.detail(
        user_id=user_id
    ))


@api.get("/api/v1/users", responses=app.ucase.user.list.response_docs)
async def user_list(page: int):
    return await app.ucase.user.list.list(page=page)
