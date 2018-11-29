from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, CreateView

from .models import Yearbooks
from present.models import Presents
from .forms import YearbookModelForm 


# Main yearbooks view
class YearbooksView(View):
    form_class = YearbookModelForm
    redirect = ''
    template_name = 'yearbook/index.html'
    deleteShow = False

    def get(self, request):
        yearbooks = Yearbooks.objects.all()[:10]
        context = {
            'title': 'Yearbooks',
            'yearbooks': yearbooks,
            'deleteShow': self.deleteShow,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/yearbook/')
        return render(request, self.template_name, {'form':form})

# details method view
def details(request, id):
    year = Yearbooks.objects.get(id=id).title
    presents = Presents.objects.filter(given_at__year=year)
    context = {
        'title': 'Presents',
        'presents': presents,
    }
    return render(request, 'yearbook/details.html', context)

# create new yearbook
class YearbookCreateView(CreateView):
    template_name = 'yearbook/create_yearbook.html'
    form_class = YearbookModelForm
    queryset = Yearbooks.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

# delete an existing yearbook
def delete(request, id):
    yearbookObject = Yearbooks.objects.get(id=id)
    yearbookObject.delete()
    return HttpResponseRedirect('/yearbook/')