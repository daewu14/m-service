from pkg.db import alchemy_tx, sql_text
from pkg.logger.log import logger


class UserRepository:
    @classmethod
    def find_by_id(cls, user_id):
        result = alchemy_tx.fetchone(query=sql_text(f"SELECT * FROM users WHERE id={user_id}"))
        logger.info("find_by_id", extra={"result": result})
        return result
