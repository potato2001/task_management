from fastapi import Depends, APIRouter,HTTPException
from sqlalchemy import exists
from sqlalchemy.orm import Session,aliased
from model import TaskModel,StatusModel,TagModel,UserModel,TaskHasTagModel
from database import SessionLocal, engine
from schema import TaskSchema,TaskUpdateSchema,TaskStatusUpdateSchema
import model
from datetime import datetime
import uuid
from auth.auth_handler import JWTBearer
from fastapi import Header
from auth.auth_handler import decodeJWT

router = APIRouter(prefix="/api/v1/task")  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
custome_uuid=str(uuid.uuid4()).replace('-', '')[:8]

#Thêm loại sản phẩm
@router.post("/create", summary="Tạo công việc", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def create_task(
    taskSchema: TaskSchema,
    authorization: str = Header(...),
    db: Session = Depends(get_database_session),
):
    user = decodeJWT(authorization.split()[1])
    if(taskSchema.assigner == ''):
        taskSchema.assigner = user['id']
    # Retrieve the default status id
    status_default = db.query(StatusModel).filter(StatusModel.name == "Cần làm").first().id
    # Create a new task instance
    new_task = TaskModel(
        id=str(uuid.uuid4()).replace('-', '')[:8],
        name=taskSchema.name,
        start_time=taskSchema.start_time,
        end_time=taskSchema.end_time,
        status_id=status_default,
        assigner=taskSchema.assigner,
        carrier=taskSchema.carrier,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # Process the tags
    if taskSchema.tag:
        for tag in taskSchema.tag:
            task_has_tag = TaskHasTagModel(
                task_id=new_task.id,
                tag_id=tag.tag_id,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
            )
            db.add(task_has_tag)

    db.commit()

    return {"message": "Tạo công việc thành công", "task_id": new_task.id}

# Sủa loại sản phẩm
@router.patch("/update/{task_id}", summary="Cập nhật công việc", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def update_task(
    task_id: str,
    taskUpdateSchema: TaskUpdateSchema,
    db: Session = Depends(get_database_session),
):
    # Retrieve the existing task
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update task fields if provided
    if taskUpdateSchema.name:
        task.name = taskUpdateSchema.name
    if taskUpdateSchema.start_time:
        task.start_time = taskUpdateSchema.start_time
    if taskUpdateSchema.end_time:
        task.end_time = taskUpdateSchema.end_time
    if taskUpdateSchema.assigner:
        task.assigner = taskUpdateSchema.assigner
    if taskUpdateSchema.carrier:
        task.carrier = taskUpdateSchema.carrier
    task.updated_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    # Process the tags
    if taskUpdateSchema.tag is not None:
        # Delete existing task tags
        db.query(TaskHasTagModel).filter(TaskHasTagModel.task_id == task_id).delete()
        # Add new tags
        for tag in taskUpdateSchema.tag:
            task_has_tag = TaskHasTagModel(
                task_id=task_id,
                tag_id=tag.tag_id,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
            )
            db.add(task_has_tag)

    db.commit()
    db.refresh(task)

    return {"message": "Cập nhật công việc thành công", "task_id": task.id}
@router.put("/update_status", summary="Cập nhật công việc", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
async def update_task(
    task_status_schema:TaskStatusUpdateSchema,
    db: Session = Depends(get_database_session),
):
    # Retrieve the existing task
    task = db.query(TaskModel).filter(TaskModel.id == task_status_schema.task_id).first()
    status = db.query(StatusModel).filter(StatusModel.id == task_status_schema.status_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    print(task)
    task.status_id = task_status_schema.status_id
    task.updated_at=datetime.now().strftime("%Y-%m-%d %H:%M")
    # Process the tags
    db.commit()
    db.refresh(task)

    return {"message": "Cập nhật trạng thái công việc thành công", "task_id": task.id}

@router.put("/undo_delete/{task_id}", summary="Hoàn tác xoá công việc",dependencies=[Depends(JWTBearer().has_role([1,2,3]))])
async def delete_task(status_id: str, db: Session = Depends(get_database_session)):
    existing_task= db.query(TaskModel).filter(TaskModel.id == status_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail=f"Công việc không tồn tại!")
    existing_task.deleted_at = None

    db.commit()

    return {"message": "Hoàn tác xoá công việc thành công"}
#Lấy tất cả loại sản phẩm

@router.get("/all", summary="Lấy tất cả công việc")
async def get_all_tasks(
    db: Session = Depends(get_database_session),
):
    # Alias the UserModel to distinguish between assigner and carrier
    Assigner = aliased(UserModel)
    Carrier = aliased(UserModel)

    # Query the database to fetch all tasks along with their status, assigner, and carrier information
    tasks = (
        db.query(TaskModel, StatusModel, Assigner, Carrier)
        .join(StatusModel, TaskModel.status_id == StatusModel.id)
        .join(Assigner, TaskModel.assigner == Assigner.id)
        .join(Carrier, TaskModel.carrier == Carrier.id)
        .all()
    )

    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")

    all_tasks = []

    for task in tasks:
        task_model, status_model, assigner, carrier = task

        # Query to get all tags associated with the task
        tags = (
            db.query(TagModel)
            .join(TaskHasTagModel, TagModel.id == TaskHasTagModel.tag_id)
            .filter(TaskHasTagModel.task_id == task_model.id, TaskHasTagModel.deleted_at == None)
            .all()
        )

        all_tasks.append({
            "id": task_model.id,
            "start_time": task_model.start_time,
            "end_time": task_model.end_time,
            "name": task_model.name,
            "description":task_model.description,
            "assigner": {
                "id": assigner.id,
                "name": assigner.name,
            },
            "carrier": {
                "id": carrier.id,
                "name": carrier.name,
            },
            "status": {
                "id": status_model.id,
                "name": status_model.name,
            },
            "tags": [{"id": tag.id, "name": tag.name} for tag in tags],
            "created_at": task_model.created_at,
            "deleted_at": task_model.deleted_at,
            "updated_at": task_model.updated_at
        })

    # Construct and return the response dictionary
    return  all_tasks
@router.get("/{task_id}", summary="Lấy một công việc", dependencies=[Depends(JWTBearer().has_role([1,2,3]))])
def get_task_by_id(
    task_id: str,
    db: Session = Depends(get_database_session),
):
    # Alias the UserModel to distinguish between assigner and carrier
    Assigner = aliased(UserModel)
    Carrier = aliased(UserModel)

    # Query the database to fetch the task along with its status, assigner, and carrier information
    task = (
        db.query(TaskModel, StatusModel, Assigner, Carrier)
        .join(StatusModel, TaskModel.status_id == StatusModel.id)
        .join(Assigner, TaskModel.assigner == Assigner.id)
        .join(Carrier, TaskModel.carrier == Carrier.id)
        .filter(TaskModel.id == task_id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_model, status_model, assigner, carrier = task

    # Query to get all tags associated with the task
    tags = (
        db.query(TagModel)
        .join(TaskHasTagModel, TagModel.id == TaskHasTagModel.tag_id)
        .filter(TaskHasTagModel.task_id == task_id)
        .all()
    )

    # Construct and return the response dictionary
    return {
        "id": task_model.id,
        "start_time": task_model.start_time,
        "end_time": task_model.end_time,
        "name": task_model.name,
        "assigner": {
            "id": assigner.id,
            "name": assigner.name,
        },
        "carrier": {
            "id": carrier.id,
            "name": carrier.name,
        },
        "status": {
            "id": status_model.id,
            "name": status_model.name,
        },
        "tags": [{"id": tag.id, "name": tag.name} for tag in tags],
        "created_at": task_model.created_at,
        "deleted_at": task_model.deleted_at,
        "updated_at": task_model.updated_at,
    }
@router.get("/task_status/{status_id}", summary="Lấy tất cả công việc theo trạng thái", dependencies=[Depends(JWTBearer().has_role([1, 2, 3]))])
def get_task_status_by_id(
    status_id: str,
    db: Session = Depends(get_database_session),
):
    # Alias the UserModel to distinguish between assigner and carrier
    Assigner = aliased(UserModel)
    Carrier = aliased(UserModel)

    # Query the database to fetch the tasks along with their status, assigner, and carrier information
    tasks = (
        db.query(TaskModel, StatusModel, Assigner, Carrier)
        .join(StatusModel, TaskModel.status_id == StatusModel.id)
        .join(Assigner, TaskModel.assigner == Assigner.id)
        .join(Carrier, TaskModel.carrier == Carrier.id)
        .filter(StatusModel.id == status_id)
        .all()  # Fetch all matching results
    )

    if not tasks:
        tasks = []

    result = []
    for task in tasks:
        task_model, status_model, assigner, carrier = task

        # Query to get all tags associated with the task
        tags = (
            db.query(TagModel)
            .join(TaskHasTagModel, TagModel.id == TaskHasTagModel.tag_id)
            .filter(TaskHasTagModel.task_id == task_model.id)
            .all()
        )

        result.append({
            "id": task_model.id,
            "start_time": task_model.start_time,
            "end_time": task_model.end_time,
            "name": task_model.name,
            "assigner": {
                "id": assigner.id,
                "name": assigner.name,
            },
            "carrier": {
                "id": carrier.id,
                "name": carrier.name,
            },
            "status": {
                "id": status_model.id,
                "name": status_model.name,
            },
            "tags": [{"id": tag.id, "name": tag.name} for tag in tags],
            "created_at": task_model.created_at,
            "deleted_at": task_model.deleted_at,
            "updated_at": task_model.updated_at,
        })

    return result

#Xóa loại sản phẩm
@router.delete("/delete/{id}", summary="Xóa công việc",dependencies=[Depends(JWTBearer().has_role([1,2,3]))])
async def delete_task(id: str, db: Session = Depends(get_database_session)):
    existing_task= db.query(TaskModel).filter(TaskModel.id == id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail=f"Công việc không tồn tại!")
    existing_task.deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    db.commit()

    return {"message": "Xoá công việc thành công"}