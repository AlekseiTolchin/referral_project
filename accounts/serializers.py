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
        extra_kwargs = {'password': {'write_only': True}}

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

    def create(self, validated_data):
        referral_user = validated_data.pop('referral_code', None)
        user = User.objects.create_user(**validated_data)

        if referral_user:
            ReferralRelations.objects.create(
                referrer=referral_user,
                referral=user
            )

        return user
