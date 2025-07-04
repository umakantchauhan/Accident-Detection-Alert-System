from flask import Blueprint, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Atlas Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["accident_detection"]
alerts_collection = db["alert_logs"]

# Create Flask Blueprint
alert_logs = Blueprint("alert_logs", __name__)

@alert_logs.route("/alerts", methods=["GET"])
def get_alerts():
    """
    Retrieve all email alert logs.
    """
    try:
        alerts = list(alerts_collection.find({}, {"_id": 0}))  
        return jsonify(alerts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
