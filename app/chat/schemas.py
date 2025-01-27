from pydantic import BaseModel, Field

class SMessageRead(BaseModel):
    id: int = Field(...)
    sender_id: int = Field(...)
    recipient_id:int = Field(...)
    content: str = Field(...)
    
class SMessageCreate(BaseModel):
    recipient_id:int = Field(...)
    content: str = Field(...)