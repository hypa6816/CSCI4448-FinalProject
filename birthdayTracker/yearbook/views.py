from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View, CreateView

from .models import Yearbooks
from present.models import Presents
# Create your views here.

class YearbooksController(View):
    template_name = 'yearbook/index.html'
    def get(self, request):
        yearbooks = Yearbooks.objects.all()[:10]

        context = {
            'title': 'Yearbooks',
            'yearbooks': yearbooks,
        }
        return render(request, template_name, context)

def details(request, id):
    year = Yearbooks.objects.get(id=id).title
    presents = Presents.objects.filter(given_at__year=year)
    context = {
        'title': 'Presents',
        'presents': presents,
    }
    return render(request, 'yearbook/details.html', context)

class addYearbookView(CreateView):
    template_name = 'create_yearbook.html'
# def details(request, id):
#     present = Presents.objects.get(id=id)
#     context = {
#         'present': present
#     }
#     return render(request, 'present/details.html', context)

def addYearbook(request):
    return HttpResponse("adding new yearbook")