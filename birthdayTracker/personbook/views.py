from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonsModelForm
from .models import Personbooks

from django.views.generic import View, CreateView, UpdateView
from django.urls import reverse


# Main Person View/ index view
class PersonsView(View):
    form_class = PersonsModelForm
    redirect = ''
    template_name = 'personbook/index.html'
    deleteShow = False
    updateShow = False
    def get(self, request):
        persons = Personbooks.objects.all()
        context = {
            'title': 'Personbookss',
            'personbooks': persons,
            'deleteShow': self.deleteShow,
            'updateShow': self.updateShow
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/personbook/')
        return render(request, self.template_name, {'form':form})
    
# details view
def details(request, id):
    personbook = Personbooks.objects.get(id=id)
    context = {
        'personbook': personbook
    }
    return render(request, 'personbook/details.html', context)

# create new personbook
class PersonCreateView(CreateView):
    template_name = 'personbook/create_person.html'
    form_class = PersonsModelForm
    queryset = Personbooks.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

# update an existing personbook
class PersonUpdateView(UpdateView):
    template_name = 'personbook/create_person.html'
    form_class = PersonsModelForm
    queryset = Personbooks.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Personbooks, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# delete an existing personbook
def delete(request, id):
    PersonObject = Personbooks.objects.get(id=id)
    PersonObject.delete()
    return HttpResponseRedirect('/personbook/')
