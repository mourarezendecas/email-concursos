import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_package.email_builder import retorna_email

SERVER_SMTP = os.getenv("SERVER_SMTP")
PORT = os.getenv("PORT")
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")

subject = "E-mail automatico - Concursos pelo Brasil"

def build_message(user):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["Subject"] = subject
    message["To"] = user['email']
    message.attach(MIMEText(retorna_email(user['name']), "html"))

    return message

def send_email(user):
    try: 
        server = smtplib.SMTP(SERVER_SMTP, PORT)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        message = build_message(user)
        server.sendmail(SENDER_EMAIL, user['email'], message.as_string())
        print(f"Email enviado para {user['email']} com sucesso!")
    except Exception as e: 
        print(f"Erro: {e}")
    finally:
        server.quit()