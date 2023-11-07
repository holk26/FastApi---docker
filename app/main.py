from fastapi import FastAPI
from .routes import work_routes
from .config.base_class import Base
from .config.session import engine
from dotenv import load_dotenv

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(work_routes.router)
