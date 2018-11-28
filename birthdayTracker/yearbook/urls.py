from django.urls import path, re_path
from . import views
from .views import YearbooksController

urlpatterns = [
    re_path(r'^$', YearbooksController.as_view()),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    path('addNewYearbook', YearbooksController.as_view().addYearbook)
]