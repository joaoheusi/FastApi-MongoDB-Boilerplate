import os
import pathlib

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig, FastMail
from src.shared.providers.email.schemas.configuration import EmailConfiguration

load_dotenv()

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_PORT = os.getenv("MAIL_PORT")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")
MAIL_TLS = os.getenv("MAIL_TLS")
MAIL_SSL = os.getenv("MAIL_SSL")
USE_CREDENTIALS = os.getenv("USE_CREDENTIALS")
VALIDATE_CERTS = os.getenv("VALIDATE_CERTS")

emailConfiguration = EmailConfiguration(
    mailUsername=MAIL_USERNAME,
    mailPassword=MAIL_PASSWORD,
    mailFrom=MAIL_FROM,
    mailServer=MAIL_SERVER,
    mailFromName=MAIL_FROM_NAME,
    mailPort=MAIL_PORT,
    mailTLS=MAIL_TLS,
    mailSSL=MAIL_SSL,
    useCredentials=USE_CREDENTIALS,
    validateCerts=VALIDATE_CERTS,
)

conf = ConnectionConfig(
    MAIL_USERNAME=emailConfiguration.mailUsername,
    MAIL_PASSWORD=emailConfiguration.mailPassword,
    MAIL_FROM=emailConfiguration.mailFrom,
    MAIL_SERVER=emailConfiguration.mailServer,
    MAIL_FROM_NAME=emailConfiguration.mailFromName,
    MAIL_PORT=emailConfiguration.mailPort,
    MAIL_TLS=emailConfiguration.mailTLS,
    MAIL_SSL=emailConfiguration.mailSSL,
    USE_CREDENTIALS=emailConfiguration.useCredentials,
    VALIDATE_CERTS=emailConfiguration.validateCerts,
    TEMPLATE_FOLDER=pathlib.Path(__file__).parent.joinpath("templates"),
)

fast_mail = FastMail(conf)
