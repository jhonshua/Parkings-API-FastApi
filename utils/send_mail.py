from typing import List
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from schemas.user.user_schemas import  EmailSchema


# Configuración del servidor SMTP (reemplaza con tus datos)
conf = ConnectionConfig(
    MAIL_USERNAME ="josepepes33321@gmail.com",
    MAIL_PASSWORD = "pkdy yhib phek sgsm",
    MAIL_FROM = "josepepes33321@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,  # Enable explicit TLS for secure communication
    USE_CREDENTIALS=True,  # Authentication required
    MAIL_SSL_TLS=False,  # Set this to False as recommended by Gmail (use STARTTLS instead)  **Corrected**
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