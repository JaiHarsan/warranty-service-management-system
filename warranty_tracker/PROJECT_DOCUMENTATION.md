# WarrantyCare - Project Documentation

## 1. Project Title
WarrantyCare: Warranty & Proactive Product Service Intelligence Platform

## 2. Abstract
WarrantyCare is a full-stack platform designed to help consumers manage their product warranties, run rule-based health checks, and find nearby service centres.

## 3. Problem Statement
Consumers often forget warranty expiry dates, lose physical documents, and fail to recognize subtle hardware defects until the warranty has expired, leading to expensive out-of-pocket repairs.

## 4. Objectives
- Centralize warranty tracking and document storage.
- Provide automated reminders for expiring warranties.
- Offer an intelligent, symptom-based health check engine.
- Locate nearest relevant service centres based on product category.

## 5. Proposed Solution
WarrantyCare provides an intuitive web interface for managing a "Digital Warranty Wallet," receiving smart alerts, and submitting prototype appointment requests to service centres.

## 6. System Architecture
- **Frontend**: Single-page application built with HTML5, CSS3, and Vanilla JS, communicating via the Fetch API.
- **Backend**: Python, Django, Django REST Framework handling routing and authentication.
- **Database**: MongoDB paired with MongoEngine.

## 7. Technology Stack
- **Frontend**: HTML/CSS/Vanilla JavaScript
- **Backend**: Python 3, Django, DRF
- **Database**: MongoDB
- **Security**: Token-based custom auth, PBKDF2 Password Hashing

## 8. Main Modules
- **Accounts**: Registration, Login, Token generation, User Isolation
- **Products & Warranties**: CRUD and dynamic expiration calculus
- **Health Checks**: Rule engine evaluating symptoms and returning Risk Levels
- **Service Centres & Appointments**: Search logic and prototype booking system
- **Notifications & Documents**: Storage and alerting mechanisms

## 9. Database Design (MongoDB)
- `users`: stores `name`, `email`, `password_hash`, `token`, `created_at`
- `products`: stores `user_id`, `brand`, `product_name`, `category`
- `warranties`: references `product_id`, tracks `end_date`, `status`
- `health_checks`: stores symptom `responses`, evaluated `risk_level`
- `service_centres`: geospatial approximation via `latitude`/`longitude`
- `appointments`: tracks `service_centre_id`, `product_id`, `date`, `status`

## 10. API Architecture
RESTful stateless architecture relying on `Authorization: Bearer <token>` for access control and isolation.

## 11. Health Rule Engine
- **Input**: User selects YES/NO/NOT_SURE for symptoms (e.g. overheating).
- **Rule Evaluation**: Deterministic checks evaluate critical threshold conditions.
- **Risk Level**: GREEN, YELLOW, or RED.
- **Recommendation**: E.g. "Service Recommended."

## 12. Security
- Password hashing via Django's `make_password` (PBKDF2/bcrypt).
- Strict user isolation across all endpoints.
- `.env` configured to prevent secret leaks.

## 13. Testing
Automated logic and system checks performed via `manage.py check`.

## 14. Limitations
- OCR logic requires external API integrations (Google Cloud Vision).
- Appointment requests are internal prototypes.
- Native Django Admin is incompatible with MongoEngine.

## 15. Future Enhancements
- Email/SMS integrations for Cron jobs.
- AI-based generative diagnostic insights instead of rigid rule branches.
