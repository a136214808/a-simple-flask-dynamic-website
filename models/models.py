from datetime import datetime
from datetime import datetime
from sqlalchemy import create_engine, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://c21122021:Zyc123456789@csmysql.cs.cf.ac.uk:3306/c21122021_flask_cmt120')
Base = declarative_base()  # 生成SQLORM基类


class User(Base):
    # 对应MySQL中数据表的名字
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    passwd = Column(String(100),nullable=False)
    register = Column(DateTime,default=datetime.now)
    email = Column(String(100),nullable=False)

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text,nullable=False)
    dateAdd = Column(DateTime, default=datetime.now())

class individual(Base):
    __tablename__ = 'individual'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    name = Column(String(20),nullable=False)
    caddress = Column(String(100))
    haddress = Column(String(100))
    phone = Column(String(14))
    sex = Column(String(10))
    school = Column(String(20))

    def __str__(self):
        return self.email
class Review(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100),nullable=False)
    content = Column(String(200),nullable=False)
    dateAdd = Column(DateTime, default=datetime.now())
