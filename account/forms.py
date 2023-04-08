from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import models
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationFrom(forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Return Password",
                                 widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError('Ikkala maydondagi parol bir biriga mos kelishi kerak!')
        return data['password_2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['data_of_birth', 'photo']