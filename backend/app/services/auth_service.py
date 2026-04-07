"""认证与用户服务"""

from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..config import get_settings
from ..models.user import User

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """认证服务"""

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return pwd_context.verify(password, password_hash)

    @staticmethod
    def create_access_token(user_id: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
        payload = {
            "sub": user_id,
            "exp": expire,
            "type": "access",
        }
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    @staticmethod
    def decode_access_token(token: str) -> Optional[str]:
        try:
            payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
            if payload.get("type") != "access":
                return None
            return str(payload.get("sub"))
        except JWTError:
            return None

    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email_or_username(db: Session, identity: str) -> Optional[User]:
        return (
            db.query(User)
            .filter(or_(User.email == identity, User.username == identity))
            .first()
        )

    @staticmethod
    def register_user(
        db: Session,
        *,
        email: str,
        username: str,
        password: str,
        display_name: str,
    ) -> User:
        existing = (
            db.query(User)
            .filter(or_(User.email == email, User.username == username))
            .first()
        )
        if existing:
            raise ValueError("邮箱或用户名已存在")

        user = User(
            email=email,
            username=username,
            password_hash=AuthService.hash_password(password),
            display_name=display_name,
            role="user",
            is_active=True,
            is_superuser=False,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def authenticate(db: Session, identity: str, password: str) -> Optional[User]:
        user = AuthService.get_user_by_email_or_username(db, identity)
        if not user or not user.is_active:
            return None
        if not AuthService.verify_password(password, user.password_hash):
            return None
        return user
