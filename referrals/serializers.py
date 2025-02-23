from rest_framework import serializers
from .models import ReferralCode


class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ['code', 'expiration_date', 'created_at', 'active']
        read_only_fields = ['code', 'created_at']