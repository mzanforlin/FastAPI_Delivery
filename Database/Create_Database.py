from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.user import User
from Database.Base import Base
from Database.Engine import engine

# Criando a engine para se conectar ao banco de dados


# Criando a sessão
Base.metadata.create_all(engine)
