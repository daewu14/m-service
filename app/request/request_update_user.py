import app.request
import typing


class RequestUpdateUser(app.request.BaseModel):
    name: typing.Optional[str] = None
    email: typing.Optional[str] = None
    password: typing.Optional[str] = None
