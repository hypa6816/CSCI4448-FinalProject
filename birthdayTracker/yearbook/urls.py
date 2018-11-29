from django.urls import path, re_path
from . import views
from .views import YearbooksView, YearbookCreateView
import home

urlpatterns = [
    # Main View
    re_path(r'^$', YearbooksView.as_view()),
    # Detail View
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    # Add New Yearbook View
    path('addNewYearbook', YearbookCreateView.as_view()),
    # Delete Existing Yearbook
    re_path(r'^delete (?P<id>\d+)/$', views.delete),
    path('deleteYearbook', YearbooksView.as_view(deleteShow= True)),
    path('undoDeleteYearbook', YearbooksView.as_view(deleteShow= False)),
]