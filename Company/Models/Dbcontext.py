from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

url="postgresql://postgres:admin@localhost:5432/Company_gis"

engine = create_engine(url)
Session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def open_db():
    db = Session()
    try:

        yield db
    finally:
        db.close()
