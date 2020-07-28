from django import forms
from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ('username','first_name','last_name','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('portfolio',)
