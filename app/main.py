from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import auth, crud, models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}


@app.post("/signup", response_model=schemas.UserPublic, status_code=201)
def signup(user_in: schemas.UserSignup, db: Session = Depends(get_db)):
    user = crud.create_user(db, user_in)
    if user is None:
        raise HTTPException(status_code=409, detail="Email already registered")
    return user


@app.post("/login", response_model=schemas.Token)
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, credentials.email, credentials.password)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )
    access_token = auth.create_access_token(subject=str(user.id))
    return schemas.Token(access_token=access_token)
