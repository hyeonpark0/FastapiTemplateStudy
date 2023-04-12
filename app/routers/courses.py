from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.shared.dependencies import get_db
from app.shared.constants import Tags

from app.models import courses as model
from app.schemas.courses import CourseSchema, CourseMsg, CourseInsertion

courses = APIRouter(
    prefix='/courses',
    tags=[Tags.courses]
)

@courses.get('/')
async def get_courses(db: Session = Depends(get_db)) -> list[CourseSchema]:
    return model.read_courses(db)

@courses.get('/slice')
async def get_courses_slice(
        start: int,
        end: int,
        db: Session = Depends(get_db)
    ) -> list[CourseSchema]:
    return model.read_courses_slice(db, start, end)

@courses.get('/{id}')
async def get_course(
        id: str,
        db: Session = Depends(get_db),
        response: Response = None
    ):
    course = model.read_course(db, id)
    if not course:
        response.status_code = status.HTTP_404_NOT_FOUND
    return course if course else {}

@courses.post('/')
async def post_course(
        course: CourseInsertion,
        db: Session = Depends(get_db)
    ) -> CourseMsg:
    return model.create_course(db, course)

@courses.delete('/{id}')
async def delete_course(id: str, db: Session = Depends(get_db)) -> CourseMsg:
    return model.delete_course(db, id)

@courses.put('/{id}')
async def put_course(
        id: str,
        course: CourseInsertion,
        db: Session = Depends(get_db)
    ) -> CourseMsg:
    return model.update_course(db, id, course)
