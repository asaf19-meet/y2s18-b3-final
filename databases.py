# Database related imports
# Make sure to import your tables!
from model import Base, Student, Tutor, Time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///Student.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)


def add_student(student_name, student_location):
    print("Added a student!")
    student = Student(name=student_name, location=student_location)
    session.add(student)
    session.commit()

def get_tutor_by_username():
    tutors = session.query(Tutor).all()
    return tutors

def add_tutor(tutor_username, tutor_name, tutor_password, tutor_location):
    print("Added a tutor!")
    tutor = Tutor(username = tutor_username, name = tutor_name, password = tutor_password, location = tutor_location)
    session.add(tutor)
    session.commit()

def add_time(time, subject, tutor_username):
    print("Added Time!")
    time = Time(time = time, subject = subject, tutor_username = tutor_username)
    session.add(time)
    session.commit()


# add_tutor("usernme","Mohammad", "passworddd", "Jerusalem")

# add_time("monday", "CS", "usernme")

print(get_tutor_by_username())