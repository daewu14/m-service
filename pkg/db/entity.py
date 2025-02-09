from sqlalchemy import Engine


class Connection:
    def __init__(self, engine: Engine, str_url: str):
        self.engine = engine
        self.str_url = str_url
