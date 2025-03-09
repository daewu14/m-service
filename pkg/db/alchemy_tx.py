from pkg.db.alchemy import Alchemy
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from pkg.db.alchemy_stmt import AlchemyStmt
from pkg.logger.log import logger

alchemy = Alchemy()
db_read = alchemy.engine_read()
db_write = alchemy.engine_write()
sql_text = text


class AlchemyTx:

    def __init__(self):
        self.stmt = AlchemyStmt()

    @classmethod
    async def fetchone(cls, stmt: select):
        async with AsyncSession(db_read.async_engine) as session:
            try:
                result = await session.execute(stmt)
                data = result.scalar_one_or_none()
                return data
            except Exception as e:
                raise e

    @classmethod
    async def fetchall(cls, stmt: select):
        async with AsyncSession(db_read.async_engine) as session:
            try:
                result = await session.execute(stmt)
                return result.scalars().all()
            except Exception as e:
                raise e

    @classmethod
    async def insert(cls, model):
        async with AsyncSession(db_write.async_engine) as session:
            try:
                async with session.begin():
                    session.add(model)

                await session.commit()
                await session.refresh(model)
                detached_model = model.__dict__.copy()  # Create a standalone copy
                await session.close()
                return detached_model
            except Exception as e:
                await session.rollback()
                await session.close()
                raise e

    @classmethod
    async def execute(cls, stmt):
        async with AsyncSession(db_write.async_engine) as session:
            try:
                result = await session.execute(stmt)
                await session.commit()
                await session.close()
                return result
            except Exception as e:
                await session.rollback()
                await session.close()
                raise e

    @classmethod
    def get_session(cls, write_engine: bool = True) -> AsyncSession:
        """
        Get session for read or write
        :param write_engine:
        :return: AsyncSession
        """
        session_write = sessionmaker(db_write.async_engine, expire_on_commit=False, class_=AsyncSession)
        session_read = sessionmaker(db_read.async_engine, expire_on_commit=False, class_=AsyncSession)
        if write_engine:
            return session_write()
        return session_read()
