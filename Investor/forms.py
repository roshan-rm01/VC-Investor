from django import forms
from .models import Company, Investor


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ('name', 'location', 'firm')

