from sqlalchemy import create_engine
from orm import model
# 创建连接实例
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                       encoding="utf8", echo=True)

# 构造会话对象
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)()


def insertUser(username,password):
    Session.add(model.User(name=username, password=password))
    Session.commit()
    Session.close()


def checkUser(username, password):
    result = Session.query(model.User).filter(model.User.name==username).filter(model.User.password==password).first()
    if result:
        return True
    else:
        return False

