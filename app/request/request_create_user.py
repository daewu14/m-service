import app.request
import typing
class RequestCreateUser(app.request.BaseModel):
    name: str
    email: typing.Optional[str] = None
    password: str