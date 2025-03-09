from datetime import datetime

from app.model.user import User
from pkg.db import db_adapter, sql_text
import uuid

from pkg.helper.paginate import Paginate


class UserRepository:
    @classmethod
    def find_by_id(cls, user_id):
        stmt = db_adapter.stmt.select(User).where(User.id == user_id)
        result = db_adapter.fetchone(stmt)
        return result

    @classmethod
    def create(cls, user: User):
        result = db_adapter.insert(user)
        return result

    @classmethod
    async def create_with_session(cls, user: User):
        """
        Example of using session
        :param user:
        :return: User
        """
        session = db_adapter.get_session()
        try:
            async with session.begin():
                session.add(user)

            await session.commit()
            await session.refresh(user)
            detached_model = user.__dict__.copy()
            await session.close()
            return detached_model
        except Exception as e:
            await session.rollback()
            await session.close()
            raise e

    @classmethod
    async def generate_uuid(cls):
        s_uuid = str(uuid.uuid4())
        check_uuid = await db_adapter.fetchone(db_adapter.stmt.select(User).where(User.uuid == s_uuid))
        if check_uuid is not None:
            return await cls.generate_uuid()

        return s_uuid

    @classmethod
    async def update_values_by_id(cls, values: dict, user_id):
        values['updated_at'] = datetime.now().isoformat()
        stmt = db_adapter.stmt.update(User).where(User.id == user_id).values(values)
        result = await db_adapter.execute(stmt)
        affected_rows = result.rowcount
        return affected_rows

    @classmethod
    def find_by_email(cls, email: str):
        stmt = db_adapter.stmt.select(User).where(User.email == email)
        result = db_adapter.fetchone(stmt)
        return result

    @classmethod
    def get_with_paginate(cls, paginate: Paginate):
        stmt = db_adapter.stmt.select(User).order_by(User.id.desc()).offset(paginate.offset).limit(paginate.limit)
        return db_adapter.fetchall(stmt)

    @classmethod
    def find_by_uuid(cls, uuid: str):
        stmt = db_adapter.stmt.select(User).where(User.uuid == uuid)
        result = db_adapter.fetchone(stmt)
        return result
