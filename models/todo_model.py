from sqlalchemy import Column, String, Integer, BOOLEAN
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos" #table name
    
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, index=True) 
    description= Column(String, nullable=True)
    completed= Column(BOOLEAN, default=False)

