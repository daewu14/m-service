from pkg.db import alchemy_tx


class UserRepository:
    @classmethod
    async def find_by_id(cls, user_id):
        await alchemy_tx.fetchone(query="select * from users where id = ? limit 1", value=user_id)
