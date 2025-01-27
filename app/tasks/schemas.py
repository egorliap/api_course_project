from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional

class STask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    given: date = Field(...)
    lesson_id: int
    lesson: Optional[str] = Field(...)
    
    @field_validator("given")
    @classmethod
    def validate_date(cls, value: str) -> date:
        if value and value <= datetime.now().date():
            raise ValidationError("Wrong data for given task")
        return value

class STaskAdd(BaseModel):
    given: date = Field(...)
    lesson: Optional[str] = Field(...)
    
    @field_validator("given")
    @classmethod
    def validate_date(cls, value: str) -> date:
        if value and value <= datetime.now().date():
            raise ValidationError("Wrong date for given task")
        return value
    
class STaskUpdate(BaseModel):
    given: date = Field(...)
    lesson: Optional[str] = Field(...)
    
    @field_validator("given")
    @classmethod
    def validate_date(cls, value) -> date:
        if value and value >= datetime.now().date():
            raise ValidationError("Wrong date for given task")
        return value
    