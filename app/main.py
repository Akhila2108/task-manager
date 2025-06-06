from fastapi import FastAPI
from typing import List

app = FastAPI()

# Dummy in-memory task list
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Build FastAPI App", "completed": True},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Task Manager!"}

@app.get("/tasks")
def get_tasks() -> List[dict]:
    return tasks
