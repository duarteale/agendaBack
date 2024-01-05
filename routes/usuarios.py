from fastapi import APIRouter
from fastapi import HTTPException
from schemas.usuario import *
from methods.usuariodb import *
from typing import List

usuario = APIRouter()

# Method for Usuarios
@usuario.get('', response_model=List[Usuario], tags=['Usuarios'])
async def get_all_usuarios():
    # Send all usuarios
    try:
        usuarios = getUsuarios()
        if usuarios:
            return usuarios
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'Usuarios: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting usuarios: {e}")

@usuario.get('/eliminados', response_model=List[Usuario], tags=['Usuarios'])
async def get_all_usuarios():
    # Send all usuarios
    try:
        usuarios = getUsuarios(activo=False)
        if usuarios:
            return usuarios
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'Usuarios: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting usuarios: {e}")
    
@usuario.get('/{id}', response_model=Usuario, tags=['Usuarios'])
async def get_usuario(id: str):
    # Check if usuarios exists
    try:
        usuario = getUsuarioDB(id=id)
        if usuario:
            return usuario
        raise HTTPException(status_code=404, detail=f'Usuario: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting usuario {id}: {e}")

@usuario.post('', response_model=CreateUsuarioOut, tags=['Usuarios'])
async def create_usuario(usuario: CreateUsuario):
    try:
        new_usuario = createUsuarioDB(usuario=usuario)
        return new_usuario
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: Usuario creation failed: {e}")

@usuario.put('/{id}', response_model=UpdateUsuario, tags=['Usuarios'])
async def update_usuario(id: str, usuario: UpdateUsuario):
    try:
        updatedUsuario = updateUsuarioDB(id=id, updated_usuario=usuario)
        if updatedUsuario:
            return updatedUsuario
        raise HTTPException(status_code=404, detail=f'Usuario: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Usuario ID: {id}, Error {e}")

@usuario.delete('/{id}', response_model=Usuario, tags=['Usuarios'])
async def delete_usuario(id: str):
    try:
        deleteUsuario = deleteUsuarioDB(id=id)
        if deleteUsuario:
            return deleteUsuario
        raise HTTPException(status_code=404, detail=f'Usuario: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Delete Failed for Usuario ID: {id}, Error {e}")


    
@usuario.post('/login', response_model=Usuario, tags=['Usuarios'])
async def login(user:Login):
    # Check if usuarios exists
    try:
        usuario = getUsuarioLoginDB(user=user)
        if usuario:
            return usuario
        raise HTTPException(status_code=404, detail=f'Usuario: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting usuario {id}: {e}")
    
@usuario.post('/changepassword', response_model=Usuario, tags=['Usuarios'])
async def changePassword(user:ChangePassword):
    try:
        usuario = changePasswordDB(user=user)
        if usuario:
            return usuario
        raise HTTPException(status_code=404, detail=f'Usuario: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Usuario ID: {id}, Error {e}")