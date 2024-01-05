from pydantic import BaseModel
from uuid import uuid4

class Contacto(BaseModel):
    id: str = str(uuid4())
    nombre: str
    apellido: str
    telefono: str
    email: str
    direccion: str
    ciudad: str    

class CreateContactoIn(BaseModel):
    nombre: str
    apellido: str
    telefono:str
    email: str
    direccion: str
    ciudad: str    

class CreateContactoOut(BaseModel):
    id: str = str(uuid4())
    nombre: str
    apellido: str
    telefono:str
    email: str
    direccion: str
    ciudad: str    

class UpdateContacto(BaseModel):
    nombre: str
    apellido: str
    telefono:str
    email: str    
    direccion: str
    ciudad: str    