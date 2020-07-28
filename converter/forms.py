from django import forms
from . import models

class conv(forms.ModelForm):
    class Meta:
        model = models.con
        fields = "__all__"

class deci(forms.ModelForm):
    class Meta:
        model = models.dec
        fields = "__all__"
