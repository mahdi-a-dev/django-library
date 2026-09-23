from django import forms
from .views import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ["book"]