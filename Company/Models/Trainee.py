from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Models.Dbcontext import Base


class Trainee(Base):
    __tablename__ = "Trainees"
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Image = Column(String)
    Adress = Column(String)
    Grade = Column(String)
    dep_id = Column(Integer,ForeignKey('Departments.Id',ondelete='NO ACTION'))


