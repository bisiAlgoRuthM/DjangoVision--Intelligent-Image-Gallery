from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'label', 'image', 'tags']
