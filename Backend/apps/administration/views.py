import logging
from django.db import connection
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter

from apps.authentication.models import UserProfileModel
from apps.administration.models import AppointmentModel, AdminAuditLogModel
from apps.administration.serializers import (
    AdminDashboardResponseSerializer,
    AdminAuditLogSerializer,
    AppointmentSerializer,
)

logger = logging.getLogger("clinic_core")


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class SystemHealthView(APIView):
    """
    **System Integration Health Check**

    Returns database connection status and framework version.
    """

    def get(self, request):
        db_ok = False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_ok = True
        except Exception as e:
            logger.error(f"DB health check failed: {e}")

        return Response(
            {
                "success": True,
                "status": "healthy" if db_ok else "degraded",
                "database_connected": db_ok,
                "framework": "Django REST Framework",
                "timestamp": timezone.now().isoformat(),
            },
            status=status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE,
        )


class AdminDashboardView(APIView):
    """
    **Admin Dashboard Analytics** (Udbhav – Module 4)

    Uses high-performance Django ORM aggregations (Count + Q filters)
    to return system-wide stats and the 5 most recent audit logs.
    """

    @extend_schema(responses={200: AdminDashboardResponseSerializer})
    def get(self, request):
        # Single aggregation query per table – no N+1 issues
        user_stats = UserProfileModel.objects.aggregate(
            total_users=Count("id"),
            active_users=Count("id", filter=Q(is_active=True)),
        )

        appt_stats = AppointmentModel.objects.aggregate(
            total_appointments=Count("id"),
            scheduled_appointments=Count("id", filter=Q(status="scheduled")),
            completed_appointments=Count("id", filter=Q(status="completed")),
            cancelled_appointments=Count("id", filter=Q(status="cancelled")),
        )

        total_logs = AdminAuditLogModel.objects.count()
        recent_logs = AdminAuditLogModel.objects.order_by("-created_at")[:5]

        # Record that the dashboard was viewed
        client_ip = request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@py-digital.com",
            action="VIEW_DASHBOARD",
            resource="ADMIN_ANALYTICS",
            ip_address=client_ip,
            details="Accessed admin dashboard analytics summary",
        )

        payload = {
            "success": True,
            "stats": {
                "total_users": user_stats["total_users"] or 0,
                "active_users": user_stats["active_users"] or 0,
                "total_appointments": appt_stats["total_appointments"] or 0,
                "scheduled_appointments": appt_stats["scheduled_appointments"] or 0,
                "completed_appointments": appt_stats["completed_appointments"] or 0,
                "cancelled_appointments": appt_stats["cancelled_appointments"] or 0,
                "total_audit_logs": total_logs,
            },
            "recent_logs": recent_logs,
        }

        serializer = AdminDashboardResponseSerializer(payload)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuditLogListView(APIView):
    """
    **Admin Audit Log List** (paginated)

    Returns all admin audit logs in descending chronological order.
    Supports `?page=1&page_size=20` query parameters.
    """

    @extend_schema(
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number"),
            OpenApiParameter(name="page_size", type=int, description="Results per page (max 100)"),
        ]
    )
    def get(self, request):
        logs = AdminAuditLogModel.objects.order_by("-created_at")
        paginator = StandardPagination()
        page = paginator.paginate_queryset(logs, request)
        serializer = AdminAuditLogSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AppointmentListCreateView(ListCreateAPIView):
    """
    **Appointment Management – List & Create** (Udbhav – Module 4)

    Supports filtering by status (`?status=scheduled`) and searching by patient/doctor name (`?search=Smith`).
    Automatically logs `CREATE_APPOINTMENT` audit logs on creation.
    """

    serializer_class = AppointmentSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        queryset = AppointmentModel.objects.order_by("-created_at")
        status_param = self.request.query_params.get("status")
        search_param = self.request.query_params.get("search")

        if status_param:
            queryset = queryset.filter(status=status_param)
        if search_param:
            queryset = queryset.filter(
                Q(patient_name__icontains=search_param) | Q(doctor_name__icontains=search_param)
            )
        return queryset

    def perform_create(self, serializer):
        appointment = serializer.save()
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@py-digital.com",
            action="CREATE_APPOINTMENT",
            resource=f"APPOINTMENT_{appointment.id}",
            ip_address=client_ip,
            details=f"Created appointment for {appointment.patient_name} with {appointment.doctor_name}",
        )


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    """
    **Appointment Management – Detail, Update & Soft-Delete** (Udbhav – Module 4)

    Allows retrieve, update, and soft-delete of individual appointments.
    Automatically logs audit trail on update and delete.
    """

    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        appointment = serializer.save()
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@py-digital.com",
            action="UPDATE_APPOINTMENT",
            resource=f"APPOINTMENT_{appointment.id}",
            ip_address=client_ip,
            details=f"Updated appointment for {appointment.patient_name} (Status: {appointment.status})",
        )

    def perform_destroy(self, instance):
        # Soft-delete execution using TimeStampedModel soft delete
        instance.delete()
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@py-digital.com",
            action="DELETE_APPOINTMENT",
            resource=f"APPOINTMENT_{instance.id}",
            ip_address=client_ip,
            details=f"Soft-deleted appointment for {instance.patient_name}",
        )


class SeedDemoDataView(APIView):
    """
    **Seed Demo Data** – for local testing & Postman verification only.
    """

    def post(self, request):
        created = []

        if UserProfileModel.objects.count() == 0:
            UserProfileModel.objects.create(
                email="admin@py-digital.com",
                full_name="Udbhav Admin",
                is_active=True,
            )
            created.append("admin user")

        if AppointmentModel.objects.count() == 0:
            AppointmentModel.objects.create(
                patient_name="John Doe",
                patient_phone="+91 9876543210",
                patient_email="john@example.com",
                doctor_name="Dr. Smith",
                appointment_date=timezone.now(),
                status="scheduled",
                notes="Cardiology consultation",
            )
            AppointmentModel.objects.create(
                patient_name="Jane Roy",
                patient_phone="+91 9123456789",
                patient_email="jane@example.com",
                doctor_name="Dr. Mehta",
                appointment_date=timezone.now(),
                status="completed",
                notes="Dermatology consultation",
            )
            created.append("2 appointments")

        msg = f"Seeded: {', '.join(created)}" if created else "Demo data already exists."
        return Response(
            {"success": True, "message": msg},
            status=status.HTTP_201_CREATED,
        )
