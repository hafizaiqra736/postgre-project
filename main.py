from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.todo_model import Todo
from pydantic import BaseModel
from typing import List, Optional


#create database tables
Todo.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}


#dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db # value pose and return when function call not build connection again and again
    finally:
        db.close()
        
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

    
class TodoResponse(TodoCreate):
    id: int
    model_config = {
        "from attributes":True
    }  
    
#create a new todo
@app.post("/todos/", response_model=TodoResponse)
def create_todo(todo: TodoCreate,db: Session = Depends(get_db)):
    try:
      db_todo = Todo(title=todo.title, description=todo.description, completed= todo.completed)
      #jab hmain db ki values ko change krna to yh 3 use krta
      db.add(db_todo) #added data
      db.commit() #final db ka andr affect kary ga
      db.refresh(db_todo) # db change by refresing
      return db_todo
    except Exception as e:
      print("an exception occurred", e)
        

#get all todos
@app.get("/todos/")
def get_todos(db:Session = Depends(get_db)):
    return db.query(Todo).all()

#get a Todo by ID
@app.get("/todos/{tod_id}")
def fet_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
    