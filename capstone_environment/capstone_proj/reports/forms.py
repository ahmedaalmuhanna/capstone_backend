from django import forms
from .models import Report , IOCS 




class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['profile','reference','details','title','is_approve']


class IOCSForm(forms.ModelForm):
    class Meta:
        model = IOCS
        fields = "__all__"


