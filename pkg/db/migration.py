from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from pkg.db.alchemy import Alchemy
from sqlalchemy.sql import text
import asyncio

from pkg.logger.log import logger

alchemy = Alchemy()
db_migration = alchemy.engine_migration()
async_session_migration = sessionmaker(db_migration.async_engine, expire_on_commit=False, class_=AsyncSession)

_create_table_sql = """
CREATE TABLE IF NOT EXISTS dw_migrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ts_migrate BIGINT NULL,
    migration varchar(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);
"""

_create_index_ts_sql = """
CREATE INDEX dw_migrations_ts_index ON dw_migrations (ts_migrate);
"""

_check_index_exist_sql = """
SELECT COUNT(*)
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'dw_migrations'
  AND index_name = 'dw_migrations_ts_index';
"""


async def _execute():
    async with AsyncSession(db_migration.async_engine) as session:
        try:
            async def close():
                await session.close()
                await db_migration.async_engine.dispose()

            await session.execute(text(_create_table_sql))
            await session.commit()
            await close()

            # Check if the index exists
            index_exists = (await session.execute(text(_check_index_exist_sql))).fetchone()[0]
            if index_exists == 0:
                await session.execute(text(_create_index_ts_sql))
                await session.commit()

            await close()

        except Exception as e:
            raise e


def initiate_migration():
    asyncio.run(_execute())


async def execute_migration(timestamp, sql: str, migration_file: str) -> int:
    timestamp = round(timestamp, 0)
    async with AsyncSession(db_migration.async_engine) as session:
        try:
            async def close():
                await session.close()
                await db_migration.async_engine.dispose()

            check_version = (
                await session.execute(text(f"select * from dw_migrations where ts_migrate = {timestamp}"))).fetchall()
            if len(check_version) > 0:
                await close()
                return 0

            mig = migration_file.replace(".py -> up", "")
            mig = mig.replace(".py -> down", "")
            mig = mig.replace("migrations/", "")

            await session.execute(text(sql))
            await session.execute(text(f"insert into dw_migrations (ts_migrate, migration) values ({timestamp},'{mig}')"))
            await session.commit()
            await close()
            print(f"Success execute migration {migration_file}")
            return 1

        except Exception as e:
            await session.rollback()
            await db_migration.async_engine.dispose()
            raise e
