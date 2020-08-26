from django.urls import path
from .import views

urlpatterns = [
  path('create_ad', views.create_ad, name='create_ad'),
  path('<slug>', views.detail_ad_view, name='ad_detail'),
  path('<slug>/edit', views.edit_ad_view, name='edit_ad'),
  path('<slug>/delete', views.delete_ad_view, name='delete_ad'),
  
]
