from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio Credentials (Set these in a .env file)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_sms_alert(message, phone_number):
    """
    Send an SMS alert using Twilio when an accident is detected.
    
    Args:
        message (str): The alert message to send.
        phone_number (str): The recipient's phone number (include country code, e.g., +1234567890).
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        print(f"✅ SMS Alert Sent to {phone_number}. Message SID: {sms.sid}")
        return True

    except Exception as e:
        print(f"❌ Error sending SMS: {e}")
        return False
