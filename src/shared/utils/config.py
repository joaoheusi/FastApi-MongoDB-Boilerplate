import os

from dotenv import load_dotenv

load_dotenv()
PWD_ENCRYPTION_KEY = os.getenv("PWD_ENCRYPTION_KEY")
UUID_ENCRYPTION_KEY = os.getenv("UUID_ENCRYPTION_KEY")
