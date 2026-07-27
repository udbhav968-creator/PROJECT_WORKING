from rest_framework import serializers
from apps.administration.models import AdminAuditLogModel, AppointmentModel


class AdminAuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAuditLogModel
        fields = ["id", "admin_email", "action", "resource", "severity", "compliance_category", "ip_address", "details", "created_at"]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = [
            "id", "patient_name", "patient_phone", "patient_email",
            "doctor_name", "department", "priority", "consultation_type",
            "token_number", "appointment_date", "status", "notes",
            "created_at", "updated_at",
        ]


class DepartmentStatsSerializer(serializers.Serializer):
    department = serializers.CharField()
    count = serializers.IntegerField()


class SystemStatsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    total_appointments = serializers.IntegerField()
    scheduled_appointments = serializers.IntegerField()
    in_consultation_appointments = serializers.IntegerField()
    completed_appointments = serializers.IntegerField()
    cancelled_appointments = serializers.IntegerField()
    emergency_triage_count = serializers.IntegerField()
    total_audit_logs = serializers.IntegerField()


class AdminDashboardResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField(default=True)
    institute = serializers.CharField(default="Healthcare Clinic Enterprise Core")
    stats = SystemStatsSerializer()
    department_breakdown = DepartmentStatsSerializer(many=True)
    recent_logs = AdminAuditLogSerializer(many=True)
