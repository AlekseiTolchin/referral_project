from django.contrib import admin
from .models import ReferralCode, ReferralRelations
from .forms import ReferralCodeForm


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    form = ReferralCodeForm


@admin.register(ReferralRelations)
class ReferralRelations(admin.ModelAdmin):
    pass
