from sqlalchemy.orm import Session
from models.rol.rol_model import Role
from schemas.roles.roles_schemas import RolSchema
import json

#todos los usarios
def get_all_rol(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(Role).offset(skip).limit(limit).all()
    return roles

#un usuario por id
def get_rol(db: Session, rol_id: int):
     return db.query(Role).filter(Role.id == rol_id).first()

#creamos usuario
def create_rol(db: Session, rol_data: RolSchema):
   
    name = rol_data['name']
    name_json = json.dumps(name)
    ability_json  = rol_data['ability']
 
    _Role = Role(
        name = name_json.strip('"'),
        ability = ability_json,
    )
    
    db.add(_Role)
    db.commit()
    db.refresh(_Role)
    return _Role

#eliminar rol por id
def delete_rol(db: Session, rol_id: int) -> bool:
    rol_to_delete = get_rol(db=db, rol_id=rol_id)
    if rol_to_delete is None:
        return False
    db.delete(rol_to_delete)
    db.commit()

    return True