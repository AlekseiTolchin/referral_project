from django.urls import path
from .views import CreateReferralCodeView


urlpatterns = [
    path('referral-codes/', CreateReferralCodeView.as_view(), name='create-code'),
]