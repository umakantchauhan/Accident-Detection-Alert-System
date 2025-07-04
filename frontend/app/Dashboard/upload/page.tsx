"use client"

import { VideoUpload } from "../components/video-upload"

export default function UploadPage() {
  return (
      <div className="space-y-6">
        <h2 className="text-3xl font-bold tracking-tight">Upload Video</h2>
        <VideoUpload />
      </div>
  )
}

