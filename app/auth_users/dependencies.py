from datetime import datetime, timezone

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from app.config import get_auth_data
from .models import User
from .service import UserService


def get_token(request: Request) -> str:
    token = request.cookies.get("users_access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found"
        )
    return token


async def get_current_user(token: str = Depends(get_token)) -> User:
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(
            token, key=auth_data["secret_key"], algorithms=[auth_data["algorithm"]]
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not valid"
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token does not contain user_id (sub)",
        )

    user: User = await UserService.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not found"
        )

    return user
