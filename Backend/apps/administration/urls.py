from django.urls import path
from apps.administration.views import (
    AdminDashboardView,
    SystemHealthView,
    AuditLogListView,
    AppointmentListCreateView,
    AppointmentDetailView,
    SeedDemoDataView,
)

urlpatterns = [
    path("dashboard/", AdminDashboardView.as_view(), name="admin-dashboard"),
    path("health/", SystemHealthView.as_view(), name="system-health"),
    path("audit-logs/", AuditLogListView.as_view(), name="audit-log-list"),
    path("appointments/", AppointmentListCreateView.as_view(), name="appointment-list-create"),
    path("appointments/<uuid:pk>/", AppointmentDetailView.as_view(), name="appointment-detail"),
    path("seed-demo-data/", SeedDemoDataView.as_view(), name="seed-demo-data"),
]
