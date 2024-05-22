from fastapi import FastAPI
from Routers import position,login,user,status,task,tag,comment
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

origins = [
    "http://localhost",
    "http://localhost:8080",  # Adjust this based on your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Người dùng
app.include_router(user.router, tags=['User Controller'], prefix='')
#Đăng nhập
app.include_router(login.router, tags=['Login Controller'], prefix='')
#Vị trí
app.include_router(position.router, tags=['Position Controller'], prefix='')
#Trạng thái
app.include_router(status.router, tags=['Status Controller'], prefix='')
#Công việc
app.include_router(task.router, tags=['Task Controller'], prefix='')
#Tag
app.include_router(tag.router, tags=['Tag Controller'], prefix='')
#Comment
app.include_router(comment.router, tags=['Comment Controller'], prefix='')
#Task_Has_Tag
# app.include_router(task_has_tag.router, tags=['Task Has Tag Controller'], prefix='')
