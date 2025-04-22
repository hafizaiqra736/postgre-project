# grocery_schema.py
from pydantic import BaseModel
from typing import List

class GroceryBase(BaseModel):
    description: str
    tasks: List[str]
    completed: bool = False

class GroceryCreate(GroceryBase):
    pass

class GroceryShow(GroceryBase):
    id: int
    class Config:
        orm_mode = True

    class Config:
        from_attributes = True
       
