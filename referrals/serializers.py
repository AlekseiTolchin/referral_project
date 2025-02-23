from rest_framework import serializers
from .models import ReferralCode


class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ['code', 'expiration_date', 'created_at', 'active']
        read_only_fields = ['code', 'created_at']

    def perform_create(self, serializer):
        self.request.user.referralcode_set.filter(active=True).update(active=False)

        serializer.save(
            user=self.request.user,
            active=True
        )
