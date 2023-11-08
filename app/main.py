from fastapi import FastAPI
from .routes import job
from .config.base_class import Base
from .config.session import engine
from dotenv import load_dotenv

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(job.router)
