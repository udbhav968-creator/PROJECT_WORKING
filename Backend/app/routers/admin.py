from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import get_db
from app.services.admin_service import AdminService
from app.schemas.admin import AdminDashboardSummaryResponse, HealthCheckResponse
from app.config.settings import settings
from app.models.user import UserModel
from app.models.appointment import AppointmentModel

router = APIRouter(prefix="/admin", tags=["Administration & Integration Module"])


@router.get("/dashboard", response_model=AdminDashboardSummaryResponse)
def get_admin_dashboard_summary(request: Request, db: Session = Depends(get_db)):
    """
    **Admin Dashboard Summary Endpoint (Udbhav Module)**
    
    Returns aggregated metrics (user counts, appointment statistics) 
    and recent system audit logs in a single optimized response.
    """
    stats = AdminService.get_dashboard_stats(db)
    recent_logs = AdminService.get_recent_audit_logs(db, limit=5)
    
    # Log this admin view action
    client_ip = request.client.host if request.client else "127.0.0.1"
    AdminService.create_audit_log(
        db,
        admin_email="admin@py-digital.com",
        action="VIEW_DASHBOARD",
        resource="ADMIN_ANALYTICS",
        ip_address=client_ip,
        details="Accessed admin dashboard summary stats"
    )

    return AdminDashboardSummaryResponse(
        success=True,
        stats=stats,
        recent_logs=recent_logs
    )


@router.get("/health", response_model=HealthCheckResponse)
def health_check(db: Session = Depends(get_db)):
    """
    **System Integration Health Check Endpoint**
    
    Verifies backend operational status and database connection health.
    """
    db_connected = False
    try:
        db.execute(text("SELECT 1"))
        db_connected = True
    except Exception:
        db_connected = False

    return HealthCheckResponse(
        status="healthy" if db_connected else "degraded",
        version=settings.VERSION,
        database_connected=db_connected
    )


@router.post("/seed-demo-data")
def seed_demo_data(db: Session = Depends(get_db)):
    """
    **Testing & Verification Helper Utility**
    
    Seeds initial roles, users, and appointments for local testing and dashboard evaluation.
    """
    # Seed Demo Users if empty
    if db.query(UserModel).count() == 0:
        demo_user = UserModel(
            email="admin@py-digital.com",
            full_name="Udbhav Admin",
            hashed_password="pbkdf2_sha256$hashedsecret",
            is_active=True
        )
        db.add(demo_user)

    # Seed Demo Appointments if empty
    if db.query(AppointmentModel).count() == 0:
        app1 = AppointmentModel(
            patient_name="John Doe",
            patient_phone="+91 9876543210",
            patient_email="john@example.com",
            doctor_name="Dr. Smith",
            appointment_date=datetime.now(timezone.utc),
            status="scheduled",
            notes="Regular cardiology checkup"
        )
        app2 = AppointmentModel(
            patient_name="Jane Roy",
            patient_phone="+91 9123456789",
            patient_email="jane@example.com",
            doctor_name="Dr. Mehta",
            appointment_date=datetime.now(timezone.utc),
            status="completed",
            notes="Dermatology consultation"
        )
        db.add_all([app1, app2])

    db.commit()
    return {"success": True, "message": "Demo data successfully seeded for testing!"}
