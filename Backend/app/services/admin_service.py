from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.user import UserModel
from app.models.appointment import AppointmentModel
from app.models.admin_log import AdminAuditLogModel
from app.schemas.admin import SystemStatsSchema, AuditLogResponseSchema


class AdminService:
    @staticmethod
    def get_dashboard_stats(db: Session) -> SystemStatsSchema:
        """
        Executes high-performance ORM count aggregations to return system statistics.
        Ignores soft-deleted records.
        """
        total_users = db.query(func.count(UserModel.id)).filter(UserModel.is_deleted == False).scalar() or 0
        active_users = db.query(func.count(UserModel.id)).filter(UserModel.is_deleted == False, UserModel.is_active == True).scalar() or 0

        total_appointments = db.query(func.count(AppointmentModel.id)).filter(AppointmentModel.is_deleted == False).scalar() or 0
        scheduled_appointments = db.query(func.count(AppointmentModel.id)).filter(AppointmentModel.is_deleted == False, AppointmentModel.status == "scheduled").scalar() or 0
        completed_appointments = db.query(func.count(AppointmentModel.id)).filter(AppointmentModel.is_deleted == False, AppointmentModel.status == "completed").scalar() or 0
        cancelled_appointments = db.query(func.count(AppointmentModel.id)).filter(AppointmentModel.is_deleted == False, AppointmentModel.status == "cancelled").scalar() or 0

        total_audit_logs = db.query(func.count(AdminAuditLogModel.id)).filter(AdminAuditLogModel.is_deleted == False).scalar() or 0

        return SystemStatsSchema(
            total_users=total_users,
            active_users=active_users,
            total_appointments=total_appointments,
            scheduled_appointments=scheduled_appointments,
            completed_appointments=completed_appointments,
            cancelled_appointments=cancelled_appointments,
            total_audit_logs=total_audit_logs
        )

    @staticmethod
    def get_recent_audit_logs(db: Session, limit: int = 10):
        """Fetches recent admin audit logs."""
        logs = db.query(AdminAuditLogModel).filter(
            AdminAuditLogModel.is_deleted == False
        ).order_by(AdminAuditLogModel.created_at.desc()).limit(limit).all()

        return [
            AuditLogResponseSchema(
                id=log.id,
                admin_email=log.admin_email,
                action=log.action,
                resource=log.resource,
                ip_address=log.ip_address,
                details=log.details,
                created_at=log.created_at.isoformat()
            )
            for log in logs
        ]

    @staticmethod
    def create_audit_log(db: Session, admin_email: str, action: str, resource: str, ip_address: str = None, details: str = None):
        """Creates a new administrative audit log."""
        log = AdminAuditLogModel(
            admin_email=admin_email,
            action=action,
            resource=resource,
            ip_address=ip_address,
            details=details
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log
