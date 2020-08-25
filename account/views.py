from django.shortcuts import render,redirect,HttpResponse,reverse
from django.contrib.auth import login,authenticate,logout
from django.core.exceptions import ValidationError

from account.forms import RegistrationForm, LoginForm , AccountUpdateForm

from advertisement.models import ADPost

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect(reverse('index'))
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect(reverse('index'))

def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect(reverse('index'))

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect(reverse('index'))

	else:
		form = LoginForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)

def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
					"cnumber":  request.POST['cnumber'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
					"cnumber" : request.user.cnumber,
				}
			)

	context['account_form'] = form

	ads = ADPost.objects.filter(author=request.user)
	context["ads"] = ads
	

	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})