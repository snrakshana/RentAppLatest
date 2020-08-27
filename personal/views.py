from django.shortcuts import render
from account.models import User
from django.http import HttpResponse

from advertisement.models import ADPost

def index(request):
    users = User.objects.all()
    ads = ADPost.objects.all()
    context = {
        'users':users,
        'ads':ads
    }
    return render(request,'personal/index.html',context)

def test(request):
 	return HttpResponse("sdfsdf")

