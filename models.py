from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    task_id: int
    title: str
    content: Optional[str] = None
    status: Optional[bool] = False


