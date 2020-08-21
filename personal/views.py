from django.shortcuts import render
from account.models import User

def index(request):
    users = User.objects.all()

    context = {
        'users':users
    }
    return render(request,'personal/index.html',context)


