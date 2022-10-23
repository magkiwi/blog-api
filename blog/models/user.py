from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from blog.managers.user import UserManager

STATUS_CHOICES = [("active", "active"), ("disabled", "disabled")]


class User(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    username = None
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=1024, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_title = models.CharField(max_length=1024, blank=True, null=True)

    groups = models.ForeignKey(
        Group,
        related_name="user_set",
        related_query_name="user",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''} - {self.id}"
