# 🏥 Healthcare Clinic Backend API – Enterprise Architecture

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20.svg?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-00758F.svg?logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT_SimpleJWT-black.svg)
![NABH/HIPAA](https://img.shields.io/badge/Compliance-NABH%2FHIPAA-blue.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg?logo=githubactions&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-Collection-FF6C37.svg?logo=postman&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

> Enterprise-grade RESTful backend for the **Healthcare Clinic Website**, developed as an internship project at **PY Digital Services Pvt. Ltd.**

---

## 📑 Table of Contents
1. [Tech Stack](#tech-stack)
2. [Team Module Allocation](#team-module-allocation)
3. [Module 4 – Administration & System Integration](#module-4--administration--system-integration)
4. [Enterprise Healthcare Features](#enterprise-healthcare-features)
5. [Project Structure](#project-structure)
6. [Quickstart (Local Setup)](#quickstart-local-setup)
7. [MySQL Configuration](#mysql-configuration)
8. [API Endpoints Reference](#api-endpoints-reference)
9. [JWT Authentication Guide](#jwt-authentication-guide)
10. [Running Tests](#running-tests)
11. [Postman Collection](#postman-collection)
12. [CI/CD Pipeline](#cicd-pipeline)
13. [Deployment (Vercel)](#deployment-vercel)

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| Language | Python 3.10+ |
| Web Framework | Django 5.0.7 |
| REST API Layer | Django REST Framework (DRF) 3.15 |
| Database (Production) | MySQL 8.0+ (via `PyMySQL` driver) |
| Database (Local Dev) | SQLite (zero-config fallback) |
| Authentication | JWT – `djangorestframework-simplejwt` |
| API Documentation | OpenAPI 3.0 – `drf-spectacular` (Swagger UI + ReDoc) |
| Environment Config | `django-environ` |
| CORS Handling | `django-cors-headers` |
| Static File Serving | `whitenoise` 6.7.0 |
| Testing | Django `APITestCase` (DRF TestClient) |
| API Testing Tool | Postman (Collection included) |
| Version Control | Git + GitHub |
| CI/CD | GitHub Actions |
| Deployment | Vercel (Serverless WSGI) |

---

## 👨‍💻 Team Module Allocation

| Team Member | Module | Responsibilities |
| :--- | :--- | :--- |
| Abusufiyan / Harshavardhan | Module 1 – Authentication | JWT Login, RBAC, User Management |
| Gautam / Alok Verma | Module 2 – Appointments | Booking APIs, Doctor Schedules |
| Suhaib / Aniket Ghatage | Module 3 – Content | Blogs, Testimonials, Services |
| **Udbhav** | **Module 4 – Administration & System Integration** | Base Models, Admin Analytics, OPD Tokens, Audit Logging, Appointment CRUD, Exception Handling, API Docs, Postman, Testing, CI/CD |

---

## 🏥 Enterprise Healthcare Features

Module 4 serves as the **architectural backbone** for the entire backend system, incorporating clinical & administrative best practices:

1. **🎟️ Clinical OPD Token Auto-Generation**:
   - Auto-generates unique OPD Token numbers (e.g. `CLINIC-OPD-9F3A12`, `CLINIC-CARD-101`).
   - Supports OPD, IPD, Emergency Care, and Teleconsultation routing.

2. **🏥 Department Breakdown & Priority Triage Analytics**:
   - Dynamic clinical statistics across departments (Cardiology, Neurology, Orthopedics, Pediatrics, Oncology, Emergency Care).
   - Real-time emergency triage monitoring (`emergency_triage_count`).

3. **🛡️ NABH & HIPAA Audit Trail**:
   - Audits administrative & clinical actions with severity classifications (`INFO`, `WARNING`, `CRITICAL`).
   - Tracks compliance categories (`NABH_PATIENT_SAFETY`, `HIPAA_PRIVACY`, `NABH_CLINICAL_UPDATE`).

4. **⚡ System Integration Health & Latency Monitor**:
   - `/api/admin/health/` returns database connectivity status, query execution latency in milliseconds (`database_latency_ms`), and compliance audit status.

---

## 🏗️ Module 4 – Core Implementation Detail

### 1. 🛡️ Database Design & Optimization
**File:** [`Backend/apps/core/models.py`](./Backend/apps/core/models.py)

All database models across the project inherit from `TimeStampedModel`, providing:
- **UUID Primary Keys** (`uuid.uuid4()`) preventing ID enumeration attacks.
- **Soft Deletion (`is_deleted`)** ensuring patient medical records are archived safely rather than hard-deleted.
- **SoftDeleteManager** filtering `is_deleted=False` on normal queries while retaining raw access via `all_objects`.

---

### 2. 📊 Admin Dashboard & Clinical APIs
**File:** [`Backend/apps/administration/views.py`](./Backend/apps/administration/views.py)

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/admin/dashboard/` | `GET` | Aggregated system stats, clinical department breakdown, and recent audit logs |
| `/api/admin/health/` | `GET` | System health, DB connection, latency (ms), and NABH compliance status |
| `/api/admin/audit-logs/` | `GET` | Paginated audit logs with severity filtering (`?severity=CRITICAL`) |
| `/api/admin/appointments/` | `GET` / `POST` | List/Search/Filter appointments & Create appointment with OPD Token |
| `/api/admin/appointments/<uuid:pk>/` | `GET` / `PUT` / `DELETE` | Retrieve, update status, or soft-delete an appointment |
| `/api/admin/seed-demo-data/` | `POST` | Seeds realistic clinical demo records (idempotent) |

---

### 3. 🚨 Exception Handling
**File:** [`Backend/apps/core/exceptions.py`](./Backend/apps/core/exceptions.py)

Intercepts all HTTP & database errors and normalises them into a single response contract:
```json
{
  "success": false,
  "errors": [
    "department: Invalid department choice.",
    "appointment_date: Date must be in ISO 8601 format."
  ]
}
```

---

### 4. 📚 API Documentation
Auto-generated OpenAPI 3.0 schema via `drf-spectacular`:
- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
- **ReDoc:** `http://127.0.0.1:8000/api/redoc/`
- **Schema JSON:** `http://127.0.0.1:8000/api/schema/`

---

### 5. 📬 Postman Collection
**File:** [`Backend/Postman_Collection.json`](./Backend/Postman_Collection.json)

Includes request templates for:
- JWT Token obtain & refresh
- System Health Check (with latency check)
- Admin Dashboard Summary & Department Breakdown
- Paginated Audit Logs & Severity Filter
- Full Appointment CRUD Operations (List, Create, Get, Update, Soft-Delete)
- Demo Data Seeding

---

### 6. 🧪 Automated Unit Testing
**File:** [`Backend/apps/administration/tests.py`](./Backend/apps/administration/tests.py)

14 automated unit tests covering:
- Health check latency & metadata
- Clinical data seeding idempotency
- Dashboard analytics structure & department breakdown keys
- Severity filtering on audit log list
- Appointment creation with token auto-generation
- Retrieval, updates, and soft-delete verification

Run with: `python manage.py test`

---

## 📁 Project Structure

```
PROJECT_WORKING/
├── vercel.json                 # Vercel serverless deployment configuration
├── requirements.txt            # Root dependencies for deployment
├── .github/
│   └── workflows/
│       └── django_ci.yml       # GitHub Actions CI pipeline
│
├── Backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Postman_Collection.json
│   │
│   ├── clinic_core/             # Django Core Configuration
│   │   ├── __init__.py          # PyMySQL initialization
│   │   ├── settings.py          # Settings, Whitenoise, JWT, CORS, DRF
│   │   ├── urls.py              # Root URL Router
│   │   └── wsgi.py              # WSGI Entrypoint
│   │
│   └── apps/
│       ├── core/                # Shared Core App
│       │   ├── models.py        # TimeStampedModel (UUID + Soft-Delete)
│       │   └── exceptions.py    # Custom Exception Handler
│       │
│       ├── authentication/      # Auth & Role Management
│       │   ├── models.py        # UserProfileModel, RoleModel
│       │   └── admin.py
│       │
│       └── administration/      # Udbhav's Module 4 (Administration & System Integration)
│           ├── models.py        # AppointmentModel (OPD Token), AdminAuditLogModel (NABH)
│           ├── serializers.py   # Serializers & Department Breakdown
│           ├── views.py         # Dashboard, Health, Audit, Appointment APIs
│           ├── urls.py          # URL Routing
│           ├── admin.py         # Django Admin Registrations
│           └── tests.py         # 14 Automated Unit Tests
│
└── README.md
```

---

## 🚀 Quickstart (Local Setup)

```bash
# 1. Navigate to backend
cd Backend

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Seed clinical demo data
# POST http://127.0.0.1:8000/api/admin/seed-demo-data/

# 6. Run server
python manage.py runserver
```

| Interface | URL |
| :--- | :--- |
| 🏠 API Root | http://127.0.0.1:8000/ |
| 📄 Swagger UI | http://127.0.0.1:8000/api/docs/ |
| 📘 ReDoc | http://127.0.0.1:8000/api/redoc/ |
| 🔑 JWT Token | http://127.0.0.1:8000/api/token/ |
| 📊 Admin Dashboard | http://127.0.0.1:8000/api/admin/dashboard/ |
| 🏥 Django Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🗄️ MySQL Configuration

Set the following in `.env` to connect to MySQL:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=clinic_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

## 🧪 Running Tests

```bash
cd Backend
python manage.py test apps.administration
```

**Expected Output:**
```
Found 14 test(s).
..............
----------------------------------------------------------------------
Ran 14 tests in 1.288s

OK
```

---

## 🤖 CI/CD Pipeline & Cloud Deployment

- **GitHub Actions:** Auto-runs unit tests on every push to `main`.
- **Vercel Deployment:** Built with `vercel.json` WSGI configuration and `whitenoise` static asset handling.
