import os


class Config:

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port


def read() -> Config:
    return Config(
        dbname=os.getenv("DB_NAME_READ"),
        user=os.getenv("DB_USER_READ"),
        password=os.getenv("DB_PASSWORD_READ"),
        host=os.getenv("DB_HOST_READ"),
        port=os.getenv("DB_PORT_READ", '3306')
    )


def write() -> Config:
    return Config(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", '3306')
    )


def migration() -> Config:
    return Config(
        dbname=os.getenv("DB_MIGRATION_NAME", "flask_srvc"),
        user=os.getenv("DB_MIGRATION_USER", "root"),
        password=os.getenv("DB_MIGRATION_PASSWORD", "password"),
        host=os.getenv("DB_MIGRATION_HOST", "localhost"),
        port=os.getenv("DB_MIGRATION_PORT", '3306')
    )
