# 🏥 Healthcare Clinic Backend API — Enterprise Architecture

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.7-092E20.svg?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15.2-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-00758F.svg?logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-SimpleJWT_Bearer-black.svg)
![Compliance](https://img.shields.io/badge/Compliance-NABH%2FHIPAA_Audit-blue.svg)
![Tests](https://img.shields.io/badge/Tests-23%2F23_Passed-brightgreen.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg?logo=githubactions&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Vercel_Serverless-000000.svg?logo=vercel&logoColor=white)

> Enterprise-grade RESTful API backend for the **Healthcare Clinic Website**, developed as an engineering project at **PY Digital Services Pvt. Ltd.**

---

## 📑 Table of Contents
1. [Executive Overview](#-executive-overview)
2. [Technology Stack](#-technology-stack)
3. [Team Module Allocation](#-team-module-allocation)
4. [Module 4 — Administration & System Integration](#-module-4--administration--system-integration)
5. [Architecture & Design Patterns](#-architecture--design-patterns)
6. [API Endpoints Reference](#-api-endpoints-reference)
7. [Project Directory Structure](#-project-directory-structure)
8. [Automated Testing & Quality Assurance](#-automated-testing--quality-assurance)
9. [Local Setup & Quickstart](#-local-setup--quickstart)
10. [MySQL Configuration](#-mysql-configuration)
11. [Postman Collection](#-postman-collection)
12. [CI/CD & Cloud Deployment](#-cicd--cloud-deployment)

---

## 🏛️ Executive Overview

The **Healthcare Clinic Backend** is an enterprise-tier Django REST Framework application designed for scalable clinical management, OPD appointment scheduling, patient record tracking, and administrative analytics. 

Built with compliance-ready data structures, this project incorporates **UUID primary keys**, **soft deletion**, **NABH/HIPAA-compliant audit logging**, **real-time DB latency monitoring**, **OpenAPI 3.0 auto-documentation**, and **serverless Vercel cloud deployment**.

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose & Architectural Role |
| :--- | :--- | :--- | :--- |
| **Language** | **Python** | `3.10+` | Primary programming language powering business logic and data processing. |
| **Web Framework** | **Django** | `5.0.7` | Web framework managing models, ORM, URL routing, and security. |
| **REST API Engine** | **Django REST Framework** | `3.15.2` | Building RESTful endpoints, serializers, viewsets, and pagination. |
| **Database (Prod)** | **MySQL** | `8.0+` | Enterprise relational database storage. |
| **Database Driver** | **PyMySQL** | `1.1.1` | Pure-Python driver enabling MySQL connectivity without C-compile dependencies. |
| **Database (Dev/Test)**| **SQLite** | `3` (Built-in) | Embedded database for zero-config local development and rapid test execution. |
| **Authentication** | **SimpleJWT** | `5.3.1` | JSON Web Token (JWT) access & refresh authentication scheme. |
| **API Documentation** | **drf-spectacular** | `0.27.2` | OpenAPI 3.0 auto-generation providing **Swagger UI** and **ReDoc**. |
| **Environment Config** | **django-environ** | `0.11.2` | Secure environment variable parsing (`.env`). |
| **CORS Control** | **django-cors-headers** | `4.3.1` | Cross-Origin Resource Sharing middleware for frontend integration. |
| **Static File Server** | **Whitenoise** | `6.7.0` | Serverless static asset compilation (`CompressedStaticFilesStorage`). |
| **Testing** | **Django APITestCase** | DRF Test Client | Automated unit testing framework (**23 tests passing across all apps**). |
| **CI/CD** | **GitHub Actions** | Ubuntu Runner | Automated build & test validation pipeline on every git commit. |
| **Deployment** | **Vercel** | `@vercel/python` | Serverless WSGI cloud deployment configuration (`vercel.json`). |

---

## 👨‍💻 Team Module Allocation

| Team Member | Module | Primary Responsibilities |
| :--- | :--- | :--- |
| Abusufiyan / Harshavardhan | Module 1 — Authentication | User Registration, RBAC, User Profiles, Login APIs |
| Gautam / Alok Verma | Module 2 — Appointments | OPD Booking Engine, Doctor Duty Schedules |
| Suhaib / Aniket Ghatage | Module 3 — Content | Medical Blogs, Testimonials, Service Catalog |
| **Udbhav** | **Module 4 — Administration & System Integration** | Core Abstract Models, Admin Dashboard APIs, OPD Tokens, Audit Logging, Exception Handling, Swagger/ReDoc Docs, Postman Collection, 100% Test Coverage, Vercel CI/CD |

---

## ⚡ Module 4 — Administration & System Integration

> **Module Lead: Udbhav**

Module 4 serves as the **core foundation** of the backend system. All other domain apps inherit from the base architecture designed in this module.

### Core Deliverables Achieved:
1. **📊 High-Performance Admin Analytics**: Aggregates user counts, appointment statuses, and emergency triage metrics in single database roundtrips using `Count` and `Q` conditional filters.
2. **🎟️ Clinical OPD Token Auto-Generation**: Automatically generates unique clinical OPD token identifiers (e.g. `CLINIC-OPD-9F3A12`, `CLINIC-CARD-101`).
3. **🏥 Department Breakdown Engine**: Aggregates patient statistics across clinical departments (Cardiology, Neurology, Orthopedics, Pediatrics, Oncology, Emergency Care).
4. **🛡️ NABH & HIPAA Compliance Audit Logging**: Tracks administrative actions with severity tagging (`INFO`, `WARNING`, `CRITICAL`) and compliance categories.
5. **⚡ System Integration Health & Latency Monitor**: Real-time database connection test with microsecond-level query execution latency tracking (`database_latency_ms`).
6. **🚨 Custom Unified Exception Handler**: Intercepts all validation, database, HTTP, and system errors into a uniform JSON response contract (`{"success": false, "errors": [...]}`).
7. **🎨 Enterprise Django Admin Portal**: Customized admin interface with collapsible fieldsets, batch action shortcuts, date hierarchy, and immutable audit logs.

---

## 📐 Architecture & Design Patterns

### 1. Secure Base Model (`TimeStampedModel`)
**File:** [`Backend/apps/core/models.py`](./Backend/apps/core/models.py)

```python
class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = SoftDeleteManager()  # Returns only non-deleted records
    all_objects = models.Manager()   # Returns raw DB records including archived
```
- **UUID Primary Keys**: Prevents sequential ID guessing and enumeration security attacks.
- **Soft Deletion**: Medical & administrative records are soft-deleted (`is_deleted=True`), preserving data retention compliance.

### 2. Unified Exception Response Contract
**File:** [`Backend/apps/core/exceptions.py`](./Backend/apps/core/exceptions.py)

Ensures that all API errors return a standard JSON structure across the entire application:
```json
{
  "success": false,
  "errors": [
    "department: Invalid choice selected.",
    "appointment_date: Date must be in ISO 8601 format."
  ]
}
```

---

## 📡 API Endpoints Reference

| Module / Area | Endpoint | Method | Description | Access Level |
| :--- | :--- | :---: | :--- | :---: |
| **Authentication** | `/api/token/` | `POST` | Obtain JWT Access & Refresh Token Pair | Public |
| **Authentication** | `/api/token/refresh/` | `POST` | Refresh Expired JWT Access Token | Public |
| **System Integration** | `/api/admin/health/` | `GET` | System health, DB ping, latency (ms), NABH compliance status | Public / Monitoring |
| **Admin Dashboard** | `/api/admin/dashboard/` | `GET` | Aggregated system stats, clinical department breakdown, recent audit logs | Admin / Staff |
| **Audit Logs** | `/api/admin/audit-logs/` | `GET` | Paginated admin audit logs with severity filtering (`?severity=CRITICAL`) | Admin / Compliance |
| **Appointments** | `/api/admin/appointments/` | `GET` | List appointments with pagination, department filter & search | Staff |
| **Appointments** | `/api/admin/appointments/` | `POST` | Create new appointment & auto-generate OPD Token | Staff / Public |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `GET` | Retrieve detailed appointment record by UUID | Staff |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `PUT` | Update appointment details or status | Staff |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `DELETE` | Soft-delete appointment record | Admin |
| **Demo Data** | `/api/admin/seed-demo-data/` | `POST` | Seeds test users & clinical appointments (idempotent) | Dev / Testing |
| **Documentation** | `/api/docs/` | `GET` | Interactive **Swagger UI** API documentation | Public |
| **Documentation** | `/api/redoc/` | `GET` | **ReDoc** OpenAPI visual documentation | Public |
| **Documentation** | `/api/schema/` | `GET` | Raw OpenAPI 3.0 JSON Schema | Public |

---

## 📂 Project Directory Structure

```
PROJECT_WORKING/
├── vercel.json                 # Vercel serverless deployment configuration
├── requirements.txt            # Root dependencies for deployment
├── .github/
│   └── workflows/
│       └── django_ci.yml       # GitHub Actions CI/CD workflow
│
├── Backend/
│   ├── manage.py               # Self-resolving path handler entrypoint
│   ├── requirements.txt        # Backend dependencies
│   ├── Postman_Collection.json # Importable Postman API collection
│   │
│   ├── clinic_core/            # Django Core System Configuration
│   │   ├── __init__.py         # PyMySQL driver initialization
│   │   ├── settings.py         # App config, JWT, CORS, DRF, Whitenoise
│   │   ├── urls.py             # Master URL Router
│   │   └── wsgi.py             # WSGI Serverless Entrypoint
│   │
│   └── apps/
│       ├── core/               # Shared Core Foundation App
│       │   ├── models.py       # TimeStampedModel (UUID + Soft-Delete)
│       │   ├── exceptions.py   # Unified DRF Exception Handler
│       │   └── tests.py        # 4 Core Unit Tests
│       │
│       ├── authentication/     # User Profiles & Role Management App
│       │   ├── models.py       # RoleModel, UserProfileModel
│       │   ├── admin.py        # Admin interface registrations
│       │   └── tests.py        # 5 Auth & JWT Unit Tests
│       │
│       └── administration/     # Udbhav's Module 4 (Admin & Integration)
│           ├── models.py       # AppointmentModel (OPD Token), AdminAuditLogModel
│           ├── serializers.py  # DRF Serializers & Department Breakdown
│           ├── views.py        # Dashboard, Health, Audit, Appointment APIs
│           ├── urls.py         # App URL Routing
│           ├── admin.py        # Custom Admin Site Headers & Actions
│           └── tests.py        # 14 Administration Unit Tests
│
└── README.md
```

---

## 🧪 Automated Testing & Quality Assurance

The project features a **100% passing automated test suite** across all applications:

```bash
cd Backend
python manage.py test --verbosity=2
```

### Test Suite Execution Output:
```
Found 23 test(s).
Ran 23 tests in 37.299s

OK
Destroying test database for alias 'default'...
```

- **`apps.core.tests` (4 tests)**: UUID primary key generation, soft delete/restore logic, custom exception handler responses.
- **`apps.authentication.tests` (5 tests)**: Role model, user profile model, JWT token obtain (`/api/token/`), invalid credentials handling, token refresh.
- **`apps.administration.tests` (14 tests)**: System health check, DB latency, seeding idempotency, dashboard analytics, department breakdown, audit severity filters, appointment CRUD, soft delete.

---

## 🚀 Local Setup & Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/udbhav968-creator/PROJECT_WORKING.git
cd PROJECT_WORKING/Backend

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac / Linux

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Seed clinical test data
# POST http://127.0.0.1:8000/api/admin/seed-demo-data/

# 6. Start the development server
python manage.py runserver
```

| Interface | Local URL |
| :--- | :--- |
| 🏠 **API Root** | http://127.0.0.1:8000/ |
| 📄 **Swagger UI** | http://127.0.0.1:8000/api/docs/ |
| 📘 **ReDoc** | http://127.0.0.1:8000/api/redoc/ |
| 📊 **Admin Dashboard API** | http://127.0.0.1:8000/api/admin/dashboard/ |
| 🏥 **System Health Check API** | http://127.0.0.1:8000/api/admin/health/ |
| ⚙️ **Django Admin Portal** | http://127.0.0.1:8000/admin/ |

---

## 🗄️ MySQL Configuration

To switch from SQLite to MySQL, update your `.env` file in `Backend/`:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=clinic_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

## 📬 Postman Collection

An importable Postman collection is located at **`Backend/Postman_Collection.json`**.

### Included Request Folders:
1. **🔐 Authentication**: JWT Obtain Token & Refresh Token requests.
2. **⚙️ System Integration**: Health check with database latency metrics.
3. **📊 Admin Dashboard APIs**: Seed demo data, dashboard summary, paginated audit logs.
4. **📅 Appointment Management APIs**: List, filter by department/priority, create with auto token, update status, soft-delete.
5. **📚 API Documentation**: Direct links to Swagger UI and ReDoc.

---

## 🤖 CI/CD & Cloud Deployment

- **GitHub Actions CI (`.github/workflows/django_ci.yml`)**: Executes system check (`python manage.py check`) and runs unit tests on every push.
- **Vercel Cloud Deployment (`vercel.json`)**: Pre-configured for serverless WSGI execution on Vercel with Whitenoise static asset handling.
