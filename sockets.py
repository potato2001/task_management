import socketio
from auth.auth_handler import decodeJWT

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/sockets'
)

connected_clients = set()

@sio_server.event
async def connect(sid, environ):
    connected_clients.add(sid)
    print(f'{sid}: connected')
    await sio_server.emit('join', sid)

@sio_server.event
async def updateTask(sid, task_id):
    await sio_server.emit('receiveUpdateTask', {"taskId": task_id})

@sio_server.event
async def createTask(sid, status_id):
    await sio_server.emit('receiveCreateTask', {"statusId": status_id})

@sio_server.event
async def sendStatusChange(sid, prevStatus, nextStatus):
    for client_sid in connected_clients:
        if client_sid != sid:
            await sio_server.emit('receiveStatusChange', {"prevStatus": prevStatus, "nextStatus": nextStatus}, room=client_sid)

@sio_server.event
async def disconnect(sid):
    connected_clients.remove(sid)
    print(f'{sid}: disconnected')
