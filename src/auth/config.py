import os

from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = 30
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
