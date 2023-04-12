import uuid
from copy import copy

from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float

from app.db.database import Base
from app.schemas.courses import CourseInsertion

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=True)
    hours = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

def read_courses(db: Session):
    return db.query(Course).all()

def read_course(db: Session, id: int):
    return db.query(Course).filter(Course.id == id).first()

def read_courses_slice(db: Session, start: int = 0, end: int = 100):
    return db.query(Course).offset(start).limit(end).all()

def create_course(db: Session, course: CourseInsertion):
    generated_id = uuid.uuid4().hex[:24]
    db_course = Course(id=generated_id, **course.__dict__)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, id: int):
    sql = db.query(Course).filter(Course.id == id)
    course = copy(sql.first())
    sql.delete(synchronize_session=False)
    db.commit()
    return {'msg': 'deleted', 'course': course}

def update_course(db: Session, id: str, course: CourseInsertion):
    sql = db.query(Course).filter(Course.id == id)
    sql.update(course.__dict__)
    db.commit()
    return {'msg': 'updated', 'course': course}
