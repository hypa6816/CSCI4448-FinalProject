from django.urls import path
from . import views

urlpatterns = [
    path('goHome', views.index),
    path('', views.index, name='index')
]