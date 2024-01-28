from sqlalchemy import Column, Integer, String, Text, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    birthDay = Column(DateTime, nullable=False)
    
    
class Score(Base):
    __tablename__ = "score"
    
    id = Column(Integer, primary_key=True)
    korean = Column(Integer,nullable=False)
    english = Column(Integer,nullable=False)
    math = Column(Integer,nullable=False)
    history = Column(Integer,nullable=False)
    name_id = Column(String,ForeignKey("person.name"))
    name = relationship("Person",backref="scores")
    