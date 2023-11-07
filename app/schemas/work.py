from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WorkBase(BaseModel):
    title: str
    location: str
    snippet: Optional[str] = None
    salary: Optional[str] = None
    source: str
    type: Optional[str] = None
    link: str
    company: str
    updated: datetime
    id: int


class WorkCreate(WorkBase):
    title: str
    location: str
    snippet: Optional[str] = None
    salary: Optional[float] = None
    source: str
    type: Optional[str] = None
    link: str
    company: str
    updated: datetime


class Work(WorkBase):
    id_jod: int

    class Config:
        orm_mode = True
