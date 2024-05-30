from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List


class PositionSchema(BaseModel):
    name:str
    role:int
class UserSchema(BaseModel):
    name:str
    email:str
    phone:str
    password:str
    address:str
    gender:int
    dob:str
    description:Optional[str]
    position_id:str
class AdminControlUserSchema(BaseModel):
    name:str
    email:str
    phone:str
    address:str
    gender:int
    dob:str
    description:Optional[str]
    position_id:str
class UserControlSchema(BaseModel):
    name:str
    phone:str
    description:Optional[str]
    address:str
    gender:int
    dob:str
class StatusSchema(BaseModel):
    name:str
    color:str
    background_color:str
    is_completed:int
class TagToTaskSchema(BaseModel):
    tag_id:str  
class TaskSchema(BaseModel):
    name:str
    description:str
    start_time:str
    end_time:str
    assigner:str
    carrier:str
    tags: Optional[List[str]] = None
    description: str
class TagSchema(BaseModel):
    id: str
    name:str
    color:str
    background_color:str
    is_default:int
class TagCreateRequest(BaseModel):
    name:str
    color:str
    background_color:str
class CommentSchema(BaseModel):
    task_id:str
    user_id:str
    message:str
class TaskHasTagsSchema(BaseModel):
    task_id:str
    tag_id:str
class TaskUpdateSchema(BaseModel):
    name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    assigner: Optional[str] = None
    carrier: Optional[str] = None
    tag: Optional[List[TagSchema]] = []
class CommentUpdateSchema(BaseModel):
    task_id:str
    user_id:str
    message:str
class TaskStatusUpdateSchema(BaseModel):
    task_id:str
    status_id:str

# class ProductSchema(BaseModel):
#     product_code :str
#     product_name :str
#     product_brand :str
#     product_description: Optional[str] = None  
#     unit_price :int
#     status:str
#     provider_uuid:str
#     category_uuid:str

# class CategorySchema(BaseModel):
#     category_name :Optional[str] = None  
#     status:Optional[str] = None 

# class CategoryUpdateSchema(BaseModel):
#     category_name :Optional[str] = None  
#     status:Optional[str] = None 

# class CustomerSchema(BaseModel):
#     # CustomerID :int
#     CustomerName: str
#     CustomerAddress: str
#     CustomerPhone: str
#     CustomerEmail: str

# class InvoiceSchema(BaseModel):
#     InvoiceID :int
#     UserID :int
#     TotalCost: int
#     # OrderDetail_OrderDetailID:int

# class ProviderSchema(BaseModel):
#     provider_name: str
#     provider_phone: str
#     provider_email: str
#     provider_address: str
#     status: str

# class InventorySchema(BaseModel):
#     InventoryID: int
#     QuantityAvailable: int
#     Product_ProductID: int
#     Invoice_InvoiceID: int  

# class MultipleCategoriesSchema(BaseModel):
#     categories: List[CategorySchema]
# class ProductDetail(BaseModel):
#     ProductID: int
#     OrderQuantity: int
# class OrderDetailSchema(BaseModel):
#     # OrderDetailID: int
#     # OrderDetailCode:str
#     CustomerID: int
#     Products: List[ProductDetail]
#     # OrderQuantity: int
#     # ReceivedDate: str
#     # OrderDate:str
#     Status: int
