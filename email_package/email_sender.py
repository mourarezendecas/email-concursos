import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_package.email_builder import retorna_email

SERVER_SMTP = os.getenv("SERVER_SMTP")
PORT = os.getenv("PORT")
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")

subject = "E-mail automatico - teste"
body = retorna_email()

message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["Subject"] = subject
message.attach(MIMEText(body, "html"))


def send_email(email):
    try: 
        server = smtplib.SMTP(SERVER_SMTP, PORT)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        message["To"] = email
        server.sendmail(SENDER_EMAIL, email, message.as_string())
        print(f"Email enviado para {email} com sucesso!")
    except Exception as e: 
        print(f"Erro: {e}")
    finally:
        server.quit()