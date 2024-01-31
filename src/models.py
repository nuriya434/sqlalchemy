from sqlalchemy import (Column, Integer, MetaData, String, Table,)
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Student (Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]

metadata = MetaData()
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='course')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='students')
