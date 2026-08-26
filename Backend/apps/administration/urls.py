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
    GeminiAiChatbotView,
    SystemMetricsView,
    HospitalStatsView,
    PatientFeedbackView,
    IcuOccupancyTelemetryView,
    PharmacyBloodBankTelemetryView,
    UnifiedAiModelSuiteView,
    MlOpsPipelineView,
    DeepTrainModelsView,
    AmbulanceDispatchView,
    KaggleGitHubDatasetView,
    TrainKaggleModelsView,
    NextGen50FeaturesView,
    GenomicSequencingView,
    RadiologyXrayAiView,
    FineTuneAiModelsView,
)

urlpatterns = [
    # System Health & Integration APIs (Udbhav - Module 4)
    path('health/', SystemHealthView.as_view(), name='system-health'),
    path('seed-demo-data/', SeedDemoDataView.as_view(), name='seed-demo-data'),
    path('system-metrics/', SystemMetricsView.as_view(), name='system-metrics'),
    path('hospital-stats/', HospitalStatsView.as_view(), name='hospital-stats'),
    path('patient-feedback/', PatientFeedbackView.as_view(), name='patient-feedback'),
    path('icu-occupancy/', IcuOccupancyTelemetryView.as_view(), name='icu-occupancy'),
    path('pharmacy-blood-bank/', PharmacyBloodBankTelemetryView.as_view(), name='pharmacy-blood-bank'),
    path('ai-model-suite/', UnifiedAiModelSuiteView.as_view(), name='ai-model-suite'),
    path('mlops-pipeline/', MlOpsPipelineView.as_view(), name='mlops-pipeline'),
    path('deep-train-models/', DeepTrainModelsView.as_view(), name='deep-train-models'),
    path('ambulance-dispatch/', AmbulanceDispatchView.as_view(), name='ambulance-dispatch'),
    path('kaggle-github-datasets/', KaggleGitHubDatasetView.as_view(), name='kaggle-github-datasets'),
    path('train-kaggle-models/', TrainKaggleModelsView.as_view(), name='train-kaggle-models'),
    path('next-gen-50-features/', NextGen50FeaturesView.as_view(), name='next-gen-50-features'),
    path('genomic-sequencing/', GenomicSequencingView.as_view(), name='genomic-sequencing'),
    path('radiology-xray-ai/', RadiologyXrayAiView.as_view(), name='radiology-xray-ai'),
    path('fine-tune-ai-models/', FineTuneAiModelsView.as_view(), name='fine-tune-ai-models'),

    # Admin Analytics & Compliance Auditing APIs
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('audit-logs/', AuditLogListView.as_view(), name='audit-log-list'),

    # Appointment Management & OPD Token APIs
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/track/<str:token_number>/', TokenTrackerView.as_view(), name='appointment-track'),
    path('appointments/<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/<uuid:pk>/slip/', AppointmentPDFSlipView.as_view(), name='appointment-pdf-slip'),

    # Next-Gen Innovations (Razorpay, Twilio WhatsApp, Gemini AI Summarizer, Gemini Chatbot)
    path('create-razorpay-order/', RazorpayOrderCreateView.as_view(), name='create-razorpay-order'),
    path('send-whatsapp-notification/', WhatsAppNotificationSendView.as_view(), name='send-whatsapp-notification'),
    path('summarize-prescription/', PrescriptionSummarizerAiView.as_view(), name='summarize-prescription'),
    path('chat-gemini-ai/', GeminiAiChatbotView.as_view(), name='chat-gemini-ai'),
]
