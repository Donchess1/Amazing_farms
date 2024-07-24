from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.gallery, name='gallery'),
    path('', views.service, name='service'),
    path('', views.contact, name='contact'),
    path('', views.about, name='about'),
    path('', views.why, name='why'),
    ]
