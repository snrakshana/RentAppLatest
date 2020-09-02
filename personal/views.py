from django.shortcuts import render
from account.models import User
from django.http import HttpResponse

from advertisement.models import ADPost
from django.core.paginator import Paginator

def index(request):
    users = User.objects.all()
    ads = ADPost.objects.all()

    paginator = Paginator(ads,8)
    page = request.GET.get('page')

    ads = paginator.get_page(page)

    context = {
        'users':users,
        'ads':ads
    }
    return render(request,'personal/index.html',context)

def test(request):
 	return HttpResponse("sdfsdf")

