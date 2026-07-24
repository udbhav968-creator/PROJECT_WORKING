# 🏥 Healthcare Clinic Website Backend (Django + DRF)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-092E20.svg)
![DRF](https://img.shields.io/badge/DRF-3.15+-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-00758F.svg)
![JWT](https://img.shields.io/badge/JWT-SimpleJWT-black.svg)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2ea44f.svg)

Welcome to the enterprise backend repository for the **Healthcare Clinic Website**. This project was developed as part of the internship assignment at **PY Digital Services Pvt. Ltd.**

---

## 🛠️ Required Tech Stack
- **Language**: Python 3.10+
- **Framework**: Django 5.0+ & Django REST Framework (DRF)
- **Database**: MySQL (supported via `PyMySQL` driver with SQLite zero-setup dev fallback)
- **Authentication**: JWT Token Authentication (`rest_framework_simplejwt`)
- **API Documentation**: OpenAPI / Swagger UI & ReDoc (`drf-spectacular`)
- **Testing & Debugging**: DRF `APITestCase` suite & `Postman_Collection.json`
- **VCS & CI/CD**: Git, GitHub, and GitHub Actions CI Pipeline

---

## 👨‍💻 Module 4: Administration & System Integration (Udbhav's Work)

Udbhav engineered the core foundation and integration module for the backend:

### 1. 🛡️ Database Design & Optimization (`TimeStampedModel`)
- **UUID Primary Keys**: Uses `uuid.uuid4()` for primary keys across all models to prevent sequential ID enumeration attacks.
- **Soft Deletion (`is_deleted`)**: Implements an `is_deleted` boolean flag on base models. When records are "deleted", they are preserved for medical compliance and historical auditing while being automatically excluded from standard ORM querysets.
- **MySQL Driver Support**: Configured `PyMySQL` so MySQL databases can be used seamlessly across environments.

### 2. 📊 High-Performance Admin Dashboard APIs (`/api/admin/dashboard/`)
- Uses Django ORM aggregations (`Count`, `Q` conditional filters) to calculate system metrics (total users, active appointments, completed visits, audit counts) in a single database query.

### 3. 🚨 Custom DRF Exception Handling
- Intercepts all DRF exceptions, database errors, and validation errors, returning a unified JSON format:
```json
{
  "success": false,
  "errors": ["field: This field is required."]
}
```

### 4. 📬 Postman Collection & Automated Tests
- Postman Collection file at `Backend/Postman_Collection.json`.
- Run automated unit tests using `python manage.py test`.

---

## 🚀 Quickstart Guide

```bash
cd Backend

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start Django Development Server
python manage.py runserver
```

- **Interactive Swagger Docs**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **ReDoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **JWT Token Endpoint**: [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)
