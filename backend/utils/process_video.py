import cv2
import os
from ultralytics import YOLO

# Load trained YOLOv8 model (ensure the correct path to best.pt)
MODEL_PATH = os.path.join(os.getcwd(), "models", "best.pt")
model = YOLO(MODEL_PATH)

def process_video(video_path):
    """Process video and detect crashes using YOLOv8."""
    
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found at '{video_path}'")

    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define output file path
    output_folder = os.path.join(os.getcwd(), "uploads")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_path = os.path.join(output_folder, f"processed_{os.path.basename(video_path)}")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Process video frame by frame
    crash_detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLOv8 inference
        results = model(frame)

        # Use YOLOv8's built-in visualization method (matches Colab output)
        detected_frame = results[0].plot()

        # Write processed frame to output video
        out.write(detected_frame)

    # Release resources
    cap.release()
    out.release()

    return {
        "output_path": os.path.basename(output_path),
        "crash_detected": crash_detected
    }
