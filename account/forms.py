from django import forms
from django.contrib.auth.forms import UserCreationForm,authenticate

from account.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100,help_text="required please add a valid email")

    class Meta:
        model = User
        fields = ('email','username','cnumber','password1','password2')


class LoginForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('email', 'username','cnumber' )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = User.objects.exclude(pk=self.instance.pk).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)
   
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = User.objects.exclude(pk=self.instance.pk).get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)

	def cnumber(self):
		account = User.objects.exclude(pk=self.instance.pk).get(cnumber=cnumber)
	
		




    
   