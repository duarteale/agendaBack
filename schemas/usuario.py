from pydantic import BaseModel
from uuid import uuid4

class Usuario(BaseModel):
    id: str = str(uuid4())
    usuario: str
    nombre: str
    apellido: str
    email: str

class CreateUsuario(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str
    password: str

class CreateUsuarioOut(BaseModel):
    id: str = str(uuid4())
    usuario: str
    nombre: str
    apellido: str
    email: str

class UpdateUsuario(BaseModel):
    usuario: str
    nombre: str
    apellido: str
    email: str

class Login(BaseModel):
    usuario: str
    password: str

#Crear la ruta, el metodo PUT/PATCH siempre en usuario.
class ChangePassword(BaseModel):
    usuario: str
    password: str
    newPassword: str