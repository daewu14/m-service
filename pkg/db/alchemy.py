import os

from sqlalchemy import create_engine
from pkg.db.config import read, write, migration, Config
from pkg.db.entity import Connection, ConnectionStatus
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text

class Alchemy:
    _instance_read = None
    _instance_write = None
    _instance_migration = None

    def connection(config: Config, use_async: bool = True) -> Connection:
        driver = os.getenv("DB_DRIVER")

        def sqlite():
            return f"sqlite:///{config.dbname}"

        def mysql():
            if config.password is None:
                return f"mysql+aiomysql://{config.user}@{config.host}:{config.port}/{config.dbname}"
            return f"mysql+aiomysql://{config.user}:{config.password}@{config.host}:{config.port}/{config.dbname}"

        def postgresql():
            return f"postgresql://{config.user}:{config.password}@{config.host}:{config.port}/{config.dbname}"

        map_driver = {
            "sqlite": sqlite,
            "mysql": mysql,
            "postgresql": postgresql,
        }

        driver_selected = map_driver.get(driver)

        if driver_selected is None:
            raise ConnectionError(f"Driver {driver} not supported")

        db_url = driver_selected()
        engine = None
        async_engine = None
        if use_async:
            async_engine = create_async_engine(db_url, echo=False)
        else:
            engine = create_engine(db_url)

        return Connection(engine=engine, async_engine=async_engine, str_url=db_url)

    @classmethod
    def engine_read(cls) -> Connection:
        if cls._instance_read is None:
            cls._instance_read = cls.connection(config=read())
        return cls._instance_read

    @classmethod
    def engine_write(cls) -> Connection:
        if cls._instance_write is None:
            cls._instance_write = cls.connection(config=write())
        return cls._instance_write

    @classmethod
    def engine_migration(cls) -> Connection:
        if cls._instance_migration is None:
            cls._instance_migration = cls.connection(config=migration())
        return cls._instance_migration


    @classmethod
    def _engines(cls) -> dict[str, Connection]:
        engines: dict[str, Connection] = {}
        if read().is_configured():
            engines["read"] = cls.engine_read()
        if write().is_configured():
            engines["write"] = cls.engine_write()
        if migration().is_configured():
            engines["migration"] = cls.engine_migration()
        return engines

    @classmethod
    async def check_connection(cls) -> ConnectionStatus:
        enginess = cls._engines()
        status = False
        messages = []
        if len(enginess) == 0 :
            return ConnectionStatus(is_connect=status, is_no_db_configured=True, message="No db configured")

        for key, connection in enginess.items():
            try:
                async with connection.async_engine.connect() as conn:
                    await conn.execute(text("select 1"))
                    status = True
                    messages.append(f"DB {key} Connected")
                    await conn.close()
                await connection.async_engine.dispose()
            except Exception as e:
                status = False
                messages.append(f"DB {key} Error: {str(e)}")

        return ConnectionStatus(is_connect=status, message=" | ".join(messages), is_no_db_configured=False)

    async def close_connection(self):
        for key, connection in self._engines().items():
            try:
                await connection.async_engine.dispose()
            except Exception as e:
                print(f"Database {key} was closed unexpectedly: {str(e)}")

        self._instance_write = None
        self._instance_read = None
        self._instance_migration = None