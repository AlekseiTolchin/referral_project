from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from referrals.models import ReferralCode, ReferralRelations


class UserSerializer(serializers.ModelSerializer):
    referral_code = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'referral_code')

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def validate_referral_code(self, value):
        if value:
            try:
                code = ReferralCode.objects.get(
                    code=value,
                    active=True,
                )
                return code.user
            except ReferralCode.DoesNotExist:
                raise serializers.ValidationError('Недействительный реферальный код')

        return None

    def create(self, validated_data):
        referral_user = validated_data.pop('referral_code', None)
        user = super().create(validated_data)

        if referral_user:
            ReferralRelations.objects.create(
                referrer=referral_user,
                referral=user
            )

        return user
