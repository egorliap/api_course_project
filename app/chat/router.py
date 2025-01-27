import asyncio
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

from .schemas import SMessageCreate, SMessageRead
from app.users.models import User
from app.users.dependencies import get_current_user
from .service import MessageService

from typing import List, Dict


router = APIRouter(prefix='/chat', tags=['chat handler'])

@router.get("/messages/{id}", response_model=List[SMessageRead])
async def get_messages(user_id:int, current_user:User = Depends(get_current_user)):
    return await MessageService.get_message_between_users(user1_id=user_id, user2_id=current_user.id) or []

@router.post("/messages", response_model=SMessageCreate)
async def send_message(message: SMessageCreate, current_user: User = Depends(get_current_user)):
    await MessageService.insert(
        sender_id = current_user.id,
        content = message.content,
        recipient_id = message.recipient_id
        )
    
    message_data ={
        'sender_id': current_user.id,
        'recipient_id': message.recipient_id,
        'content': message.content
        }
    await notify_user(message.recipient_id, message_data)
    await notify_user(current_user.id, message_data)
    
    return {'recipient_id': message.recipient_id, 'content': message.content, 'status': 'ok', 'message': 'Message successfully saved'}

# Активные WebSocket-подключения: {user_id: websocket}
active_connections: Dict[int, WebSocket] = {}

async def notify_user(user_id:int, message: dict):
    if user_id in active_connections:
        websocket = active_connections[user_id]
        await websocket.send_json(message)
        
@router.websocket("/websocket/{id}")
async def websocket_endpoint(websocket: WebSocket, user_id:int):
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        active_connections.pop(user_id, None)