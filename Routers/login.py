from fastapi import Depends, Form,status,APIRouter, Header,UploadFile,File
from fastapi.responses import JSONResponse
from sqlalchemy import exists
import base64
from auth.auth_handler import decodeJWT
from sqlalchemy.orm import Session
from auth.auth_handler import signJWT,JWTBearer
from model import UserModel,PositionModel
from datetime import datetime
import uuid
from schema import UserSchema
import shutil
import os
# import schema
from database import SessionLocal, engine
import model
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()  
model.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
class UserLogin(BaseModel):
    email: str
    password: str
class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str
    new_confirm_password: str
class UserCreate(BaseModel):
    name: str
    dob: str
    gender: int
    phone: str
    address: str
    email: str
    password: str
    position_id: str
    description: str
@router.post("/api/v1/signup", summary="Đăng ký")
async def create_account(
    user: UserCreate,
    db: Session = Depends(get_database_session)
):
    user_exists = db.query(exists().where(UserModel.email == user.email)).scalar()
    if user_exists:
        return JSONResponse(status_code=400, content={"message": "Tài khoản bị trùng"})
    elif len(user.password) < 8:
        return JSONResponse(status_code=400, content={"message": "Mật khẩu tối thiểu là 6 ký tự"})
    hashed_password = pwd_context.hash(user.password)

    new_user = UserModel(
        id=str(uuid.uuid4()).replace('-', '')[:8],
        name=user.name,
        email=user.email,
        password=hashed_password,
        phone=user.phone,
        address=user.address,
        gender=user.gender,
        position_id=user.position_id,
        dob=user.dob,
        description=user.description,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "data": "Tài khoản đã được tạo thành công!"
    }

@router.post("/api/v1/login", status_code=status.HTTP_200_OK, summary="Đăng nhập")
async def login(user_login: UserLogin, db: Session = Depends(get_database_session)):
    email = user_login.email
    password = user_login.password

    if password == '1':
        return JSONResponse(status_code=400, content={"message": "Sai mật khẩu"})
    user_exists = db.query(exists().where(UserModel.email == email)).scalar()
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user.deleted_at:
        return JSONResponse(status_code=400, content={"message": "Tài khoản đã bị ngưng kích hoạt, vui lòng liên hệ quản trị viên để nhận được hỗ trợ"})

    if not user_exists:
        return JSONResponse(status_code=400, content={"message": "Không có tài khoản"})
    elif not pwd_context.verify(password, user.password):
        return JSONResponse(status_code=400, content={"message": "Sai mật khẩu"})
    else:
        role = db.query(PositionModel).filter(PositionModel.id == user.position_id).first().role
        return signJWT(email, user.id, role)  


# @router.post("/api/v1/refresh")
# async def refresh_token(refresh_token: str):
#     return refresh_access_token(refresh_token)


#Đổi mật khẩu
@router.patch("/api/v1/change_password", dependencies=[Depends(JWTBearer().has_role([2, 1]))], summary="Đổi mật khẩu")
async def change_password(
    password: PasswordUpdate,
    db: Session = Depends(get_database_session),
    authorization: str = Header(...),
):
    Duser = db.query(UserModel).filter(UserModel.email == email).first()
    user = decodeJWT(authorization.split()[1])
    email = user.get("email")
    if Duser is None:
        return JSONResponse(status_code=404, content={"message": "Người dùng không tồn tại!"})
    if not pwd_context.verify(password.old_password, Duser.password):
        return JSONResponse(status_code=400, content={"message": "Sai mật khẩu!"})
    if password.new_password != password.new_confirm_password:
        return JSONResponse(status_code=400, content={"message": "Mật khẩu xác nhận không khớp!"})
    if len(password.new_password) < 8:
        return JSONResponse(status_code=400, content={"message": "Mật khẩu quá ngắn!"})
    hashed_new_password = pwd_context.hash(password.new_password)
    Duser.password = hashed_new_password
    db.commit()
    db.refresh(Duser)
    return JSONResponse(status_code=200, content={"message": "Đổi mật khẩu thành công!"})