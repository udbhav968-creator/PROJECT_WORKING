from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clinic_core.views import visual_frontend_home_view


@api_view(['GET'])
def root_api_directory_view(request):
    """
    JSON API Directory Endpoint
    """
    return Response({
        "success": True,
        "service": "Pure Health Clinic Backend REST API Core",
        "institute": "Pure Health Clinic & Hospital Systems",
        "status": "online",
        "endpoints": {
            "swagger_documentation": "/api/docs/",
            "redoc_documentation": "/api/redoc/",
            "system_health": "/api/admin/health/",
            "admin_dashboard": "/api/admin/dashboard/",
            "appointments_list": "/api/admin/appointments/",
            "user_auth": "/api/auth/register/",
            "medical_services": "/api/content/services/",
            "doctors_directory": "/api/content/doctors/",
            "jwt_obtain_token": "/api/token/",
        }
    })


urlpatterns = [
    # Root Visual Website Landing (HTML Frontend UI)
    path('', visual_frontend_home_view, name='visual-frontend-home'),

    # JSON API Directory
    path('api/', root_api_directory_view, name='root-api-directory'),

    path('admin/', admin.site.urls),
    
    # OpenAPI Schema & Interactive Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Application Modules (Modules 1, 2, 3, 4)
    path('api/auth/', include('apps.authentication.urls')),
    path('api/admin/', include('apps.administration.urls')),
    path('api/content/', include('apps.content.urls')),
]
