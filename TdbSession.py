#sqlclchemy在SQL语句的基础上又封装了一层

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义User类对象
class User(Base):
    #表的名字:
    __tablename__ = 'user'

    #表的结构:
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

#初始化数据库链接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/test')

#创建DBSession类型：
DBSession = sessionmaker(bind = engine)



#添加记录函数
def addInfo(id1, name1):
    #创建session对象：
    session = DBSession()
    #创建新User对象
    new_user = User(id = id1, name = name1)
    #添加到session
    session.add(new_user)
    #提交保存到数据库
    session.commit()
    #关闭session
    session.close()

#查询记录
def queryInfo(id1):
    #创建session对象：
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id == id1).one()
    # 打印类型和对象的name属性:
    print('type:', type(user))
    print('name:', user.name)
    # 关闭Session:
    session.close()

# addInfo('5', 'Bob')
queryInfo('5')


