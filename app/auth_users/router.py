from fastapi import APIRouter, Depends, HTTPException, Response, status

from .models import User
from .schemas import SUserAuth, SUserRegister
from .service import UserService
from .auth import authenticate_user, create_access_token, get_password_hash
from .dependencies import get_current_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UserService.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )

    if not user_data.user_role:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="User must have a role"
        )

    user_dict = user_data.model_dump()
    user_dict["password"] = get_password_hash(user_data.password)

    await UserService.insert(**user_dict)

    return {"status": "ok", "message": "User is registered"}


@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)

    if not check:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong email or password"
        )

    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)

    return {"access_token": access_token, "refresh_token": None}


@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {"message": "Пользователь успешно вышел из системы"}
