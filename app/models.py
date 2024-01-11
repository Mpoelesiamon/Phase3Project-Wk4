from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    class_name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    # teacher = relationship('Teacher', back_populates='classes')
    students = relationship('Student', back_populates='class')

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)

    classes = relationship('Class', back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    classes = relationship('Class', back_populates='teacher')

