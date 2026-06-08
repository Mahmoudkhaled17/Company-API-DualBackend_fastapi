from sqlalchemy import Column, Integer, String
from Models.Dbcontext import Base

class Department(Base):
    __tablename__ = 'Departments'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Manager = Column(String)
