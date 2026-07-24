# ⚙️ Healthcare Clinic Backend API

FastAPI enterprise backend for the Healthcare Clinic project.

## Architecture Highlights (Udbhav Module)
- **Framework**: FastAPI + Pydantic v2
- **ORM**: SQLAlchemy 2.0 with custom `BaseModel` (UUIDs + `is_deleted` soft deletion)
- **Exception Middleware**: Custom global handlers for unified JSON error responses.
- **Admin Dashboard Router**: `/api/v1/admin/dashboard` & `/api/v1/admin/health`
- **Testing**: `pytest` test suite with `TestClient`

## Endpoints
- `GET /`: Health check & API metadata
- `GET /api/v1/admin/health`: Database connection status
- `GET /api/v1/admin/dashboard`: Aggregated admin analytics and audit logs
- `POST /api/v1/admin/seed-demo-data`: Seed test data for dashboard verification
