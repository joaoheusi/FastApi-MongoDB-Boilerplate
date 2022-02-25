from cryptography.fernet import Fernet
from src.shared.utils.config import KEY


def encrypt(str_pwd: str) -> str:
    key = str(KEY).encode()
    fernet = Fernet(key)
    encoded_pwd = str_pwd.encode()
    encrypted_pwd = fernet.encrypt(encoded_pwd).decode()
    return encrypted_pwd


def validate(str_pwd, encrypted_pwd) -> bool:
    key = str(KEY).encode()
    fernet = Fernet(key)
    check_pwd = encrypted_pwd.encode()
    dec_pwd = fernet.decrypt(check_pwd).decode()
    if str_pwd == dec_pwd:
        return True
    return False
