from django.contrib import admin
from apps.administration.models import AppointmentModel, AdminAuditLogModel

# Customizing Django Admin Site Header & Titles for Enterprise Medical Hospital Portal
admin.site.site_header = "🏥 Healthcare Hospital & Clinic Administration Portal"
admin.site.site_title = "Hospital Portal Admin"
admin.site.index_title = "Clinical Operations & System Integration Control Center"


@admin.register(AppointmentModel)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'token_number',
        'patient_name',
        'department',
        'doctor_name',
        'priority',
        'status',
        'appointment_date',
        'is_deleted',
    )
    list_filter = (
        'status',
        'priority',
        'department',
        'consultation_type',
        'is_deleted',
        'appointment_date',
    )
    search_fields = ('token_number', 'patient_name', 'doctor_name', 'patient_phone', 'patient_email')
    ordering = ('-created_at',)
    date_hierarchy = 'appointment_date'

    fieldsets = (
        ('OPD & Triage Identification', {
            'fields': ('token_number', 'department', 'priority', 'consultation_type')
        }),
        ('Patient Details', {
            'fields': ('patient_name', 'patient_phone', 'patient_email')
        }),
        ('Clinical Assignment', {
            'fields': ('doctor_name', 'appointment_date', 'status', 'notes')
        }),
        ('System Archival', {
            'fields': ('is_deleted',),
            'classes': ('collapse',),
        }),
    )

    actions = ['mark_completed', 'mark_in_consultation', 'restore_records']

    @admin.action(description="Mark selected appointments as Completed")
    def mark_completed(self, request, queryset):
        queryset.update(status='completed')

    @admin.action(description="Mark selected appointments as In Consultation")
    def mark_in_consultation(self, request, queryset):
        queryset.update(status='in_consultation')

    @admin.action(description="Restore selected soft-deleted records")
    def restore_records(self, request, queryset):
        queryset.update(is_deleted=False)


@admin.register(AdminAuditLogModel)
class AdminAuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'severity',
        'admin_email',
        'action',
        'resource',
        'compliance_category',
        'ip_address',
    )
    list_filter = ('severity', 'compliance_category', 'action', 'created_at')
    search_fields = ('admin_email', 'action', 'resource', 'details', 'ip_address')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'admin_email', 'action', 'resource', 'severity', 'compliance_category', 'ip_address', 'details', 'created_at', 'updated_at', 'is_deleted')

    def has_add_permission(self, request):
        return False  # Audit logs are immutable system records

    def has_delete_permission(self, request, obj=None):
        return False  # Audit logs cannot be deleted
