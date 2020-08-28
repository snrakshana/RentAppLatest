
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from advertisement.models import ADPost
from django.http import HttpResponse
from account.models import User

from advertisement.forms import CreateAdvertisementForm, UpdateAdvertisementForm


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
        return redirect(reverse('index'))

    context['form'] = form

    return render(request, "advertisement/create_ad.html", context)


def detail_ad_view(request, slug):
    context = {}
    ad_detail = get_object_or_404(ADPost, slug=slug)
    context['ad_detail'] = ad_detail
    return render(request, 'advertisement/ad_detail.html', context)


def edit_ad_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    ad_post = get_object_or_404(ADPost, slug=slug)

    if ad_post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateAdvertisementForm(
            request.POST or None, request.FILES or None, instance=ad_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            ad_post = obj

    form = UpdateAdvertisementForm(
        initial={
            "title": ad_post.title,
            "description": ad_post.description,
            "image": ad_post.image,
            "district":ad_post.district,
            "price":ad_post.price,
            "city":ad_post.city,
            "is_negotiable":ad_post.is_negotiable,
            "fuel_type":ad_post.fuel_type,
            "transmission":ad_post.transmission,
            "body_type":ad_post.body_type,
            "vehicle_model":ad_post.vehicle_model,
            "vehicle_brand":ad_post.vehicle_brand,





        }
    )

    context['form'] = form
    return render(request, 'advertisement/edit_ad.html', context)


def delete_ad_view(request, slug):

    delete_ad = ADPost.objects.get(slug=slug)
    if request.method == 'POST':
        delete_ad.delete()
        return redirect(reverse('index'))




