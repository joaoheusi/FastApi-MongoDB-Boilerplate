# Fastapi boilerplate

## Contains

- Fastapi
- Async MongoDB Database with Beanie ODM
- Scalable folder structure
- Authentication
- Users (CRUD)

## Quickstart

1. Create virtual environment using `python -m venv env`.
2. Activate the virtual environment.
3. Install dependencies with `pip install requirements.txt`

4. Create .env file on main folder with the following structure

```
# MONGODB - CONNECTION STRING
# mongodb+srv://<username>:<password>@<address>/<database>?retryWrites=true&w=majority
MONGO_URL=your_mongodb_url

# FERNET ENCRYPTION KEY
ENCRYPTION_KEY=fernet_encryption_key

# JWT
JWT_ALGORITHM=HS256
JWT_SECRET_KEY=your_jwt_secret_key
```

Any string can be used as the jwt secret key.
To generate fernet encryption key, on python console run:

```
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode("utf-8"))

```

Paste the output in the .env file

5. Run `uvicorn app:app --reload` for development.

## Future

- User sign-up w/ e-mail
- Route testing
