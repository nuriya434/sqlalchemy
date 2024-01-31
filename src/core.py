from sqlalchemy import insert

from models import students 
from models import Student 
from database import engine, session_factory 
from models import metadata
from models import Course
# Создание таблицы в базе
def create_tables():
    metadata.drop_all (engine)
    metadata.create_all (engine)

def insert_data():
    with engine.connect() as connection:
        statement = insert(students).values(
            [
                {'first_name': 'test_user'}, 
                {'first_name":"test_user_2'},
            ]
        )
        connection.execute(statement)
        connection .commit()

def insert_data():
    with session_factory() as session:
        student_1 = Student (first_name='test_user_1231')
        student_2 = Student(first_name='test_user_3211')
        session.add_all([student_1, student_2]) 
        session.commit()



def insert_course_data():
    with session_factory() as session:
        course_1 = Course(name='Math')
        course_2 = Course(name='Physics')
        session.add_all([course_1, course_2])
        session.commit()
