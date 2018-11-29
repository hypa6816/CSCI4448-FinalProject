from django.urls import path, re_path
from . import views
from .views import PresentsView, PresentCreateView, PresentUpdateView
import home

urlpatterns = [
    # Main View
    path('', PresentsView.as_view()),
    # Detail View
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    # Add Present
    path('addNewPresent', PresentCreateView.as_view()),
    # Delete Present
    re_path(r'^delete/(?P<id>\d+)/$', views.delete),
    path('deletePresent', PresentsView.as_view(deleteShow= True)),
    path('undoDeletePresent', PresentsView.as_view(deleteShow= False)),
    # Update Present
    re_path(r'^update/(?P<id>\d+)/$', PresentUpdateView.as_view( success_url="/present/"), name='present-update'),
    path('updatePresent', PresentsView.as_view(updateShow= True)),
    path('undoUpdatePresent', PresentsView.as_view(updateShow= False)),

]