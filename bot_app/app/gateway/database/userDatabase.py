from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    address = Column(String)

#Base.metadata.create_all(engine)
#todo implementar método para criar tabelas caso elas não existam e não executar o 
# método Base.metadata.create_all(engine) caso todas as tabelas existam