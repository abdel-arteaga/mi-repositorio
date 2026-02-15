from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(150), nullable=False)
    genero = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False)  # "Leído" o "No leído"

    def __repr__(self):
        return f"<Libro(titulo='{self.titulo}', autor='{self.autor}')>"