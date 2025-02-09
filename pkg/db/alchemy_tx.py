from pkg.db.alchemy import Alchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from typing import Optional, List, Dict

alchemy = Alchemy()
db_read = alchemy.engine_read()
db_write = alchemy.engine_write()


class AlchemyTx:

    @classmethod
    async def fetchone(cls, query: select, arguments: dict = {}):
        async with AsyncSession(db_read.engine) as session:
            try:
                result = await session.execute(query, arguments)
                return result.fetchone()
            except Exception as e:
                raise e

    @classmethod
    async def fetchall(cls, query: select, arguments: dict = {}):
        async with AsyncSession(db_read.engine) as session:
            try:
                result = await session.execute(query, arguments)
                rows = result.fetchall()
                return [dict(row._mapping) for row in rows] if rows else []
            except Exception as e:
                raise e

    @classmethod
    async def insert(cls, model):
        async with AsyncSession(db_write) as session:
            try:
                async with session.begin():
                    session.add(model)
                    await session.commit()
                    return model.id
            except Exception as e:
                session.rollback()
                raise e
