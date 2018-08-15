from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class Student(Base):
    __tablename__ = "students"
    username = Column(String, primary_key = True)
    name = Column(String)
    password = Column(String)
    location = Column(String)
    grade = Column(String)
    math_tutor_username = Column(String, ForeignKey("Tutors.username"))
    biology_tutor_username = Column(String, ForeignKey("Tutors.username"))
    physics_tutor_username = Column(String, ForeignKey("Tutors.username"))
    math_tutor = relationship("Tutor", back_populates="students_math", foreign_keys=[math_tutor_username])
    biology_tutor = relationship("Tutor", back_populates="students_biology", foreign_keys=[biology_tutor_username])
    physics_tutor = relationship("Tutor", back_populates="students_physics", foreign_keys=[physics_tutor_username])

    def __repr__(self):
        return ("Student name: {}, Student's password: {}, Student's Location:{}, Student's grade: {}".format(self.name, self.password, self.location, self.grade))

class Tutor(Base):
    __tablename__ = "Tutors"
    username = Column(String, primary_key = True)
    name = Column(String)
    password = Column(String)
    location = Column(String)
    subjects = Column(String)
    experience = Column(String)
    degree = Column(String)
    students_math = relationship("Student", back_populates="math_tutor")
    students_biology = relationship("Student", back_populates="bilogy_tutor")
    students_physics = relationship("Student", back_populates="physics_tutor")


    def __repr__(self):
        return ("Tutor Name: {},Tutor's password: {}, Tutor's Location: {}, subjects: {}, experience: {}, degree: {}".format(self.name,self.password, self.location, self.subjects, self.experience, self.degree))

# class Time(Base):
#     __tablename__ = "Time"
#     id = Column(Integer, primary_key = True)
#     time = Column(String)
#     subject = Column(String)
#     # tutor = relationship("Tutor", back_populates="Time")
#     tutor_username = Column(String, ForeignKey("Tutors.username"))

    # def __repr__(self):
    #     return("{},{}".format(self.time, self.subject))