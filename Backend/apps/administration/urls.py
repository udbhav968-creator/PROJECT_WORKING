from django.urls import path
from apps.administration.views import (
    SystemHealthView,
    AdminDashboardView,
    AuditLogListView,
    AppointmentListCreateView,
    AppointmentDetailView,
    AppointmentPDFSlipView,
    SeedDemoDataView,
)

urlpatterns = [
    # System Health & Integration APIs (Udbhav - Module 4)
    path('health/', SystemHealthView.as_view(), name='system-health'),
    path('seed-demo-data/', SeedDemoDataView.as_view(), name='seed-demo-data'),

    # Admin Analytics & Compliance Auditing APIs
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('audit-logs/', AuditLogListView.as_view(), name='audit-log-list'),

    # Appointment Management & OPD Token APIs
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/<uuid:pk>/slip/', AppointmentPDFSlipView.as_view(), name='appointment-pdf-slip'),
]
