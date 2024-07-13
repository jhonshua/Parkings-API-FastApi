from fastapi import APIRouter
from controllers.user_controller import get_all_users, create_user, get_user, update_user, delete_user

router = APIRouter()

# Retorna todos los usuarios
@router.get("/")
def get_all_users_data():
    return get_all_users()  # Debería ser: return get_user()

# Retorna un usuario específico por ID
@router.get("/{user_id}")
def get_single_user(user_id: int):
    return get_user(user_id)

# Crear un usuario
@router.post("/", status_code=201)
def create_single_user(user_data: dict):
    return create_user(user_data)

# Actualizar un usuario por ID
@router.put("/{user_id}", status_code=202)
def update_single_user(user_id: int, new_data: dict):
    return update_user(user_id, new_data)

# Eliminar un usuario por ID
@router.delete("/{user_id}", status_code=200)
def delete_single_user(user_id: int):
    return delete_user(user_id)
