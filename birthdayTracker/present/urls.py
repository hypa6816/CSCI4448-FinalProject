from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details')
]