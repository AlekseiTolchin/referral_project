from django.contrib.auth import get_user_model
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReferralCode
from .serializers import (
    ReferralCodeSerializer,
    EmailSerializer,
    ReferralUserSerializer
)

User = get_user_model()


class CreateReferralCodeView(APIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальная система'],
        summary='Создать реферальный код',
        description='Создание нового реферального кода для текущего пользователя'
    )

    def post(self, request):
        serializer = ReferralCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteReferralCodeView(APIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальная система'],
        summary='Удалить реферальный код',
        description='Удаление реферального кода по id'
    )

    def delete(self, request, pk):
        try:
            referral_code = ReferralCode.objects.get(pk=pk)
        except ReferralCode.DoesNotExist:
            return Response(
                {'detail': 'Реферальный код не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

        if referral_code.user != request.user:
            raise PermissionDenied('Вы не можете удалить этот код')

        referral_code.delete()
        return Response(
            {'detail': 'Реферальный код успешно удален'},
            status=status.HTTP_200_OK
        )


class GetReferralByEmailView(APIView):
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальная система'],
        summary="Получить реферальный код по email",
        description="Получение активного реферального кода по email реферера",
    )

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            referral_code = ReferralCode.objects.filter(
                user=user,
                expiration_date__gte=timezone.now()
            ).latest('created_at')
        except User.DoesNotExist:
            return Response(
                {'detail': "Пользователь не найден"},
                status=status.HTTP_404_NOT_FOUND
            )
        except ReferralCode.DoesNotExist:
            return Response(
                {"detail": 'Активный реферальный код отсутствует'},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(ReferralCodeSerializer(referral_code).data)


class UserReferralsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальная система'],
        summary='Получить список рефералов по id',
        description='Возвращает список всех пользователей, зарегистрированных по вашему реферальному коду',
        responses={200: ReferralUserSerializer(many=True)}
    )

    def get(self, request, user_id):
        if not request.user.is_staff and request.user.id != int(user_id):
            return Response(
                {"detail": "Вы можете просматривать только своих рефералов"},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            referrer = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "Пользователь не найден"},
                status=status.HTTP_404_NOT_FOUND
            )

        referrals = User.objects.filter(
            referred_by__referrer=referrer
        ).order_by('-date_joined')

        serializer = ReferralUserSerializer(referrals, many=True)
        return Response(serializer.data)
