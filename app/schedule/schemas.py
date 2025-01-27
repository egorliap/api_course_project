from datetime import datetime, timedelta, date, time
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict, ValidationError

class SLesson(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    student_id: int
    teacher_id: int
    start_at: date = Field(...)
    duration: int = Field(..., ge=5, le=120)
    task: Optional[str] = Field(...)
    
    @field_validator("start_at")
    @classmethod
    def validate_date_start(cls, value: str) -> str:
        if value and value <= datetime.now().date():
            ValidationError("Wrong date for date staring")
        return value
   
class SLessonAdd(BaseModel):
    start_at: date = Field(...)
    duration: int = Field(..., ge=5, le=120)
    task: Optional[str] = Field(...)
    
    @field_validator("start_at")
    @classmethod
    def validate_date_start(cls, value: str) -> str:
        if value and value <= datetime.now().date():
            ValidationError("Wrong date for date staring")
        return value
    
class SLessonUpdate(BaseModel):
    start_at: date = Field(...)
    duration: int = Field(..., ge=5, le=120)
    task: Optional[str] = Field(...)
    
    @field_validator("start_at")
    @classmethod
    def validate_date_start(cls, value: str) -> str:
        if value and value <= datetime.now().date():
            ValidationError("Wrong date for date staring")
        return value