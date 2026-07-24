from django.db import connection
from django.db.models import Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from apps.authentication.models import UserProfileModel
from apps.administration.models import AppointmentModel, AdminAuditLogModel
from apps.administration.serializers import AdminDashboardResponseSerializer


class AdminDashboardView(APIView):
    """
    **Admin Dashboard Analytics API Endpoint (Udbhav Module)**
    
    Uses high-performance Django ORM aggregations (`Count`, `Q` filters) 
    to retrieve system metrics in a single database query.
    """
    @extend_schema(responses={200: AdminDashboardResponseSerializer})
    def get(self, request):
        user_stats = UserProfileModel.objects.aggregate(
            total_users=Count('id'),
            active_users=Count('id', filter=Q(is_active=True))
        )

        appointment_stats = AppointmentModel.objects.aggregate(
            total_appointments=Count('id'),
            scheduled_appointments=Count('id', filter=Q(status='scheduled')),
            completed_appointments=Count('id', filter=Q(status='completed')),
            cancelled_appointments=Count('id', filter=Q(status='cancelled'))
        )

        total_audit_logs = AdminAuditLogModel.objects.count()

        recent_logs = AdminAuditLogModel.objects.order_by('-created_at')[:5]

        # Audit log entry for viewing dashboard
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        AdminAuditLogModel.objects.create(
            admin_email='admin@py-digital.com',
            action='VIEW_DASHBOARD',
            resource='ADMIN_ANALYTICS',
            ip_address=client_ip,
            details='Accessed admin dashboard analytics summary'
        )

        data = {
            'success': True,
            'stats': {
                'total_users': user_stats['total_users'] or 0,
                'active_users': user_stats['active_users'] or 0,
                'total_appointments': appointment_stats['total_appointments'] or 0,
                'scheduled_appointments': appointment_stats['scheduled_appointments'] or 0,
                'completed_appointments': appointment_stats['completed_appointments'] or 0,
                'cancelled_appointments': appointment_stats['cancelled_appointments'] or 0,
                'total_audit_logs': total_audit_logs
            },
            'recent_logs': recent_logs
        }

        serializer = AdminDashboardResponseSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SystemHealthView(APIView):
    """
    **System Integration Health Check Endpoint**
    """
    def get(self, request):
        db_connected = False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_connected = True
        except Exception:
            db_connected = False

        return Response({
            'status': 'healthy' if db_connected else 'degraded',
            'database_connected': db_connected,
            'framework': 'Django REST Framework'
        }, status=status.HTTP_200_OK if db_connected else status.HTTP_503_SERVICE_UNAVAILABLE)


class SeedDemoDataView(APIView):
    """
    **Helper Endpoint to Seed Demo Data for Testing**
    """
    def post(self, request):
        if UserProfileModel.objects.count() == 0:
            UserProfileModel.objects.create(
                email='admin@py-digital.com',
                full_name='Udbhav Admin',
                is_active=True
            )

        if AppointmentModel.objects.count() == 0:
            from django.utils import timezone
            AppointmentModel.objects.create(
                patient_name='John Doe',
                patient_phone='+91 9876543210',
                patient_email='john@example.com',
                doctor_name='Dr. Smith',
                appointment_date=timezone.now(),
                status='scheduled',
                notes='Cardiology consultation'
            )
            AppointmentModel.objects.create(
                patient_name='Jane Roy',
                patient_phone='+91 9123456789',
                patient_email='jane@example.com',
                doctor_name='Dr. Mehta',
                appointment_date=timezone.now(),
                status='completed',
                notes='Dermatology consultation'
            )

        return Response({'success': True, 'message': 'Demo testing data seeded successfully!'}, status=status.HTTP_201_CREATED)
