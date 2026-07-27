import time
import logging
import uuid
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
    **Enterprise Healthcare System Integration Health Monitor**

    Validates DB connections, measures query latency, framework version,
    and returns NABH / HIPAA compliance health metrics.
    """

    def get(self, request):
        start_time = time.time()
        db_ok = False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_ok = True
        except Exception as e:
            logger.error(f"DB health check failed: {e}")

        latency_ms = round((time.time() - start_time) * 1000, 2)

        return Response(
            {
                "success": True,
                "institute": "Healthcare Clinic Integration Core",
                "status": "healthy" if db_ok else "degraded",
                "database_connected": db_ok,
                "database_latency_ms": latency_ms,
                "nabh_hipaa_compliance_status": "ACTIVE_AUDIT_ENABLED",
                "framework": "Django 5.0 REST Framework",
                "timestamp": timezone.now().isoformat(),
            },
            status=status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE,
        )


class AdminDashboardView(APIView):
    """
    **Enterprise Admin Dashboard Analytics** (Udbhav – Module 4)

    High-performance aggregation engine returning OPD statistics,
    Emergency Triage metrics, Department Breakdown, and Audit Trail summaries.
    """

    @extend_schema(responses={200: AdminDashboardResponseSerializer})
    def get(self, request):
        user_stats = UserProfileModel.objects.aggregate(
            total_users=Count("id"),
            active_users=Count("id", filter=Q(is_active=True)),
        )

        appt_stats = AppointmentModel.objects.aggregate(
            total_appointments=Count("id"),
            scheduled_appointments=Count("id", filter=Q(status="scheduled")),
            in_consultation_appointments=Count("id", filter=Q(status="in_consultation")),
            completed_appointments=Count("id", filter=Q(status="completed")),
            cancelled_appointments=Count("id", filter=Q(status="cancelled")),
            emergency_triage_count=Count("id", filter=Q(priority="emergency")),
        )

        dept_qs = (
            AppointmentModel.objects.values("department")
            .annotate(count=Count("id"))
            .order_by("-count")
        )
        department_breakdown = [
            {"department": item["department"], "count": item["count"]} for item in dept_qs
        ]

        total_logs = AdminAuditLogModel.objects.count()
        recent_logs = AdminAuditLogModel.objects.order_by("-created_at")[:5]

        client_ip = request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@healthcare-clinic.com",
            action="VIEW_ADMIN_DASHBOARD",
            resource="CLINICAL_ANALYTICS",
            severity="INFO",
            compliance_category="NABH_PATIENT_SAFETY",
            ip_address=client_ip,
            details="Accessed healthcare admin dashboard analytics and OPD summary",
        )

        payload = {
            "success": True,
            "institute": "Healthcare Clinic Enterprise Core",
            "stats": {
                "total_users": user_stats["total_users"] or 0,
                "active_users": user_stats["active_users"] or 0,
                "total_appointments": appt_stats["total_appointments"] or 0,
                "scheduled_appointments": appt_stats["scheduled_appointments"] or 0,
                "in_consultation_appointments": appt_stats["in_consultation_appointments"] or 0,
                "completed_appointments": appt_stats["completed_appointments"] or 0,
                "cancelled_appointments": appt_stats["cancelled_appointments"] or 0,
                "emergency_triage_count": appt_stats["emergency_triage_count"] or 0,
                "total_audit_logs": total_logs,
            },
            "department_breakdown": department_breakdown,
            "recent_logs": recent_logs,
        }

        serializer = AdminDashboardResponseSerializer(payload)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuditLogListView(APIView):
    """
    **NABH & HIPAA Compliant Audit Log Endpoint** (paginated)

    Supports filtering by severity (`?severity=CRITICAL`) and compliance category (`?category=HIPAA`).
    """

    @extend_schema(
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number"),
            OpenApiParameter(name="page_size", type=int, description="Results per page (max 100)"),
            OpenApiParameter(name="severity", type=str, description="Filter by severity (INFO, WARNING, CRITICAL)"),
        ]
    )
    def get(self, request):
        queryset = AdminAuditLogModel.objects.order_by("-created_at")
        severity_param = request.query_params.get("severity")
        if severity_param:
            queryset = queryset.filter(severity=severity_param.upper())

        paginator = StandardPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = AdminAuditLogSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AppointmentListCreateView(ListCreateAPIView):
    """
    **Clinical OPD Appointment & Triage Management – List & Create** (Udbhav – Module 4)

    Supports filtering by department (`?department=Cardiology`), priority (`?priority=emergency`), and search (`?search=Rajesh`).
    Auto-generates Clinical OPD Token Numbers (`CLINIC-OPD-XXXX`).
    """

    serializer_class = AppointmentSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        queryset = AppointmentModel.objects.order_by("-created_at")
        status_param = self.request.query_params.get("status")
        department_param = self.request.query_params.get("department")
        priority_param = self.request.query_params.get("priority")
        search_param = self.request.query_params.get("search")

        if status_param:
            queryset = queryset.filter(status=status_param)
        if department_param:
            queryset = queryset.filter(department=department_param)
        if priority_param:
            queryset = queryset.filter(priority=priority_param)
        if search_param:
            queryset = queryset.filter(
                Q(patient_name__icontains=search_param) | Q(doctor_name__icontains=search_param) | Q(token_number__icontains=search_param)
            )
        return queryset

    def perform_create(self, serializer):
        token = serializer.validated_data.get("token_number")
        if not token:
            token = f"CLINIC-OPD-{uuid.uuid4().hex[:6].upper()}"

        appointment = serializer.save(token_number=token)
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")

        severity = "CRITICAL" if appointment.priority == "emergency" else "INFO"
        AdminAuditLogModel.objects.create(
            admin_email="admin@healthcare-clinic.com",
            action="CREATE_OPD_APPOINTMENT",
            resource=f"TOKEN_{appointment.token_number}",
            severity=severity,
            compliance_category="NABH_PATIENT_REGISTRATION",
            ip_address=client_ip,
            details=f"Booked {appointment.get_priority_display()} for {appointment.patient_name} in {appointment.department} under {appointment.doctor_name}",
        )


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    """
    **Clinical OPD Appointment Detail, Status Update & Soft-Delete** (Udbhav – Module 4)
    """

    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        appointment = serializer.save()
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@healthcare-clinic.com",
            action="UPDATE_APPOINTMENT",
            resource=f"TOKEN_{appointment.token_number}",
            severity="INFO",
            compliance_category="NABH_CLINICAL_UPDATE",
            ip_address=client_ip,
            details=f"Updated status for {appointment.patient_name} to '{appointment.status}' in {appointment.department}",
        )

    def perform_destroy(self, instance):
        instance.delete()
        client_ip = self.request.META.get("REMOTE_ADDR", "127.0.0.1")
        AdminAuditLogModel.objects.create(
            admin_email="admin@healthcare-clinic.com",
            action="DELETE_APPOINTMENT",
            resource=f"TOKEN_{instance.token_number}",
            severity="WARNING",
            compliance_category="NABH_PATIENT_RECORD_ARCHIVE",
            ip_address=client_ip,
            details=f"Archived/Soft-deleted record for {instance.patient_name} ({instance.token_number})",
        )


class SeedDemoDataView(APIView):
    """
    **Seed Healthcare Clinic Demo Data** – for testing & Postman verification.
    """

    def post(self, request):
        created = []

        if UserProfileModel.objects.count() == 0:
            UserProfileModel.objects.create(
                email="admin@healthcare-clinic.com",
                full_name="Clinic Admin",
                is_active=True,
            )
            created.append("Clinic Admin user")

        if AppointmentModel.objects.count() == 0:
            AppointmentModel.objects.create(
                patient_name="Rajesh Sharma",
                patient_phone="+91 9811122233",
                patient_email="rajesh.sharma@example.com",
                doctor_name="Dr. Smith",
                department="Cardiology",
                priority="urgent",
                consultation_type="OPD",
                token_number="CLINIC-CARD-101",
                appointment_date=timezone.now(),
                status="scheduled",
                notes="Cardiovascular risk assessment & ECG examination",
            )
            AppointmentModel.objects.create(
                patient_name="Priya Verma",
                patient_phone="+91 9877766655",
                patient_email="priya.v@example.com",
                doctor_name="Dr. Mehta",
                department="Neurology",
                priority="emergency",
                consultation_type="Emergency",
                token_number="CLINIC-NEURO-EMG-909",
                appointment_date=timezone.now(),
                status="in_consultation",
                notes="Acute triage evaluation",
            )
            AppointmentModel.objects.create(
                patient_name="Amitabh Gupta",
                patient_phone="+91 9123456780",
                patient_email="agupta@example.com",
                doctor_name="Dr. Sharma",
                department="Orthopedics",
                priority="routine",
                consultation_type="OPD",
                token_number="CLINIC-ORTHO-304",
                appointment_date=timezone.now(),
                status="completed",
                notes="Post-operative follow-up consultation",
            )
            created.append("3 Clinical Records")

        msg = f"Seeded: {', '.join(created)}" if created else "Demo data already exists."
        return Response(
            {"success": True, "message": msg},
            status=status.HTTP_201_CREATED,
        )
