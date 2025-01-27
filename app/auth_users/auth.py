from datetime import datetime, timezone, timedelta

from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr

from app.config import get_auth_data
from app.auth_users.models import User
from .service import UserService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(
        to_encode, key=auth_data["secret_key"], algorithm=auth_data["algorithm"]
    )
    return encode_jwt


async def authenticate_user(email: EmailStr, password: str) -> User | None:
    user: User = await UserService.find_one_or_none(email=email)
    if (
        not user
        or verify_password(plain_password=password, hashed_password=user.password)
        is False
    ):
        return None
    return user
