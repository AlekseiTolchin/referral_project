from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReferralCode
from .serializers import ReferralCodeSerializer


class CreateReferralCodeView(APIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальные коды'],
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
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Реферальные коды'],
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
