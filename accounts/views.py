from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .serializers import UserSerializer


class RegisterAPIView(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        tags=['Регистрация и аутентификация'],
        summary='Зарегистрировать пользователя с реферальным кодом или без него',
        description='Поле "referral_code" заполняется при наличии реферального кода'
    )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=201)
        return Response(serializer.errors, status=400)


@extend_schema(
        tags=['Регистрация и аутентификация'],
        summary='Получить JWT токен',
    )
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(
        tags=['Регистрация и аутентификация'],
        summary='Обновить JWT токен',
    )
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(
        tags=['Регистрация и аутентификация'],
        summary='Проверить JWT токен на актуальность',
    )
class CustomTokenVerifyView(TokenVerifyView):
    pass
