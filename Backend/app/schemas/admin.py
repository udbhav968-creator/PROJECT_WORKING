from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class SystemStatsSchema(BaseModel):
    total_users: int
    active_users: int
    total_appointments: int
    scheduled_appointments: int
    completed_appointments: int
    cancelled_appointments: int
    total_audit_logs: int


class AuditLogResponseSchema(BaseModel):
    id: str
    admin_email: str
    action: str
    resource: str
    ip_address: Optional[str] = None
    details: Optional[str] = None
    created_at: str

    model_config = ConfigDict(from_attributes=True)


class AdminDashboardSummaryResponse(BaseModel):
    success: bool = True
    stats: SystemStatsSchema
    recent_logs: List[AuditLogResponseSchema]


class HealthCheckResponse(BaseModel):
    status: str = "healthy"
    version: str
    database_connected: bool
