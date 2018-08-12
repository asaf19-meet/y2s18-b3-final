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

    def __repr__(self):
        return ("Student name: {}, Student's password: {}, Student's Location:{}".format(self.name, self.password, self.location))

class Tutor(Base):
    __tablename__ = "Tutors"
    username = Column(String, primary_key = True)
    name = Column(String)
    password = Column(String)
    location = Column(String)
    times = relationship("Time")
    def __repr__(self):
        return ("Tutor Name: {},Tutor's password: {}, Tutor's Location: {}, times: {}".format(self.name,self.password, self.location, self.times))

class Time(Base):
    __tablename__ = "Time"
    id = Column(Integer, primary_key = True)
    time = Column(String)
    subject = Column(String)
    # tutor = relationship("Tutor", back_populates="Time")
    tutor_username = Column(String, ForeignKey("Tutors.username"))

    def __repr__(self):
        return("time: {},{}")