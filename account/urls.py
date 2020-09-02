from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('register',views.registration_view, name = "register"),
    path('logout',views.logout_view, name = "logout"),
    path('login',views.login_view, name = "login"),
    path('account',views.account_view, name = "account"),
    path('must_authenticate',views.must_authenticate_view, name = "must_authenticate"),
   
]