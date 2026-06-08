from sqlalchemy import Column, String, Integer, ForeignKey
from Models.Dbcontext import Base


class CrsResult(Base):
    __tablename__ = 'CrsResults'
    Id = Column(Integer, primary_key=True)
    Degree = Column(Integer)

    courses_id = Column(Integer, ForeignKey('Courses.Id',ondelete='NO ACTION'))
    trainee_id = Column(Integer, ForeignKey('Trainees.Id',ondelete='NO ACTION'))

