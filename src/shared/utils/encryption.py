from cryptography.fernet import Fernet
from src.shared.utils.config import PWD_ENCRYPTION_KEY, UUID_ENCRYPTION_KEY


def encrypt(str_pwd: str) -> str:
    key = str(PWD_ENCRYPTION_KEY).encode()
    fernet = Fernet(key)
    encoded_pwd = str_pwd.encode()
    encrypted_pwd = fernet.encrypt(encoded_pwd).decode()
    return encrypted_pwd


def encrypt_uuid(uuid: str) -> str:
    key = str(UUID_ENCRYPTION_KEY).encode()
    fernet = Fernet(key)
    encoded_uuid = uuid.encode()
    encrypted_uuid = fernet.encrypt(encoded_uuid).decode()
    return encrypted_uuid


def decrypt_uuid(encrypted_uuid: str) -> str:
    key = str(UUID_ENCRYPTION_KEY).encode()
    fernet = Fernet(key)
    check_uuid = encrypted_uuid.encode()
    dec_uuid = fernet.decrypt(check_uuid).decode()
    return dec_uuid


def validate(str_pwd, encrypted_pwd) -> bool:
    key = str(PWD_ENCRYPTION_KEY).encode()
    fernet = Fernet(key)
    check_pwd = encrypted_pwd.encode()
    dec_pwd = fernet.decrypt(check_pwd).decode()
    if str_pwd == dec_pwd:
        return True
    return False
