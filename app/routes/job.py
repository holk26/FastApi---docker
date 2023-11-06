from fastapi import APIRouter, HTTPException
from ..models import work as models
from ..schemas import work as schemas
from ..config.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/jobs/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return models.create_job(db=db, job=job)


@router.get("/jobs/", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = models.get_jobs(db, skip=skip, limit=limit)
    return jobs


@router.get("/jobs/{job_id}", response_model=schemas.Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = models.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job
