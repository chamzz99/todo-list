from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate


def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, limit: int = 5):
    return db.query(Task)\
        .filter(Task.is_completed == False)\
        .order_by(Task.created_at.desc(), Task.id.desc())\
        .limit(limit)\
        .all()


def mark_task_done(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db_task.is_completed = True
        db.commit()
        db.refresh(db_task)
    return db_task
