# API Documentation

## Authentication
### `POST /api/register/`
Registers a new user. Expects `email`, `name`, `password`.

### `POST /api/login/`
Returns a Bearer token. Expects `email`, `password`.

### `POST /api/logout/`
Clears the token in the backend. Requires Authentication.

### `GET /api/me/`
Returns the currently authenticated user profile. Requires Authentication.

## Products
### `GET /api/products/`
Retrieves products for the authenticated user.

### `POST /api/products/`
Creates a product. Expects `brand`, `category`, `product_name`.

### `GET /api/products/<id>/`
Retrieves a specific product details.

## Health Checks
### `POST /api/health-check/`
Submits a health check. Evaluates rules and returns a risk score. Expects `product_id`, `responses` dict.

## Service Centres & Appointments
### `GET /api/service-centres/`
Returns mock service centres (supports filtering).

### `POST /api/appointments/`
Books a prototype appointment. Expects `product_id`, `service_centre_id`.

## Documents & Notifications
### `GET /api/documents/`
Lists user's uploaded documents.

### `GET /api/notifications/`
Lists unread/read notifications.
