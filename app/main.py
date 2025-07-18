from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, crud, database

app = FastAPI()

# Dependency for getting DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks")
def create_task(title: str, description: str = "", is_completed: bool = False, db: Session = Depends(get_db)):
    return crud.create_task(db, title=title, description=description, is_completed=is_completed)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str = None, description: str = None, is_completed: bool = None, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, title, description, is_completed)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
