from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.task import TaskResponse, TaskCreate
from dependencies import get_db
from services import task as task_service

# Prefix
router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)


@router.post("", response_model=TaskResponse, status_code=201)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)


@router.patch("/{task_id}/done", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.mark_task_done(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
