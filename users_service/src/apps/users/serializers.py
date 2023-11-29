from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from src.apps.users import enums as user_enums

User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    role: user_enums.UserRoles = None

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "password",
        ]
        read_only_fields = ["created_datetime", "updated_datetime", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(list(exc))
        return value

    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data, role=self.role)
        return user

    def update(self, instance: User, validated_data: dict):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class VendorUserSerializer(BaseUserSerializer):
    role = user_enums.UserRoles.VENDOR


class CustomerUserSerializer(BaseUserSerializer):
    role = user_enums.UserRoles.CUSTOMER
