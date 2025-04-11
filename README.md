# Flask-Account-Takeover-Vulnerable-App

🔐 Password Reset Vulnerability Demo (Flask)
This is a simple Flask application built to demonstrate a common insecure password reset implementation.

⚠️ Vulnerability Simulated:
Uses weak, predictable MD5-hashed numeric tokens for password reset.

Email addresses are Base64 + Hex encoded, making the reset link seem obfuscated but still predictable.

No expiry or user-agent checks in reset logic.

💡 Purpose:
This app is designed for educational and testing purposes — to help learners, bug bounty hunters, and security professionals understand how insecure token generation and encoding can be exploited in real-world applications.

🔧 Features:
User registration & login

Insecure "forgot password" mechanism

Flask + SQLite backend

Minimal dependencies, easy to run locally

🚨 Disclaimer:
This project is for educational use only. Do not use these insecure patterns in production.
