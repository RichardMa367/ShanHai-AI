"""认证相关请求与响应模型"""

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=32)
    password: str = Field(..., min_length=8, max_length=128)
    display_name: str = Field(..., min_length=1, max_length=32)


class LoginRequest(BaseModel):
    email_or_username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class UserProfile(BaseModel):
    id: str
    email: EmailStr
    username: str
    display_name: str
    role: str
    is_active: bool


class AuthTokenResponse(BaseModel):
    success: bool = True
    message: str = "ok"
    access_token: str
    token_type: str = "bearer"
    user: UserProfile
