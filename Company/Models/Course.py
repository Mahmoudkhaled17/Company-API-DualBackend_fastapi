from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.Dbcontext import Base


class Course(Base):
    __tablename__ = 'Courses'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Degree = Column(Integer)
    Min_Degree = Column(Integer)
    Credit_Hours = Column(Integer)

    dep_id=Column(Integer, ForeignKey('Departments.Id',ondelete='NO ACTION'))


