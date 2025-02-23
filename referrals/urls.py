from django.urls import path
from .views import CreateReferralCodeView, DeleteReferralCodeView


urlpatterns = [
    path('referral-codes/', CreateReferralCodeView.as_view(), name='create-code'),
    path('referral-codes/<int:pk>/', DeleteReferralCodeView.as_view(), name='delete-code')
]