from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text="required please add a valid email")

    class Meta:
        model = User
        fields = ('email','username','cnumber','password1','password2')