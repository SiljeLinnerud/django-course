from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portofolio = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('portofolio','profile_picture')
