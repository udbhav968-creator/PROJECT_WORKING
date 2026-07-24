# 🏥 Healthcare Clinic Backend API

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20.svg?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-00758F.svg?logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT_SimpleJWT-black.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg?logo=githubactions&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-Collection-FF6C37.svg?logo=postman&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

> Enterprise-grade RESTful backend for the **Healthcare Clinic Website**, developed as an internship project at **PY Digital Services Pvt. Ltd.**

---

## 📑 Table of Contents
1. [Tech Stack](#tech-stack)
2. [Team Module Allocation](#team-module-allocation)
3. [Module 4 – Administration & System Integration](#module-4--administration--system-integration)
4. [Project Structure](#project-structure)
5. [Quickstart (Local Setup)](#quickstart-local-setup)
6. [MySQL Configuration](#mysql-configuration)
7. [API Endpoints Reference](#api-endpoints-reference)
8. [JWT Authentication Guide](#jwt-authentication-guide)
9. [Running Tests](#running-tests)
10. [Postman Collection](#postman-collection)
11. [CI/CD Pipeline](#cicd-pipeline)
12. [Deployment (Vercel)](#deployment-vercel)

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
| **Udbhav** | **Module 4 – Administration & System Integration** | Base Models, Admin Dashboard APIs, Exception Handling, API Docs, Postman, Testing, CI/CD |

---

## 🏗️ Module 4 – Administration & System Integration

> **Owner: Udbhav**

This module is the **architectural backbone** of the entire backend. Every other module inherits from the foundations built here.

---

### 1. 🛡️ Database Design & Optimization

**File:** [`Backend/apps/core/models.py`](./Backend/apps/core/models.py)

All database models across the project inherit from `TimeStampedModel`, which provides:

| Feature | Implementation | Why It Matters |
| :--- | :--- | :--- |
| **UUID Primary Keys** | `uuid.uuid4()` (36-char string) | Prevents sequential ID enumeration attacks |
| **Soft Deletion** | `is_deleted = BooleanField(default=False)` | Medical records must never be hard-deleted |
| **Auto Timestamps** | `created_at`, `updated_at` (auto-managed) | Full audit trail on every record |
| **SoftDeleteManager** | Filters `is_deleted=False` on all default queries | Deleted records are invisible to normal ORM calls |
| **MySQL Support** | `PyMySQL.install_as_MySQLdb()` in `clinic_core/__init__.py` | Django connects to MySQL without C extension dependencies |

---

### 2. 📊 Admin Dashboard APIs

**File:** [`Backend/apps/administration/views.py`](./Backend/apps/administration/views.py)

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/admin/dashboard/` | `GET` | Aggregated system stats + 5 recent audit logs |
| `/api/admin/health/` | `GET` | Live DB connection status + timestamp |
| `/api/admin/audit-logs/` | `GET` | Paginated list of all admin audit log entries |
| `/api/admin/seed-demo-data/` | `POST` | Seeds test users & appointments (idempotent) |

**Performance approach:** Uses Django ORM `Count()` + `Q()` conditional filters to calculate all user and appointment statistics in **a single database roundtrip** per table — no Python-level loops.

---

### 3. 🚨 Exception Handling

**File:** [`Backend/apps/core/exceptions.py`](./Backend/apps/core/exceptions.py)

Registered as `EXCEPTION_HANDLER` in DRF settings. Intercepts **all** exception types and normalises them into a single, predictable response shape:

```json
{
  "success": false,
  "errors": [
    "email: This field is required.",
    "password: Ensure this field has at least 8 characters."
  ]
}
```

---

### 4. 📚 API Documentation

Auto-generated from code using `drf-spectacular`. No manual maintenance needed — the docs update themselves as new endpoints are added by other team members.

| URL | Interface |
| :--- | :--- |
| `/api/docs/` | Swagger UI (interactive) |
| `/api/redoc/` | ReDoc (clean reference) |
| `/api/schema/` | Raw OpenAPI 3.0 JSON |

---

### 5. 📬 Postman Collection

**File:** [`Backend/Postman_Collection.json`](./Backend/Postman_Collection.json)

Import this file directly into Postman. Contains all request templates for:
- JWT Token obtain & refresh
- System Health Check
- Admin Dashboard Summary
- Paginated Audit Logs
- Demo Data Seeding
- Swagger / ReDoc links

---

### 6. 🧪 Testing & Debugging

**File:** [`Backend/apps/administration/tests.py`](./Backend/apps/administration/tests.py)

10 automated unit tests covering:
- Health check DB connectivity
- Response timestamp presence
- Idempotent data seeding
- Dashboard response structure validation
- Dashboard stats key verification
- User and appointment count assertions
- Paginated audit log list (count + results keys)

Run with: `python manage.py test`

---

### 7. ⚙️ Backend Integration

- **CORS**: `django-cors-headers` middleware registered for cross-origin frontend access.
- **JWT**: `SimpleJWT` Bearer token authentication wired into DRF's `DEFAULT_AUTHENTICATION_CLASSES`.
- **Rate Limiting**: DRF throttling configured: `anon: 100/day`, `user: 1000/day`.
- **Environment Variables**: All secrets loaded from `.env` via `django-environ`. Never hardcoded.
- **Pagination**: `PageNumberPagination` (10 results/page, configurable via `?page_size=`) applied globally.

---

### 8. 🔍 Final Review

- All models support **soft deletion** — no medical record is ever permanently erased.
- All API responses follow a **uniform `success` / `errors` schema**.
- All credentials are **loaded from environment variables** — zero secrets in code.
- All endpoints are **documented in Swagger UI** and **testable in Postman**.
- GitHub Actions **CI pipeline auto-runs tests** on every push to `main`.

---

## 📁 Project Structure

```
PROJECT_WORKING/
├── .github/
│   └── workflows/
│       └── django_ci.yml          # CI/CD – runs tests on every push
│
├── Backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env                        # Environment variables (gitignored in prod)
│   ├── vercel.json                 # Serverless deployment config
│   ├── Postman_Collection.json     # Ready-to-import Postman file
│   │
│   ├── clinic_core/                # Django project core
│   │   ├── __init__.py             # PyMySQL driver initialization
│   │   ├── settings.py             # All Django + DRF + JWT + MySQL settings
│   │   ├── urls.py                 # Master URL router
│   │   └── wsgi.py                 # WSGI entrypoint
│   │
│   └── apps/
│       ├── core/                   # Shared foundation
│       │   ├── models.py           # TimeStampedModel (UUID + soft-delete)
│       │   └── exceptions.py       # Custom DRF exception handler
│       │
│       ├── authentication/         # Users & Roles
│       │   ├── models.py           # RoleModel, UserProfileModel
│       │   └── admin.py            # Django Admin registration
│       │
│       └── administration/         # Udbhav's Module 4
│           ├── models.py           # AppointmentModel, AdminAuditLogModel
│           ├── serializers.py      # DRF Serializers
│           ├── views.py            # Dashboard, Health, AuditLogs, Seed views
│           ├── urls.py             # URL patterns
│           ├── admin.py            # Django Admin registration
│           └── tests.py            # 10 automated unit tests
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

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Seed demo data via Postman or run:
# POST http://127.0.0.1:8000/api/admin/seed-demo-data/

# 6. Start development server
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

To switch from SQLite to MySQL, set these in your `.env` file:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=clinic_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

The `PyMySQL` driver is pre-configured — **no additional C libraries or `mysqlclient` needed**.

---

## 🔑 JWT Authentication Guide

1. **Obtain Token** — `POST /api/token/` with `{"username": "...", "password": "..."}`
2. **Use Token** — Add `Authorization: Bearer <access_token>` header to protected requests
3. **Refresh Token** — `POST /api/token/refresh/` with `{"refresh": "<refresh_token>"}`

- Access token expires in **60 minutes**
- Refresh token expires in **1 day**

---

## 🧪 Running Tests

```bash
cd Backend
python manage.py test
```

**Expected output:**
```
Found 10 test(s).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.XXXs
OK
```

---

## 📬 Postman Collection

1. Open **Postman**
2. Click **Import**
3. Select `Backend/Postman_Collection.json`
4. Run requests in this order:
   - `POST /api/admin/seed-demo-data/` — seed test data
   - `GET /api/admin/health/` — verify DB connection
   - `GET /api/admin/dashboard/` — view analytics
   - `GET /api/admin/audit-logs/` — view paginated logs

---

## 🤖 CI/CD Pipeline

On every `git push` to `main`:

1. GitHub Actions boots an **Ubuntu runner**
2. Installs **Python 3.11** and all `requirements.txt` dependencies
3. Runs `python manage.py test`
4. ✅ Green badge = all tests pass

---

## ☁️ Deployment (Vercel)

The `Backend/vercel.json` is configured for **serverless WSGI deployment** on Vercel. Set your environment variables in the Vercel dashboard and deploy directly from this GitHub repository.
