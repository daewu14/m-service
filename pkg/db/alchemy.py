import os

from sqlalchemy import create_engine
from pkg.db.config import read, write, migration, Config
from pkg.db.entity import Connection
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Alchemy:
    _instance_read = None
    _instance_write = None
    _instance_migration = None
    _session = None

    def close(self):
        self._instance_write = None
        self._instance_read = None
        self._instance_migration = None

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
