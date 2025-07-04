"use client";

import Notifications from "./notifications/page";

const DashboardPage = () => {
  return (
    <div className="p-4 space-y-4 bg-gray-100 min-h-screen">
      {/* Dashboard Header */}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-800"> Home</h1>
      </div>

      {/* Recent Notifications Card */}
      <div className="bg-white shadow-md rounded-xl p-8 m-6">
        <h2 className="text-2xl font-semibold text-gray-900 mb-3">
          🔔 Recent Notifications
        </h2>
        <div className="overflow-y-auto max-h-80 bg-blue-200">
          <Notifications />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
