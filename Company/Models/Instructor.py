from sqlalchemy import Column, Integer, String, ForeignKey
from Models.Dbcontext import Base

class Instructor(Base):
    __tablename__ = 'Instructors'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Image = Column(String)
    Salary = Column(String)
    Address = Column(String)

    dept_id = Column(Integer, ForeignKey('Departments.Id',ondelete='NO ACTION'))
    course_id = Column(Integer, ForeignKey('Courses.Id',ondelete='NO ACTION'))


