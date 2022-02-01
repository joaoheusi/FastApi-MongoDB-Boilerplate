from typing import cast

from fastapi import HTTPException, Request, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from src.auth.services import authorize_user, decode_jwt_token


class JWTBearer(OAuth2PasswordBearer):
    def __init__(self, tokenUrl: str, module_name: str | None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error, tokenUrl=tokenUrl)
        self.module_name = module_name

    async def __call__(self, request: Request) -> str | None:
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if authorization:
            user_id = await decode_jwt_token(param)
            if not user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token or expired token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            if scheme.lower() != "bearer":
                if self.auto_error:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Invalid authentication method.",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
            if self.module_name:
                if not await authorize_user(cast(str, user_id), self.module_name):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="User not authorized to call this method.",
                    )
            return param
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid Authorization Header.",
                headers={"WWW-Authenticate": "Bearer"},
            )
