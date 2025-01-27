from sqlalchemy import select, and_, or_
from app.service.base import BaseService
from .models import Message

from app.service.base import Base
from app.db import async_session_maker

class MessageService(Base):
    model = Message
    
    async def get_message_between_users(cls, user1_id:int, user2_id:int):
        async with async_session_maker() as session:
            query = select(cls.model).filter(
                or_(
                    and_(cls.model.sender_id == user1_id, cls.model.recipient_id == user2_id),
                    and_(cls.model.sender_id == user2_id, cls.model.recipient_id == user1_id)
                    )
                ).order_by(cls.model.id)
            result = await session.execute(query)
            return result.scalar().all()