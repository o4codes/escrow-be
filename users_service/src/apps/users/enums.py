from django.db import models


class UserRoles(models.TextChoices):
    VENDOR = "VENDOR"
    CUSTOMER = "CUSTOMER"
    ADMIN = "ADMIN"

