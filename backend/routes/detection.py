import os
import cv2
from ultralytics import YOLO
from utils.email_alert import send_email_alert
from utils.sms_alert import send_sms_alert
from utils.call_alert import make_call_alert

# Load YOLOv8 trained model
MODEL_PATH = os.path.join(os.getcwd(), "models", "best.pt")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Trained model not found at '{MODEL_PATH}'. Place 'best.pt' in 'models/' folder.")

try:
    model = YOLO(MODEL_PATH)
    print("✅ Trained YOLOv8 model (best.pt) loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Error loading YOLO model: {str(e)}")


def detect_crash(video_path, model, output_folder):
    """Detect crashes in a video and save output with YOLOv8 detection."""
    
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Prepare output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_path = os.path.join(output_folder, f"processed_{os.path.basename(video_path)}")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    crash_detected = False  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLOv8 detection
        results = model(frame)

        # Check if any detected object is labeled as "accident"
        for result in results:
            for box in result.boxes:
                label = result.names[int(box.cls[0])]  
                if label.lower() == "accident":  
                    crash_detected = True

        # Use YOLOv8’s built-in plotting function for accurate visualization
        detected_frame = results[0].plot()
        out.write(detected_frame)

    cap.release()
    out.release()

    return output_path, crash_detected  


def process_video(video_path):
    """Process video and check for accident detection."""
    
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found at '{video_path}'")

    output_folder = os.path.join(os.getcwd(), "uploads")

    try:
        # Detect accident in video
        result_path, crash_detected = detect_crash(video_path, model, output_folder)

        # Calculate video duration
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        duration_sec = frame_count / fps
        cap.release()

        # Send email alert if accident is detected
        if crash_detected:
            print("🚨 Accident Detected! Sending Alerts...")
            send_email_alert(
                subject="🚨 Accident Alert!",
                message="An accident has been detected in the video. Immediate action required!",
                to_email="aigalshaan18@gmail.com",
                phone_number="+918530890568"
            )

        #  Send SMS Alert if an accident is detected
        if crash_detected:
            print("🚨 Accident Detected! Sending SMS Alert...")
            send_sms_alert(
                message="🚨 Accident detected at location XYZ. Immediate action required!",
                phone_number="+918530890568"
            )
        
        if crash_detected:
            print("🚨 Accident Detected! Sending Alerts...")

            # Make a Call Alert
            make_call_alert("+918530890568")  

        return {
            "output_path": os.path.basename(result_path),
            "crash_detected": crash_detected,  
            "frame_count": frame_count,
            "video_duration_sec": int(duration_sec),
        }

    except Exception as e:
        raise Exception(f"Error processing video: {str(e)}")
