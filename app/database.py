import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Motor de conexión a PostgreSQL
engine = create_engine(DATABASE_URL)

# Sesión local para interactuar con la BD en cada petición
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredarán los modelos (tablas)
Base = declarative_base()

# Función generadora para obtener la sesión de la BD y cerrarla automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()