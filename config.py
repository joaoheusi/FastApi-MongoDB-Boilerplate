import os
from typing import List

from dotenv import load_dotenv

from src.modules.users.models.documents import User

load_dotenv()

DOCUMENT_MODELS: List = [User]
MONGODB_URL = os.getenv("MONGO_URL")
