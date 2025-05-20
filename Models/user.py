from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from Database.Base import Base

class User(Base):
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(70), nullable=False)
    age = Column(Integer, nullable=False)

def soma(a, b):
    return a + b

