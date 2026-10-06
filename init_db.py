
from app.database import engine, Base
from app.models import Category, KnowledgeArticle, Ticket


def initialize_database():
    print("Conectando a la base de datos PostgreSQL en Docker...")
    # Lee los modelos y crea las tablas si no existen
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas exitosamente en PostgreSQL!")

if __name__ == "__main__":
    initialize_database()