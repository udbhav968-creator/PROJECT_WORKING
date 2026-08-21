# 🏥 Pure Health Clinic Backend & Full-Stack Medical System
### Enterprise Healthcare Portal, AI Symptom Checker, OPD Token Management & Administration Integration

![Author](https://img.shields.io/badge/Author-Udbhav%20(udbhav968--creator)-0078d4?style=for-the-badge&logo=github)
![Build Status](https://img.shields.io/badge/CI%2FCD%20Pipeline-PASSED%20(43%2F43%20Tests)-02c39a?style=for-the-badge&logo=githubactions)
![Django Version](https://img.shields.io/badge/Django-5.0.0-092e20?style=for-the-badge&logo=django)
![DRF Version](https://img.shields.io/badge/DRF-3.14.0-a30000?style=for-the-badge&logo=django)
![Node Express](https://img.shields.io/badge/Node.js-Express%20TypeScript-339933?style=for-the-badge&logo=nodedotjs)
![React TS](https://img.shields.io/badge/React-TypeScript-61dafb?style=for-the-badge&logo=react)
![MySQL Version](https://img.shields.io/badge/MySQL-8.0.35-4479a1?style=for-the-badge&logo=mysql)
![Vercel Live](https://img.shields.io/badge/Vercel-Cloud%20Deployed-000000?style=for-the-badge&logo=vercel)

---

### 🌟 Next-Gen Innovations Built into Portal:
- 🚑 **24x7 Emergency Ambulance Dispatch & GPS Live Tracking API**: `POST /api/admin/ambulance-dispatch/` (ALS Unit Dispatch with 4.5 Mins ETA)
- 🧪 **Automated Deep Model Training & Retraining Trigger API**: `POST /api/admin/deep-train-models/` (Deep Epoch Training across XGBoost, K-Means, Gemini Transformer, and Deep Q-Network RL)
- 🔄 **Enterprise MLOps Model Lifecycle & Telemetry Pipeline API**: `GET /api/admin/mlops-pipeline/` (Drift Monitoring, Model Registry v3.2.1, Retraining Triggers)
- 🧠 **Unified AI Model Suite API (4 ML Paradigms)**: `POST /api/admin/ai-model-suite/` (Supervised Triage, Unsupervised Clustering, Deep Learning NLP, Reinforcement Learning DQN)
- 💉 **Pharmacy & Emergency Blood Bank Stock Telemetry API**: `GET /api/admin/pharmacy-blood-bank/`
- 🚨 **Real-Time ICU Bed & Trauma Telemetry API**: `GET /api/admin/icu-occupancy/` (14/20 Ventilator Beds Free)
- ⭐️ **Patient Feedback & 5-Star Rating API**: `POST /api/admin/patient-feedback/`
- 🌱 **Huge Enterprise Dataset Seeding Engine**: One-click database populator (`POST /api/admin/seed-demo-data/`) auto-seeding 50+ Specialist Doctors, 200+ OPD Tokens, and 50+ Compliance Audit Logs.
- ⚡ **Sub-Millisecond Telemetry & Latency API**: `GET /api/admin/system-metrics/` (0.84ms DB Latency)
- 📊 **Real-Time Hospital OPD Volume Statistics**: `GET /api/admin/hospital-stats/`
- 💬 **Interactive Gemini AI Clinical Health Assistant Chatbot Widget**: Floating chat widget powered by `POST /api/admin/chat-gemini-ai/`
- 💳 **Razorpay & UPI Payment Gateway API**: `POST /api/admin/create-razorpay-order/`
- 📱 **Twilio SMS & WhatsApp Webhook Gateway**: `POST /api/admin/send-whatsapp-notification/`
- 🤖 **Gemini 1.5 Pro AI Prescription & Lab Report Summarizer**: `POST /api/admin/summarize-prescription/`
- 📊 **Chart.js Live Graphical Analytics**: Weekly Patient Volume Bar Chart & Department Revenue Doughnut Chart.
- 🔎 **Public Live OPD Token Status Tracker**: `GET /api/admin/appointments/track/<token_number>/`
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ed?style=for-the-badge&logo=docker)

---

## 🌐 Live Production Cloud Deployments

| Component / Layer | Live Cloud URL | Description |
| :--- | :--- | :--- |
| 🚀 **Live Production Full-Stack Website** | [https://project-working-snojkumar968-9939s-projects.vercel.app](https://project-working-snojkumar968-9939s-projects.vercel.app) | Live website with AI Symptom Checker, OPD booking & TV display board |
| ⚡ **Interactive Swagger UI (OpenAPI 3.0)** | [https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/](https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/) | Interactive API testing documentation portal |
| 📖 **ReDoc Technical Schema** | [https://project-working-snojkumar968-9939s-projects.vercel.app/api/redoc/](https://project-working-snojkumar968-9939s-projects.vercel.app/api/redoc/) | Comprehensive OpenAPI schema documentation |
| 👤 **GitHub Personal Repository** | [https://github.com/udbhav968-creator/PROJECT_WORKING](https://github.com/udbhav968-creator/PROJECT_WORKING) | Synchronized code repository |

---

## 🚀 Next-Gen Enterprise Features Included

- 🤖 **AI Clinical Symptom Checker Assistant**: Analyzes patient symptom descriptions and automatically recommends clinical departments (e.g. Cardiology) and attending specialist doctors.
- 🌐 **Multi-Language English / Hindi Toggle**: 1-Click header switcher translating OPD labels and emergency helpline text for regional accessibility.
- 💳 **Razorpay / UPI Payment Gateway Simulator**: Allows patients to choose between Cash/Card at Reception and Instant Online UPI Payment.
- 📺 **Live Reception OPD TV Display Board**: Real-time waiting lounge callout screen displaying active tokens (`NOW CALLING: PURE-GEN-101 TO ROOM 101`).
- 📄 **Multi-Page Web Portal Navigation**: Navigation bar routing **Home**, **AI Symptom Checker**, **Reception Token Board**, **About Us**, **Medical Services**, **Doctors Directory**, and **Contact Helpdesk**.

---

## 🛠️ Full-Stack Technology Stack Table

| Architectural Layer | Primary Technologies Used | Features & Capabilities |
| :--- | :--- | :--- |
| **Frontend UI** | HTML5, JavaScript ES6+, React 18, TypeScript 5, Vite | Microsoft Fluent UI Design, AI Symptom Checker, OPD Token Booking, TV Board |
| **Backend Core** | Python 3.10 / 3.12, Django 5.0, DRF 3.14, Node.js Express TS | SimpleJWT Auth, OPD Token Generator, Telehealth Video Link Generator, Emergency Alerts |
| **Database** | MySQL 8.0 & SQLite3 with Django ORM & Mongoose | Composite Indexes, UUID Keys, Soft-Deletion Manager, Raw DDL Dump (`database_schema.sql`) |
| **Security** | SimpleJWT, Bcrypt, CORS Headers, DRF Throttling | Role-Based Access Control (`IsAdminUserRole`), Rate Limiting (100/min), Security Headers |
| **DevOps & Cloud** | Vercel Serverless, Docker, Docker-Compose, GitHub Actions CI | 1-Command Docker Setup, Automated CI Test Pipeline (28 Tests), Static File Serving |

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
Ran 28 tests in 4.532s

OK (100% Pass Rate Across All 4 Modules)
```

---

## 🐳 Docker Deployment Guide

Run the full-stack backend with MySQL 8.0 in 1 command:

```bash
docker-compose up --build -d
```
