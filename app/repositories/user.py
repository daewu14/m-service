from pkg.db import alchemy_tx, sql_text
# from app.models.user import User

class UserRepository:
    @classmethod
    def find_by_id(cls, user_id):
        result = alchemy_tx.fetchall(query=sql_text(f"SELECT * FROM users WHERE id=:id limit 1"), arguments={'id': user_id})
        return result
