from fastapi import Depends, Header,APIRouter,HTTPException,Body
from sqlalchemy.orm import Session
from auth.auth_handler import decodeJWT
from model import UserModel,PositionModel
from database import SessionLocal, engine
import model
from auth.auth_handler import JWTBearer
from schema import UserSchema,UserControlSchema,AdminControlUserSchema
from datetime import datetime

router = APIRouter(prefix="/api/v1/admin")  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.patch("/user/update/{user_id}", summary="Cập nhật thông tin bản thân", dependencies=[Depends(JWTBearer().has_role([1]))])
async def update_user(
    user_id: str,
    user_update: AdminControlUserSchema,
    db: Session = Depends(get_database_session),
):
    user_data = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.name is not None:
        user_data.name = user_update.name
    if user_update.email is not None:
        user_data.email = user_update.email
    if user_update.phone is not None:
        user_data.phone = user_update.phone
    if user_update.address is not None:
        user_data.address = user_update.address
    if user_update.gender is not None:
        user_data.gender = user_update.gender
    if user_update.dob is not None:
        user_data.dob = user_update.dob
    if user_update.description is not None:
        user_data.description = user_update.description
    if user_update.position_id is not None:
        user_data.position_id = user_update.position_id
    db.commit()

    return {"message": "Cập nhật người dùng thành công"}
@router.patch("/user/activate/{user_id}", summary="Thay đổi trạng thái tài khoản thành công", dependencies=[Depends(JWTBearer().has_role([1]))])
async def update_user(
    user_id: str,
    db: Session = Depends(get_database_session),
):
    user_data = db.query(UserModel).filter(UserModel.id == user_id).first()
    deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    if user_data.deleted_at != None:
        user_data.deleted_at = None
        db.commit()
    else:
        user_data.deleted_at = deleted_at
        db.commit()


    return {"message": "Thay đổi trạng thái tài khoản thành công"}
