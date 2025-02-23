from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterAPIView

urlpatterns = [
    path('', RegisterAPIView.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # получение пары JWT - токенов
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # обновление токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # проверка действительности токена
]