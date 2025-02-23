from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True, blank=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4()).replace("-", "")[:8].upper()
        super().save(*args, **kwargs)

