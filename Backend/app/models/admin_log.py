from sqlalchemy import Column, String
from app.database.base import BaseModel


class AdminAuditLogModel(BaseModel):
    __tablename__ = "admin_audit_logs"

    admin_email = Column(String(255), nullable=False, index=True)
    action = Column(String(100), nullable=False)
    resource = Column(String(100), nullable=False)
    ip_address = Column(String(45), nullable=True)
    details = Column(String(500), nullable=True)
