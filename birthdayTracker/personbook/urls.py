from django.urls import re_path, path
from . import views
import home
from .views import PersonsView, PersonCreateView, PersonUpdateView

urlpatterns = [
    # Main View
    path('', PersonsView.as_view()),
    # Detail View
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    # Add New Person View
    path('addNewPerson', PersonCreateView.as_view()),
    # Delete Person
    re_path(r'^delete/(?P<id>\d+)/$', views.delete),
    path('deletePerson', PersonsView.as_view(deleteShow= True)),
    path('undoDeletePerson', PersonsView.as_view(deleteShow= False)),
    # Update a Person
    re_path(r'^update/(?P<id>\d+)/$', PersonUpdateView.as_view( success_url="/personbook/"), name='Person-update'),
    path('updatePerson', PersonsView.as_view(updateShow= True)),
    path('undoUpdatePerson', PersonsView.as_view(updateShow= False)),
]