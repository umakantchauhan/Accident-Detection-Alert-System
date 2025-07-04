from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio Credentials from .env file
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  

def make_call_alert(to_phone):
    """
    Make a phone call using Twilio and play a message when answered.

    Args:
        to_phone (str): The recipient's phone number (must be verified in Twilio if using a trial account).
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        call = client.calls.create(
            to=to_phone,
            from_=TWILIO_PHONE_NUMBER,
            twiml="<Response><Say>🚨 Alert! An accident has been detected at location XYZ. Immediate action is required.</Say></Response>"
        )

        print(f"✅ Call Alert Initiated to {to_phone}. Call SID: {call.sid}")
        return True

    except Exception as e:
        print(f"❌ Error making call: {e}")
        return False
