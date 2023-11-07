from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Aquí asumimos que DATABASE_URL está en tu archivo .env y tiene la cadena de conexión.
DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+mysqlconnector://root:admin@localhost:3306/users")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
