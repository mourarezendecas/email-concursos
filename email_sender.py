import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv, dotenv_values

subject = "Hello from Python"
body = "This is a email body"

sender = os.getenv("EMAIL_SENDER")

recipient = ""

sender_password = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print('Message sent')

send_email(subject, body, sender,  recipient, sender_password)