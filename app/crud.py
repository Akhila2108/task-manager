from sqlalchemy.orm import Session
from .schemas import TaskCreate, TaskUpdate, UserSignup
from . import security
from app import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, signup: UserSignup):
    if get_user_by_email(db, signup.email):
        return None
    db_user = models.User(
        email=signup.email,
        hashed_password=security.hash_password(signup.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        is_completed=task.is_completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return None

    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed

    db.commit()
    db.refresh(db_task)
    return db_task



def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
