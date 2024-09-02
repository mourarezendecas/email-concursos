import smtplib
import os
from email.mime.text import MIMEText
from database_connection import get_emails

subject = "Email Subject"
body = "This is the body of the text message"
sender = os.getenv("EMAIL_SENDER")
recipients = get_emails()
password = os.getenv("APPLICATION_PASSWORD")

def send_email(subject, body, sender, recipients, password):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        for mail in recipients:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = mail
            smtp_server.sendmail(sender, recipients, msg.as_string())
            print(f"Message sent to {mail}!")
    smtp_server.close()

send_email(subject, body, sender, recipients, password)