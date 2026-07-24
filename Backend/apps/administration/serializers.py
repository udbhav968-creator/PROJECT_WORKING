from rest_framework import serializers
from apps.administration.models import AdminAuditLogModel, AppointmentModel


class AdminAuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAuditLogModel
        fields = ['id', 'admin_email', 'action', 'resource', 'ip_address', 'details', 'created_at']


class SystemStatsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    total_appointments = serializers.IntegerField()
    scheduled_appointments = serializers.IntegerField()
    completed_appointments = serializers.IntegerField()
    cancelled_appointments = serializers.IntegerField()
    total_audit_logs = serializers.IntegerField()


class AdminDashboardResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField(default=True)
    stats = SystemStatsSerializer()
    recent_logs = AdminAuditLogSerializer(many=True)
