from django.urls import include, path
from rest_framework import routers

from src.apps.users import views as users_views


router = routers.DefaultRouter()
router.register("customers", users_views.CustomerViewSet)
router.register("vendors", users_views.VendorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
