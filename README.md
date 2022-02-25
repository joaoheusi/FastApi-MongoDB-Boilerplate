# Fastapi boilerplate

## Contains

- Fastapi
- Async MongoDB Database with Beanie ODM
- Scalable folder structure
- Authentication
- Users (CRUD)

## Quickstart

Install dependencies
` pip install requirements.txt`

Create .env file on main folder. It needs to contain

```
MONGO_URL=your_mongodb_url

#FERNET ENCRYPTION KEY
ENCRYPTION_KEY=fernet_encryption_key

#FERNET ENCRYPTION KEY
JWT_ALGORITHM=HS256
JWT_SECRET_KEY=your_jwt_secret_key
```

## Future

- User sign-up w/ e-mail
- Route testing
