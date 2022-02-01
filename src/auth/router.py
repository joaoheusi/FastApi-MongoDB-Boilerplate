from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from src.auth.bearer import JWTBearer
from src.auth.schemas import AuthForm, AuthToken
from src.auth.services import authenticate_user

auth_scheme = JWTBearer(tokenUrl="auth", module_name=None)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("", response_model=AuthToken)
async def authenticate(form_data: AuthForm = Body(...)):
    token = await authenticate_user(form_data=form_data)
    return JSONResponse(status_code=status.HTTP_200_OK, content=token.dict())


@router.post("/validate", response_model=AuthToken)
async def validate_token(auth=Depends(auth_scheme)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"Success": "Token Validated"},
    )
