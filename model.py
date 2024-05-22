from typing import Text
from sqlalchemy import Column,Date,BLOB,ForeignKey
from sqlalchemy.types import String, Integer, Text, Float

from database import Base
from sqlalchemy.orm import  relationship
class UserModel(Base):
    __tablename__= "users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    password = Column(String)
    address = Column(String)
    gender = Column(Integer)
    avatar = Column(String)
    dob = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    deleted_at = Column(String)
    position_id=Column(String)
class PositionModel(Base):
    __tablename__= "position"
    id  = Column(String, primary_key=True, index=True)
    name=Column(String)
    role=Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)
class StatusModel(Base):
    __tablename__= "status"
    id  = Column(String, primary_key=True, index=True)
    name =Column(String)
    color=Column(String)
    background_color=Column(String)
    is_default=Column(String)
    is_completed=Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)
class TaskModel(Base):
    __tablename__= "task"
    id  = Column(String, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    assigner=Column(String)
    carrier=Column(String)
    start_time=Column(String)
    end_time=Column(String)
    status_id=Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)
class TagModel(Base):
    __tablename__= "tag"
    id  = Column(String, primary_key=True, index=True)
    name =Column(String)
    color=Column(String)
    background_color=Column(String)
    is_default=Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)
class TaskHasTagModel(Base):
    __tablename__= "task_has_tag"
    # id = Column(String, primary_key=True, index=True)
    task_id = Column(String, primary_key=True, index=True)
    tag_id = Column(String, primary_key=True, index=True)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)
class CommentModel(Base):
    __tablename__= "comment"
    id  = Column(String, primary_key=True, index=True)
    task_id=Column(String, primary_key=True, index=True)
    user_id=Column(String, primary_key=True, index=True)
    message = Column(String)
    created_at=Column(String)
    updated_at=Column(String)
    deleted_at=Column(String)

