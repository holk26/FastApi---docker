from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class WorkBase(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    snippet: Optional[str] = None
    salary: Optional[float] = None
    source: Optional[str] = None
    type: Optional[str] = None
    link: Optional[str] = None
    company: Optional[str] = None
    updated: Optional[datetime] = None
    id: Optional[int] = None


class WorkCreate(WorkBase):
    pass  # No need to repeat fields, they are inherited from WorkBase


class Work(WorkBase):
    # Make sure this is named correctly, previously it was 'id_jod'
    id_job: Optional[int] = None

    class Config:
        orm_mode = True
