from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ReferralCodeSerializer
from .models import ReferralCode


class CreateReferralCodeView(generics.CreateAPIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [IsAuthenticated]
    queryset = ReferralCode.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
