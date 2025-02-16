from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession


class Connection:
    def __init__(self, engine: Engine, async_engine: AsyncEngine, str_url: str):
        self.engine = engine
        self.str_url = str_url
        self.async_engine = async_engine

class ConnectionStatus:

    def __init__(self, is_connect: bool, is_no_db_configured: bool, message: str):
        self.is_connect = is_connect
        self.is_no_db_configured = is_no_db_configured
        self.message = message