from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, CreateView

from .models import Yearbooks
from present.models import Presents
from .forms import YearbookModelForm 
# Create your views here.

class YearbooksView(View):
    form_class = YearbookModelForm
    redirect = ''
    yearbooks = Yearbooks.objects.all()[:10]
    template_name = 'yearbook/index.html'
    context = {
            'title': 'Yearbooks',
            'yearbooks': yearbooks,
        }
    def get(self, request):
        return render(request, self.template_name, self.context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/yearbook/')
        return render(request, self.template_name, {'form':form})

def details(request, id):
    year = Yearbooks.objects.get(id=id).title
    presents = Presents.objects.filter(given_at__year=year)
    context = {
        'title': 'Presents',
        'presents': presents,
    }
    return render(request, 'yearbook/details.html', context)

class YearbookCreateView(CreateView):
    template_name = 'yearbook/create_yearbook.html'
    form_class = YearbookModelForm
    queryset = Yearbooks.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

# def details(request, id):
#     present = Presents.objects.get(id=id)
#     context = {
#         'present': present
#     }
#     return render(request, 'present/details.html', context)

def addYearbook(request):
    return HttpResponse("adding new yearbook")