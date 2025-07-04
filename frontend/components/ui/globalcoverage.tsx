"use client"

import { motion } from "framer-motion"
import { Clock, Shield, Car } from "lucide-react"
import { Fragment } from "react"
import Image from "next/image"
import pic1 from "@/public/images/pic.jpg"

export function GlobalCoverage() {
  return (
    <section className="relative" id="vision">
      <Fragment>
        <div className="absolute inset-0 z-0">
          {/* Background pattern by @ibelick (https://bg.ibelick.com/) */}
          <div className="relative size-full bg-white">
            <div className="absolute size-full bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)]" />
          </div>
        </div>
        <div className="relative z-1">
          <div className="container mx-auto max-w-6xl py-24 px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
              <div>
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5 }}
                >
                  <span className="inline-flex items-center gap-2 px-3 py-1 text-sm font-medium rounded-full bg-green-100 text-green-700">
                     {/* <Globe className="w-4 h-4" />  */}
                    Our Motivation
                  </span>

                  <h2 className="mt-6 text-4xl font-bold tracking-tight">
                  With every action, we aim to <span className="text-green-600">save lives</span> and create hope
                  </h2>

                  <p className="mt-4 text-lg text-gray-600 max-w-xl text-justify">
                    Our road safety system is revolutionizing accident prevention and emergency response
                    providing real-time monitoring and instant alerts to save lives.
                  </p>

                  {/* <div className="mt-10 grid grid-cols-1 sm:grid-cols-3 gap-6">
                    <div className="flex items-center gap-3">
                      <div className="p-2 rounded-lg bg-green-100">
                        <Clock className="w-6 h-6 text-green-700" />
                      </div>
                      <div>
                        <p className="font-medium">20 Sec</p>
                        <p className="text-sm text-gray-600">Response time</p>
                      </div>
                    </div>

                    <div className="flex items-center gap-3">
                      <div className="p-2 rounded-lg bg-green-100">
                        <Shield className="w-6 h-6 text-green-700" />
                      </div>
                      <div>
                        <p className="font-medium">24/7</p>
                        <p className="text-sm text-gray-600">Monitoring</p>
                      </div>
                    </div>

                    <div className="flex items-center gap-3">
                      <div className="p-2 rounded-lg bg-green-100">
                        <Car className="w-6 h-6 text-green-700" />
                      </div>
                      <div>
                        <p className="font-medium">1M+</p>
                        <p className="text-sm text-gray-600">Cars will be protected</p>
                      </div>
                    </div>
                  </div> */}
                </motion.div>
              </div>

              <div className="relative">
                <motion.div
                  initial={{ opacity: 0, scale: 0.95 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.5, delay: 0.2 }}
                  className="relative aspect-[4/3]"
                >
                  <div
                    className="absolute inset-0 bg-dot-pattern opacity-10"
                    style={{
                      backgroundImage: `url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='10' cy='10' r='1.5' fill='%23333'/%3E%3C/svg%3E")`,
                      backgroundSize: "20px 20px",
                    }}
                  />
                  <Image
                    src={pic1} 
                    alt="Global coverage map"
                    className="rounded-xl shadow-2xl border border-white "
                  />
                </motion.div>
              </div>
            </div>
          </div>
        </div>
      </Fragment>
    </section>
  )
}

