from datetime import datetime, timezone

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from app.config import get_auth_data
from app.users.models import User
from app.users.service import UserService
from app.users.dependencies import get_current_user


async def is_authorized_student(user: User = Depends(get_current_user)) -> User:
    if not user.is_student:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='User is not a student')
    return user
    