"use client"

import Link from "next/link"
import { Home, Upload, Bell } from "lucide-react" // Using Bell icon for Notifications

const menuItems = [
  { name: "Home", icon: Home, href: "/Dashboard" },
  { name: "Upload", icon: Upload, href: "/Dashboard/upload" },
  { name: "Notifications", icon: Bell, href: "/Dashboard/notifications" },  // Corrected Notifications path
]

export function Sidebar() {
  return (
    <div className="flex h-screen w-[240px] flex-col border-r border-[#f1f1f1] bg-green-700 rounded-r-2xl">
      <div className="flex h-[60px] items-center px-4">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-[#00D959] rounded-full flex items-center justify-center">
            <span className="text-white font-medium text-50px">A</span>
          </div>
          <span className="text-white text-lg font-medium">AccidentAI</span>
        </div>
      </div>
      <nav className="flex-3 px-2 py-3">
        {menuItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="
              flex items-center gap-4 rounded-lg px-3 py-2 text-[16px] text-white
              transition duration-300 ease-in-out
              hover:bg-green-600
              hover:scale-105
              hover:shadow-md
              hover:rotate-1
              border-l-2 border-white
              my-5
            "
          >
            <item.icon className="h-[18px] w-[18px]" />
            {item.name}
          </Link>
        ))}
      </nav>
    </div>
  )
}
