from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Presents
from .forms import PresentsModelForm
from django.views.generic import View, CreateView, UpdateView
from django.urls import reverse


# Index View/Main View
class PresentsView(View):
    form_class = PresentsModelForm
    redirect = ''
    template_name = 'present/index.html'
    deleteShow = False
    updateShow = False
    def get(self, request):
        presents = Presents.objects.all()
        context = {
            'title': 'Presents',
            'presents': presents,
            'deleteShow': self.deleteShow,
            'updateShow': self.updateShow
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/present/')
        return render(request, self.template_name, {'form':form})

# Delete Present Method
def delete(request, id):
    PresentObject = Presents.objects.get(id=id)
    PresentObject.delete()
    return HttpResponseRedirect('/present/')

# View present details
def details(request, id):
    present = Presents.objects.get(id=id)
    context = {
        'present': present
    }
    return render(request, 'present/details.html', context)

# Create a present
class PresentCreateView(CreateView):
    template_name = 'present/create_present.html'
    form_class = PresentsModelForm
    queryset = Presents.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

# Change or update an existing present
class PresentUpdateView(UpdateView):
    template_name = 'present/create_present.html'
    form_class = PresentsModelForm
    queryset = Presents.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Presents, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


