from django.contrib import admin
from apps.administration.models import AppointmentModel, AdminAuditLogModel


@admin.register(AppointmentModel)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'doctor_name', 'appointment_date', 'status', 'is_deleted', 'created_at')
    search_fields = ('patient_name', 'doctor_name', 'patient_phone')
    list_filter = ('status', 'is_deleted', 'appointment_date')


@admin.register(AdminAuditLogModel)
class AdminAuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_email', 'action', 'resource', 'ip_address', 'created_at')
    search_fields = ('admin_email', 'action', 'resource')
    list_filter = ('action', 'created_at')
