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

#FASTAPI_MAIL
MAIL_USERNAME="email@address.com", # email address
MAIL_PASSWORD="password", # password
MAIL_FROM="another@address.com", # e-mail that will appear to receiver, can be the same or another
MAIL_PORT=587, # Mail server port. Ex: 587
MAIL_SERVER="smtp.gmail.com", # Mail server. Ex: smtp.gmail.com
MAIL_FROM_NAME="Fastapi Boilerplate Mailer", # Name used to send mail
MAIL_TLS=True, # bool
MAIL_SSL=False, # bool
USE_CREDENTIALS=True, # bool
VALIDATE_CERTS=True, # bool

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
