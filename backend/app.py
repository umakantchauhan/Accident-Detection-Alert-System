from flask import Flask, request, jsonify, send_file, abort
from flask_cors import CORS
import os
from routes.detection import process_video
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create the folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# MongoDB Atlas Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["accident_detection"]
alerts_collection = db["alert_logs"]

@app.route("/")
def home():
    """Home route to check API status."""
    return jsonify({"message": "🚗 Accident Detection API Running Successfully!"})

# Upload and process video
@app.route("/upload", methods=["POST"])
def upload_video():
    """Handle video upload and crash detection."""
    if "video" not in request.files:
        return jsonify({"error": "❗ No video file uploaded"}), 400

    video_file = request.files["video"]
    if video_file.filename == "":
        return jsonify({"error": "❗ No selected file"}), 400

    if video_file and allowed_file(video_file.filename):
        video_path = os.path.join(app.config["UPLOAD_FOLDER"], video_file.filename)
        video_file.save(video_path)

        try:
            # Run crash detection
            result_data = process_video(video_path)
            result_path = result_data["output_path"]
            crash_detected = result_data["crash_detected"]

            return jsonify({
                "status": "success",
                "message": "✅ Crash detection complete!",
                "crash_detected": crash_detected,
                "result_video": f"/download/{os.path.basename(result_path)}",
            })
        except Exception as e:
            return jsonify({"error": f"❗ Error processing video: {str(e)}"}), 500
    else:
        return jsonify({"error": "❗ Invalid file format. Please upload a video."}), 400

# Serve and download the processed video
@app.route("/download/<filename>", methods=["GET"])
def download_video(filename):
    """Serve the processed video for download."""
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if not os.path.exists(file_path):
        abort(404, description="File not found.")
    return send_file(
        file_path, as_attachment=True, mimetype="video/mp4", download_name="processed_video.mp4"
    )

# Fetch stored accident alert logs
@app.route("/alerts", methods=["GET"])
def get_alerts():
    """Fetch all stored alert logs from MongoDB Atlas."""
    try:
        alerts = list(alerts_collection.find({}, {"_id": 0}))  
        return jsonify(alerts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# @app.route("/alerts", methods=["DELETE"])
# def clear_alerts():
#     """Delete all alert logs from MongoDB."""
#     alerts_collection.delete_many({})  # Clear all records
#     return jsonify({"status": "success", "message": "All alerts cleared!"})

# Allowed video file types
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

def allowed_file(filename):
    """Check if the uploaded file format is valid."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)