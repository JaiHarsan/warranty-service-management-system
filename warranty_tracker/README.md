# WarrantyCare

## 1. What was built
A full-stack skeleton and MVP foundation for the **WarrantyCare** platform (Warranty & Proactive Product Service Intelligence Platform). The foundation connects a Django backend (with Django REST Framework) to MongoDB using MongoEngine, and serves a Vanilla JS/HTML/CSS frontend.

## 2. Project structure
```text
warranty_tracker/
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── accounts/
│   │   ├── products/
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── warranties/
│   │   ├── health_checks/
│   │   ├── service_centres/
│   │   ├── appointments/
│   │   ├── notifications/
│   │   ├── documents/
│   │   └── service_history/
│   └── manage.py
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── api.js
│   └── assets/
└── venv/
```

## 3. Technology stack
Frontend: HTML + CSS + Vanilla JS
Backend: Python + Django + Django REST Framework
Database: MongoDB (MongoEngine)

## 4. Setup instructions
1. Ensure MongoDB is running locally on port 27017 or update the `MONGODB_URI` environment variable.
2. Activate the virtual environment: `venv\Scripts\activate`
3. Run the backend server: `cd backend && python manage.py runserver`
4. Serve the frontend: Open `frontend/index.html` in your browser or run a simple python http server inside the `frontend` folder (`python -m http.server 8000`).

## 5. Environment variables
Create a `.env` file in the `backend` folder:
```
SECRET_KEY=your_secret_key
DEBUG=True
MONGODB_URI=mongodb://localhost:27017/warrantycare
```

## 6. API summary
- `GET /api/products/`: List products
- `POST /api/products/`: Create a product

## 7. Known limitations
- The MVP establishes the architecture and folder structure, but full CRUD endpoints and complex rule engine algorithms have not been completely fleshed out due to complexity and execution limits.
- OCR fallback, Map integration, and true Authentication flow require further expansion of the existing templates.
