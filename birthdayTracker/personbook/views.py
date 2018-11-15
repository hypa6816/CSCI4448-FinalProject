from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Personbooks
# Create your views here.

def index(request):
        # return HttpResponse('Hello, this is personbook view')

    personbooks = Personbooks.objects.all()[:10]

    context = {
        'title': 'Person Books',
        'personbooks': personbooks,
    }
    return render(request, 'personbook/index.html', context)

def details(request, id):
    personbook = Personbooks.objects.get(id=id)
    context = {
        'personbook': personbook
    }
    return render(request, 'personbook/details.html', context)
