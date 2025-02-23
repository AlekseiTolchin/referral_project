from django import forms
from .models import ReferralCode


class ReferralCodeForm(forms.ModelForm):
    class Meta:
        model = ReferralCode
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'readonly': 'readonly'})
        }
