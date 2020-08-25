from django.shortcuts import render
from account.models import User

from advertisement.models import ADPost

def index(request):
    users = User.objects.all()
    ads = ADPost.objects.all()
    context = {
        'users':users,
        'ads':ads
    }
    return render(request,'personal/index.html',context)


