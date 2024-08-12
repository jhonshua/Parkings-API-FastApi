from typing import List
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from schemas.user.user_schemas import  EmailSchema
from dotenv import load_dotenv
import os

load_dotenv() 

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAILS_FROM_EMAIL = os.getenv('EMAILS_FROM_EMAIL')
SMTP_PORT = os.getenv('SMTP_PORT')

SMTPL_HOST = os.getenv('SMTPL_HOST')

MAIL_USER_STARTTLS = os.getenv('MAIL_USER_STARTTLS')
USE_CREDENTIAL = os.getenv('USE_CREDENTIALS')
SMTP_SSL_TLS = os.getenv('SMTP_SSL_TLS')

# Configuración del servidor SMTP (reemplaza con tus datos)
conf = ConnectionConfig(
    MAIL_USERNAME = SMTP_USER,
    MAIL_PASSWORD = SMTP_PASSWORD,
    MAIL_FROM = EMAILS_FROM_EMAIL,
    MAIL_PORT=SMTP_PORT,
    MAIL_SERVER =SMTPL_HOST,
    USE_CREDENTIALS=MAIL_USER_STARTTLS, 
    MAIL_STARTTLS=USE_CREDENTIAL,  
    MAIL_SSL_TLS=SMTP_SSL_TLS, 
)

async def send_email(data: EmailSchema):
    
    html = f"""<p>Thanks for using Fastapi-mail{data.password}</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients = [data.email],
        body = html,
        subtype = MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return  "Email sent successfully"


async def send_email_password(data: EmailSchema):
    
    html = f"""<p>Thanks for using Fastapi-mail{data.password}</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients = [data.email],
        body = html,
        subtype = MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return  "Email sent successfully"