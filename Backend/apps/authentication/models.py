from django.db import models
from apps.core.models import TimeStampedModel


class RoleModel(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name


class UserProfileModel(TimeStampedModel):
    email = models.EmailField(unique=True, db_index=True)
    full_name = models.CharField(max_length=255)
    role = models.ForeignKey(RoleModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.email} ({self.full_name})"
