# ⚙️ Django REST Framework Backend

Enterprise Backend API for Healthcare Clinic built with Python, Django 5, DRF, MySQL, and JWT Authentication.

## App Structure
- `clinic_core/`: Master settings, URLs, WSGI, PyMySQL driver initialization, SimpleJWT settings.
- `apps/core/`: `TimeStampedModel` base model with UUID primary keys and `is_deleted` soft-deletion support; DRF custom exception handler.
- `apps/authentication/`: `RoleModel`, `UserProfileModel`, JWT token configuration.
- `apps/administration/`: `AdminDashboardView`, `SystemHealthView`, `SeedDemoDataView`, ORM aggregations, Postman collection, unit tests.
