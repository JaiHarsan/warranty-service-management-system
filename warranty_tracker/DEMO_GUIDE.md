# WarrantyCare Demo Guide

Follow these exact steps for the final project presentation.

## Prerequisites
1. Open a terminal, activate `venv`.
2. Start MongoDB locally (port 27017).
3. Run `python backend/manage.py check` to confirm framework health.
4. Run `python backend/manage.py seed_demo` to initialize demo values securely (PBKDF2 hashes).
5. Start backend: `python backend/manage.py runserver`
6. Open `http://127.0.0.1:8000/` in Chrome/Edge.

## Demonstration Flow
1. **Login**: Use `rahul@example.com` and password `demo123`.
2. **Dashboard**: Show the summary cards. Observe the generated "HP Laptop" and "Samsung Smartphone".
3. **Product & Health Check**: 
   - Click "View Product" on the HP Laptop.
   - Click "Start Health Check". 
   - The UI pushes configured symptoms to the Python Engine.
4. **Health Report**: Point out the "Potential Issue Detected" response with the Risk level (YELLOW/RED) computed securely on the backend, not hard-coded on the client.
5. **Service Centres**: Click "Find Service Centres". This hits the prototype location tracker and displays "HP Authorized SC".
6. **Appointment Request**: Click "Request Appointment". An asynchronous POST creates a `WS-2026-xxxx` mock request.
7. **Logout**: Return to nav and press Logout. Re-login to prove token states operate via `localStorage` and `Bearer` headers safely.
