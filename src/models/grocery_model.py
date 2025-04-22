# grocery_model.py
from sqlalchemy import Column, Integer, String, Boolean, JSON
from src.config.database import Base

class Grocery(Base):
    __tablename__ = "grocery_tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    tasks = Column(JSON)  # For example: ["sugar", "oil"]
    completed = Column(Boolean, default=False)
