"use client";
import { useEffect, useState } from "react";

interface Alert {
  timestamp: string;
  email_status: string;
  email_to: string;
  sms_status: string;
  call_status: string;
  message: string;
}

export default function Notifications() {
  const [alerts, setAlerts] = useState<Alert[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data))
      .catch((err) => console.error("Error fetching alerts:", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Accident Alert Logs</h1>
      <div className="bg-white p-4 shadow rounded-lg">
      <div className="overflow-y-auto max-h-400 bg-green-100">
        {alerts.length > 0 ? (
          <ul>
            {alerts.map((alert, index) => (
              <li key={index} className="mb-2 border-b pb-2">
                <p><strong>Time:</strong> {new Date(alert.timestamp).toLocaleString()}</p>
                <p><strong>Email Sent To:</strong> {alert.email_to}</p>
                <p><strong>Message:</strong> {alert.message}</p>
                <p><strong>SMS Status:</strong> {alert.sms_status}</p>
                <p><strong>CALL Status:</strong> {alert.call_status}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No alerts found.</p>
        )}
        </div>
      </div>
    </div>
  );
}
