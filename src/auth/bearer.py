from fastapi import HTTPException, Request, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
from src.auth.services import decode_jwt_token


class AuthForm(BaseModel):
    username: str
    password: str


class AuthToken(BaseModel):
    accessToken: str
    tokenType: str


class JWTBearer(OAuth2PasswordBearer):
    def __init__(self, tokenUrl: str, moduleName: str | None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error, tokenUrl=tokenUrl)
        self.moduleName = moduleName

    async def __call__(self, request: Request) -> str | None:
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if authorization:
            if not decode_jwt_token(param):
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
            return param
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid Authorization Header.",
                headers={"WWW-Authenticate": "Bearer"},
            )
