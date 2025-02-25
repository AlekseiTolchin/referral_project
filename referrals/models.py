import uuid

from django.contrib.auth.models import User
from django.db import models


class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    code = models.CharField(max_length=20, unique=True, blank=True, verbose_name='Реферальный код')
    expiration_date = models.DateTimeField(verbose_name='Дата окончания действия кода')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Реферальный код'
        verbose_name_plural = 'Реферальные коды'

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4()).replace("-", "")[:8].upper()

        if self.active and self.pk is None:
            ReferralCode.objects.filter(
                user=self.user,
                active=True
            ).update(active=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Реферальный код пользователя {self.user.username}'


class ReferralRelations(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals', verbose_name='Реферер')
    referral = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referred_by', verbose_name='Реферал')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Реферальная связь'
        verbose_name_plural = 'Реферальные связи'

    def __str__(self):
        return f'Реферер - {self.referrer} -> Реферал - {self.referral}'
