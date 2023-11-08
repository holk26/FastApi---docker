from app.config.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func


class Work(Base):
    __tablename__ = "works"

    id_jod = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Título del trabajo
    location = Column(String(255), index=True)
    snippet = Column(String(1024))
    salary = Column(String(255))
    source = Column(String(255))
    type = Column(String(255))
    link = Column(String(255))  # Enlace al listado de trabajo
    company = Column(String(255))  # Nombre de la compañía
    updated = Column(DateTime, server_default=func.now(), onupdate=func.now())
    id = Column(String(255))
