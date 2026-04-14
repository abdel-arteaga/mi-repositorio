from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo import Base

DATABASE_URL = "mysql+pymysql://root:alex24@localhost/biblioteca_db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
