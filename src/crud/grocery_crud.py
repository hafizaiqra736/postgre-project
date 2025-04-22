# grocery_crud.py
from sqlalchemy.orm import Session
from src.models.grocery_model import Grocery
from src.schemas.grocery_schema import GroceryCreate

def create_grocery(db: Session, grocery: GroceryCreate):
    db_grocery = Grocery(**grocery.dict())
    db.add(db_grocery)
    db.commit()
    db.refresh(db_grocery)
    return db_grocery

def get_all_groceries(db: Session):
    return db.query(Grocery).all()

def get_grocery(db: Session, grocery_id: int):
    return db.query(Grocery).filter(Grocery.id == grocery_id).first()

def update_grocery(db: Session, grocery_id: int, grocery: GroceryCreate):
    db_grocery = db.query(Grocery).filter(Grocery.id == grocery_id).first()
    if db_grocery:
        for key, value in grocery.dict().items():
            setattr(db_grocery, key, value)
        db.commit()
        db.refresh(db_grocery)
    return db_grocery

def delete_grocery(db: Session, grocery_id: int):
    db_grocery = db.query(Grocery).filter(Grocery.id == grocery_id).first()
    if db_grocery:
        db.delete(db_grocery)
        db.commit()
    return db_grocery
