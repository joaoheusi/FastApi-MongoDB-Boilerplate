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
3. Install dependencies with.

` pip install requirements.txt`

4. Create .env file on main folder with the following structure

```
# MONGODB - CONNECTION STRING
# mongodb+srv://<username>:<password>@<address>/<database>?retryWrites=true&w=majority
MONGO_URL=your_mongodb_url

# FERNET ENCRYPTION KEY
ENCRYPTION_KEY=fernet_encryption_key

# JWT - any string can be the jwt secret key
JWT_ALGORITHM=HS256
JWT_SECRET_KEY=your_jwt_secret_key
```

To generate fernet encryption key:

```
from cryptography.fernet import Fernet
key = Fernet.generate_key()

```

5. Run `uvicorn app:app --reload` for development.

## Future

- User sign-up w/ e-mail
- Route testing
