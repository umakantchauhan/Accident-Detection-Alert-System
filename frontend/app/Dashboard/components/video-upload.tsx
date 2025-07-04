"use client"

import VideoUploader from "./VideoUploader";

export function VideoUpload() {
  return (
    <div className="space-y-6 p-6">
      <h2 className="text-2xl font-bold text-[#1a1d1f]">Upload Video for Crash Detection</h2>
      <VideoUploader /> 
    </div>
  )
}
