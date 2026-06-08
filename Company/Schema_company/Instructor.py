from pydantic import BaseModel,ConfigDict,Field

class instructor(BaseModel):
    model_config = ConfigDict(extra="forbid",from_attributes=True)
    instructor_id: int=Field(validation_alias="Id")
    instructor_name: str=Field(validation_alias="Name")
    instructor_image_url: str=Field(validation_alias="Image")
    instructor_address: str=Field(validation_alias="Address")
    instructor_salary: str=Field(validation_alias="Salary")