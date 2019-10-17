from django.urls import path
from . import views

#root = ~/IWS
urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('trial/', views.trial, name='trial')
]
