import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"] ,
  theme: {
    extend: {
      colors: {
        ink: "#101114",
        graphite: "#1a1c22",
        ember: "#ff5f3b",
        mint: "#5ce0b8",
        fog: "#c9ced6"
      },
      fontFamily: {
        display: ["Space Grotesk", "system-ui", "sans-serif"],
        body: ["IBM Plex Sans", "system-ui", "sans-serif"]
      }
    }
  },
  plugins: []
};

export default config;
