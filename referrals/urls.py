from django.urls import path
from .views import CreateReferralCodeView, DeleteReferralCodeView, GetReferralByEmailView, UserReferralsView


urlpatterns = [
    path('referral-codes/', CreateReferralCodeView.as_view(), name='create-code'),
    path('referral-codes/<int:pk>/', DeleteReferralCodeView.as_view(), name='delete-code'),
    path('referral-codes/email/', GetReferralByEmailView.as_view(), name='get-code-by-email'),
    path('referrals/by-user/<int:user_id>/', UserReferralsView.as_view(), name='referrals-by-user'),
]