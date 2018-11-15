from django.shortcuts import render
from django.http import HttpResponse

from .models import Presents
# Create your views here.

def index(request):
        # return HttpResponse('Hello, this is present view')

    presents = Presents.objects.all()[:10]

    context = {
        'title': 'Presents',
        'presents': presents,
    }
    return render(request, 'present/index.html', context)

def details(request, id):
    present = Presents.objects.get(id=id)
    context = {
        'present': present
    }
    return render(request, 'present/details.html', context)
