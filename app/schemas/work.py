from pydantic import BaseModel


class JobBase(BaseModel):
    title: str


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int

    class Config:
        orm_mode = True
