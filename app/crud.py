from sqlalchemy.orm import Session
from app import models

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, title: str, description: str = "", is_completed: bool = False):
    task = models.Task(title=title, description=description, is_completed=is_completed)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(db: Session, task_id: int, title: str = None, description: str = None, is_completed: bool = None):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if is_completed is not None:
            task.is_completed = is_completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
