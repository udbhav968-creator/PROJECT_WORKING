from rest_framework.permissions import BasePermission


class IsAdminUserRole(BasePermission):
    """
    Custom Permission allowing access only to users with 'Admin' or 'SuperAdmin' role.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if hasattr(request.user, 'user_profile') and request.user.user_profile.role:
            return request.user.user_profile.role.name.lower() in ['admin', 'superadmin']
        return request.user.is_staff or request.user.is_superuser


class IsDoctorUserRole(BasePermission):
    """
    Custom Permission allowing access only to users with 'Doctor' or 'Staff' role.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if hasattr(request.user, 'user_profile') and request.user.user_profile.role:
            return request.user.user_profile.role.name.lower() in ['doctor', 'staff', 'admin']
        return True


class IsPatientUserRole(BasePermission):
    """
    Custom Permission allowing access to authenticated Patient users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
