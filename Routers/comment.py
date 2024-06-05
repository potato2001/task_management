from fastapi import Depends, APIRouter,HTTPException
from sqlalchemy import exists
from sqlalchemy.orm import Session
from model import CommentModel,UserModel,TaskModel, PositionModel
from database import SessionLocal, engine
from schema import CommentSchema
import model
from datetime import datetime
import uuid
from auth.auth_handler import JWTBearer

router = APIRouter(prefix="/api/v1/comment")  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Thêm loại sản phẩm
@router.post("/create", summary="Tạo Comment")
async def create_comment(
    commmentSchema: CommentSchema,
    db: Session = Depends(get_database_session),
):
    new_comment = CommentModel(
        id=str(uuid.uuid4()).replace('-', '')[:8],  
        message=commmentSchema.message,
        task_id=commmentSchema.task_id,
        user_id=commmentSchema.user_id,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "Tạo comment thành công"}

# Sủa loại sản phẩm
@router.patch("/update/{comment_id}", summary="Cập nhật Comment",dependencies=[Depends(JWTBearer().has_role([1,2,3]))])
async def update_tag(
    comment_id: str,
    message: str,
    db: Session = Depends(get_database_session),
):
    existing_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not existing_comment:
        raise HTTPException(status_code=404, detail="Comment không tồn tại!")

    existing_comment.message = message
    existing_comment.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    existing_comment.deleted_at =None

  
    db.commit()
    db.refresh(existing_comment)

    return {"message": "Chỉnh sửa Comment thành công"}

#Lấy tất cả loại sản phẩm
@router.get("/comments_in_task/{task_id}", summary="Lấy tất cả comment theo task")
def get_comments_in_task(
    task_id: str,
    db: Session = Depends(get_database_session),
):
    comments = (
        db.query(CommentModel)
        .join(UserModel, CommentModel.user_id == UserModel.id)
        .join(TaskModel, CommentModel.task_id == TaskModel.id)
        .filter(CommentModel.task_id == task_id)
        .order_by(CommentModel.created_at.desc())  # Ordering by created_at from past to present
        .all()
    )
    
    if not comments:
        return []
    
    all_comments = []
    for comment in comments:
        user_data = db.query(UserModel, PositionModel).join(PositionModel, UserModel.position_id == PositionModel.id).filter(UserModel.id == comment.user_id).first()
        user, position = user_data
        all_comments.append({
            "id": comment.id,
            "message": comment.message,
            "task_id": comment.task_id,
            "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "address": user.address,
            "gender": user.gender,
            "dob": user.dob,
            "avatar": user.avatar,
            "position": position
        },
            "created_at": comment.created_at,
            "updated_at": comment.updated_at,
        })
    
    return all_comments
@router.get("/{task_id}/{comment_id}", summary="Lấy một comment",dependencies=[Depends(JWTBearer().has_role([1]))])
def get_comment_by_id(
    comment_id: str,
    db: Session = Depends(get_database_session),
):
    comment = (
    db.query(CommentModel).filter(CommentModel.id==comment_id).first()
    )
    return comment
#Xóa loại sản phẩm
@router.delete("/delete/{comment_id}", summary="Xóa Comment",dependencies=[Depends(JWTBearer().has_role([1]))])
async def delete_comment(comment_id:str, db: Session = Depends(get_database_session)):
    existing_comment= db.query(CommentModel).filter(CommentModel.id == comment_id).first()

    if not existing_comment:
        raise HTTPException(status_code=404, detail=f"Comment không tồn tại!")
    existing_comment.deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    db.commit()

    return {"message": "Xoá Comment thành công"}