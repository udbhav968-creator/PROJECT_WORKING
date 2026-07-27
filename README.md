# 🏥 Healthcare Clinic Website & Appointment Management Backend API

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.7-092E20.svg?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.15.2-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-00758F.svg?logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-SimpleJWT_Bearer-black.svg)
![Telehealth](https://img.shields.io/badge/Telehealth-Jitsi_Video-blue.svg)
![Compliance](https://img.shields.io/badge/Compliance-NABH%2FHIPAA_Audit-green.svg)
![Tests](https://img.shields.io/badge/Tests-23%2F23_Passed-brightgreen.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg?logo=githubactions&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Vercel_Serverless-000000.svg?logo=vercel&logoColor=white)

> Enterprise-grade, production-scaled RESTful API backend for the **Healthcare Clinic Website & Appointment Management System**, developed as an engineering project at **PY Digital Services Pvt. Ltd.** Reference Inspiration: [Divit Pure Health Clinic](https://divitpurehealthclinic.com/).

---

## 📑 Table of Contents
1. [Executive Overview](#-executive-overview)
2. [Technology Stack](#-technology-stack)
3. [Team Module Allocation](#-team-module-allocation)
4. [Module 4 — Administration & System Integration](#-module-4--administration--system-integration)
5. [Enterprise Production Scaling & Hardening](#-enterprise-production-scaling--hardening)
6. [Advanced Clinical & Enterprise Features](#-advanced-clinical--enterprise-features)
7. [Core Architecture & Design Patterns](#-core-architecture--design-patterns)
8. [Comprehensive API Reference Table](#-comprehensive-api-reference-table)
9. [Project Directory Structure](#-project-directory-structure)
10. [Automated Testing & Quality Assurance](#-automated-testing--quality-assurance)
11. [Local Setup & Docker Deployment](#-local-setup--docker-deployment)
12. [MySQL Database Schema](#-mysql-database-schema)
13. [Postman Collection Guide](#-postman-collection-guide)
14. [CI/CD Pipeline & Cloud Deployment](#-cicd-pipeline--cloud-deployment)

---

## 🏛️ Executive Overview

The **Healthcare Clinic Backend** is an enterprise-tier Django REST Framework application designed for scalable clinical management, OPD appointment scheduling, patient record tracking, and administrative analytics.

Built with compliance-ready data structures, this project incorporates **UUID primary keys**, **soft deletion**, **Doctor Duty Roster tracking**, **Tele-consultation video room auto-generation**, **WhatsApp notification formatting**, **Printable OPD Slip HTML generation**, **NABH/HIPAA-compliant audit logging**, **MySQL connection pooling**, **DRF rate limiting throttles**, **production Docker containerization**, **real-time DB latency monitoring**, **OpenAPI 3.0 auto-documentation**, **GitHub Actions CI/CD automation**, and **serverless Vercel cloud deployment**.

---

## 🛠️ Technology Stack

| Layer | Technology | Version / Spec | Architectural Purpose |
| :--- | :--- | :--- | :--- |
| **Language** | **Python** | `3.10+` | Core backend programming language powering models, views, and business logic. |
| **Web Framework** | **Django** | `5.0.7` | Web framework managing ORM, security middleware, routing, and migrations. |
| **REST API Engine** | **Django REST Framework** | `3.15.2` | Building RESTful endpoints, serializers, viewsets, and rate limiting. |
| **Production Database** | **MySQL** | `8.0+` | Enterprise relational database storage engine with connection pooling (`CONN_MAX_AGE=600`). |
| **Database Driver** | **PyMySQL** | `1.1.1` | Pure-Python driver enabling MySQL connectivity without C-compile dependencies. |
| **Local Dev Database** | **SQLite** | `3` (Built-in) | Embedded database for zero-configuration local development and rapid testing. |
| **Containerization** | **Docker & Compose** | `3.8 Spec` | Containerized microservice deployment with Gunicorn (4 workers, 2 threads). |
| **Authentication** | **SimpleJWT** | `5.3.1` | JSON Web Token (JWT) access & refresh authentication scheme (`/api/token/`). |
| **Video Telehealth** | **Jitsi Meet API** | Open Protocol | Auto-generates instant video room links for remote tele-consultations. |
| **API Documentation** | **drf-spectacular** | `0.27.2` | OpenAPI 3.0 auto-generator powering **Swagger UI** (`/api/docs/`) and **ReDoc**. |
| **Environment Config** | **django-environ** | `0.11.2` | Secure environment variable parsing (`.env`). |
| **CORS Management** | **django-cors-headers** | `4.3.1` | Cross-Origin Resource Sharing middleware for front-end integration. |
| **Static Asset Server** | **Whitenoise** | `6.7.0` | Serverless static asset compilation (`CompressedStaticFilesStorage`). |
| **Testing Engine** | **Django APITestCase** | DRF Test Client | Automated unit testing framework (**23 tests passing across all 3 apps**). |
| **CI/CD** | **GitHub Actions** | Ubuntu Runner | Automated build, check, and test validation pipeline on every git commit. |
| **Cloud Hosting** | **Vercel** | `@vercel/python` | Serverless WSGI cloud deployment configuration (`vercel.json`). |

---

## 👨‍💻 Team Module Allocation

| Team Member | Assigned Module | Primary Responsibilities |
| :--- | :--- | :--- |
| Thota Harshavardhan Reddy | Module 1 — Authentication | User Registration, RBAC, User Profiles, Login APIs |
| Alok Verma | Module 2 — Appointments | OPD Booking Engine, Doctor Availability |
| Aniket Ghatage | Module 3 — Content | Medical Blogs, Testimonials, Service Catalog |
| **Udbhav** | **Module 4 — Administration & System Integration** | Core Abstract Models, Admin Dashboard APIs, Doctor Duty Roster, Tele-Consultation Video Links, WhatsApp Notification Generator, Printable OPD Slips, Audit Logging, Exception Handling, Swagger/ReDoc Docs, Postman Collection, MySQL DDL Schema, Dockerization, Production Connection Pooling, 100% Test Coverage, Vercel CI/CD |

---

## ⚡ Module 4 — Administration & System Integration

> **Module Lead: Udbhav**

Module 4 serves as the **core foundation** of the backend system. All other domain apps inherit from the base architecture designed in this module.

### Core Deliverables & Capabilities:
1. **📊 High-Performance Admin Analytics**: Aggregates user counts, appointment statuses, doctor availability, and emergency triage metrics in single database roundtrips using `Count` and `Q` conditional filters.
2. **🎟️ Clinical OPD Token Auto-Generation**: Automatically generates unique clinical OPD token identifiers (e.g. `PURE-OPD-9F3A12`, `PURE-GEN-101`).
3. **🩺 Doctor Duty Roster Tracker**: Manages real-time Doctor shift schedules (`On Duty`, `In Surgery`, `On Break`, `Off Duty`), assigned OPD rooms, and shift hours.
4. **📹 Tele-Consultation Video Room Auto-Generator**: Auto-generates instant Jitsi video room links (`https://meet.jit.si/purehealth-opd-XXXX`) for remote patients.
5. **📱 WhatsApp OPD Notification Generator**: Formats instant WhatsApp OPD booking messages for automated patient messaging.
6. **📄 Printable OPD Token Slip Endpoint**: Endpoint (`/api/admin/appointments/<id>/slip/`) rendering printable HTML slips for clinic reception desks.
7. **🏥 Department Breakdown Engine**: Aggregates patient statistics across clinical departments (General Consultation, Diagnostic Support, Chronic Care, Wellness Guidance, Cardiology, Neurology, Orthopedics, Emergency Care).
8. **🛡️ NABH & HIPAA Compliance Audit Logging**: Tracks administrative actions with severity tagging (`INFO`, `WARNING`, `CRITICAL`) and compliance categories.
9. **⚡ System Integration Health & Latency Monitor**: Real-time database connection test with microsecond-level query execution latency tracking (`database_latency_ms`).
10. **🚨 Custom Unified Exception Handler**: Intercepts all validation, database, HTTP, and system errors into a uniform JSON response contract (`{"success": false, "errors": [...]}`).

---

## 🔒 Enterprise Production Scaling & Hardening

| Feature | Production Configuration | Architectural Benefit |
| :--- | :--- | :--- |
| 🛡️ **Rate Limiting (DRF Throttling)** | `anon: 100/minute`, `user: 1000/minute` | Prevents DDoS attacks, brute-force login attempts, and API scraping. |
| 🗄️ **MySQL Connection Pooling** | `CONN_MAX_AGE = 600`, `CONN_HEALTH_CHECKS = True` | Reuses active MySQL database connections for 10 minutes, eliminating connection overhead. |
| 🔒 **Security Headers** | `SECURE_BROWSER_XSS_FILTER = True`, `SECURE_CONTENT_TYPE_NOSNIFF = True`, `X_FRAME_OPTIONS = 'DENY'` | Protects against XSS attacks, MIME-sniffing vulnerabilities, and Clickjacking. |
| 📝 **Structured Process Logging** | Verbose formatters for `clinic_core` and `django.request` with ISO timestamps | Real-time production auditing compatible with Datadog / Sentry / ELK. |
| 🐳 **Production Docker Container** | `Dockerfile` (Python 3.10-slim + Gunicorn 4 workers / 2 threads) | 1-command reproducible production container deployment. |
| 🐙 **Docker Compose** | `docker-compose.yml` linking MySQL 8.0 & Django Gunicorn service | Production multi-container orchestration. |

---

## 🚀 Advanced Clinical & Enterprise Features

### 1. Doctor Duty Roster (`DoctorRosterModel`)
Tracks live doctor shifts and room allocations across the hospital:
```python
class DoctorRosterModel(TimeStampedModel):
    doctor_name = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=100, choices=AppointmentModel.DEPARTMENT_CHOICES)
    shift_hours = models.CharField(max_length=100, default='09:00 AM - 05:00 PM')
    duty_status = models.CharField(max_length=50, choices=DUTY_STATUS_CHOICES, default='on_duty')
    room_number = models.CharField(max_length=50, default='OPD Room 101')
```

### 2. Tele-Consultation Video Room Link Auto-Generator
When an appointment is created with `consultation_type='Teleconsultation'`, a video room URL is automatically generated:
```python
if consult_type == "Teleconsultation" and not video_url:
    video_url = f"https://meet.jit.si/purehealth-opd-{token.lower()}"
```

### 3. Printable OPD Slip HTML Generator
Endpoint `GET /api/admin/appointments/<id>/slip/` returns printable HTML OPD token receipts formatted for clinic reception desk printers.

---

## 📐 Core Architecture & Design Patterns

### Secure Base Model (`TimeStampedModel`)
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

---

## 📡 Comprehensive API Reference Table

| Area | Endpoint | Method | Description | Access Level |
| :--- | :--- | :---: | :--- | :---: |
| **Root Landing** | `/` | `GET` | Live JSON API welcome page & directory | Public |
| **Authentication** | `/api/token/` | `POST` | Obtain JWT Access & Refresh Token Pair | Public |
| **Authentication** | `/api/token/refresh/` | `POST` | Refresh Expired JWT Access Token | Public |
| **System Health** | `/api/admin/health/` | `GET` | System health, DB ping, latency (ms), NABH compliance status | Public / Monitoring |
| **Admin Dashboard**| `/api/admin/dashboard/` | `GET` | Aggregated system stats, Doctor Roster status, department breakdown, audit logs | Admin / Staff |
| **Audit Logs** | `/api/admin/audit-logs/` | `GET` | Paginated admin audit logs with severity filtering (`?severity=CRITICAL`) | Admin / Compliance |
| **Appointments** | `/api/admin/appointments/` | `GET` | List appointments with pagination, department filter & search | Staff |
| **Appointments** | `/api/admin/appointments/` | `POST` | Create appointment, auto-generate OPD Token & Telehealth Video Link | Staff / Public |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `GET` | Retrieve detailed appointment record by UUID | Staff |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `PUT` | Update appointment details or status | Staff |
| **Appointments** | `/api/admin/appointments/<uuid:pk>/` | `DELETE` | Soft-delete appointment record | Admin |
| **OPD Slip Print** | `/api/admin/appointments/<uuid:pk>/slip/` | `GET` | Generate printable HTML OPD token slip for reception printing | Staff / Reception |
| **Demo Data** | `/api/admin/seed-demo-data/` | `POST` | Seeds test users, Doctor Roster & clinical appointments (idempotent) | Dev / Testing |
| **Documentation** | `/api/docs/` | `GET` | Interactive **Swagger UI** API documentation | Public |
| **Documentation** | `/api/redoc/` | `GET` | **ReDoc** OpenAPI visual documentation | Public |
| **Documentation** | `/api/schema/` | `GET` | Raw OpenAPI 3.0 JSON Schema | Public |

---

## 📂 Project Directory Structure

```
PROJECT_WORKING/
├── Dockerfile                  # Enterprise Gunicorn production Docker container
├── docker-compose.yml          # Multi-container orchestration (MySQL 8.0 + Django)
├── vercel.json                 # Vercel serverless deployment configuration
├── requirements.txt            # Root dependencies for deployment
├── .github/
│   └── workflows/
│       └── django_ci.yml       # GitHub Actions CI/CD workflow
│
├── Backend/
│   ├── manage.py               # Self-resolving path handler entrypoint
│   ├── requirements.txt        # Backend dependencies
│   ├── database_schema.sql     # MySQL DDL Database Schema Export File
│   ├── Postman_Collection.json # Importable Postman API collection
│   │
│   ├── clinic_core/            # Django Core System Configuration
│   │   ├── __init__.py         # PyMySQL driver initialization
│   │   ├── settings.py         # App config, JWT, CORS, DRF, Whitenoise, Throttles, Connection Pooling
│   │   ├── urls.py             # Master URL Router & Root Landing Page
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
│           ├── models.py       # AppointmentModel, DoctorRosterModel, AdminAuditLogModel
│           ├── serializers.py  # DRF Serializers, DoctorRoster & WhatsApp Text
│           ├── views.py        # Dashboard, Health, Audit, Appointment, Slip APIs
│           ├── urls.py         # App URL Routing
│           ├── admin.py        # Custom Admin Site Headers, Roster & Actions
│           └── tests.py        # 14 Administration Unit Tests
│
└── README.md
```

---

## 🧪 Automated Testing & Quality Assurance

The project features a **100% passing automated test suite** across all applications:

```bash
cd Backend
python manage.py test apps.core apps.authentication apps.administration
```

### Test Suite Execution Output:
```text
Found 23 test(s).
System check identified no issues (0 silenced).
.......................
----------------------------------------------------------------------
Ran 23 tests in 20.482s

OK
Destroying test database for alias 'default'...
```

---

## 🚀 Local Setup & Docker Deployment

### Option A: Local Python Environment
```bash
# 1. Clone repository
git clone https://github.com/pydigitalservices/HealthCare.git
cd HealthCare/Backend

# 2. Virtual environment & dependencies
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

# 3. Migrate and run
python manage.py migrate
python manage.py runserver
```

### Option B: Production Docker Deployment (1 Command)
```bash
docker-compose up --build -d
```

---

## 🗄️ MySQL Database Schema

An exported MySQL DDL schema file is located at **`Backend/database_schema.sql`**.

---

## 📬 Postman Collection Guide

An importable Postman collection is located at **`Backend/Postman_Collection.json`**.

---

## 🤖 CI/CD Pipeline & Cloud Deployment

- **GitHub Actions CI (`.github/workflows/django_ci.yml`)**: Executes system check (`python manage.py check`), static asset compilation (`collectstatic`), and runs all 23 unit tests on every push.
- **Vercel Cloud Deployment (`vercel.json`)**: Pre-configured for serverless WSGI execution on Vercel with Whitenoise static asset handling.
- **Live Vercel Production Deployment**: [https://project-working-snojkumar968-9939s-projects.vercel.app/](https://project-working-snojkumar968-9939s-projects.vercel.app/)
