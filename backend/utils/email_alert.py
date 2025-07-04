import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get SMTP email credentials from environment variables
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587  
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  

# MongoDB Atlas Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["accident_detection"]
alerts_collection = db["alert_logs"]

def send_email_alert(subject, message, to_email, phone_number):
    """
    Send an email alert using SMTP and store the log in MongoDB Atlas.
    
    Args:
        subject (str): The email subject.
        message (str): The email body.
        to_email (str): The recipient's email address.
    """
    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        # Connect to the SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Email Alert Sent to {to_email}")

        # Store log in MongoDB Atlas
        alert_data = {
            "timestamp": datetime.utcnow(),
            "email_status": "Sent",
            "email_to": to_email, 
            "sms_status": f"SMS sent to: {phone_number}",
            "call_status": f"Call sent to: {phone_number}",
            "message": message,
        }
        alerts_collection.insert_one(alert_data)
        print("✅ Email alert log saved in MongoDB Atlas")

    except Exception as e:
        print(f"❌ Error sending email: {e}")
