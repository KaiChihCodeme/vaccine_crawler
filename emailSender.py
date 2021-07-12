from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

# Load dotenv
load_dotenv()

sender = os.getenv("SENDER_ACC")

def emailConfig(subject, to, body):
    content = MIMEMultipart()  # Create MIMEMultipart Object
    content["subject"] = subject  # Mail Subject
    content["from"] = sender  # Sender
    content["to"] = to
    content.attach(MIMEText(body))  # Mail Body
    sendEmail(content)

def sendEmail(content):
    # SMTP Server
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            applicationID = os.getenv("KAIFORDEV_APP_ID")
            smtp.ehlo()  # Authenticate SMTP Server
            smtp.starttls()  # Create Encrypted Transfer
            smtp.login(sender, applicationID)  # Sender's Email
            smtp.send_message(content)  # Send the content
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
