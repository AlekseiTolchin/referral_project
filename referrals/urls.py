from django.urls import path
from .views import CreateReferralCodeView, DeleteReferralCodeView, GetReferralByEmailView


urlpatterns = [
    path('referral-codes/', CreateReferralCodeView.as_view(), name='create-code'),
    path('referral-codes/<int:pk>/', DeleteReferralCodeView.as_view(), name='delete-code'),
    path('referrals-codes/email/', GetReferralByEmailView.as_view(), name='get-code-by-email')
]