from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OpenTaskAPI")

@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task_status(db, task_id, task.status)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}