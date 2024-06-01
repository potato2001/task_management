from fastapi import Depends, APIRouter,HTTPException
from sqlalchemy import exists
from sqlalchemy.orm import Session
from model import TagModel
from database import SessionLocal, engine
from schema import TagSchema, TagCreateRequest
import model
from datetime import datetime
import uuid
from auth.auth_handler import JWTBearer

router = APIRouter(prefix="/api/v1/tag")  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#Thêm loại sản phẩm
@router.post("/create", summary="Tạo Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
async def create_tag(
    tagSchema: TagCreateRequest,
    db: Session = Depends(get_database_session),
):
    tag_exists = db.query(exists().where(TagModel.name == tagSchema.name, TagModel.deleted_at == None)).scalar()
    if tag_exists:
        raise HTTPException(status_code=400, detail="Tag đã tồn tại")

    new_tag = TagModel(
        id=str(uuid.uuid4()).replace('-', '')[:8],
        name=tagSchema.name,
        color=tagSchema.color,
        background_color=tagSchema.background_color,
        is_default=False,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return {"message": "Tạo nhãn dán thành công"}

# Sủa loại sản phẩm
@router.patch("/update/{tag_id}", summary="Cập nhật Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
async def update_tag(
    tag_id: str,
    tag_update: TagCreateRequest,
    db: Session = Depends(get_database_session),
):
    existing_tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not existing_tag:
        raise HTTPException(status_code=404, detail="Nhãn dán không tồn tại!")
    if existing_tag.is_default == True:
        raise HTTPException(status_code=404, detail="Không được phép sửa nhãn dán này!")
    existing_tag.name = tag_update.name
    existing_tag.color = tag_update.color
    existing_tag.background_color = tag_update.background_color
    existing_tag.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    existing_tag.deleted_at =None

  
    db.commit()
    db.refresh(existing_tag)

    return {"message": "Chỉnh sửa nhãn dán thành công"}

#Hoàn tác xoá đăng nhập
@router.patch("/undo_delete/{status_id}", summary="Hoàn tác xóa Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
async def undo_delete_tag(status_id: str, db: Session = Depends(get_database_session)):
    existing_tag= db.query(TagModel).filter(TagModel.id == status_id).first()
    if not existing_tag:
        raise HTTPException(status_code=404, detail=f"Tag không tồn tại!")
    existing_tag.deleted_at = None
    db.commit()

    return {"message": "Hoàn tác xoá Tag thành công"}
#Lấy tất cả loại sản phẩm
@router.get("/all", summary="Lấy tất cả Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
def get_tag(
    db: Session = Depends(get_database_session),
):
    tags = (
    db.query(TagModel).filter(TagModel.deleted_at==None).all()

    )
    return tags
@router.get("/{tag_id}", summary="Lấy một Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
def get_tag_by_id(
    tag_id: str,
    db: Session = Depends(get_database_session),
):
    tag = (
    db.query(TagModel).filter(TagModel.id==tag_id).first()
    )
    return  tag
#Xóa loại sản phẩm
@router.delete("/delete/{tag_id}", summary="Xóa Tag",dependencies=[Depends(JWTBearer().has_role([1,2]))])
async def delete_tag(tag_id: str, db: Session = Depends(get_database_session)):
    existing_tag= db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not existing_tag:
        raise HTTPException(status_code=404, detail=f"Tag không tồn tại!")
    if existing_tag.is_default == True:
        raise HTTPException(status_code=404, detail="Không được phép xoá nhãn dán này!")
    existing_tag.deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    db.commit()

    return {"message": "Xoá Tag thành công"}