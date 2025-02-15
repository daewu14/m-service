from pkg.db.alchemy import Alchemy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

from pkg.logger.log import logger

alchemy = Alchemy()
db_read = alchemy.engine_read()
db_write = alchemy.engine_write()
sql_text = text
async_session_read = sessionmaker(db_read.async_engine, expire_on_commit=False, class_=AsyncSession)
async_session_write = sessionmaker(db_write.async_engine, expire_on_commit=False, class_=AsyncSession)


class AlchemyTx:

    @classmethod
    async def fetchone(cls, query: select, arguments: dict = {}):
        async with AsyncSession(db_read.async_engine) as session:
            try:
                result = await session.execute(query, arguments)
                data = result.fetchone()
                logger.info("fetchone", extra={"result": data, "query": query, "arguments": arguments})
                return data
            except Exception as e:
                raise e

    @classmethod
    async def fetchall(cls, query: select, arguments: dict = {}):
        async with AsyncSession(db_read.async_engine) as session:
            try:
                result = await session.execute(query, arguments)
                rows = result.fetchall()
                return [dict(row._mapping) for row in rows] if rows else []
            except Exception as e:
                raise e

    @classmethod
    async def insert(cls, model):
        async with AsyncSession(db_write.async_engine) as session:
            try:
                async with session.begin():
                    session.add(model)
                    await session.commit()
                    return model.id
            except Exception as e:
                session.rollback()
                raise e
