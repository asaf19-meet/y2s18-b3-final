# Database related imports
# Make sure to import your tables!
from model import Base, Student, Tutor, Time

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

def add_student(student_username, student_password, student_name, student_location, student_grade):
    print("Added a student!")
    session = DBSession()
    student = Student(username=student_username,password=student_password, name=student_name, location=student_location, grade = student_grade)
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

def add_tutor(tutor_username, tutor_password, tutor_name, tutor_location, tutor_experience, tutor_degree):
    print("Added a tutor!")
    session = DBSession()
    tutor = Tutor(username = tutor_username, name = tutor_name, password = tutor_password, location = tutor_location, experience = tutor_experience, degree = tutor_degree)
    session.add(tutor)
    session.commit()

def add_time(time, subject, tutor_username):
    print("Added Time!")
    session = DBSession()
    time = Time(time = time, subject = subject, tutor_username = tutor_username)
    session.add(time)
    session.commit()

if __name__ == '__main__':
    # add_student("asi", "123456","asafi", "Nazareth", "10th")
    # add_time("friday", "CS", "usernme")
    pass
print(get_students())

print(get_tutors())