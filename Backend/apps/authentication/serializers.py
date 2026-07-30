from django.contrib.auth.models import User
from rest_framework import serializers
from apps.authentication.models import RoleModel, UserProfileModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ['id', 'name', 'description']


class UserProfileSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = UserProfileModel
        fields = ['id', 'email', 'full_name', 'role_name', 'is_active', 'created_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    role_name = serializers.CharField(write_only=True, required=False, default='Patient')
    full_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'role_name']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        role_name = validated_data.pop('role_name', 'Patient')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password,
        )

        role, _ = RoleModel.objects.get_or_create(
            name=role_name,
            defaults={'description': f'Role for {role_name} users'}
        )

        UserProfileModel.objects.create(
            email=user.email,
            full_name=full_name,
            role=role,
            is_active=True
        )

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
