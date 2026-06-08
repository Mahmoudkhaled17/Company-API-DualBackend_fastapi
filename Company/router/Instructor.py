from fastapi import APIRouter ,Depends,HTTPException,status
from sqlalchemy.orm import Session
from Models.Dbcontext import open_db
from  Schema_company import Instructor as instructor_schema
from Models.Instructor import Instructor as instructor_model

inst_router = APIRouter()


@inst_router.get('/instructors',response_model=list[instructor_schema.instructor])
async def instructor_show(db:Session=Depends(open_db)):
    list_instrucor=db.query(instructor_model).all()
    if len(list_instrucor)<=0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Instructor not found")

    return list_instrucor

@inst_router.get("/instructors/{id}",response_model=instructor_schema.instructor)
async def instructor_show(id:int,db:Session=Depends(open_db)):
    theinstrucor=db.query(instructor_model).filter(instructor_model.Id==id).first()
    if theinstrucor==None:
        raise HTTPException(status_code=404,detail="Instructor not found")
    return theinstrucor

