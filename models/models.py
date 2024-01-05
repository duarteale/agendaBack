from sqlalchemy import ForeignKey
from sqlalchemy import String, Boolean
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class ContactoDB(Base):
    __tablename__ = "contacto"
    id = Column(String(250), primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(20))
    telefono = Column(String(25))
    email = Column(String(80))
    direccion = Column(String(30))
    ciudad = Column(String(30))
    activo = Column(Boolean, default=True)

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(String(250), primary_key=True)
    usuario = Column(String(50), unique=True, nullable=False)
    apellido = Column(String(20))
    nombre = Column(String(25))
    email = Column(String(80))
    password = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True)