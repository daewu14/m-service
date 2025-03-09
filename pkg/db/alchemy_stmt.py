from sqlalchemy import select, update, delete, or_, and_, insert, text, func

class AlchemyStmt:
    def __init__(self):
        self.insert = insert
        self.select = select
        self.update = update
        self.delete = delete
        self.or_ = or_
        self.and_ = and_
        self.func = func