from django import forms
from calculator.models import Calculate
class Two(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = "__all__"
