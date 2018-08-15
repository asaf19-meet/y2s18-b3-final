# Database related imports
# Make sure to import your tables!
from model import Base, Student, Tutor

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///Project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


# Your database functions are located under here (querying, adding items, etc.)
def auth_student(student_username, student_password):
    session = DBSession()
    student = session.query(Student).filter_by(username = student_username, password= student_password).first()
    print(student)
    return student

def auth_tutor(tutor_username, tutor_password):
    session = DBSession()
    tutor = session.query(Tutor).filter_by(username = tutor_username, password= tutor_password).first()
    print(tutor)
    return tutor

def delete_all_students():
    session = DBSession()
    session.query(Student).delete()
    session.commit()

def delete_all_tutors():
    session = DBSession()
    session.query(Tutor).delete()
    session.commit()


def add_student(student_username, student_password, student_name, student_location, student_grade, student_phone_number):
    print("Added a student!")
    session = DBSession()
    student = Student(username=student_username,password=student_password, name=student_name, location=student_location, grade = student_grade, phone_number = student_phone_number)
    session.add(student)
    session.commit()

def get_tutor_by_username(username):
    session = DBSession()
    tutors = session.query(Tutor).filter_by(username = username).first()
    return tutors


def get_tutors():
    session = DBSession()
    tutors = session.query(Tutor).all()
    return tutors

def get_students():
    session = DBSession()
    students = session.query(Student).all()
    return students    

def get_student_by_username(username):
    session = DBSession()
    student = session.query(Student).filter_by(username= username).first()
    return student

def get_tutors_by_subject(subject):
    session = DBSession()
    tutors = session.query(Tutor).filter_by(subjects = subject).all()
    return tutors

def add_tutor(tutor_username, tutor_password, tutor_name, tutor_location, tutor_subjects, tutor_experience, tutor_degree):
    print("Added a tutor!")
    session = DBSession()
    tutor = Tutor(username = tutor_username, name = tutor_name, password = tutor_password, location = tutor_location, subjects = tutor_subjects, experience = tutor_experience, degree = tutor_degree)
    session.add(tutor)
    session.commit()

def connect_student_tutor_biology(student_username,tutor_username):
    session = DBSession()
    student = session.query(Student).filter_by(username= student_username).first()
    student.biology_tutor_username = tutor_username
    session.commit()

def connect_student_tutor_math(student_username,tutor_username):
    session = DBSession()
    student = session.query(Student).filter_by(username= student_username).first()
    student.math_tutor_username = tutor_username
    session.commit()

def connect_student_tutor_physics(student_username,tutor_username):
    session = DBSession()
    student = session.query(Student).filter_by(username= student_username).first()
    student.physics_tutor_username = tutor_username
    session.commit()

connections = {
    "biology" : connect_student_tutor_biology,
    "math" : connect_student_tutor_math,
    "physics" : connect_student_tutor_physics
}
# def add_time(time, subject, tutor_username):
#     print("Added Time!")
#     session = DBSession()
#     time = Time(time = time, subject = subject, tutor_username = tutor_username)
#     session.add(time)
#     session.commit()b

# add_tutor("bs","bs","bs","bs","bs","bs", "bs")
# add_student("asi", "123456","asafi", "Nazareth", "10th")
# add_time("friday", "CS", "usernme")
# add_tutor("fs","fs","Mohammad","Jerusalem","biology","3 years","11th grade")
# print(get_tutors())
# print(get_students())
# connect_student_tutor_physics("asi","bs")
# print(get_students())