from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from app.config.base_class import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Job).offset(skip).limit(limit).all()


def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()


def create_job(db: Session, job: schemas.JobCreate):
    db_job = Job(title=job.title)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
