from fastapi import APIRouter
from fastapi import HTTPException
from schemas.contacto import Contacto, CreateContactoIn, CreateContactoOut, UpdateContacto
from methods.contactodb import getContactoDB, getContactos, createContactoDB, updateContactoDB, deleteContactoDB
from typing import List

contacto = APIRouter()

# Method for contactos
@contacto.get('', response_model=List[Contacto], tags=['Contactos'])
async def get_all_contactos():
    # Send all contactos
    try:
        contactos = getContactos()
        if contactos:
            return contactos
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'Contactos: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting Contactos: {e}")


@contacto.get('/eliminados', response_model=List[Contacto], tags=['Contactos'])
async def get_all_contactos():
    # Send all contactos
    try:
        contacto = getContactos(activo=False)
        if contacto:
            return contacto
        # If not found, return 404
        raise HTTPException(status_code=404, detail=f'Contactos: not found')
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"Error getting Contactos: {e}")
    
@contacto.get('/{id}', response_model=Contacto, tags=['Contactos'])
async def get_contacto(id: str):
    # Check if contacto exists
    try:
        contacto = getContactoDB(id=id)
        if contacto:
            return contacto
        raise HTTPException(status_code=404, detail=f'Contacto: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error getting Contacto {id}: {e}")

@contacto.post('', response_model=CreateContactoOut, tags=['Contactos'])
async def create_contacto(contacto: CreateContactoIn):
    try:
        new_contacto = createContactoDB(contacto=contacto)
        return new_contacto
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: Contacto creation failed: {e}")

@contacto.put('/{id}', response_model=UpdateContacto, tags=['Contactos'])
async def update_contacto(id: str, contacto: UpdateContacto):
    try:
        updatedContacto = updateContactoDB(id=id, updated_contacto=contacto)
        if updatedContacto:
            return updatedContacto
        raise HTTPException(status_code=404, detail=f'Contacto: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Update Failed for Contacto ID: {id}, Error {e}")

@contacto.delete('/{id}', response_model=Contacto, tags=['Contactos'])
async def delete_contacto(id: str):
    try:
        deleteContacto = deleteContactoDB(id=id)
        if deleteContacto:
            return deleteContacto
        raise HTTPException(status_code=404, detail=f'Contacto: {id} not found')
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Delete Failed for Contacto ID: {id}, Error {e}")
