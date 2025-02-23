from django.contrib import admin
from .models import ReferralCode
from .forms import ReferralCodeForm


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    form = ReferralCodeForm
