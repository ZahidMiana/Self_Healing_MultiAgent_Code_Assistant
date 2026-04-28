import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "AgentForge",
  description: "Self-healing multi-agent coding assistant"
};

type RootLayoutProps = {
  children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body className="bg-ink text-fog font-body antialiased">
        {children}
      </body>
    </html>
  );
}
