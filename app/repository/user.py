import app.model.user
from pkg.db import db_adapter, sql_text
import uuid


class UserRepository:
    @classmethod
    def find_by_id(cls, user_id):
        result = db_adapter.fetchall(query=sql_text(f"SELECT * FROM users WHERE id=:id limit 1"),
                                     arguments={'id': user_id})
        return result

    @classmethod
    def create(cls, user: app.model.user.User):
        result = db_adapter.insert(user)
        return result

    @classmethod
    async def generate_uuid(cls):
        s_uuid = str(uuid.uuid4())
        check_uuid = await db_adapter.fetchone(query=sql_text(f"SELECT id, uuid FROM users WHERE uuid=:uuid limit 1"),
                                               arguments={'uuid': s_uuid})
        if check_uuid is not None and len(check_uuid) > 0:
            return await cls.generate_uuid()

        return s_uuid
