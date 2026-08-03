from django.urls import path
from apps.administration.views import (
    SystemHealthView,
    AdminDashboardView,
    AuditLogListView,
    AppointmentListCreateView,
    AppointmentDetailView,
    AppointmentPDFSlipView,
    SeedDemoDataView,
    TokenTrackerView,
    RazorpayOrderCreateView,
    WhatsAppNotificationSendView,
    PrescriptionSummarizerAiView,
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
    path('appointments/track/<str:token_number>/', TokenTrackerView.as_view(), name='appointment-track'),
    path('appointments/<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/<uuid:pk>/slip/', AppointmentPDFSlipView.as_view(), name='appointment-pdf-slip'),

    # Next-Gen Innovations (Razorpay, Twilio WhatsApp, Gemini AI Summarizer)
    path('create-razorpay-order/', RazorpayOrderCreateView.as_view(), name='create-razorpay-order'),
    path('send-whatsapp-notification/', WhatsAppNotificationSendView.as_view(), name='send-whatsapp-notification'),
    path('summarize-prescription/', PrescriptionSummarizerAiView.as_view(), name='summarize-prescription'),
]
