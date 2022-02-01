from pydantic import BaseModel


class AuthForm(BaseModel):
    username: str
    password: str


class JWTData(BaseModel):
    userId: str
    exp: str


class AuthToken(BaseModel):
    accessToken: str
    tokenType: str
