from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///Dia01_PojetosComSB/1_emprestimos/base/db.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# criar as tabelas

class usuario(Base):
    pass
    

Base.metadata.create_all(bind=db)