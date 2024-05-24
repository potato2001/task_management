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
async def sendAll(sid):
    await sio_server.emit('receiveAll')

@sio_server.event
async def sendExcept(sid):
    for client_sid in connected_clients:
        if client_sid != sid:
            await sio_server.emit('receiveExcept', room=client_sid)

@sio_server.event
async def disconnect(sid):
    connected_clients.remove(sid)
    print(f'{sid}: disconnected')
