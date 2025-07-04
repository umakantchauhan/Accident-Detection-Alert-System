"use client"

export default function Notifications() {
  const notifications = [
    { id: 1, message: "Accident detected at Location A", time: "10 mins ago" },
    { id: 2, message: "Emergency response dispatched", time: "30 mins ago" },
    { id: 3, message: "Camera offline at Location B", time: "1 hour ago" },
  ]

  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Notifications</h2>
      <ul className="space-y-3">
        {notifications.map((notification) => (
          <li
            key={notification.id}
            className="p-3 bg-gray-100 rounded-md border border-gray-300"
          >
            <p className="text-gray-800">{notification.message}</p>
            <span className="text-sm text-gray-500">{notification.time}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
