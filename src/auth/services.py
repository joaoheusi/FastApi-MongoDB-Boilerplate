from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import jwt
from src.auth.config import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM, JWT_SECRET_KEY
from src.auth.schemas import AuthForm, AuthToken, JWTData
from src.modules.users.models.documents import User
from src.shared.utils.encryption import validate


async def create_jwt_token(user_id: str) -> str:
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    expire_int = int(expire.timestamp())
    encoded_jwt = jwt.encode(
        {
            "userId": user_id,
            "exp": expire_int,
        },
        key=JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    return encoded_jwt


async def decode_jwt_token(token: str) -> str | bool:
    try:
        data = jwt.decode(
            token=token,
            key=JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
        )
        jwt_data = JWTData(
            userId=data["userId"],
            exp=data["exp"],
        )
        return jwt_data.userId
    except Exception:
        print(Exception)
        return False


async def authenticate_user(form_data: AuthForm) -> AuthToken:
    user = await User.find_one(User.username == form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with given username not found.",
        )
    if not validate(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong Username/Password combination.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    jwt_token = await create_jwt_token(user.id)
    resp = AuthToken(
        accessToken=jwt_token,
        tokenType="Bearer",
    )
    return resp


async def authorize_user(user_id: str, module_name: str = None) -> bool:
    user = await User.find_one(User.id == user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid or expired access token.",
        )
    if not user.isActive:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="This token belongs to an inactive user.",
        )
    if module_name not in user.allowedModules:
        return False
    return True
