from pydantic import BaseModel, EmailStr, Field, ConfigDict


class STeacher(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(...)