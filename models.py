import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False)
    category = Column(String, nullable=False)

if __name__ == '__main__':
    engine = create_engine('sqlite:///data.sqlite3')
    Base.metadata.create_all(engine)