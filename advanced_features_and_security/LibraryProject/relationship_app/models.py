from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    """
    Profile linked to the custom user model
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
