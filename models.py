from sqlalchemy import Column, String, Integer
from database import Base

class Nvi(Base):
    __tablename__ = 'nvi'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    book = Column(String(50))
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String(255))


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book = Column(String(100))


class Acf(Base):
    __tablename__ = 'acf'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    book = Column(String(50))
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(String(255))
