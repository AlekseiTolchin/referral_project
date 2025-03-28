# Generated by Django 5.1.6 on 2025-02-25 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_alter_referralcode_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referralrelations',
            options={'verbose_name': 'Реферальная связь', 'verbose_name_plural': 'Реферальные связи'},
        ),
        migrations.AlterField(
            model_name='referralrelations',
            name='referral',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='referred_by', to=settings.AUTH_USER_MODEL, verbose_name='Реферал'),
        ),
        migrations.AlterField(
            model_name='referralrelations',
            name='referrer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to=settings.AUTH_USER_MODEL, verbose_name='Реферер'),
        ),
    ]
