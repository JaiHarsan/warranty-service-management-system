# System Architecture

## Component Flow
```text
[ User ]
   | (Browser UI)
   v
[ Vanilla JS Frontend ]
   | (Fetch API / JSON)
   | (Header: Bearer Token)
   v
[ Django REST API ]
   | (Authentication Middleware)
   | (Business Logic & Rule Engine)
   v
[ MongoEngine ORM ]
   | (BSON)
   v
[ MongoDB Local ]
```

## Health Check Engine Flow
```text
Product Symptoms (UI Form)
   -> POST /api/health-check/
   -> Django API evaluates token & owns product
   -> `evaluate()` inside `rules.py`
   -> Assigns [GREEN / YELLOW / RED] Risk Level
   -> Saves to MongoDB HealthCheck Collection
   -> Returns JSON Report payload to UI
```

