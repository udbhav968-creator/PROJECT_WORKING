# 🏥 Healthcare Clinic Website & Backend

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg)

Welcome to the **Healthcare Clinic Website & Backend Repository**. This project was developed as part of the internship assignment at **PY Digital Services Pvt. Ltd.**

---

## 👨‍💻 Team Module Allocations

| Team Member | Module Assignment | Key Responsibilities |
| :--- | :--- | :--- |
| **Abusufiyan / Harshavardhan** | *Authentication* | JWT Auth, RBAC, User/Doctor Login |
| **Gautam / Alok Verma** | *Appointments* | Booking APIs, Doctor Schedules |
| **Suhaib / Aniket Ghatage** | *Content* | Blogs, Testimonials, Services |
| **Udbhav** | *Administration & System Integration* | Base Database Models, Soft-Deletion, Admin Dashboard APIs, Global Exception Middleware, API Docs, CI/CD |

---

## 🏗️ Module 4: Administration & System Integration (Udbhav's Work)

This module forms the underlying core architecture of the backend. Key implementations include:

### 1. 🛡️ Database Architecture & Soft-Deletion (`BaseModel`)
- **UUIDv4 Primary Keys**: Replaced auto-incrementing integer IDs with 36-character UUID strings to eliminate ID enumeration security risks.
- **Soft Deletion (`is_deleted`)**: Medical records cannot be permanently destroyed. All ORM models inherit an `is_deleted` flag, preserving data for regulatory compliance while filtering it out of routine API queries.
- **Timestamps**: Automatic `created_at` and `updated_at` timestamps for every database record.

### 2. 📊 High-Performance Admin Dashboard APIs (`/api/v1/admin/dashboard`)
- Built aggregated metric endpoints using SQLAlchemy `func.count()` queries to return system stats (total users, active appointments, pending reviews, audit logs) in a single database roundtrip.

### 3. 🚨 Unified Exception Handling Middleware
- Intercepts all `HTTPException`, `RequestValidationError`, `SQLAlchemyError`, and 500 runtime errors, formatting them into a standard, predictable JSON schema:
```json
{
  "success": false,
  "message": "Invalid request parameters.",
  "errors": ["email: Field required"]
}
```

### 4. 🧪 Postman Collection & Automated Tests
- Full `Postman_Collection.json` provided at `Backend/Postman_Collection.json` for manual and automated API route testing.
- Automated `pytest` suite in `Backend/app/tests/` covering root endpoints, database health, demo seeding, and dashboard analytics.

---

## 🚀 Quickstart Guide

### Running the Backend Locally
```bash
cd Backend

# Install dependencies
pip install -r requirements.txt

# Run FastAPI development server
uvicorn app.main:app --reload
```

- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running Automated Tests
```bash
cd Backend
pytest
```
