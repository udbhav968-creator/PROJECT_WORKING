# 🏥 Pure Health Clinic Backend & Full-Stack Medical System
### Enterprise Healthcare Portal, OPD Token Management & Administration Integration

![Build Status](https://img.shields.io/badge/CI%2FCD%20Pipeline-PASSED%20(28%2F28%20Tests)-02c39a?style=for-the-badge&logo=githubactions)
![Django Version](https://img.shields.io/badge/Django-5.0.0-092e20?style=for-the-badge&logo=django)
![DRF Version](https://img.shields.io/badge/DRF-3.14.0-a30000?style=for-the-badge&logo=django)
![Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-brightgreen?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ed?style=for-the-badge&logo=docker)

---

## 🌐 Live Production Cloud Deployments

| Component / Layer | Live Cloud URL | Description |
| :--- | :--- | :--- |
| 🚀 **Live Production REST API Core** | [https://project-working-snojkumar968-9939s-projects.vercel.app](https://project-working-snojkumar968-9939s-projects.vercel.app) | Root JSON directory & live backend REST service |
| ⚡ **Interactive Swagger UI (OpenAPI 3.0)** | [https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/](https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/) | Interactive API testing documentation portal |
| 📖 **ReDoc Technical Schema** | [https://project-working-snojkumar968-9939s-projects.vercel.app/api/redoc/](https://project-working-snojkumar968-9939s-projects.vercel.app/api/redoc/) | Comprehensive OpenAPI schema documentation |
| 👤 **GitHub Personal Repository** | [https://github.com/udbhav968-creator/PROJECT_WORKING](https://github.com/udbhav968-creator/PROJECT_WORKING) | Synchronized code repository |

---

## 👨‍💻 Complete Full-Stack Team Architecture Matrix

| Module | Core Deliverables & Features | Assigned Developer | Status |
| :--- | :--- | :--- | :---: |
| **Module 1: Authentication & User Management** | User Registration (`/api/auth/register/`), Login (`/api/auth/login/`), User Profile (`/api/auth/profile/`), SimpleJWT Tokens & Role-Based Access Control (`IsAdminUserRole`, `IsDoctorUserRole`, `IsPatientUserRole`) | Thota Harshavardhan Reddy | ✅ **100% Complete** |
| **Module 2: OPD Appointments & Queue Management** | Clinical OPD Token Auto-Generator (`PURE-OPD-XXXX`), Tele-Health Video Room Auto-Generator, Emergency Triage Alerts, Reception Printable OPD Slip Generator (`/api/admin/appointments/<uuid>/slip/`) | Alok Verma | ✅ **100% Complete** |
| **Module 3: Content Management APIs** | Medical Services Catalog (`/api/content/services/`), Doctors Directory (`/api/content/doctors/`), Medical Blogs (`/api/content/blogs/`), Testimonials (`/api/content/testimonials/`), Contact Inquiries (`/api/content/contact/`) | Aniket Ghatage | ✅ **100% Complete** |
| **Module 4: Administration & System Integration** | Single-Query Analytics Engine (`/api/admin/dashboard/`), Financial OPD Revenue Calculation, System Health Monitor (`/api/admin/health/`), NABH Audit Trail Logging (`/api/admin/audit-logs/`), Postman Collection, Database DDL Dump, Automated Test Suite (28 Tests) | Udbhav | ✅ **100% Complete** |

---

## ⚡ Complete REST API Reference Table

| Module | HTTP Method | Endpoint Path | Description |
| :--- | :---: | :--- | :--- |
| **Module 1** | `POST` | `/api/auth/register/` | Register new Patient, Doctor, or Staff user |
| **Module 1** | `POST` | `/api/auth/login/` | User Login & acquire JWT access/refresh tokens |
| **Module 1** | `GET` | `/api/auth/profile/` | Retrieve authenticated user profile & assigned role |
| **Module 2** | `GET` | `/api/admin/appointments/` | List & filter OPD appointments by status/dept/priority |
| **Module 2** | `POST` | `/api/admin/appointments/` | Book OPD Token, generate video room link & trigger SMS/WhatsApp payload |
| **Module 2** | `GET` | `/api/admin/appointments/<uuid>/slip/` | Printable HTML OPD token slip for reception desks |
| **Module 3** | `GET` | `/api/content/services/` | List medical services & clinical specialties |
| **Module 3** | `GET` | `/api/content/doctors/` | List board-certified doctors & OPD shift hours |
| **Module 3** | `GET` | `/api/content/blogs/` | List health blog articles & patient education posts |
| **Module 3** | `GET` | `/api/content/testimonials/` | List approved patient reviews & rating feedback |
| **Module 3** | `POST` | `/api/content/contact/` | Submit patient contact inquiry & helpdesk message |
| **Module 4** | `GET` | `/api/admin/health/` | System DB health monitor & latency benchmark |
| **Module 4** | `GET` | `/api/admin/dashboard/` | Clinical analytics, revenue calculation & doctor duty roster |
| **Module 4** | `GET` | `/api/admin/audit-logs/` | NABH & HIPAA audit trail log viewer |

---

## 🧪 Automated Testing & Verification

Run the full 28-unit test suite locally:

```bash
cd Backend
python manage.py test apps.core apps.authentication apps.administration apps.content
```

Output:
```text
Found 28 test(s).
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 28 tests in 5.414s

OK
```

---

## 🐳 Docker Deployment Guide

Run the full-stack backend with MySQL 8.0 in 1 command:

```bash
docker-compose up --build -d
```
