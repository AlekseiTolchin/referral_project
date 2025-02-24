import uuid

from django.contrib.auth.models import User
from django.db import models


class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True, blank=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4()).replace("-", "")[:8].upper()

        if self.active and self.pk is None:
            ReferralCode.objects.filter(
                user=self.user,
                active=True
            ).update(active=False)

        super().save(*args, **kwargs)


class ReferralRelations(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referral = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referred_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.referrer} -> {self.referral}'
