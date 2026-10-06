from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)     # Ej: Cyberpunk 2077 / Crash PC
    platform = Column(String(50), nullable=False)  # Ej: PC, PlayStation, Xbox

    # Relaciones con otras tablas
    articles = relationship("KnowledgeArticle", back_populates="category")
    tickets = relationship("Ticket", back_populates="category")


class KnowledgeArticle(Base):
    __tablename__ = "knowledge_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    keywords = Column(String(255), nullable=False) # Para búsquedas por palabras clave
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="articles")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    reference_code = Column(String(20), unique=True, index=True) # Ej: TCK-9482
    user_email = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    log_file_path = Column(String(255), nullable=True) # Ruta del archivo .log subido
    auto_tag = Column(String(50), nullable=True)        # Ej: GPU_CRASH
    deflected = Column(Boolean, default=False)         # Indica si el usuario resolvió con artículo
    created_at = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="tickets")