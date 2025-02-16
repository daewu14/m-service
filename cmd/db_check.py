import asyncio

from pkg.db import check_connection
from pkg.logger.log import logger


def run():
    asyncio.run(_async_run())

async def _async_run():
    check = await check_connection()
    if check.is_connect:
        logger.info("Database Connected")
    elif check.is_no_db_configured:
        logger.info("Application running without db connection", extra={"detail": check.message})
    else:
        logger.error("Database Not Connected", extra={"detail": check.message})
        exit(1)