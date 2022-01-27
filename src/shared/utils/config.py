import os

from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("ENCRYPTION_KEY")
