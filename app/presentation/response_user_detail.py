from datetime import datetime

import app.presentation


class ResponseUserDetail(app.presentation.BaseModel):
    id: int
    uuid: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
