# Project Limitations

The WarrantyCare platform is designed as an MVP prototype for academic evaluation. The following conscious scope limitations apply:

- **OCR Fallback**: While the architecture supports document uploading, true Optical Character Recognition (OCR) requires expensive paid Cloud APIs. The system abstracts this into a manual entry fallback.
- **Service Booking**: Appointment generation generates prototype internal Service Requests (`WS-2026-XXXX`). It does not ping actual external manufacturer Webhooks or confirm real-world availability.
- **Notifications**: Reminders are generated within the database for the Notification Center UI. Cloud Push features (SMTP Email/Twilio SMS) are not implemented.
- **Admin Panel**: Django's native SQLite Admin is unsupported due to the MongoEngine architecture. Database administration relies on standard MongoDB CLI/Atlas interfaces.
- **Mapping**: Distance routing calculates mathematically via pure Coordinates. Visual Web Map integration (e.g., Leaflet) is excluded to avoid API key dependencies.
