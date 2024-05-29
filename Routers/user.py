from fastapi import Depends, Header,APIRouter,HTTPException,UploadFile,File
from sqlalchemy.orm import Session
from auth.auth_handler import decodeJWT
from model import UserModel,PositionModel
from database import SessionLocal, engine
import model
from auth.auth_handler import JWTBearer
from schema import UserSchema,UserControlSchema,AdminControlUserSchema
from datetime import datetime

router = APIRouter(prefix="/api/v1/user")  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("", summary="Lấy thông tin bản thân", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def get_user(
    authorization: str = Header(...),
    db: Session = Depends(get_database_session),
):
    # Decode JWT to get user information
    user = decodeJWT(authorization.split()[1])
    email = user.get("email")

    # Query the database to get the user along with the position name
    user_data = db.query(UserModel, PositionModel).join(PositionModel, UserModel.position_id == PositionModel.id).filter(UserModel.email == email).first()

    if user_data:
        user, position = user_data
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "address": user.address,
            "gender": user.gender,
            "dob": user.dob,
            "avatar": user.avatar,
            "position": position,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "deleted_at": user.deleted_at
        }
    else:
        return {"error": "User not found"}, 404
    
@router.get("/all", summary="Lấy thông tin tất cả user", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def get_user_all(
    db: Session = Depends(get_database_session),
):
    # Query the database to get the user along with the position name
    user_data = db.query(UserModel, PositionModel).join(PositionModel, UserModel.position_id == PositionModel.id).all()
    users = []
    for data in user_data:
        user, position = data
        users.append({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone,
                "address": user.address,
                "gender": user.gender,
                "dob": user.dob,
                "avatar": user.avatar,
                "position": position,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "deleted_at": user.deleted_at
            })
    return users
@router.patch("/update", summary="Cập nhật thông tin bản thân", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def update_user(
    user_update: UserControlSchema,
    authorization: str = Header(...),
    db: Session = Depends(get_database_session),
):
    user = decodeJWT(authorization.split()[1])
    email = user.get("email")

    user_data = db.query(UserModel).filter(UserModel.email == email).first()

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.name is not None:
        user_data.name = user_update.name
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


    db.commit()

    return {"message": "Cập nhật người dùng thành công"}
@router.patch("/avatar", summary="Cập nhật ảnh đại diện", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def update_avatar(
    authorization: str = Header(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_database_session),
):
    user = decodeJWT(authorization.split()[1])
    email = user.get("email")

    user_data = db.query(UserModel).filter(UserModel.email == email).first()

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    # Save the file to a designated location
    file_location = f"images/{user_data.id}_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    # Update the user's avatar field
    user_data.avatar = "/"+file_location
    user_data.updated_at =  datetime.now().strftime("%Y-%m-%d %H:%M")
    db.commit()

    return {"message": "Cập nhật ảnh đại diện thành công", "avatar": file_location}
# @router.patch("/update/{user_id}", summary="Cập nhật thông tin bản thân", dependencies=[Depends(JWTBearer().has_role([1]))])
# async def update_user(
#     user_id: str,
#     user_update: AdminControlUserSchema,
#     db: Session = Depends(get_database_session),
# ):
#     user_data = db.query(UserModel).filter(UserModel.id == user_id).first()

#     if not user_data:
#         raise HTTPException(status_code=404, detail="User not found")

#     if user_update.name is not None:
#         user_data.name = user_update.name
#     if user_update.email is not None:
#         user_data.email = user_update.email
#     if user_update.phone is not None:
#         user_data.phone = user_update.phone
#     if user_update.address is not None:
#         user_data.address = user_update.address
#     if user_update.gender is not None:
#         user_data.gender = user_update.gender
#     if user_update.dob is not None:
#         user_data.dob = user_update.dob
#     if user_update.description is not None:
#         user_data.description = user_update.description
#     if user_update.position_id is not None:
#         user_data.position_id = user_update.position_id
#     db.commit()

#     return {"message": "Cập nhật người dùng thành công"}