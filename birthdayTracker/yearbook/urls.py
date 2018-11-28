from django.urls import path, re_path
from . import views
from .views import YearbooksView, YearbookCreateView

urlpatterns = [
    re_path(r'^$', YearbooksView.as_view()),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    path('addNewYearbook', YearbookCreateView.as_view())
]