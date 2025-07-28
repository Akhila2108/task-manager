# Task Manager API

A FastAPI-based task management API with PostgreSQL as the database and Docker for containerization.

---

## Features

- Create, Read, Update, Delete (CRUD) tasks
- Swagger UI docs at `http://localhost:8000/docs`
- PostgreSQL integration via SQLAlchemy
- Dockerized for easy setup

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Akhila2108/task-manager.git
cd task-manager
```

2. **Start the app using Docker**

```bash
docker-compose up --build
```

This will:
- Set up the PostgreSQL container (`task-manager-db`)
- Build and run the FastAPI app (`task-manager-web`)
- Mount the project directory to the container

3. **Access the API**

Once the app is running, open browser and visit:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---


## Project Structure

```
task-manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & routes
│   ├── crud.py          # CRUD logic
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB session & engine setup
│   └── create_db.py     # DB table creation script
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Manually Create Tables (Optional)

If you want to manually create database tables outside Docker:

```bash
python app/create_db.py
```

---

## Future Improvements

- [ ] Add authentication with OAuth2 or JWT
- [ ] Add task deadlines and priorities
- [ ] Add filtering/searching on task list
- [ ] Write unit tests with `pytest`

