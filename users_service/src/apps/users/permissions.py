from rest_framework import permissions


class IsAuthenticatedOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            if request.user == obj or request.user.is_superuser:
                return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False
