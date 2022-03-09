from pydantic import BaseModel


class EmailConfiguration(BaseModel):
    mailUsername: str
    mailPassword: str
    mailFrom: str
    mailServer: str
    mailFromName: str
    mailPort: int
    mailTLS: bool
    mailSSL: bool
    useCredentials: bool
    validateCerts: bool
