from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from pkg.db.alchemy_tx import async_session_read, async_session_write

Column = Column
Integer = Integer
String = String
DateTime = DateTime
ForeignKey = ForeignKey


class Model(declarative_base()):
    __abstract__ = True

    def read(self):
        return async_session_read.query(self.__class__)

    def write(self):
        return async_session_write.query(self.__class__)
