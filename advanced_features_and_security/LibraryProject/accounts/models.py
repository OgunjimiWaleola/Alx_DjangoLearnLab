from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    Adds extra fields required for our application
    """

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username
