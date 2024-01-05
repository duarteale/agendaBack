from starlette.requests import Request
from fastapi import FastAPI, HTTPException
from routes.usuarios import usuario
from routes.contactos import contacto
from fastapi.middleware.cors import CORSMiddleware
from methods.cnx import SessionLocal
from models.models import *
from passlib.context import CryptContext

app = FastAPI()


# Origins admited
origins = ["*"]

# Add Middleware CORS (Cross-Origin Resource Sharing )
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Routes
app.include_router(usuario, prefix='/usuarios')
app.include_router(contacto, prefix='/contactos')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(password_plana, password_hash):
    return pwd_context.verify(password_plana, password_hash)

@app.get('/')
def root():
    return 'Estás entrando al backend, para swagger /docs'

@app.get('/test')
def test():
    resp = {'nombre':'Ale', 'apellido': 'Duarte'} #Para el navegador es un JSON
    return resp