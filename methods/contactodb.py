from schemas.contacto import Contacto, CreateContactoIn, CreateContactoOut, UpdateContacto
from models.models import ContactoDB
from methods.cnx import SessionLocal
from uuid import uuid4

# Funcion que nos muestra todos los Contactos
def getContactos(activo=True):
      try:
            db = SessionLocal()
            contactos = db.query(ContactoDB).filter(ContactoDB.activo == activo).all()
            if contactos:
                  db.close()
                  return contactos
            return None
      except Exception as e:
            raise e
      finally:
            db.close()

      # Function to get one task
def getContactoDB(id: str):
      try:
            db = SessionLocal()
            contacto = db.query(ContactoDB).filter(ContactoDB.id == id).first()
            if contacto:
                  db.close()
                  return contacto
            return None
      except Exception as e:
            raise e   
      
# Creation of "contacto" is used in the "POST" method
def createContactoDB(contacto: CreateContactoIn):
      try:
            db = SessionLocal()
            new_contacto = ContactoDB(
                              id=str(uuid4()),
                              nombre=contacto.nombre,
                              apellido=contacto.apellido, 
                              telefono=contacto.telefono,
                              email=contacto.email,
                              direccion=contacto.direccion,
                              ciudad=contacto.ciudad
                              )
            db.add(new_contacto)
            db.commit()
            db.refresh(new_contacto)
            return new_contacto
      except Exception as e:
            db.rollback()
            raise e
      finally:
            db.close_all()

# Function to get update the "contacto" is used in "PUT" methods
def updateContactoDB(id: str, updated_contacto: UpdateContacto):
      try:
            db = SessionLocal()
            contacto = db.query(ContactoDB).filter(ContactoDB.id == id).first()
            print(contacto)
            if contacto:
                  contacto.nombre=updated_contacto.nombre
                  contacto.apellido=updated_contacto.apellido
                  contacto.telefono=updated_contacto.telefono
                  contacto.email=updated_contacto.email
                  contacto.direccion=updated_contacto.direccion
                  contacto.ciudad=updated_contacto.ciudad

                  db.commit()
                  db.refresh(contacto)
                  return contacto
            return None
      except Exception as e:
            db.rollback()
            raise e
      finally:
            db.close()

# Function to remove a "contacto" by their ID, mode logical
def deleteContactoDB(id: str):
      try:
            db = SessionLocal()
            contacto = db.query(ContactoDB).filter(ContactoDB.id == id).first()
            if contacto:
                  contacto.activo = False
                  db.commit()
                  db.refresh(contacto)
            db.close()
            return contacto
      except Exception as e:
            raise e
      finally:
            db.close()
