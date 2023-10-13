from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class StudentSubject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")

Student.subjects = relationship("StudentSubject", back_populates="student")
Subject.students = relationship("StudentSubject", back_populates="subject")

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

artem = Student(name='Artem')
kevin = Student(name='Kevin')
viktor = Student(name='Viktor')

english = Subject(name='English')
math = Subject(name='Math')
history = Subject(name='History')

alice_subjects = [StudentSubject(student=artem, subject=english),
                  StudentSubject(student=artem, subject=math)]
bob_subjects = [StudentSubject(student=kevin, subject=english),
                StudentSubject(student=kevin, subject=history)]
carol_subjects = [StudentSubject(student=viktor, subject=math),
                  StudentSubject(student=viktor, subject=history)]

session.add_all([artem, kevin, viktor, english, math, history])
session.commit()

english_students = (
    session.query(Student)
    .join(StudentSubject)
    .join(Subject)
    .filter(Subject.name == 'English')
    .all()
)

for student in english_students:
    print(student.name)

average_students_per_subject = (
    session.query(
        StudentSubject.subject_id,
        func.count(StudentSubject.student_id).label("student_count")
    )
    .group_by(StudentSubject.subject_id)
    .subquery()
)

subjects_with_more_students = (
    session.query(Subject)
    .join(average_students_per_subject, Subject.id == average_students_per_subject.c.subject_id)
    .filter(average_students_per_subject.c.student_count > func.avg(average_students_per_subject.c.student_count))
    .all()
)

for subject in subjects_with_more_students:
    print(subject.name)