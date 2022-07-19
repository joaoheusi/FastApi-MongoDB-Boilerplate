# Fastapi boilerplate

## Contains

- Fastapi
- Async MongoDB Database with Beanie ODM
- Scalable folder structure
- Authentication
- Users (CRUD)
- User Registration
- Email validation with Fastapi-mail

## Quickstart

1. Create virtual environment using `python -m venv env`.
2. Activate the virtual environment.
3. Install dependencies with `pip install requirements.txt`

4. Create .env file on main folder with the following structure

```
# MONGODB - CONNECTION STRING
# mongodb+srv://<username>:<password>@<address>/<database>?retryWrites=true&w=majority
MONGO_URL=your_mongodb_url

# FERNET ENCRYPTION KEYS
PWD_ENCRYPTION_KEY=fernet_encryption_key
UUID_ENCRYPTION_KEY=fernet_encryption_key

# JWT
JWT_ALGORITHM=HS256
JWT_SECRET_KEY=your_jwt_secret_key

#FASTAPI_MAIL
MAIL_USERNAME="email@address.com"
MAIL_PASSWORD=password
MAIL_FROM=another@address.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME="Fastapi Boilerplate Mailer"
MAIL_TLS=True
MAIL_SSL=False
USE_CREDENTIALS=True
VALIDATE_CERTS=True

#API URL (used in email validation)
API_URL="http://localhost:8000"

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

## Testing

Testing is made possible by running the tests.py file in the project's root directory
They are organized in a folder called tests that is also in the project's root directory

## Future

- Route testing (Currently on development)
