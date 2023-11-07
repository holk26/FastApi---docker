from fastapi import APIRouter, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.config.session import SessionLocal
from app.models.work import Work
import requests
import json
import os
from dotenv import load_dotenv
from app.schemas.work import WorkCreate
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

load_dotenv()
router = APIRouter()
api_key = os.getenv("API_KEY_JOOBLE")
print(api_key)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/data")
def get_work_online():
    url = "https://es.jooble.org/api/" + api_key
    headers = {"Content-type": "application/json"}
    data = json.dumps({"keywords": "it", "location": "Madrid"})
    response = requests.post(url, headers=headers, data=data)
    return response.json()


@router.post("/api/data")
def save_work(db: Session = Depends(get_db)):
    url = "https://es.jooble.org/api/" + os.getenv("API_KEY_JOOBLE")
    headers = {"Content-type": "application/json"}
    data = json.dumps({"keywords": "it", "location": "Madrid"})
    response = requests.post(url, headers=headers, data=data)
    jobs = response.json().get('jobs', [])
    for job_data in jobs:
        try:
            # Intenta crear una instancia de WorkCreate con los datos obtenidos
            job = WorkCreate(**job_data)
            work = Work(**job.dict())
            db.add(work)
        except ValidationError as e:
            # Maneja los errores de validación aquí
            # Por ejemplo, puedes decidir continuar con el siguiente trabajo,
            # registrar el error, o detener el proceso y devolver un error HTTP.
            # Aquí se continúa con el siguiente trabajo después de registrar el error.
            print(
                f"Error de validación para el trabajo: {job_data['title']}, {e}")

    try:
        # Intenta cometer todos los trabajos agregados a la sesión de la base de datos.
        db.commit()
    except SQLAlchemyError as e:
        # Si hay un error de SQLAlchemy durante el commit, haz rollback y devuelve un error HTTP.
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "success", "jobs_saved": len(jobs)}


@router.get("/api/data/{id_jod}")
def get_work(id_jod: Optional[int] = None, db: Session = Depends(get_db)):
    if id_jod is not None:
        work = db.query(Work).filter(Work.id_jod == id_jod).first()
        if work is None:
            raise HTTPException(
                status_code=404, detail="Trabajo no encontrado")
        return work
    else:
        works = db.query(Work).all()
        return works
