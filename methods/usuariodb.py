from schemas.usuario import *
from models.models import UsuarioDB
from methods.cnx import SessionLocal
from uuid import uuid4

# Function to get all Usuarios 
def getUsuarios(activo=True):
    try:
        db = SessionLocal()
        usuarios = db.query(UsuarioDB).filter(UsuarioDB.activo == activo).all()
        if usuarios:
            db.close()
            return usuarios
        return None
    except Exception as e:
        raise e
    finally:
        db.close()

# Function to get one task
def getUsuarioDB(id: str):
    try:
        db = SessionLocal()
        usuario = db.query(UsuarioDB).filter(UsuarioDB.id == id).first()
        if usuario:
            db.close()
            return usuario
        return None
    except Exception as e:
        raise e                   
    
# Creation of "usuario" is used in the "POST" method
def createUsuarioDB(usuario: CreateUsuario):
    try:
        db = SessionLocal()
        new_usuario = UsuarioDB(
                        id=str(uuid4()),
                        usuario=usuario.usuario,
                        nombre=usuario.nombre, 
                        apellido=usuario.apellido, 
                        email=usuario.email, 
                        password=usuario.password               
                        )
        db.add(new_usuario)
        db.commit()
        db.refresh(new_usuario)
        return new_usuario
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close_all()

# Function to get update the "Usuario" is used in "PUT" methods
def updateUsuarioDB(id: str, updated_usuario: UpdateUsuario):
    try:
        db = SessionLocal()
        usuario = db.query(UsuarioDB).filter(UsuarioDB.id == id).first()
        print(usuario)
        if usuario:
            usuario.nombre=updated_usuario.nombre
            usuario.apellido=updated_usuario.apellido
            usuario.usuario=updated_usuario.usuario
            usuario.email=updated_usuario.email
            db.commit()
            db.refresh(usuario)
            return usuario
        return None
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Function to remove a "Usuario" by their ID, mode logical
def deleteUsuarioDB(id: str):
    try:
        db = SessionLocal()
        usuario = db.query(UsuarioDB).filter(UsuarioDB.id == id).first()
        if usuario:
            usuario.activo = False
            db.commit()
            db.refresh(usuario)
        db.close()
        return usuario
    except Exception as e:
        raise e
    finally:
        db.close()


def getUsuarioLoginDB(user:Login):
    try:
        db = SessionLocal()
        usuario = db.query(UsuarioDB).filter(UsuarioDB.password == user.password, UsuarioDB.usuario == user.usuario).first()
        if usuario:
            db.close()
            return usuario
        return None
    except Exception as e:
        raise e 

def changePasswordDB(user:ChangePassword):
    try:
        db = SessionLocal()
        usuario = db.query(UsuarioDB).filter(UsuarioDB.password == user.password, UsuarioDB.usuario == user.usuario).first()
        if usuario:
            usuario.password=user.newPassword
            db.commit()
            db.refresh(usuario)
            db.close()
            return usuario
        return None
    except Exception as e:
        raise e 