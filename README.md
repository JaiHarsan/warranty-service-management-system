# 🛠️ Warranty Service Management System

A web-based application designed to help users manage product warranties, maintain product information, schedule service appointments, and access service centre details from one place.

The system combines a web frontend with a Django backend to organize warranty-related information and simplify product service management.

## 📌 Table of Contents
    
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Running the Application](#-running-the-application)
- [Application Pages](#-application-pages)
- [Backend Modules](#-backend-modules)
- [API Documentation](#-api-documentation)
- [Database](#-database)
- [Testing](#-testing)
- [Security Considerations](#-security-considerations)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 📖 Overview

The Warranty Service Management System provides a centralized platform for managing product warranty information and related service activities.

Users can access the web interface to manage products, view product details, work with service appointments, and find service centre information. The Django backend organizes the application's business logic and handles communication between the frontend and the database.

The project is structured into separate frontend and backend components to improve maintainability and make future development easier.

## ❗ Problem Statement

Managing product warranties manually can lead to misplaced warranty information, difficulty tracking service appointments, and delays in finding service centres.

Customers may struggle to remember warranty expiry dates, maintain purchase records, and identify appropriate service options.

The Warranty Service Management System aims to organize these activities in a centralized web application, making warranty and service information easier to access and manage.

## 🎯 Objectives

- Provide a centralized platform for warranty-related information.
- Organize product details and warranty records.
- Support service appointment management.
- Provide access to service centre information.
- Maintain product and service-related records systematically.
- Separate frontend presentation from backend application logic.
- Provide a foundation for future improvements in warranty tracking and customer service.

## ✨ Features

### 1. User Interface

- Dedicated web pages for different application functions.
- Login page for the user authentication interface.
- Dashboard for accessing application features.
- Consistent styling using CSS.
- JavaScript files for frontend functionality and API communication.

### 2. Product Management

- Product listing page.
- Add-product interface.
- Individual product details page.
- Centralized organization of product information.

### 3. Warranty Management

- Warranty-related backend module.
- Support for organizing warranty information.
- Foundation for tracking warranty records and expiry information.

### 4. Service Appointment Management

- Dedicated appointments page.
- Backend appointment management module.
- Organization of service-related appointment information.

### 5. Service Centre Management

- Dedicated service centre page.
- Backend module for service centre information.
- Centralized access to service-related details.

### 6. Additional Backend Modules

The backend is divided into multiple Django applications:

- Accounts
- Products
- Warranties
- Appointments
- Service Centres
- Service History
- Documents
- Health Checks
- Notifications

The exact functionality available in each module depends on its implementation in the source code.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| HTML5 | Structure of web pages |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions |
| Python | Backend programming |
| Django | Backend web framework |
| SQLite | Local database |
| Git | Version control |
| GitHub | Source code hosting |
| Visual Studio Code | Development environment |

## 📂 Project Structure

```text
warranty-service-management-system/
│
└── warranty_tracker/
    │
    ├── README.md
    ├── ABSTRACT.md
    ├── API_DOCUMENTATION.md
    ├── ARCHITECTURE.md
    ├── DEMO_GUIDE.md
    ├── PROJECT_DOCUMENTATION.md
    ├── PROJECT_STRUCTURE.md
    ├── OBJECTIVES.md
    ├── LIMITATIONS.md
    ├── HEALTH_RULE_ENGINE.md
    ├── REQUIREMENTS_TRACEABILITY.md
    ├── VIVA_QUESTIONS.md
    │
    ├── backend/
    │   │
    │   ├── manage.py
    │   ├── db.sqlite3
    │   ├── .env.example
    │   │
    │   ├── config/
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── asgi.py
    │   │   └── wsgi.py
    │   │
    │   └── apps/
    │       │
    │       ├── accounts/
    │       ├── appointments/
    │       ├── documents/
    │       ├── health_checks/
    │       ├── notifications/
    │       ├── products/
    │       ├── service_centres/
    │       ├── service_history/
    │       └── warranties/
    │
    └── frontend/
        │
        ├── index.html
        ├── login.html
        ├── dashboard.html
        ├── products.html
        ├── add-product.html
        ├── product.html
        ├── appointments.html
        ├── service-centres.html
        │
        ├── css/
        │   └── style.css
        │
        └── js/
            ├── api.js
            └── layout.js
```

**Note:** The structure above summarizes the main files and directories. Some supporting files, migrations, management commands, and tests are omitted for readability.

## 🏗️ System Architecture

The application follows a frontend-backend architecture.

```text
           USER
             |
             v
      WEB FRONTEND
   HTML, CSS, JavaScript
             |
             v
      API COMMUNICATION
             |
             v
       DJANGO BACKEND
             |
      +------+------+ 
      |      |      |
      v      v      v
   Products Warranties Appointments
      |      |      |
      +------+------+ 
             |
             v
          DATABASE
           SQLite
```

### Architecture Components

**1. Frontend**

The frontend provides the user interface through HTML, CSS, and JavaScript.

**2. API communication**

The frontend JavaScript handles communication with the backend through the application's configured API endpoints.

**3. Backend**

Django handles URL routing, application logic, and database interactions through its application modules.

**4. Database**

SQLite provides local database storage for development.

## ⚙️ Prerequisites

Install the following software before running the application:

- Python
- pip, the Python package installer
- Visual Studio Code or another code editor
- Git
- A modern web browser

Verify the installations:

```bash
python --version
python -m pip --version
git --version
```

If the `python` command is unavailable on Windows, try:

```bash
py --version
```

## 🚀 Installation and Setup

### Step 1: Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/JaiHarsan/warranty-service-management-system.git
```

### Step 2: Open the project

```bash
cd warranty-service-management-system
```

Open the project in Visual Studio Code:

```bash
code .
```

### Step 3: Navigate to the backend

```bash
cd warranty_tracker/backend
```

### Step 4: Create a virtual environment

A virtual environment keeps project dependencies separate from other Python projects.

On Windows:

```bash
python -m venv venv
```

Activate it using Command Prompt:

```bash
venv\Scripts\activate
```

If you are using PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

If the project contains a `requirements.txt` file, install its dependencies using:

```bash
python -m pip install -r requirements.txt
```

If that file is not present, install Django:

```bash
python -m pip install django
```

Install any additional dependencies required by the actual source code before running the application.

### Step 6: Configure environment variables

Review the `.env.example` file and the backend settings.

If the project requires environment variables, create a local `.env` file and provide the appropriate values.

Do not commit real passwords, secret keys, API tokens, or other sensitive information to GitHub.

### Step 7: Apply database migrations

Run:

```bash
python manage.py migrate
```

This creates or updates the database tables required by the Django application.

### Step 8: Start the backend server

```bash
python manage.py runserver
```

When Django starts successfully, open:

http://127.0.0.1:8000/

If the application uses a different configured port, use the address shown in the terminal.

## ▶️ Running the Application

### Start the backend

Open a terminal in the backend directory:

```bash
cd warranty_tracker/backend
```

Activate the virtual environment if necessary:

```bash
venv\Scripts\activate
```

Start the Django development server:

```bash
python manage.py runserver
```

### Open the frontend

The frontend files are located in:

```text
warranty_tracker/frontend/
```

Open `index.html` in a browser or use the Live Server extension in Visual Studio Code if appropriate for the application.

**Important:** If the frontend makes API requests to Django, keep the backend running and ensure the API base URL and browser CORS/CSRF settings match the actual project configuration. Opening the HTML files alone does not start the backend.

## 🖥️ Application Pages

| Page | File | Purpose |
|---|---|---|
| Home | `index.html` | Main application entry page |
| Login | `login.html` | User login interface |
| Dashboard | `dashboard.html` | Central navigation and overview |
| Products | `products.html` | Product listing interface |
| Add Product | `add-product.html` | Product entry interface |
| Product Details | `product.html` | Individual product information |
| Appointments | `appointments.html` | Service appointment interface |
| Service Centres | `service-centres.html` | Service centre information |

The actual functionality of each page depends on the frontend JavaScript and backend integration.

## 🔧 Backend Modules

The backend is divided into Django applications to organize different responsibilities.

| Module | Responsibility |
|---|---|
| `accounts` | Account-related functionality |
| `products` | Product information and management |
| `warranties` | Warranty-related records and logic |
| `appointments` | Service appointment functionality |
| `service_centres` | Service centre information |
| `service_history` | Service history functionality |
| `documents` | Document-related functionality |
| `health_checks` | Health-check logic and rules |
| `notifications` | Notification-related functionality |

Each module contains Python files such as `models.py`, `views.py`, `urls.py`, and `tests.py`, where applicable.

- **Models:** Define database structures and relationships.
- **Views:** Handle requests and application logic.
- **URLs:** Map URL patterns to views.
- **Tests:** Contain automated tests for application behavior.
- **Migrations:** Track database schema changes.

## 🔗 API Documentation

Detailed API information is maintained in:

[`API_DOCUMENTATION.md`](API_DOCUMENTATION.md)

The Django backend defines its URL configuration in:

```text
backend/config/urls.py
```

Individual application URL files include:

```text
backend/apps/accounts/urls.py
backend/apps/products/urls.py
backend/apps/warranties/urls.py
backend/apps/appointments/urls.py
backend/apps/service_centres/urls.py
backend/apps/service_history/urls.py
backend/apps/documents/urls.py
backend/apps/health_checks/urls.py
backend/apps/notifications/urls.py
```

The exact endpoint paths, HTTP methods, request fields, and response formats should be taken from the implemented URL patterns and API documentation.

## 🗄️ Database

The project includes a local SQLite database:

```text
backend/db.sqlite3
```

SQLite is useful for local development because it does not require a separate database server.

Django models and migrations manage the database structure.

Useful commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

To create a Django administrator account, if the project uses Django's admin interface:

```bash
python manage.py createsuperuser
```

Then start the development server and visit:

http://127.0.0.1:8000/admin/

The administrator URL may differ if the project has customized its URL configuration.

**Database note:** Do not publish a database containing private user information, real credentials, or confidential records. For a fresh installation, follow the project's database and demo-data instructions.

## 🧪 Testing

Django provides a built-in testing framework.

Run the project's automated tests using:

```bash
python manage.py test
```

You can also run tests for a specific application. For example:

```bash
python manage.py test apps.products
```

Use the correct application label if the project's Django configuration defines a different label.

Recommended manual testing:

- Verify that the frontend pages load correctly.
- Check whether the backend starts without errors.
- Test product-related operations.
- Test warranty-related functionality.
- Check appointment-related operations.
- Verify service centre information.
- Check API responses and error handling.
- Confirm that data is stored and retrieved correctly.

## 🔐 Security Considerations

- Keep secret keys and passwords outside the public repository.
- Use environment variables for sensitive configuration.
- Never publish private user data or confidential database records.
- Configure Django's `DEBUG` setting appropriately before deployment.
- Set `ALLOWED_HOSTS` for the intended deployment environment.
- Use HTTPS for production deployments.
- Validate and sanitize user input.
- Configure authentication, permissions, CSRF protection, and CORS as required by the application.
- Do not use Django's development server as a production server.

## 🚧 Future Enhancements

Potential improvements include:

- Automatic warranty expiry reminders.
- Email or SMS notifications for service appointments.
- Product purchase and warranty document uploads.
- Warranty expiry status indicators.
- Advanced product search and filtering.
- Service appointment status tracking.
- Improved customer and administrator dashboards.
- Reporting and analytics.
- Role-based access control.
- Automated deployment and production hosting.
- Expanded automated testing.

These are possible future improvements and are not necessarily implemented in the current version.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes.
4. Test the application.
5. Commit your changes.

   ```bash
   git add .
   git commit -m "Add your feature"
   ```

6. Push your branch.

   ```bash
   git push origin feature/your-feature
   ```

7. Open a Pull Request on GitHub.

Please ensure that your changes do not introduce secrets, unnecessary generated files, or unrelated modifications.

## 📄 License

No license has been specified here. If you want others to reuse, modify, or distribute this project, add an appropriate `LICENSE` file to the repository.

## 👨‍💻 Author

**Jai Harsan**

GitHub: [@JaiHarsan](https://github.com/JaiHarsan)

Project Repository: [Warranty Service Management System](https://github.com/JaiHarsan/warranty-service-management-system)

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.

**Warranty Service Management System — Organizing product warranties and service information in one place.**

