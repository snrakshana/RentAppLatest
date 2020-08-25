from django.shortcuts import render ,redirect,reverse
from advertisement.models import ADPost
from account.models import User

from advertisement.forms import CreateAdvertisementForm

def create_ad(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect(reverse('must_authenticate'))

	form = CreateAdvertisementForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = User.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateAdvertisementForm()

	context['form'] = form

	return render(request, "advertisement/create_ad.html", context)


