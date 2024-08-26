"use client";
import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navbar() {
  const pathname = usePathname();
  const nav_links = [
    {
      name: "All Reviews",
      href: "/",
    },
    {
      name: "Positive Reviews",
      href: "/positive",
    },
    {
      name: "Negative Reviews",
      href: "/negative",
    },
    {
      name: "Neutral Reviews",
      href: "/neutral",
    },
  ];
  return (
    <div className="flex justify-center items-center sticky top-0 min-w-full z-50">
      <div className="rounded-2xl md:rounded-full px-2 py-2 border shadow-md flex flex-wrap gap-2 md:gap-4 bg-gray-100">
        {nav_links.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            className={`${
              pathname === link.href
                ? "bg-primary text-white"
                : "text-gray-500 hover:bg-primary hover:text-white"
            } px-3 py-2 rounded-full text-sm font-medium`}
          >
            {link.name}
          </Link>
        ))}
      </div>
    </div>
  );
}
