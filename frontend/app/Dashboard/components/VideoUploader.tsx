import React, { useState } from "react";
import axios from "axios";
import { CloudUpload, Download, CheckCircle, AlertCircle } from "lucide-react";

const VideoUploader: React.FC = () => {
  const [video, setVideo] = useState<File | null>(null);
  const [videoPreview, setVideoPreview] = useState<string | null>(null);
  const [outputVideoUrl, setOutputVideoUrl] = useState<string | null>(null);
  const [status, setStatus] = useState<string>("");
  const [uploading, setUploading] = useState<boolean>(false);

  // Handle file selection
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      setVideo(file);
      setVideoPreview(URL.createObjectURL(file));
    }
  };

  // Handle video upload and crash detection
  const handleUpload = async () => {
    if (!video) {
      alert("Please select a video first!");
      return;
    }
    
    setUploading(true);
    const formData = new FormData();
    formData.append("video", video);

    try {
      setStatus("Uploading and processing video...");
      const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      
      if (response.data.status === "success") {
        setStatus(response.data.crash_detected ? "Crash Detected!" : "No Crash Detected.");
        setOutputVideoUrl(`http://127.0.0.1:5000${response.data.result_video}`);
      } else {
        setStatus("Error processing video.");
      }
    } catch (error) {
      setStatus("Error uploading or processing the video.");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-l-screen bg-gray-100 p-6">
      <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-lg">
        <h2 className="text-xl font-semibold text-gray-900 mb-4 text-center">📂 Upload Video for Crash Detection</h2>
        
        <label className="flex flex-col items-center justify-center border-2 border-dashed border-gray-600 rounded-lg p-6 cursor-pointer hover:bg-gray-50">
          <CloudUpload className="w-12 h-12 text-gray-500 mb-2" />
          <span className="text-gray-600 text-sm">Click to Upload or Drag & Drop</span>
          <input type="file" accept="video/*" onChange={handleFileChange} className="hidden" />
        </label>

        {videoPreview && (
          <div className="mt-4">
            <video src={videoPreview} controls className="w-full rounded-lg shadow-md" />
          </div>
        )}
        
        <button
          onClick={handleUpload}
          disabled={uploading}
          className={`mt-4 w-full py-2 rounded-lg font-semibold ${uploading ? "bg-gray-400" : "bg-blue-600 hover:bg-blue-700 text-white"}`}
        >
          {uploading ? "Uploading..." : "Upload & Detect"}
        </button>
        
        {status && (
          <div className={`mt-4 p-3 rounded-lg text-center ${status.includes("Crash Detected") ? "bg-red-100 text-red-600" : "bg-green-100 text-green-600"}`}>
            {status.includes("Crash Detected") ? <AlertCircle className="inline mr-2" /> : <CheckCircle className="inline mr-2" />}
            {status}
          </div>
        )}

        {outputVideoUrl && (
          <a href={outputVideoUrl} download className="mt-4 flex items-center justify-center gap-2 w-full py-2 bg-green-500 text-white rounded-lg hover:bg-green-600">
            <Download /> Download Processed Video
          </a>
        )}
      </div>
    </div>
  );
};

export default VideoUploader;