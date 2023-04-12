from typing import  TypedDict
from pydantic import BaseModel

class CourseSchema(BaseModel):
    id: str
    title: str
    description: str
    hours: int
    price: float

class CourseMsg(TypedDict):
    msg: str
    course: CourseSchema

class CourseInsertion(BaseModel):
    title: str
    description: str
    hours: int
    price: float
