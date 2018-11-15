from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Yearbooks
# Create your views here.

def index(request):
        # return HttpResponse('Hello, this is yearbook view')

    yearbooks = Yearbooks.objects.all()[:10]

    context = {
        'title': 'Yearbooks',
        'yearbooks': yearbooks,
    }
    return render(request, 'yearbook/index.html', context)

def details(request, id):
    yearbook = Yearbooks.objects.get(id=id)
    context = {
        'yearbook': yearbook
    }
    return render(request, 'yearbook/details.html', context)
