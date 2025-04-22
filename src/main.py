# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.grocery_schema import GroceryCreate, GroceryShow
from src.crud import grocery_crud
from src.session.get_db import get_db
from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/groceries/", response_model=GroceryShow)
def create_item(grocery: GroceryCreate, db: Session = Depends(get_db)):
    return grocery_crud.create_grocery(db, grocery)

@app.get("/groceries/", response_model=list[GroceryShow])
def read_items(db: Session = Depends(get_db)):
    return grocery_crud.get_all_groceries(db)

@app.get("/groceries/{grocery_id}", response_model=GroceryShow)
def read_item(grocery_id: int, db: Session = Depends(get_db)):
    item = grocery_crud.get_grocery(db, grocery_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/groceries/{grocery_id}", response_model=GroceryShow)
def update_item(grocery_id: int, grocery: GroceryCreate, db: Session = Depends(get_db)):
    return grocery_crud.update_grocery(db, grocery_id, grocery)

@app.delete("/groceries/{grocery_id}")
def delete_item(grocery_id: int, db: Session = Depends(get_db)):
    grocery_crud.delete_grocery(db, grocery_id)
    return {"message": "Deleted"}
