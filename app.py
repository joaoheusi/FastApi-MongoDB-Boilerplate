from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class HelloSchema(BaseModel):
    message: str


@app.get("/", response_model=HelloSchema)
def hello():
    return JSONResponse(
        {"message": "Hello there!"},
        status_code=status.HTTP_200_OK,
    )
