from django.contrib.auth import get_user_model
from rest_framework import viewsets

from src.apps.users import (
    serializers as user_serializers,
    enums as user_enums,
    permissions as user_permissions,
)

User = get_user_model()


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role=user_enums.UserRoles.CUSTOMER)
    serializer_class = user_serializers.CustomerUserSerializer
    permission_classes = [user_permissions.IsAuthenticatedOrCreateOnly]


class VendorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role=user_enums.UserRoles.VENDOR)
    serializer_class = user_serializers.VendorUserSerializer
    permission_classes = [user_permissions.IsAuthenticatedOrCreateOnly]
