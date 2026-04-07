"""用户认证API路由"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from ...db import get_db
from ...models.auth_schemas import (
    AuthTokenResponse,
    LoginRequest,
    RegisterRequest,
    UserProfile,
)
from ...models.user import User
from ...services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["认证"])
security = HTTPBearer(auto_error=False)


def _to_profile(user: User) -> UserProfile:
    return UserProfile(
        id=user.id,
        email=user.email,
        username=user.username,
        display_name=user.display_name,
        role=user.role,
        is_active=user.is_active,
    )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    if not credentials or not credentials.credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="未登录")

    user_id = AuthService.decode_access_token(credentials.credentials)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="令牌无效或已过期")

    user = AuthService.get_user_by_id(db, user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户不存在或已禁用")

    return user


@router.post("/register", response_model=AuthTokenResponse, summary="注册")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = AuthService.register_user(
            db,
            email=request.email.lower().strip(),
            username=request.username.strip(),
            password=request.password,
            display_name=request.display_name.strip(),
        )
        token = AuthService.create_access_token(user.id)
        return AuthTokenResponse(
            message="注册成功",
            access_token=token,
            user=_to_profile(user),
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login", response_model=AuthTokenResponse, summary="登录")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = AuthService.authenticate(db, request.email_or_username.strip(), request.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名/邮箱或密码错误")

    token = AuthService.create_access_token(user.id)
    return AuthTokenResponse(
        message="登录成功",
        access_token=token,
        user=_to_profile(user),
    )


@router.get("/me", response_model=UserProfile, summary="获取当前用户")
def me(current_user: User = Depends(get_current_user)):
    return _to_profile(current_user)
