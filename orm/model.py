class Book():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return "id:%s name:%s price:%s" % (self.id, self.name, self.price)


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                       encoding="utf8", echo=True)

Base = declarative_base()


# 创建表
class User(Base):
    __tablename__ ="user"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)


# 生成表
Base.metadata.create_all(engine)


