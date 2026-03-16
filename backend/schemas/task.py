from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


# NEW TASK CREATING
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# GETTING TASKS


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: Optional[str]
    is_completed: bool
    created_at: datetime
