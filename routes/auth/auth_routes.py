from fastapi import APIRouter
from config.db_config import SessionLocal
from fastapi import Depends,Body
from controllers.auth.auth_controller import login, logout, reset
from schemas.auth.auth_schemas import   ResponseAuth
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# autenticar usuario
@router.post("/login")
async def user_login(body_data= Body(...),db: Session = Depends(get_db)):
        try:
                userlogin = login(body_data, db)
                if userlogin:
                        return ResponseAuth(status="Ok", 
                                code="200", 
                                message="login successfully", 
                                token = userlogin)
       
                else:
                        return ResponseAuth(status="Ok", 
                                code="401 ", 
                                message="login incorrect")
       
        except Exception as e:
                return ResponseAuth(status="Error",
                          code="500",  
                          message="User error login{e}")
        

    
# salir de seccion usuario
@router.get("/logout")
def user_logout():
        return logout()
    
# reset pass
@router.post("/reset")
def pass_reset():
        return reset()