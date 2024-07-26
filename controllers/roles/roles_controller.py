from sqlalchemy.orm import Session
from models.rol.rol_model import Role
from schemas.roles.roles_schemas import RolSchema
import json

#todos los usarios
def get_all_rol(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(Role).offset(skip).limit(limit).all()
    return roles

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