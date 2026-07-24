from django.urls import path
from apps.administration.views import AdminDashboardView, SystemHealthView, SeedDemoDataView

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('health/', SystemHealthView.as_view(), name='system-health'),
    path('seed-demo-data/', SeedDemoDataView.as_view(), name='seed-demo-data'),
]
