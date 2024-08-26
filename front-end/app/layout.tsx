import type { Metadata } from "next";
// import { Inter } from "next/font/google";
import { Inter as FontSans } from "next/font/google";
import "./globals.css";

import { cn } from "@/lib/utils";

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
});

export const metadata: Metadata = {
  title: "Kenya Airways Reviews",
  description:
    "Positive, negative, and neutral reviews of Kenya Airways collected from google, x,facebook, tripadvisor and airlineratings.com",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={cn(
          "min-h-screen bg-background font-sans antialiased",
          fontSans.variable
        )}
      >
        <div className="max-w-6xl p-5 m-auto bg-blue-500  bg-opacity-5">
          {children}
        </div>
      </body>
    </html>
  );
}
