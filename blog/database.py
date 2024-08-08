from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import Depends

URL_DATABASE = 'mysql+pymysql://root:admin@localhost:3306/myauth' 


engine = create_engine(
    URL_DATABASE
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

db_dependency = Annotated[Session, Depends(get_db)]