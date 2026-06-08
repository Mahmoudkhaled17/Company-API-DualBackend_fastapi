from fastapi import FastAPI

from Models.Dbcontext import Base,engine,open_db
from Models import Course,crsResult,Department,Instructor,Trainee
from router.Instructor import inst_router



Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(inst_router)
