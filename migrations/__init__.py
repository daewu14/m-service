from pkg.helper.py_execute import read_get_variables
from pkg.db.migration import execute_migration
import asyncio

from pkg.logger.log import logger


def run(flag: str):
    file_vars = read_get_variables("migrations/")
    ttl_executed = 0
    for file_var in file_vars:
        if file_var != "migrations/__init__.py":
            ts = file_vars[file_var]['timestamp']
            sql = file_vars[file_var]['sql_up']
            if flag == "up":
                sql = file_vars[file_var]['sql_up']
            if flag == "down":
                sql = file_vars[file_var]['sql_down']

            ttl_executed += sync_exec_migrations(timestamp=ts, sql=sql, file=file_var+f" -> {flag}")

    logger.info(f"Executed {ttl_executed} migrations")


def sync_exec_migrations(timestamp, sql: str, file: str) -> int:
    return asyncio.run(execute_migration(timestamp, sql, file))
