from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class Database:
    DATABASE_URL = "sqlite:///schumacher/database/banco.db"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL, echo=True)
        self.Base = declarative_base()
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine) 


    def get_session(self):
        return self.SessionLocal
    
db = Database()
